from Bio import PDB
import argparse
import numpy as np
 
aa_codes = {
    'ALA': 'A',
    'CYS': 'C',
    'ASP': 'D',
    'GLU': 'E',
    'PHE': 'F',
    'GLY': 'G',
    'HIS': 'H',
    'LYS': 'K',
    'ILE': 'I',
    'LEU': 'L',
    'MET': 'M',
    'ASN': 'N',
    'PRO': 'P',
    'GLN': 'Q',
    'ARG': 'R',
    'SER': 'S',
    'THR': 'T',
    'VAL': 'V',
    'TYR': 'Y',
    'TRP': 'W',
}
def extract_sequence_from_pdb(pdb_file):
    parser = PDB.PDBParser()
    structure = parser.get_structure('PDB', pdb_file)
    
    seq = []
    rec = structure[0]
    chain_id = 0

    
    for i, chain in enumerate(rec):
        if i != chain_id:##select chain A:i=0 or B:i=1
            continue
        for residue in filter(lambda r: r.get_resname() != 'HOH',chain):
            for atom in filter(lambda a: a.name =='CA' , residue):
                seq.append(aa_codes[str(residue).split(" ")[1]])

    
    return ''.join(seq)
    
def create_parser():
    parser = argparse.ArgumentParser()

    # train strategy
    parser.add_argument("--p",type=float,default=0.5,
                        help="please select the noise probability of labelnoise")
    parser.add_argument("--use_sasa",action="store_true",
                        help="whether to use the sasa feature")
    parser.add_argument("--use_bfactor",action="store_true",
                        help="whether to use the bfactor feature")
    parser.add_argument("--use_dihedral",action="store_true",
                        help="whether to use the dihedral feature")
    parser.add_argument("--use_coordinate",action="store_true",
                        help="whether to use the coordinate feature")
    parser.add_argument("--lambda1",type=float,default=0.2,
                        help="lambda1 in sasa,bfactor,corrdinate loss")
    parser.add_argument("--lambda2",type=float,default=0.5,
                        help="lambda2 in dihedral loss")
    parser.add_argument("--use_denoise",action="store_true",
                        help="whether to ues denoise")
    parser.add_argument("--noise_type",type=str,default="wild",
                        help="what kind of noise adding on protein, either wild or substitute")
    parser.add_argument("--date",type=str,default="Sep_25th",
                        help="date using save the filename")
    parser.add_argument("--gnn",type=str,default="egnn",
                        help="GNN gin, gin-virtual, or gcn, or gcn-virtual or egnn (default: gin-virtual)")

    # train model
    parser.add_argument("--problem_type",type=str,default="multi_label_classification")
    parser.add_argument("--lr", type=float, default=1e-3,
                        help="learning rate")
    parser.add_argument("--init_lr",type=float,default=1e-7,
                        help="init learning rate for warmup")
    parser.add_argument("--warmup",type=int,default=0,
                        help="warm up step")
    parser.add_argument("--weight_decay",type=float,default=1e-2,
                        help="weight_decay")
    parser.add_argument("--num_classes",type=int,default=20,
                        help="number of GNN output (default: 20)")
    parser.add_argument("--epochs",type=int,default=300,
                        help="number of epochs to train (default: 100)")
    parser.add_argument("--step_schedule",type=int,default=350,
                        help="number of epoch schedule lr")
    parser.add_argument("--batch_token_num",type=int,default=4096,
                        help="how many tokens in one batch")
    parser.add_argument("--max_graph_token_num",type=int,default=4000,
                        help="max token num a graph has")
    parser.add_argument("--node_dim",type=int,default=26,
                        help="number of node feature")
    parser.add_argument("--edge_dim",type=int,default=93,
                        help="number of edge feature")
    parser.add_argument("--layer_num",type=int,default=6,
                        help="number of layer")
    parser.add_argument("--input_dim",type=int,default= 1293, #31 or 1293
                        help="dim of input")
    parser.add_argument("--ouput_dim",type=int,default= 1943, #31 or 1293
                        help="dim of input")
    parser.add_argument("--dropout",type=float,default=0,
                        help="dropout rate")
    parser.add_argument("--subtitude_label",action="store_true",
                        help="whether smooth the label by subtitude table")
    parser.add_argument("--JK",type=str,default="last",
                        help="using what nodes embedding to make prediction,last or sum")
    parser.add_argument("--portion",type=int,default=40,
                        help="mix ratio of af and cath dataset")
    parser.add_argument("--clip",type=float,default=4.0,
                        help="mix ratio of af and cath dataset")
    
    # dataset 
    parser.add_argument("--mix_dataset",action="store_true",
                        help="whether mix alphafold and cath dataset")
    parser.add_argument("--c_alpha_max_neighbors",type=int,default=10,
                        help="the parameter of KNN which used construct the graph, 10 or 20")

    #Attention: If you have dataset,you can change these with your dataset!
    parser.add_argument("--protein_dataset",type=str,default="data/cath40_k10_dyn_imem",
                        help="main protein dataset")
    parser.add_argument("--mutant_dataset",type=str,default="data/evaluation",
                        help="mutation dataset")
    parser.add_argument("--gnn_config",type=str,default="src/Egnnconfig/egnn.yaml",
                        help="gnn config")
    parser.add_argument("--data_list",type=str,default="")
    parser.add_argument("--cate",type=str,default="src/Egnnconfig/egnn.yaml",
                        help="gnn config")

    args = parser.parse_args()
    return args

def deal3DiRes(threeDifile):
    with open(threeDifile) as inF:
        for line in inF:
            line = line.strip().split("\t")
            ## 3Di Token
            token_3di = line[-2].strip()
            ## 3Di Embedding
            matrix_3di = np.array(line[-1].strip().split(","), dtype=float)
            matrix_3di_reshape = matrix_3di.reshape(-1,10) 
            break
        return token_3di, matrix_3di_reshape
 
    
if __name__ == "__main__":
    seq = extract_sequence_from_pdb("./AF-F7EMJ6-F1-model_v4.pdb")
    sequence = "MAATMRFFPILCLVLFFSHGVASRQRSHSKEKKKSKESSVGAVGTSRSRDFAFRLYRALASEAPGQNVFFSPMSVSMSLGMLSLGSGLKTKAQILEGLGLSLQQGQEDMLHKGFQQLLQQFSQPSDGLQLSLGSALFTDPAVHIRDHFLSAMKTLYMSDMFSTNFGNPESAKKQINDYVAKKTNGKIVDLIKDLDSTHVMVVVNYIFFKAKWQTAFSSTNTHKMDYHVTPKKTIQVPMMNREDIYSYILDQNISCTVVGIPYQGNTFALFILPSEGKMKRVEDGLDERTLRNWLKMFTKRQLDLYLPKFSIEGTYKLEKILPKLGIQDIFTTHADLSGLTDHTNIKLSEMVHKSMVEVDESGTTAAASTGILFTLRSARPSSLKVEFTRPFLVVIMDGTNLYFIGKVIQP"
    print('pdb: ',seq)
    print('uniprot ',sequence)



