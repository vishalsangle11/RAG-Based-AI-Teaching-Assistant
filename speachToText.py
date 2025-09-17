import whisper
import json

model = whisper.load_model("large-v2")
result = model.transcribe(audio="Audios/sample.mp3",
                         language="hi",
                         task="translate",
                         word_timestamps=False)

chunks=[]
for segment in result["segments"]:
    chunks.append({"START":segment["start"],"END":segment["end"],"TEXT":segment["text"]})

with open("Output.json","w") as f:
    json.dump(chunks,f)