import os
import whisper
import json

audios=os.listdir("Audios")
for audio in audios:
    num=audio.split("_")[0]
    name=audio.split("_")[1][:-4]
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print(num,"->",name)
    model = whisper.load_model("large-v2")
    result = model.transcribe(audio=f"Audios/{audio}",
                         language="hi",
                         task="translate",
                         word_timestamps=False)
    chunks=[]
    for segment in result["segments"]:
        chunks.append({"START":segment["start"],"END":segment["end"],"TEXT":segment["text"],"VideoName":name,"VideoNumber":num})

    metaData={"Chunks":chunks,"Text":result["text"]}
    with open(f"json/{audio}.json","w") as f:
        json.dump(metaData,f)