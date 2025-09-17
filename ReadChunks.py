import requests
import json
import os
import pandas as pd
import numpy as np
import joblib
from sklearn.metrics.pairwise import cosine_similarity

def createEmbedding(text_lst):
    r=requests.post("http://localhost:11434/api/embed",json={
        "model":"bge-m3",
        "input":text_lst
    })

    embedding=r.json()["embeddings"]
    return embedding

jsons=os.listdir("json")
my_dicts=[]
chunk_id=0

for json_file in jsons:
    print(f"Creating embeddings for the json file {json_file}")
    with open(f"json/{json_file}") as f:
        content=json.load(f)
    embeddings = createEmbedding([c["TEXT"] for c in content["Chunks"]])
    for idx,chunk in enumerate(content["Chunks"]):
        chunk["Chunks_ID"]=chunk_id
        chunk["embedding"]=embeddings[idx]
        my_dicts.append(chunk)
        chunk_id+=1


df = pd.DataFrame.from_records(my_dicts)
# Saving the file using the joblib 
joblib.dump(df,"Embedding.joblib")
# print(df)

question_asked=input("Enter the query to be asked : ")
question_embedding=createEmbedding([question_asked])[0]
# print(question_embedding)

# Findind similarity of question embedding with other embedding 
# print(np.vstack(df["embedding"].values))
# print(np.vstack(df["embedding"].shape))
similarity=cosine_similarity(np.vstack(df["embedding"]),[question_embedding]).flatten()
topResult=3
max_idx=similarity.argsort()[::-1][0:topResult]
newDf=df.loc[max_idx]
print(newDf[["START","END","VideoName","TEXT","VideoNumber"]])