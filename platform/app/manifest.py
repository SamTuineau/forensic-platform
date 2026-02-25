import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List


def create_manifest(scan_results: List[Dict]) -> Path:
    """Generate a manifest JSON file from scan results and return its path."""
    data = {
        "scan_time": datetime.utcnow().isoformat() + "Z",
        "file_count": len(scan_results),
        "files": scan_results,
    }
    output_dir = Path("casebundles")
    output_dir.mkdir(exist_ok=True)
    manifest_path = output_dir / "latest_manifest.json"
    with manifest_path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    return manifest_path