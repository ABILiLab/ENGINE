import warnings
from Bio.PDB import PDBParser, ShrakeRupley
from Bio.PDB.PDBExceptions import PDBConstructionWarning
import numpy as np
import torch
import math
from src.Dataset.dataset_utils import safe_index, one_hot_res, log, dihedral, NormalizeProtein,get_stat
from scipy.special import softmax
from torch_geometric.data import Data
import scipy.spatial as spa
import torch.nn.functional as F

allowable_features = {
    'possible_atomic_num_list': list(range(1, 119)) + ['misc'],
    'possible_chirality_list': [
        'CHI_UNSPECIFIED',
        'CHI_TETRAHEDRAL_CW',
        'CHI_TETRAHEDRAL_CCW',
        'CHI_OTHER'
    ],
    'possible_degree_list': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'misc'],
    'possible_numring_list': [0, 1, 2, 3, 4, 5, 6, 'misc'],
    'possible_implicit_valence_list': [0, 1, 2, 3, 4, 5, 6, 'misc'],
    'possible_formal_charge_list': [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 'misc'],
    'possible_numH_list': [0, 1, 2, 3, 4, 5, 6, 7, 8, 'misc'],
    'possible_number_radical_e_list': [0, 1, 2, 3, 4, 'misc'],
    'possible_hybridization_list': [
        'SP', 'SP2', 'SP3', 'SP3D', 'SP3D2', 'misc'
    ],
    'possible_is_aromatic_list': [False, True],
    'possible_is_in_ring3_list': [False, True],
    'possible_is_in_ring4_list': [False, True],
    'possible_is_in_ring5_list': [False, True],
    'possible_is_in_ring6_list': [False, True],
    'possible_is_in_ring7_list': [False, True],
    'possible_is_in_ring8_list': [False, True],
    'possible_amino_acids': ['ALA', 'ARG', 'ASN', 'ASP', 'CYS', 'GLN', 'GLU', 'GLY', 'HIS', 'ILE', 'LEU', 'LYS',
                                'MET',
                                'PHE', 'PRO', 'SER', 'THR', 'TRP', 'TYR', 'VAL', 'HIP', 'HIE', 'TPO', 'HID', 'LEV',
                                'MEU',
                                'PTR', 'GLV', 'CYT', 'SEP', 'HIZ', 'CYM', 'GLM', 'ASQ', 'TYS', 'CYX', 'GLZ', 'misc'],
    'possible_atom_type_2': ['C*', 'CA', 'CB', 'CD', 'CE', 'CG', 'CH', 'CZ', 'N*', 'ND', 'NE', 'NH', 'NZ', 'O*',
                                'OD',
                                'OE', 'OG', 'OH', 'OX', 'S*', 'SD', 'SG', 'misc'],
    'possible_atom_type_3': ['C', 'CA', 'CB', 'CD', 'CD1', 'CD2', 'CE', 'CE1', 'CE2', 'CE3', 'CG', 'CG1', 'CG2',
                                'CH2',
                                'CZ', 'CZ2', 'CZ3', 'N', 'ND1', 'ND2', 'NE', 'NE1', 'NE2', 'NH1', 'NH2', 'NZ', 'O',
                                'OD1',
                                'OD2', 'OE1', 'OE2', 'OG', 'OG1', 'OH', 'OXT', 'SD', 'SG', 'misc'],
}


