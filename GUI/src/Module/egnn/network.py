import torch
import torch.nn as nn
from torch_scatter import scatter_mean
from torch_geometric.nn import global_mean_pool as gap
from torch_geometric.nn import GCNConv,Sequential

from src.Module.egnn.egnn_pytorch_geometric import EGNN_Sparse, Edge_EGNN_Sparse
from src.Module.egnn.utils import get_edge_feature_dims, get_node_feature_dims

class nodeEncoder(torch.nn.Module):

    def __init__(self, emb_dim):
        super(nodeEncoder, self).__inie__()

        self.atom_embedding_list = torch.nn.ModuleList()
        self.node_feature_dim = get_node_feature_dims()
        for i, dim in enumerate(self.node_feature_dim):
            emb = torch.nn.Linear(dim, emb_dim)
            torch.nn.init.xavier_uniform_(emb.weight.data)
            self.atom_embedding_list.append(emb)

    def forward(self, x):
        x_embedding = 0
        feature_dim_count = 0
        for i in range(len(self.node_feature_dim)):
            x_embedding += self.atom_embedding_list[i](
                x[:, feature_dim_count:feature_dim_count + self.node_feature_dim[i]])
            feature_dim_count += self.node_feature_dim[i]
        return x_embedding


class edgeEncoder(torch.nn.Module):

    def __init__(self, emb_dim):
        super(edgeEncoder, self).__init__()
        self.atom_embedding_list = torch.nn.ModuleList()
        self.edge_feature_dims = get_edge_feature_dims()
        for i, dim in enumerate(self.edge_feature_dims):
            emb = torch.nn.Linear(dim, emb_dim)
            torch.nn.init.xavier_uniform_(emb.weight.data)
            self.atom_embedding_list.append(emb)

    def forward(self, x):
        x_embedding = 0
        feature_dim_count = 0
        for i in range(len(self.edge_feature_dims)):
            x_embedding += self.atom_embedding_list[i](
                x[:, feature_dim_count:feature_dim_count + self.edge_feature_dims[i]])
            feature_dim_count += self.edge_feature_dims[i]
        return x_embedding


class EGNN(nn.Module):
    def __init__(self, config, input_dim, out_dim):
        super(EGNN, self).__init__()
        self.config = config
        if(self.config["cls_layer_type"] == 'transformer'):
            print('Using transformer cls layer,if you want to choose linear layer,please change cls_layer_type in egnn.yaml')

        if config["embedding"]:
            self.node_embedding = nn.Linear(input_dim, config["node_embedding_dim"])
            input_dim = config["node_embedding_dim"]
            # self.edge_embedding = edgeEncoder(input_dim)
        
        self.mpnn_layes = nn.ModuleList([
            EGNN_Sparse(
                input_dim, 
                m_dim=int(self.config["hidden_channels"]), 
                edge_attr_dim=int(self.config["edge_attr_dim"]), 
                dropout=int(self.config["dropout"]), 
                mlp_num=int(self.config["mlp_num"])) 
            for _ in range(int(self.config["n_layers"]))])
        
        
        
        if config["problem_type"] == "multi_label_classification":
            self.cls_layer = nn.Sequential(
                nn.Linear(input_dim + 1024, 2*config["hidden_channels"]), 
                nn.ReLU(inplace=True),
                nn.Dropout(p=0.1),
                nn.Linear(2*config["hidden_channels"], config["num_labels"])
            )
        self.tf_cls_layer = TransFormer_CLassifier(config, input_dim + 1024 , config["num_labels"])
        self.lin = nn.Linear(input_dim, out_dim)
        self.droplayer = nn.Dropout(float(self.config["dropout"]))
        
    def forward(self, data ,protein_data):
        # data -> esm2 data + dssp   : 271 line esm_data
        # protein_data -> protein bert data :271 line protein_data
        # x-> node feature of esm2
        x, pos, edge_index, edge_attr, batch = (
            data.x, data.pos, 
            data.edge_index,
            data.edge_attr, data.batch
        )
        # proetein bert operation
        protein_branch = gap(protein_data.x, batch = batch)
        
        input_x = torch.empty([pos.shape[0], 0]).to(x.device)
        input_x = torch.cat([input_x, x], dim=1)
        mu_r_norm = data.mu_r_norm
        input_x = torch.cat([input_x, mu_r_norm], dim=1)
        
        
        if self.config['embedding']:
            input_x = self.node_embedding(input_x)
            # edge_attr = self.edge_embedding(edge_attr)
        input_x = torch.cat([pos, input_x], dim=1)
        
        for i, layer in enumerate(self.mpnn_layes):
            h = layer(input_x, edge_index, edge_attr, batch)
            if self.config['residual']:
                input_x = input_x + h
            else:
                input_x = h
                
        x = input_x[:, 3:]
        if self.config["problem_type"] == "multi_label_classification":
            # TODO MARK
            # graph branch's output
            # graph's feature
            x_mean = scatter_mean(x, batch, dim=0)
            # concatenate sequence's feature with graph's feature
            concate_x =  torch.concat([x_mean, protein_branch], dim=1)
            if(self.config["cls_layer_type"] == 'transformer'):
                x = self.tf_cls_layer(concate_x)
            else:
                x = self.cls_layer(concate_x) # cls_layer -> fc
            return x, x_mean
        elif self.config["problem_type"] == "aa_classification":
            x = self.droplayer(x)
            x = self.lin(x)
        return x
        

