"""Download and load book data."""

import os
import json
import urllib.request
from pathlib import Path


def setup_book_data(data_dir="./data"):
    """
    Download all book data files from manifest, preserving folder structure.
    """
    data_path = Path(data_dir)
    data_path.mkdir(parents=True, exist_ok=True)
    
    manifest_path = Path(__file__).parent / "datasets" / "manifest.json"
    with open(manifest_path) as f:
        manifest = json.load(f)
    
    for item in manifest["files"]:
        # Create subdirectories if needed
        filepath = data_path / item["filename"]
        filepath.parent.mkdir(parents=True, exist_ok=True)
        
        if filepath.exists():
            print(f" {item['filename']} already exists")
        else:
            print(f"Downloading {item['filename']}...")
            try:
                urllib.request.urlretrieve(item["url"], filepath)
                print(f" Saved to {filepath}")
            except Exception as e:
                print(f" Error downloading {item['filename']}: {e}")


def load_chapter_data(chapter_num, data_dir="./notebooks/data"):
    """
    Load data for a specific chapter.
    
    Args:
        chapter_num: Chapter number (1, 2, 3, ...)
        data_dir: Where data files are stored
        
    Returns:
        Dictionary with loaded data for that chapter
    """
    import xarray as xr
    import pandas as pd
    
    data_path = Path(data_dir)
    
    # Map chapters to their data files
    chapter_files = {
        1: ["chapter1_data.csv"],
        2: ["satellite_image.nc", "station_data.csv"],
        # Add more as needed
    }
    
    if chapter_num not in chapter_files:
        raise ValueError(f"Chapter {chapter_num} not found")
    
    data = {}
    for filename in chapter_files[chapter_num]:
        filepath = data_path / filename
        
        if not filepath.exists():
            raise FileNotFoundError(
                f"{filename} not found. Run setup_book_data() first."
            )
        
        # Load based on file type
        if filename.endswith(".csv"):
            data[filename] = pd.read_csv(filepath)
        elif filename.endswith(".nc"):
            data[filename] = xr.open_dataset(filepath)
        elif filename.endswith(".h5"):
            data[filename] = xr.open_dataset(filepath)
    
    return data


def get_data_path(data_dir="./notebooks/data"):
    """Get the path to the data directory."""
    return Path(data_dir)