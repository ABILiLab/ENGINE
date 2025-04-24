# Advancing Protein Function Annotation with Equivariant Graph Networks
Protein function research helps in understanding complex biological processes within cells. However, the intricate nature of protein structures and functions, along with the rapid growth of protein sequence data, presents a pressing challenge to develop efficient computational methods for protein annotation. In this study, we propose ENGINE, a multi-channel deep learning framework designed for robust protein function annotation. ENGINE integrates an equivariant graph convolutional network model to capture geometric features from protein 3D structurals, leverages ESM-C to encode evolutionary and sequence-derived information, and combines an innovative 3D sequence representation that unifies spatial and sequential signals. We demonstrate that ENGINE consistently surpasses current state-of-the-art methods across diverse protein function prediction benchmarks, demonstrating robust generalization and high predictive accuracy. Beyond performance, ENGINE provides interpretable insights into key sequence features and substructures, enabling the identification of functionally critical residues within proteins. This facilitates a deeper mechanistic understanding of protein function annotation outcomes and supports hypothesis generation for downstream biological studies. By offering reliable predictions with biological interpretability, ENGINE contributes to advancing research into cellular processes and disease mechanisms.
# Data
The original input dataset is in **FASTA format**, containing amino acid sequences of target proteins. To obtain corresponding 3D structures in **PDB format**, we use [**ESMFold**](https://github.com/facebookresearch/esm) for structure prediction.
# Environment
Anaconda  
python 3.8
# Dependency
### Bioinformatics
biopython==1.83  
bio==1.6.2  
mygene==3.2.2  
biothings-client==0.3.1  
obonet==1.1.0  
gprofiler-official==1.0.0  
propcache==0.2.0
### Machine Learning & GNN
torch==1.11.0+cu113  
torch-cluster==1.6.0  
torch_geometric==2.5.3  
torch-scatter==2.0.9  
torch-sparse==0.6.14  
torch-spline-conv==1.2.1  
egnn-pytorch==0.2.8  
scikit-learn==1.3.2  
joblib==1.4.2  
networkx==3.1  
opencv-python==4.11.0.86  
### Data & Visualization
numpy==1.24.4  
pandas==2.0.3  
scipy==1.10.1  
matplotlib==3.7.5  
seaborn==0.13.2  
### Utilities
pyyaml==6.0.2  
click==8.1.8  
requests==2.32.3  
aiohttp==3.10.11  
ttach==0.0.3  
grad-cam==1.5.4  
### Development & System Libraries
attrs==24.3.0  
backcall==0.2.0  
pyzmq==25.1.2  
qdarkstyle==3.2.3  
qt-material==2.14  
qtpy==2.4.3  
# Feature extraction and tool description
### **Foldseek**
Extracting 3Di Tokens with Foldseek :
 [github.com/steineggerlab/foldseek.](https://github.com/steineggerlab/foldseek) Change to the corresponding Foldseek path in the **infer_main.py** file.
### **DSSP**
 Extraction of secondary structure features using [DSSP.](https://swift.cmbi.umcn.nl/gv/dssp/) Change to the corresponding DSSP path in the **infer_main.py** file
### **ESM-C**
We use the ESM-C 6B model provided by ESM
(https://github.com/evolutionaryscale/esm) for sequence embedding extraction, which is currently only supported by the Forge API. Go to https://forge.evolutionaryscale.ai/ and register an account to get the API Token.   
The **infer_main.py** file in the project uses the **Features/esm-c** path to read features by default. Please change the path to the actual location according to the result you downloaded. Example:
```python
# Modify feature loading location
esm3_6B_path = 'Features/esm-c'  # Please change the path to the file you actually downloaded
```
# Create Environment with Conda
First, create the environment.  
```python
conda create -n ENGINE python=3.8
```
Then, activate the "ENGINE" environment and enter into the workspace.
```python
conda activate ENGINE
pip install -r requirements.txt
```
# Usage
The **infer_temp** folder allows you to batch store PDB files that need to be tested and enter MF, BP or CC categories at runtime. The model file corresponding to the corresponding path in **infer_main.py** is saved in [here](https://zenodo.org/records/15276485), just download it and save it to the model folder.
For example:
```python
python ENGINE_main.py --data_list ./infer_temp --cate cc
```
The sample output file is **infer_result.csv** with the following sample content:
```python
4RH6-A,cell outer membrane,GO:0009279,0.5082
4RH6-A,cell division site,GO:0032153,0.0011
4RH6-A,cytoplasmic side of plasma membrane,GO:0009898,0.0002
4RH6-A,nuclear chromatin,GO:0000790,0.0000
4RH6-A,virion membrane,GO:0055036,0.0049
4RH6-A,inner mitochondrial membrane protein complex,GO:0098800,0.0000
4RH6-A,ribosome,GO:0005840,0.0011
4RH6-A,thylakoid,GO:0009579,0.0015
4RH6-A,nuclear envelope,GO:0005635,0.0027
4RH6-A,spliceosomal snRNP complex,GO:0097525,0.0000
4RH6-A,NADH dehydrogenase complex,GO:0030964,0.0001
4RH6-A,nucleoid,GO:0009295,0.0001
4RH6-A,respirasome,GO:0070469,0.0035
4RH6-A,neuron to neuron synapse,GO:0098984,0.0000
4RH6-A,bacterial-type flagellum,GO:0009288,0.0004
4RH6-A,cell surface,GO:0009986,0.1694
4RH6-A,host cell membrane,GO:0033644,0.1396
```
# GUI (Graphical user interface)
## Introduction
The platform integrates protein functional annotation with ENGINE. It allows you to use PDB inputs to predict information about protein function and visualise score alignments.
## Running Environment
* Anaconda
* python 3.10.13
## Running Methods
  - Step 1. Download and install the anaconda platform. (Refer to https://blog.csdn.net/m0_61607990/article/details/129531686).
   - Step 2. Enter the "GUI" folder.
   - Step 3. Using the conda environment ENGINE above
  - Step 4. Run ENGINE
  ```python
  python ENGINE_GUI_platform.py
  ```
## Use ENGINE in this platform
After successfully running the ENGINE_GUI_platform.py file, you can follow the steps below to use ENGINE on our platform.
### Input Data
- Please upload a PDB file for one of the proteins you want to predict!
### Select Parameters
- Set 'MF', 'BP', or 'CC' and choose one of the categories for GO terms prediction.
### Predict and save results
- Clicking the ‘Predict’ button allows you to perform prediction operations on the input PDB and selected parameters.  
- Click ‘Save results’ button to save the prediction result as a csv file.  
- If you want to continue to predict other proteins, please click ‘Clean’ button first.
### Results display
