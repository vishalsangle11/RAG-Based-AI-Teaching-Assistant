import joblib
import requests
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

df = joblib.load("Embedding.joblib")

def createEmbedding(text_lst):
    r=requests.post("http://localhost:11434/api/embed",json={
        "model":"bge-m3",
        "input":text_lst
    })

    embedding=r.json()["embeddings"]
    return embedding


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
print(newDf)
# print(newDf[["START","END","VideoName","TEXT","VideoNumber"]])

prompt=f'''
Here are video subtitle chunks containg start time in seconds , end time in seconds , video Name , Text at that time and video number 
{newDf[["START","END","VideoName","TEXT","VideoNumber"]].to_json(orient="records")}
--------------------------------------------------------------------------------------
{question_asked}
User asked this question related to video chunks , you have to answer where and how much content is taught in which video(Give the timestamp of the video) and guide the user to go to that video . If user asks any unrelated thing you tell hime that you can answer the query related to the course only 
'''

# for idx,item in newDf.iterrows():
#     print(idx,item["START"],item["END"],item["VideoName"],item["TEXT"],item["VideoNumber"])

def inference(prompt):
    r=requests.post("http://localhost:11434/api/generate",json={
        "model":"llama3.2",
        "prompt":prompt,
        "stream":False
    })

    response = r.json()
    print(response)
    return response

response=inference(prompt)["response"]
print(response)
with open("Response.txt","w") as f:
    f.write(response)

with open("Prompt.txt","w") as f:
    f.write(prompt)


