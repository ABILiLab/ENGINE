import torch
from utils import create_parser , deal3DiRes
from model import GNN_model_EGNN_DSSP_ESM3
from torch_geometric.data import Dataset,Data
from torch_geometric.loader import DataLoader
import os
import yaml
import pickle
import csv
import numpy as np
import pandas as pd
import argparse
import torch
import torch_cluster
from infer_utils import pipeline_get_protlgn
from Bio.PDB import PDBParser, DSSP
import tqdm
import glob

device = 'cuda' if torch.cuda.is_available() else 'cpu'

ANNOTATION_FILE = 'src/Dataset/nrPDB-GO_2019.06.18_annot.tsv'
CLASS_DICT = {
    'mf':489,
    'bp':1943,
    'cc':320
}

# 加载GO注释数据
def load_GO_annot(filename):
    # Load GO annotations
    onts = ['mf', 'bp', 'cc']
    prot2annot = {}    # 将蛋白质ID映射到对应的GO术语
    goterms = {ont: [] for ont in onts}
    gonames = {ont: [] for ont in onts}

    with open(filename, mode='r') as tsvfile:
        reader = csv.reader(tsvfile, delimiter='\t')

        # molecular function
        next(reader, None)  # skip the headers
        goterms[onts[0]] = next(reader)

        next(reader, None)  # skip the headers
        gonames[onts[0]] = next(reader)

        # biological process
        next(reader, None)  # skip the headers
        goterms[onts[1]] = next(reader)
        next(reader, None)  # skip the headers
        gonames[onts[1]] = next(reader)

        # cellular component
        next(reader, None)  # skip the headers
        goterms[onts[2]] = next(reader)
        next(reader, None)  # skip the headers
        gonames[onts[2]] = next(reader)

        next(reader, None)  # skip the headers
        counts = {ont: np.zeros(len(goterms[ont]), dtype=float) for ont in onts}
        for row in reader:
            prot, prot_goterms = row[0], row[1:]
            prot2annot[prot] = {ont: [] for ont in onts}
            for i in range(3):
                goterm_indices = [goterms[onts[i]].index(goterm) for goterm in prot_goterms[i].split(',') if
                                  (goterm != '')]
                prot2annot[prot][onts[i]] = np.zeros(len(goterms[onts[i]]))
                prot2annot[prot][onts[i]][goterm_indices] = 1.0
                counts[onts[i]][goterm_indices] += 1.0
    return prot2annot, goterms, gonames, counts

class PFresGODatasets(Dataset):
    def __init__(self,
                 pdb_file= './infer_temp',
                 category= 'cc' , # mf | cc | bp
                 esm3_6B_path = 'Features/esm-c',
                 feature_3Di_path ='Features/foldseek_3di_token' ,   # 存放3Di特征
                 dssp_executable = "/usr/bin/dssp",  # DSSP安装路径
                 foldseek_executable = "/home/ranzixu/Protein_function/feature_extracter/foldseek/bin/foldseek"  # 安装路径
                 ):
        super(PFresGODatasets, self).__init__()
        # self.pdb_root = pdb_root
        self.category = category
        self.feature_3Di_path = feature_3Di_path
        self.dssp_executable = dssp_executable
        self.foldseek_executable = foldseek_executable
        # self.data_list = glob.glob(os.path.join(self.pdb_root, '*.pdb'))
        self.data_list=[pdb_file]
        self.esm3_6B_path = esm3_6B_path

        self.class_num = CLASS_DICT[category]
        self.dssp_sec_structrue_MAP = {
             'H': [1,0,0,0,0,0,0,0,],  # Alpha helix
             'B': [0,1,0,0,0,0,0,0,],  # Beta bridge
             'E': [0,0,1,0,0,0,0,0,],  # Extended strand
             'G': [0,0,0,1,0,0,0,0,],  # 3-10 helix
             'I': [0,0,0,0,1,0,0,0,],  # Pi helix
             'T': [0,0,0,0,0,1,0,0,],  # Turn
             'S': [0,0,0,0,0,0,1,0,],  # Bend
             '-': [0,0,0,0,0,0,0,1,]   # Loop or irregular
        }                              
        self.letter_to_num = {'C': 4, 'D': 3, 'S': 15, 'Q': 5, 'K': 11, 'I': 9,
                       'P': 14, 'T': 16, 'F': 13, 'A': 0, 'G': 7, 'H': 8,
                       'E': 6, 'L': 10, 'R': 1, 'W': 17, 'V': 19, 
                       'N': 2, 'Y': 18, 'M': 12,'X':20} 
        self.init_3Di()

    def __len__(self):
        return len(self.data_list)

    def init_3Di(self):
        os.makedirs(self.feature_3Di_path, exist_ok=True)
        for pdb_file in tqdm.tqdm(self.data_list):
            id = os.path.basename(pdb_file).split('.')[0]
            if(os.path.exists(os.path.join(self.feature_3Di_path,id+".3di"))):
                continue
            os.system(f'{self.foldseek_executable} structureto3didescriptor {pdb_file} {os.path.join(self.feature_3Di_path,id+".3di")}')

    def get_dssp_ss_feature(self,pdb_file):
        parser = PDBParser(QUIET=True)
        structure = parser.get_structure('Protein', pdb_file)
        
        model = structure[0]  
        raw_dssp_feature = DSSP(model, pdb_file, dssp=self.dssp_executable)
        a_key = list(raw_dssp_feature.keys())
        sec_structure =  [ self.dssp_sec_structrue_MAP[raw_dssp_feature[i][2]] for i in a_key ]
        return sec_structure

    def load_3Di_feature(self,id):
        res = deal3DiRes(threeDifile=os.path.join(self.feature_3Di_path,f'{id}.3di'))
        edge_index = torch_cluster.knn_graph(torch.tensor(res[1]), k=7) 
        seq_token = torch.as_tensor([self.letter_to_num[aa] for aa in res[0]] , dtype=torch.long)
        graph_data = Data(x=torch.tensor(res[1], dtype=torch.float), seq=res[0], edge_index=edge_index)
        seq_token = Data(x=seq_token)
        return seq_token , graph_data

    def __getitem__(self, idx):
        
        path_file = self.data_list[idx]
        id = os.path.basename(path_file).split('.')[0]
        tmp = pipeline_get_protlgn(path_file) # protlgn online

        esm3_6B_feature = pickle.load(open(os.path.join(self.esm3_6B_path, id + '.pkl'), 'rb'))
        dssp_ss_feature = self.get_dssp_ss_feature(path_file)
        threeDi_feature_seq , threeDi_feature_graph = self.load_3Di_feature(id)
        esm3_6B_feature = torch.tensor(esm3_6B_feature)
        dssp_ss_feature = torch.tensor(dssp_ss_feature)


        fusion_feature = dssp_ss_feature
        data = Data(
            x=fusion_feature,
            pos=tmp.pos,
            mu_r_norm=tmp.mu_r_norm,
            edge_index=tmp.edge_index,
            edge_attr=tmp.edge_attr,
        )
        data_protein = Data(x = esm3_6B_feature)
        return data, data_protein, threeDi_feature_seq ,id

