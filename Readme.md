# RAG-Based AI Teaching Assistant

## Project Overview

This project is a Retrieval-Augmented Generation (RAG) based AI Teaching Assistant designed to transform educational video content into an intelligent question-answering system. The solution enables users to ask natural language questions and receive contextually relevant answers derived from the knowledge contained within video lectures.

## Objective

The primary objective of this project is to create an AI-powered learning assistant that can understand, process, and retrieve information from educational video content, making knowledge discovery faster and more interactive for learners.

## Key Features

* Automated extraction of knowledge from educational videos
* Speech-to-text conversion for video content
* Semantic search using vector embeddings
* Context-aware response generation using Large Language Models (LLMs)
* Retrieval-Augmented Generation (RAG) architecture for improved answer accuracy
* Efficient storage and retrieval of processed educational content

## Project Workflow

### 1. Video Collection

Educational videos are collected and stored as the primary data source.

### 2. Audio Extraction

Video files are converted into audio (MP3) format to facilitate speech processing.

### 3. Speech Transcription

Audio files are transcribed into structured JSON format containing the extracted textual content.

### 4. Knowledge Vectorization

The transcribed content is processed into embeddings using NLP techniques. These vector embeddings are stored for efficient semantic similarity search and retrieval.

### 5. Context Retrieval & Response Generation

When a user submits a query:

* Relevant content is retrieved using vector similarity search.
* The retrieved context is incorporated into a dynamically generated prompt.
* The prompt is sent to a Large Language Model (LLM).
* The LLM generates an accurate and contextually relevant response.

## Technologies Used

* Python
* Speech-to-Text Processing
* Natural Language Processing (NLP)
* Vector Embeddings
* Retrieval-Augmented Generation (RAG)
* Large Language Models (LLMs)
* Joblib for Data Persistence

## My Contribution

* Designed and implemented the complete data processing pipeline.
* Built automated workflows for video-to-audio conversion and transcription.
* Developed embedding generation and vector storage mechanisms.
* Implemented semantic search for relevant content retrieval.
* Integrated LLMs for context-aware answer generation.
* Created an end-to-end AI Teaching Assistant capable of answering questions from educational video content.

## Business Impact

This solution significantly reduces the time required to search through lengthy educational videos and enables learners to interact with course content through a conversational AI interface, improving accessibility and learning efficiency.


