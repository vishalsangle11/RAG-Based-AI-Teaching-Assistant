# Convert Videos To MP3
import os
import subprocess

files = os.listdir("Video")
for file in files:
    file_name = file.split("_")[0]
    tut_Num=file.split(".")[0].split("_")[1]
    print(file_name,"->",tut_Num)
    subprocess.run(["ffmpeg","-i",f"Video/{file}",f"Audios/{tut_Num}_{file_name}.mp3"])