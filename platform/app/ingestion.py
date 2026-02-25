import hashlib
from pathlib import Path
from typing import List, Dict
import os


def compute_sha256(file_path: Path) -> str:
    """Compute SHA256 of a file in chunks to avoid high memory usage."""
    hash_obj = hashlib.sha256()
    try:
        with file_path.open("rb") as f:
            for chunk in iter(lambda: f.read(65536), b""):
                hash_obj.update(chunk)
    except Exception:
        # on error, return empty string or some indicator
        return ""
    return hash_obj.hexdigest()


def scan_directory(path: str) -> List[Dict]:
    """Walk the directory recursively and collect file information including SHA256."""
    base = Path(path)
    results = []
    if not base.exists() or not base.is_dir():
        raise ValueError("Path is not a valid directory")
    for root, dirs, files in os.walk(base):
        # filter out hidden or system folders
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ('node_modules',)]
        for name in files:
            file_path = Path(root) / name
            try:
                stat = file_path.stat()
                results.append({
                    "file_path": str(file_path),
                    "size": stat.st_size,
                    "modified_time": stat.st_mtime,
                    "hash": compute_sha256(file_path),
                })
            except Exception:
                # skip files that can't be read
                continue
    return results