class EGNN_GCN_DSSP_ESM3(nn.Module):
    
    def __init__(self, config, input_dim, out_dim):
        super(EGNN_GCN_DSSP_ESM3, self).__init__()
        self.config = config
        # if(self.config["cls_layer_type"] == 'transformer'):
            # print('Using transformer cls layer,if you want to choose linear layer,please change cls_layer_type in egnn.yaml')
        if config["embedding"]:
            self.node_embedding = nn.Linear(input_dim, config["node_embedding_dim"])
            input_dim = config["node_embedding_dim"]
            # self.edge_embedding = edgeEncoder(input_dim)
        
        self.emb =  nn.Embedding(21,128)
        self.mpnn_layes = nn.ModuleList([
            EGNN_Sparse(
                input_dim, 
                m_dim=int(self.config["hidden_channels"]), 
                edge_attr_dim=int(self.config["edge_attr_dim"]), 
                dropout=int(self.config["dropout"]), 
                mlp_num=int(self.config["mlp_num"])) 
            for _ in range(int(self.config["n_layers"]))])
        
        
        
        if config["problem_type"] == "multi_label_classification":
            self.cls_layer = nn.Sequential(
                # nn.Linear(input_dim + 1024 +1+32, 2*config["hidden_channels"]), 
                # nn.Linear(input_dim + 1152 +1, 2*config["hidden_channels"]),     # 改为esm3
                # nn.Linear(input_dim + 2560 +1, 2*config["hidden_channels"]),     # 改为esm3_6B
                nn.Linear(input_dim + 2560 +128, 2*config["hidden_channels"]),     # 改为esm3
                nn.ReLU(inplace=True),
                nn.Dropout(p=0.1),
                nn.Linear(2*config["hidden_channels"], config["num_labels"]),
                # nn.Sigmoid()
            )
        # self.tf_cls_layer = TransFormer_CLassifier(config, input_dim + 1280 + 1, config["num_labels"])
        self.lin = nn.Linear(input_dim, out_dim)
        self.droplayer = nn.Dropout(float(self.config["dropout"]))
        
    def visual(self, data ,protein_data, threeDi_seq ):
        x, pos, edge_index, edge_attr, batch = (
            data.x, data.pos, 
            data.edge_index,
            data.edge_attr, data.batch
        )
        esm_branch = gap(protein_data.x, batch = batch)
        threeDi_seq_branch = gap(threeDi_seq.x, batch = batch)
        threeDi_seq_branch = threeDi_seq_branch.unsqueeze(1)
        input_x = torch.empty([pos.shape[0], 0]).to(x.device)
        input_x = torch.cat([input_x, x], dim=1)
        mu_r_norm = data.mu_r_norm
        input_x = torch.cat([input_x, mu_r_norm], dim=1)
        if self.config['embedding']:
            input_x = self.node_embedding(input_x)
        input_x = torch.cat([pos, input_x], dim=1)
        
        for i, layer in enumerate(self.mpnn_layes):
            h = layer(input_x, edge_index, edge_attr, batch)
            if self.config['residual']:
                input_x = input_x + h
            else:
                input_x = h
        
                
        x = input_x[:, 3:]
        # 1. egnn feature
        egnn_output = x
        # 2. esm branch
        esm_output = esm_branch
        x_mean = scatter_mean(x, batch, dim=0)
        concate_x =  torch.concat([x_mean, esm_branch, threeDi_seq_branch], dim=1)
        # 2. egnn feature
        cls_output = self.cls_layer[0](concate_x)
        return egnn_output, esm_output,concate_x, cls_output

    def forward(self, data ,protein_data, threeDi_seq , mask = None, edge_mask = None):
        # data -> esm2 data + dssp   : 271 line esm_data
        # protein_data -> protein bert data :271 line protein_data
        # x-> node feature of esm2
        x, pos, edge_index, edge_attr, batch = (
            data.x, data.pos, 
            data.edge_index,
            data.edge_attr, data.batch
        )
        if(edge_mask is not None):
            edge_attr = edge_attr * edge_mask.unsqueeze(1)
        if(mask is not None):
            x = x * mask

        # esm featrue operation
        esm_branch = gap(protein_data.x, batch = batch)  

        # protein CKSAAP's feature operation
        # CKSAAP_branch = gap(CKSAAP_data.x, batch = batch)

        # protein foldseek 3Di sequence feature
        threeDi_seq.x =  self.emb(threeDi_seq.x)
        threeDi_seq_branch = gap(threeDi_seq.x, batch = batch)
        # threeDi_seq_branch = threeDi_seq_branch.unsqueeze(1)

        input_x = torch.empty([pos.shape[0], 0]).to(x.device)
        input_x = torch.cat([input_x, x], dim=1)
        mu_r_norm = data.mu_r_norm
        input_x = torch.cat([input_x, mu_r_norm], dim=1)
        
        
        if self.config['embedding']:
            input_x = self.node_embedding(input_x)
            # edge_attr = self.edge_embedding(edge_attr)
        input_x = torch.cat([pos, input_x], dim=1)
        
        for i, layer in enumerate(self.mpnn_layes):
            h = layer(input_x, edge_index, edge_attr, batch)
            if self.config['residual']:
                input_x = input_x + h
            else:
                input_x = h
                
        x = input_x[:, 3:]
        if self.config["problem_type"] == "multi_label_classification":
            # TODO MARK
            # graph branch's output
            # graph's feature
            x_mean = scatter_mean(x, batch, dim=0)
            # concatenate sequence's feature with graph's feature
            concate_x =  torch.concat([x_mean, esm_branch, threeDi_seq_branch], dim=1)
            # if(self.config["cls_layer_type"] == 'transformer'):
                # x = self.tf_cls_layer(concate_x)
            # else:
            x = self.cls_layer(concate_x) # cls_layer -> fc
            return x, x_mean
        elif self.config["problem_type"] == "aa_classification":
            x = self.droplayer(x)
            x = self.lin(x)
        return x
    
class TransFormer_CLassifier(nn.Module):
    def __init__(self, config, input_dim, output_dim):
        super(TransFormer_CLassifier, self).__init__()
        self.config = config
        self.convert_layer = nn.Sequential(nn.Linear(input_dim, 64),nn.SELU(True))
        self.layer = nn.TransformerEncoderLayer(d_model=64, nhead=8, dim_feedforward=2048, dropout=0.1, activation="relu")
        self.cls_layer = nn.Linear(64, output_dim)
        # self.sigmoid = nn.Sigmoid()

    def forward(self, data):
        data = self.convert_layer(data) 
        x = self.layer(data.unsqueeze(1))
        x = self.cls_layer(x.squeeze(1))
        x = self.sigmoid(x)
        return x