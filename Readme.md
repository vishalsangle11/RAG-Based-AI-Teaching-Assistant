# How to use this RAG based Ai teaching assistant on your Data.

## Step 1: Collect your videos 
Move all your video into the Video folder

## step 2: Convert to mp3
Convert all video files to mp3 by running the program videoToMp3.py

## step 3: Convert mp3 to json
Convert all mp3 files to json by running the program mp3ToJson.py

## step 4: Convert the json to vectors
Use the program process_incoming to convert json to data frame with embedding and solve it as joblib pickel 

## step 5: Prompt generation and feeding to LLM
Read the joblib file and load it into the memory . Then create a relative prompt as per the user query and feed it to the LLM .

