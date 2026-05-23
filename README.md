# Earth Observation Using Python: Revised Edition




## Installation
```bash
pip install eoupv2
```

## Quick Start
```python
from eoupv2 import setup_book_data
import xarray as xr
import pandas as pd

# Download all data once (requires internet connection)
setup_book_data()

# Test loading data directly
satellite_data = xr.open_dataset('./notebooks/data/txt/surfrad_header.csv')
```

## What does `setup_book_data()` do?

- Downloads all datasets from Zenodo (~2 GB)
- Saves them to `./notebooks/data/*` on your machine
- Only downloads missing files (safe to run multiple times)
- Takes 5-10 minutes on first run depending on internet speed