def create_model(args, cate="mf"):
    config = 'src/Egnnconfig/egnn.yaml'
    if cate == "mf":
        config = 'src/Egnnconfig/egnn_mf.yaml'
    elif cate == "bp":
        config = 'src/Egnnconfig/egnn_bp.yaml'
    elif cate == "cc":
        config = 'src/Egnnconfig/egnn_cc.yaml'
    gnn_config=yaml.load(open(config), Loader=yaml.FullLoader)['egnn']
    args.input_dim = 13
    model = GNN_model_EGNN_DSSP_ESM3(gnn_config, args)
    return model


def GOpredict(inputpdb,CATE='CC',save_path = '',dssp_executable='/usr/bin/dssp',
              foldseek_executable='/home/ranzixu/Protein_function/feature_extracter/foldseek/bin/foldseek',device=device,num_workers=2):
    

    if CATE == 'mf':
        resume_path = 'model/model_mf.pt'  #  'mf'model path
    elif CATE == 'bp':
        resume_path = 'model/model_bp.pt'  #  'bp'model path 
    elif CATE == 'cc':
        resume_path = 'model/model_cc.pt'  #  'cc'model path 

    test_dataset = PFresGODatasets(inputpdb, category=CATE, dssp_executable=dssp_executable, foldseek_executable=foldseek_executable)
    test_loader = DataLoader(test_dataset,batch_size=1,num_workers=num_workers)

    model = load_model(resume_path,device,cate = CATE)
    prot2annot, goterms, gonames, counts = load_GO_annot(ANNOTATION_FILE)
    goterms = goterms[CATE]
    gonames = gonames[CATE]
    with torch.no_grad():
        with open(os.path.join(save_path, 'infer_result.tsv'), 'w') as f:
            f.write('Proteins\tGonames\tGoterms\tProbability\n')
            for i, batch_data in enumerate(test_loader):
                esm_data, protein_data,threeDi_feature_seq , id = batch_data
                esm_data= esm_data.to(device) # 8 dssp feature
                protein_data= protein_data.to(device)  # esm feature
                threeDi_feature_seq  = threeDi_feature_seq.to(device)
                output,_ = model(esm_data, protein_data, threeDi_feature_seq )
                act_output = torch.sigmoid(output)
                act_output = act_output.cpu().detach().numpy()
                
                for j in range(len(act_output[0])):
                    f.write(f'{id[0]}\t{gonames[j]}\t{goterms[j]}\t{act_output[0][j]:.4f}\n')
    Results_pd=pd.read_csv(os.path.join(save_path, 'infer_result.tsv'),sep='\t')   
    return Results_pd
    





def load_model(checkpoint = '' , device='cpu', cate = ''):
    args = create_parser()
    model = create_model(args , cate)
    if(checkpoint != ''):
        model.load_state_dict(torch.load(checkpoint,map_location='cpu'))
    model = model.to(device)
    return model


if __name__ == '__main__':
    inputpdb='predict.pdb'
    CATE='CC'
    evaluation_file =GOpredict(inputpdb ,device,CATE,save_path = 'Results',dssp_executable='/usr/bin/dssp',
                               foldseek_executable='/home/ranzixu/Protein_function/feature_extracter/foldseek/bin/foldseek')

    
