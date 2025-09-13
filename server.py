import os
import json
from pathlib import Path
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

DOCS_DIR = Path("docs")
app = FastAPI()

class FileRequest(BaseModel):
    filename: str

@app.get("/list_files")
def list_files():
    files = [f.name for f in DOCS_DIR.glob("*.pdf")]
    return {"files": files}

@app.post("/read_file")
def read_file(req: FileRequest):
    file_path = DOCS_DIR / req.filename
    if not file_path.exists():
        return {"error": "File not found"}
    return {"filename": req.filename, "content": file_path.read_text(encoding="utf-8")}
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