def get_receptor_inference(rec_path):
    biopython_parser = PDBParser()
    chain_id=0
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=PDBConstructionWarning)
        structure = biopython_parser.get_structure('random_id', rec_path)
        rec = structure[0]##len(structure)=1
        head = biopython_parser.get_header()['head']
        if head.find('dna') > -1:
            return False, False, False, False, False,False
    coords = []
    c_alpha_coords = []
    n_coords = []
    c_coords = []
    valid_chain_ids = []
    lengths = []
    seq = []
    for i, chain in enumerate(rec):
        if i != chain_id:##select chain A:i=0 or B:i=1
            continue
        chain_coords = []  # num_residues, num_atoms, 3
        chain_c_alpha_coords = []
        chain_n_coords = []
        chain_c_coords = []
        count = 0
        invalid_res_ids = []
        for res_idx, residue in enumerate(chain):
            if residue.get_resname() == 'HOH':
                invalid_res_ids.append(residue.get_id())
                continue
            residue_coords = []
            c_alpha, n, c = None, None, None
            for atom in residue:
                if atom.name == 'CA':
                    c_alpha = list(atom.get_vector())
                    seq.append(str(residue).split(" ")[1])
                if atom.name == 'N':
                    n = list(atom.get_vector())
                if atom.name == 'C':
                    c = list(atom.get_vector())
                residue_coords.append(list(atom.get_vector()))
            # only append residue if it is an amino acid and not some weired molecule that is part of the complex
            if c_alpha != None and n != None and c != None:
                chain_c_alpha_coords.append(c_alpha)
                chain_n_coords.append(n)
                chain_c_coords.append(c)
                chain_coords.append(np.array(residue_coords))
                count += 1
            else:
                invalid_res_ids.append(residue.get_id())
        for res_id in invalid_res_ids:
            chain.detach_child(res_id)
        lengths.append(count)
        coords.append(chain_coords)
        c_alpha_coords.append(np.array(chain_c_alpha_coords))
        n_coords.append(np.array(chain_n_coords))
        c_coords.append(np.array(chain_c_coords))
        if len(chain_coords) > 0:
            valid_chain_ids.append(chain.get_id())
    valid_coords = []
    valid_c_alpha_coords = []
    valid_n_coords = []
    valid_c_coords = []
    valid_lengths = []
    invalid_chain_ids = []
    for i, chain in enumerate(rec):
        # print("chain:",i,chain, len(valid_coords), len(valid_chain_ids), len(coords), coords[0][0].shape, len(coords[0]))
        if i != chain_id:
            continue
        if chain.get_id() in valid_chain_ids:
            valid_coords.append(coords[0])
            valid_c_alpha_coords.append(c_alpha_coords[0])
            valid_n_coords.append(n_coords[0])
            valid_c_coords.append(c_coords[0])
            valid_lengths.append(lengths[0])
        else:
            invalid_chain_ids.append(chain.get_id())
    # list with n_residues arrays: [n_atoms, 3]
    coords = [item for sublist in valid_coords for item in sublist]
    if len(valid_c_alpha_coords) == 0:
        return False, False, False, False, False,False
    c_alpha_coords = np.concatenate(valid_c_alpha_coords, axis=0)  # [n_residues, 3]
    n_coords = np.concatenate(valid_n_coords, axis=0)  # [n_residues, 3]
    c_coords = np.concatenate(valid_c_coords, axis=0)  # [n_residues, 3]

    for invalid_id in invalid_chain_ids:
        rec.detach_child(invalid_id)

    assert len(c_alpha_coords) == len(n_coords)
    assert len(c_alpha_coords) == len(c_coords)
    assert sum(valid_lengths) == len(c_alpha_coords)
    return rec, coords, c_alpha_coords, n_coords, c_coords,seq

