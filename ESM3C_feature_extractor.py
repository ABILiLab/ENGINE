from esm.sdk.forge import ESM3ForgeInferenceClient
from esm.sdk.api import ESMProtein, LogitsConfig

protein = ESMProtein(sequence="AAAAA")

# Apply for forge access and get an access token
import tqdm
import os 
import glob
import pickle
import argparse

def read_file(file_path):
    data = []
    with open(file_path,'r') as f:
        lines = f.readlines()
        for line in lines:
            data.append(line.strip())
    return data

def main_PFresGO_Datasets(f):
   """
   : return: shape [n, 2560]
   """
   save_path = 'GUI/Features/esm-c'
   forge_client = ESM3ForgeInferenceClient(model="esmc-6b-2024-12", url="https://forge.evolutionaryscale.ai", token="****") # API Token
   data = read_file(f)

   for id_path in tqdm.tqdm(data):
      id = os.path.basename(id_path).split('.')[0]
      protein = ESMProtein.from_pdb(id_path)
      protein = ESMProtein(sequence=protein.sequence)
      file_save_path = os.path.join(save_path, f"{id}.pkl") 
      if(os.path.exists(file_save_path)):
         continue

      protein_tensor = forge_client.encode(protein)
      logits_output = forge_client.logits(
            protein_tensor, LogitsConfig(sequence=True, return_embeddings=True)
        )
      convert_embedding =  logits_output.embeddings.detach().numpy()[0][1:-1]
      pickle.dump(convert_embedding  , open( file_save_path , 'wb')  )


if __name__ == "__main__":

   arg = argparse.ArgumentParser()
   arg.add_argument('--input_file',type=str)
   config = arg.parse_args()
   main_PFresGO_Datasets(config.input_file)
   