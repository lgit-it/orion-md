
# mcp_server/server.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from tools.document_tools import list_markdown_files, read_file_content, create_embeddings, cluster_texts

app = FastAPI(title="MCP Tool Server")

class DirectoryRequest(BaseModel):
    directory: str
class FilepathRequest(BaseModel):
    filepath: str
class TextsRequest(BaseModel):
    texts: List[str]
class EmbeddingsRequest(BaseModel):
    embeddings: List[List[float]]

@app.post("/tools/list_markdown_files", response_model=List[str])
def run_list_files(request: DirectoryRequest):
    try:
        return list_markdown_files.invoke({"directory": request.directory})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/tools/read_file_content", response_model=str)
def run_read_file(request: FilepathRequest):
    try:
        return read_file_content.invoke({"filepath": request.filepath})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/tools/create_embeddings", response_model=List[List[float]])
def run_create_embeddings(request: TextsRequest):
    try:
        return create_embeddings.invoke({"texts": request.texts})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/tools/cluster_texts", response_model=Dict[int, int])
def run_cluster_texts(request: EmbeddingsRequest):
    try:
        return cluster_texts.invoke({"embeddings": request.embeddings})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def read_root():
    return {"status": "MCP Server is running"}