def get_node_features( n_coords, c_coords, c_alpha_coords, coord_mask, with_coord_mask=True, use_angle=False,
                          use_omega=False):

    num_res = n_coords.shape[0]
    if use_omega:
        num_angle_type = 3
        angles = np.zeros((num_res, num_angle_type))
        for i in range(num_res - 1):
            # These angles are called φ (phi) which involves the backbone atoms C-N-Cα-C
            angles[i, 0] = dihedral(
                c_coords[i], n_coords[i], c_alpha_coords[i], n_coords[i + 1])
            # psi involves the backbone atoms N-Cα-C-N.
            angles[i, 1] = dihedral(
                n_coords[i], c_alpha_coords[i], c_coords[i], n_coords[i + 1])
            angles[i, 2] = dihedral(
                c_alpha_coords[i], c_coords[i], n_coords[i + 1], c_alpha_coords[i + 1])
    else:
        num_angle_type = 2
        angles = np.zeros((num_res, num_angle_type))
        for i in range(num_res - 1):
            # These angles are called φ (phi) which involves the backbone atoms C-N-Cα-C
            angles[i, 0] = dihedral(
                c_coords[i], n_coords[i], c_alpha_coords[i], n_coords[i + 1])
            # psi involves the backbone atoms N-Cα-C-N.
            angles[i, 1] = dihedral(
                n_coords[i], c_alpha_coords[i], c_coords[i], n_coords[i + 1])
    if use_angle:
        node_scalar_features = angles
    else:
        node_scalar_features = np.zeros((num_res, num_angle_type * 2))
        for i in range(num_angle_type):
            node_scalar_features[:, 2 * i] = np.sin(angles[:, i])
            node_scalar_features[:, 2 * i + 1] = np.cos(angles[:, i])

    if with_coord_mask:
        node_scalar_features = torch.cat([
            node_scalar_features,
            coord_mask.float().unsqueeze(-1)
        ], dim=-1)
    node_vector_features = None
    return node_scalar_features, node_vector_features

def rec_residue_featurizer(rec, chain_id, one_hot=True, add_feature=None):
    count = 0
    flag_sasa=1
    num_residue_type: int = 20
    sr = ShrakeRupley(probe_radius=1.4,  # in A. Default is 1.40 roughly the radius of a water molecule.
                            n_points=100)  # resolution of the surface of each atom. Default is 100. A higher number of points results in more precise measurements, but slows down the calculation.
    try:
        sr.compute(rec, level="R")
    except:
        flag_sasa=0
    for i, chain in enumerate(rec.get_chains()):
        if i != chain_id:
            continue
        num_res = len(list(chain.get_residues()))#len([_ for _ in rec.get_residues()])
        num_feature = 2
        if add_feature.any():
            num_feature += add_feature.shape[1]
        res_feature = torch.zeros(num_res, num_residue_type + num_feature)
        for i, residue in enumerate(chain.get_residues()):
            if flag_sasa==0:
                residue.sasa=0
            sasa = residue.sasa
            for atom in residue:
                if atom.name == 'CA':
                    bfactor = atom.bfactor
            assert not np.isinf(bfactor)
            assert not np.isnan(bfactor)
            assert not np.isinf(sasa)
            assert not np.isnan(sasa)

            residx = safe_index(
                allowable_features['possible_amino_acids'], residue.get_resname())
            res_feat_1 = one_hot_res(
                residx, num_residue_type=num_residue_type) if one_hot else [residx]
            if not res_feat_1:
                return False
            res_feat_1.append(sasa)
            res_feat_1.append(bfactor)
            if num_feature > 2:
                res_feat_1.extend(list(add_feature[count, :]))
            res_feature[count, :] = torch.tensor(res_feat_1, dtype=torch.float32)
            count += 1
    # print("numnodes:", num_res, count,len(list(chain.get_residues())))
    for k in range(num_residue_type, num_residue_type + 2):
        mean = res_feature[:, k].mean()
        std = res_feature[:, k].std()
        res_feature[:, k] = (res_feature[:, k] -mean) / (std + 0.000000001)
    return res_feature

def distance_featurizer( dist_list, divisor):
    # you want to use a divisor that is close to 4/7 times the average distance that you want to encode
    length_scale_list = [1.5 ** x for x in range(15)]
    center_list = [0. for _ in range(15)]
    num_edge = len(dist_list)
    dist_list = np.array(dist_list)
    transformed_dist = [np.exp(- ((dist_list / divisor) ** 2) / float(length_scale))
                        for length_scale, center in zip(length_scale_list, center_list)]
    transformed_dist = np.array(transformed_dist).T
    transformed_dist = transformed_dist.reshape((num_edge, -1))
    return torch.from_numpy(transformed_dist.astype(np.float32))

