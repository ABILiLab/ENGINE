from torch_geometric.nn import GCNConv, global_add_pool
import torch 
import torch.nn.functional as F

import torch.nn as nn
from src.Module.egnn.network import EGNN_GCN_DSSP_ESM3,EGNN 

class GNN_model(nn.Module):
    torch.manual_seed(12345)
    
    def __init__(self, gnn_config, args):
        super().__init__()
       
        # load graph network config which usually not change
        self.gnn_config = gnn_config
        # load global config
        self.args = args
        
        if hasattr(args, "layer_num"):
            self.gnn_config["n_layers"] = args.layer_num
        if hasattr(args, "input_dim"):
            self.gnn_config["input_dim"] = args.input_dim
        if hasattr(args, "dropout"):
            self.gnn_config["dropout"] = args.dropout
        if hasattr(args, "problem_type"):
            self.gnn_config["problem_type"] = args.problem_type
        
        # calculate input dim according to the input feature
        self.out_dim=self._calculate_output_dim()
        # self.input_dim = self._calculate_input_dim()
        self.input_dim = self.gnn_config["input_dim"]
        self.device_count = torch.cuda.device_count()
        # gnn on the rest cudas
        if "egnn" in self.args.gnn:
            self.GNN_model = EGNN(self.gnn_config,self.input_dim,self.out_dim)
        else:
            raise KeyError(f"No implement of {self.args.gnn}")
        if self.device_count > 2:
            self.GNN_model = nn.DataParallel(self.GNN_model, device_ids=[i for i in range(1, self.device_count)])
        self.GNN_model=self.GNN_model.to("cuda:1") if self.device_count == 2 else self.GNN_model.to("cuda:0")

    def forward(self, esm_data, protein_data):
        # gnn_out = self.GNN_model(data)
        # self.GNN_model's class is EGNN
        # () => forward
        gnn_out = self.GNN_model(esm_data, protein_data)
        return gnn_out
    
    @torch.no_grad()
    def _calculate_input_dim(self):
        input_size = 26
        return input_size
    
    @torch.no_grad()
    def _calculate_output_dim(self):
        output_dim = 20
        if self.args.use_sasa:
            output_dim += 1
        if self.args.use_bfactor:
            output_dim += 1
        if self.args.use_dihedral:
            output_dim += 6
        if self.args.use_coordinate:
            output_dim += 3
        return output_dim

class AModel(torch.nn.Module):
    def __init__(self, num_features=9, num_classes=2000): 
        super(AModel, self).__init__()
        # data protein [node_num , num_features] : [100 , 9]
        self.conv1 = GCNConv(num_features , 128)
        self.conv2 = GCNConv(128, num_classes )


    def forward(self, data):
        # x : [100,1024]
        # edge_index : [2, 1000]
        # batch : 2
        x, edge_index, batch = data.x, data.edge_index, data.batch
        # layer1
        x = self.conv1(x, edge_index)
        x = F.relu(x)
        # layer2
        x = self.conv2(x, edge_index)
        x = global_add_pool(x, batch)
        return F.sigmoid(x)

class GNN_model_EGNN_DSSP_ESM3(nn.Module):
    '''
    task: dssp as node into egnn, esm and token as sequence channel
    '''
    torch.manual_seed(12345)
    
    def __init__(self, gnn_config, args):
        super().__init__()
       
        # load graph network config which usually not change
        self.gnn_config = gnn_config
        # load global config
        self.args = args
        
        if hasattr(args, "layer_num"):
            self.gnn_config["n_layers"] = args.layer_num
        if hasattr(args, "input_dim"):
            self.gnn_config["input_dim"] = args.input_dim
        if hasattr(args, "dropout"):
            self.gnn_config["dropout"] = args.dropout
        if hasattr(args, "problem_type"):
            self.gnn_config["problem_type"] = args.problem_type
        
        # calculate input dim according to the input feature
        self.out_dim=self._calculate_output_dim()
        # self.input_dim =argsself._calculate_input_dim()
        self.input_dim = self.gnn_config["input_dim"]
        self.device_count = torch.cuda.device_count()
        # gnn on the rest cudas
        if "egnn" in self.args.gnn:
            self.GNN_model = EGNN_GCN_DSSP_ESM3(self.gnn_config,self.input_dim,self.out_dim)
        else:
            raise KeyError(f"No implement of {self.args.gnn}")
        if self.device_count > 2:
            self.GNN_model = nn.DataParallel(self.GNN_model, device_ids=[i for i in range(1, self.device_count)])
        self.GNN_model=self.GNN_model.to("cuda:1") if self.device_count == 2 else self.GNN_model.to("cuda:0")

    def forward(self, esm_data, protein_data, threeDi_seq  , mask=None, edge_mask=None):
        # gnn_out = self.GNN_model(data)
        # self.GNN_model's class is EGNN
        # () => forward
        gnn_out = self.GNN_model(esm_data, protein_data,threeDi_seq, mask,edge_mask)
        return gnn_out

    def visual(self, esm_data, protein_data, threeDi_seq ):
        gnn_out = self.GNN_model.visual(esm_data, protein_data,threeDi_seq)
        return gnn_out
    
    @torch.no_grad()
    def _calculate_input_dim(self):
        input_size = 26
        return input_size
    
    @torch.no_grad()
    def _calculate_output_dim(self):
        output_dim = 20
        if self.args.use_sasa:
            output_dim += 1
        if self.args.use_bfactor:
            output_dim += 1
        if self.args.use_dihedral:
            output_dim += 6
        if self.args.use_coordinate:
            output_dim += 3
        return output_dim
    