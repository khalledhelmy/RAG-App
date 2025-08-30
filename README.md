# RAG-App

This repository documents my journey to study RAG using the mini-RAG playlist.

## Installation


### Install the required packages

```bash
$ pip install -r requirements.txt
```

### Setup the environment variables

```bash
$ cp .env.example .env
```

Set your environment variables in the `.env` file.

## Run Docker Compose Services

```bash
$ cd docker
$ cs .env.example .env
```

update `.env` with your credentials

## Run FastAPI server

```bash
$ uvicorn main:app --reload --port 8000
