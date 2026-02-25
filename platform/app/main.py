from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Forensic Platform API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "Forensic Platform API running"}


from pydantic import BaseModel
from typing import Dict
from pathlib import Path


class IngestRequest(BaseModel):
    path: str


@app.post("/ingest")
def ingest(request: IngestRequest):
    try:
        from . import ingestion, manifest
        results = ingestion.scan_directory(request.path)
        manifest_path = manifest.create_manifest(results)
        return {"files_scanned": len(results), "manifest_path": str(manifest_path)}
    except Exception as e:
        return {"error": str(e)}


@app.get("/manifest")
def get_manifest():
    manifest_file = Path("casebundles/latest_manifest.json")
    if manifest_file.exists():
        return manifest_file.read_text()
    return {"error": "no manifest"}