def get_edge_features(src_list, dst_list, dist_list, divisor=4):
    seq_dist_cut: int = 64
    seq_edge = torch.absolute(torch.tensor(
        src_list) - torch.tensor(dst_list)).reshape(-1, 1)
    seq_edge = torch.where(seq_edge > seq_dist_cut,
                            seq_dist_cut, seq_edge)
    seq_edge = F.one_hot(
        seq_edge, num_classes=seq_dist_cut + 1).reshape((-1, seq_dist_cut + 1))
    contact_sig = torch.where(torch.tensor(
        dist_list) <= 8, 1, 0).reshape(-1, 1)
    # avg distance = 7. So divisor = (4/7)*7 = 4
    dist_fea = distance_featurizer(dist_list, divisor=divisor)
    return torch.concat([seq_edge, dist_fea, contact_sig], dim=-1)

def get_calpha_graph(rec, c_alpha_coords, n_coords, c_coords, coords, seq):
    chain_id = 0

    cutoff: int = 30
    c_alpha_max_neighbors: int = 10
    scalar_feature, vec_feature = get_node_features(n_coords, c_coords, c_alpha_coords, coord_mask=None, with_coord_mask=False, use_angle=False, use_omega=False)
    # Extract 3D coordinates and n_i,u_i,v_i
    # vectors of representative residues ################
    residue_representatives_loc_list = []
    n_i_list = []
    u_i_list = []
    v_i_list = []
    for i, chain in enumerate(rec.get_chains()):
        if i != chain_id:
            continue
        for i, residue in enumerate(chain.get_residues()):
            n_coord = n_coords[i]
            c_alpha_coord = c_alpha_coords[i]
            c_coord = c_coords[i]
            u_i = (n_coord - c_alpha_coord) / \
                np.linalg.norm(n_coord - c_alpha_coord)
            t_i = (c_coord - c_alpha_coord) / \
                np.linalg.norm(c_coord - c_alpha_coord)
            n_i = np.cross(u_i, t_i) / \
                np.linalg.norm(np.cross(u_i, t_i))   # main chain
            v_i = np.cross(n_i, u_i)
            assert (math.fabs(
                np.linalg.norm(v_i) - 1.) < 1e-5), "protein utils protein_to_graph_dips, v_i norm larger than 1"
            n_i_list.append(n_i)
            u_i_list.append(u_i)
            v_i_list.append(v_i)
            residue_representatives_loc_list.append(c_alpha_coord)

    residue_representatives_loc_feat = np.stack(residue_representatives_loc_list, axis=0)  # (N_res, 3)
    n_i_feat = np.stack(n_i_list, axis=0)
    u_i_feat = np.stack(u_i_list, axis=0)
    v_i_feat = np.stack(v_i_list, axis=0)
    num_residues = len(c_alpha_coords)
    if num_residues <= 1:
        raise ValueError(f"rec contains only 1 residue!")
    ################### Build the k-NN graph ##############################
    assert num_residues == residue_representatives_loc_feat.shape[0]
    assert residue_representatives_loc_feat.shape[1] == 3
    distances = spa.distance.cdist(c_alpha_coords, c_alpha_coords)

    src_list = []
    dst_list = []
    dist_list = []
    mean_norm_list = []
    for i in range(num_residues):
        dst = list(np.where(distances[i, :] < cutoff)[0])
        dst.remove(i)
        if c_alpha_max_neighbors != None and len(dst) > c_alpha_max_neighbors:
            dst = list(np.argsort(distances[i, :]))[
                1: c_alpha_max_neighbors + 1]
        if len(dst) == 0:
            # choose second because first is i itself
            dst = list(np.argsort(distances[i, :]))[1:2]
        assert i not in dst
        src = [i] * len(dst)
        src_list.extend(src)
        dst_list.extend(dst)
        valid_dist = list(distances[i, dst])
        dist_list.extend(valid_dist)
        valid_dist_np = distances[i, dst]
        sigma = np.array([1., 2., 5., 10., 30.]).reshape((-1, 1))
        weights = softmax(- valid_dist_np.reshape((1, -1))** 2 / sigma, axis=1)  # (sigma_num, neigh_num)
        # print(weights) why weight??
        assert weights[0].sum() > 1 - 1e-2 and weights[0].sum() < 1.01
        diff_vecs = residue_representatives_loc_feat[src, :] - residue_representatives_loc_feat[dst, :]  # (neigh_num, 3)
        mean_vec = weights.dot(diff_vecs)  # (sigma_num, 3)
        denominator = weights.dot(np.linalg.norm(diff_vecs, axis=1))  # (sigma_num,)
        mean_vec_ratio_norm = np.linalg.norm(mean_vec, axis=1) / denominator  # (sigma_num,)
        mean_norm_list.append(mean_vec_ratio_norm)
    assert len(src_list) == len(dst_list)
    assert len(dist_list) == len(dst_list)
    residue_representatives_loc_feat = torch.from_numpy(residue_representatives_loc_feat.astype(np.float32))
    x = rec_residue_featurizer(rec, chain_id, one_hot=True, add_feature=scalar_feature)
    if isinstance(x, bool) and (not x):
        return False
    ######key part to generate graph!!!!!main
    graph = Data(
        x=x,## 26 feature 20+sasa+b factor+ two face angle
        pos=residue_representatives_loc_feat,
        edge_attr=get_edge_features(src_list, dst_list, dist_list, divisor=4), ##edge features
        edge_index=torch.tensor([src_list, dst_list]),
        edge_dist=torch.tensor(dist_list),
        distances=torch.tensor(distances),
        mu_r_norm=torch.from_numpy(np.array(mean_norm_list).astype(np.float32)),
        seq = seq) ##about density capture
    # Loop over all edges of the graph and build the various p_ij, q_ij, k_ij, t_ij pairs
    edge_feat_ori_list = []
    for i in range(len(dist_list)):
        src = src_list[i]
        dst = dst_list[i]
        # place n_i, u_i, v_i as lines in a 3x3 basis matrix
        basis_matrix = np.stack(
            (n_i_feat[dst, :], u_i_feat[dst, :], v_i_feat[dst, :]), axis=0)
        p_ij = np.matmul(basis_matrix,residue_representatives_loc_feat[src, :] - residue_representatives_loc_feat[dst, :])
        q_ij = np.matmul(basis_matrix, n_i_feat[src, :])  # shape (3,)
        k_ij = np.matmul(basis_matrix, u_i_feat[src, :])
        t_ij = np.matmul(basis_matrix, v_i_feat[src, :])
        s_ij = np.concatenate((p_ij, q_ij, k_ij, t_ij), axis=0)  # shape (12,)
        edge_feat_ori_list.append(s_ij)

    edge_feat_ori_feat = np.stack(edge_feat_ori_list, axis=0)  # shape (num_edges, 4, 3)
    edge_feat_ori_feat = torch.from_numpy(edge_feat_ori_feat.astype(np.float32))
    graph.edge_attr = torch.cat([graph.edge_attr, edge_feat_ori_feat], axis=1)  # (num_edges, 17)
    # graph = self.remove_node(graph, graph.x.shape[0]-1)###remove the last node, can not calculate the two face angle
    # self.get_calpha_graph_single(graph, 6)
    return graph

def pipeline_get_protlgn(pdb_file):
    rec, rec_coords, c_alpha_coords, n_coords, c_coords,seq = get_receptor_inference(pdb_file)
    if rec !=False:
            if len(seq)>len(c_alpha_coords):
                del seq[-(len(seq)-len(c_alpha_coords)):]

    rec_graph = get_calpha_graph(rec, c_alpha_coords, n_coords, c_coords, rec_coords,seq)
    return rec_graph