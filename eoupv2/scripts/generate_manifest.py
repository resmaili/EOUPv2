"""
Generate manifest.json from local data files.
Call using:
python eoupv2/scripts/generate_manifest.py
"""

import json
import os
from pathlib import Path


def generate_manifest(data_dir, base_url, output_file="manifest.json"):
    """
    Auto-generate manifest.json from files in data directory (recursive).
    
    Args:
        data_dir: Local directory with your data files (can have subdirectories)
        base_url: Base URL where files will be hosted (e.g., Zenodo record URL)
        output_file: Where to save manifest.json
    """
    files = []
    data_path = Path(data_dir)
    
    if not data_path.exists():
        print(f"Error: Directory {data_dir} not found")
        return
    
    # Recursively find all files in subdirectories
    for filepath in sorted(data_path.rglob('*')):
        # Skip directories and hidden files
        if filepath.is_dir() or filepath.name.startswith('.'):
            continue
        
        # Get file size
        size_bytes = filepath.stat().st_size
        size_mb = size_bytes / (1024 * 1024)
        
        # Get relative path from data_dir to preserve folder structure
        relative_path = filepath.relative_to(data_path)
        
        files.append({
            "filename": str(relative_path).replace('\\', '/'),  # Cross-platform path
            "url": f"{base_url}/files/{filepath.name}",
            "size": f"{size_mb:.1f}MB",
            "description": f"Data file: {filepath.name}"
        })
    
    if not files:
        print(f"No files found in {data_dir}")
        return
    
    manifest = {
        "version": "1.0",
        "files": files
    }
    
    # Ensure output directory exists
    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w') as f:
        json.dump(manifest, f, indent=2)
    
    print(f"\nGenerated {output_file} with {len(files)} files")
    print(f"\nFiles in manifest:")
    for file in files:
        print(f"  - {file['filename']} ({file['size']})")


if __name__ == "__main__":
    # Configuration
    data_dir = "./notebooks/data"
    base_url = "https://zenodo.org/records/18407746"
    output_file = "eoupv2/datasets/manifest.json"
    
    print("=" * 60)
    print("EOUP v2 - Manifest Generator")
    print("=" * 60)
    print(f"\nGenerating manifest...")
    print(f"  Current Working Directory: {os.getcwd()}")
    print(f"  Data directory: {data_dir}")
    print(f"  Base URL: {base_url}")
    print(f"  Output file: {output_file}\n")
    
    generate_manifest(data_dir, base_url, output_file)