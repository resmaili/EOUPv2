import numpy as np
import matplotlib.pyplot as plt
import xarray as xr
from scipy import ndimage

# === Data Loading & Inspection ===

def quick_stats(data, name="Data"):
    """Print quick statistics for arrays/datasets."""
    print(f"\n{name} Statistics:")
    print(f"  Mean:  {np.nanmean(data):.2f}")
    print(f"  Std:   {np.nanstd(data):.2f}")
    print(f"  Min:   {np.nanmin(data):.2f}")
    print(f"  Max:   {np.nanmax(data):.2f}")
    print(f"  Shape: {data.shape}")


def data_summary(ds):
    """Quick summary of xarray Dataset variables and dimensions."""
    print(f"Dataset: {len(ds.data_vars)} variables, {len(ds.dims)} dimensions")
    for var in ds.data_vars:
        print(f"  {var}: {ds[var].shape}")


# === Preprocessing ===

def regrid_simple(data, factor=2):
    """Quick downsampling using coarsening."""
    if isinstance(data, xr.DataArray):
        dims = {d: factor for d in data.dims if d not in ['time', 'lat', 'lon']}
        return data.coarsen(dims).mean()
    return data


def remove_clouds(data, threshold=0.2):
    """Simple cloud masking for satellite data (assumes 0-1 scale)."""
    return data.where(data > threshold, np.nan)


def normalize(data):
    """Normalize data to 0-1 range."""
    return (data - np.nanmin(data)) / (np.nanmax(data) - np.nanmin(data))


# === Visualization ===

def plot_satellite_data(data, title="Satellite Data", cmap="viridis"):
    """Plot 2D satellite imagery."""
    fig, ax = plt.subplots(figsize=(10, 8))
    im = data.plot(ax=ax, cmap=cmap)
    ax.set_title(title, fontsize=14)
    plt.tight_layout()
    return fig, ax


def plot_time_series(data, title="Time Series"):
    """Quick time series plot."""
    fig, ax = plt.subplots(figsize=(12, 5))
    data.plot(ax=ax, marker='o', linewidth=2)
    ax.set_title(title, fontsize=14)
    ax.set_ylabel("Value")
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    return fig, ax


def plot_comparison(data1, data2, title1="Data 1", title2="Data 2"):
    """Side-by-side comparison of two 2D grids."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    data1.plot(ax=ax1, cmap="viridis")
    ax1.set_title(title1)
    
    data2.plot(ax=ax2, cmap="viridis")
    ax2.set_title(title2)
    
    plt.tight_layout()
    return fig, (ax1, ax2)


# === Analysis ===

def spatial_gradient(data):
    """Compute spatial gradient magnitude."""
    if isinstance(data, xr.DataArray):
        data_np = data.values
    else:
        data_np = data
    
    gy, gx = np.gradient(data_np)
    return np.sqrt(gx**2 + gy**2)


def rolling_mean(data, window=7):
    """Compute rolling mean along time dimension."""
    if isinstance(data, xr.DataArray):
        return data.rolling(time=window, center=True).mean()
    return pd.Series(data).rolling(window=window, center=True).mean()


def anomaly(data, reference=None):
    """Compute anomaly from mean or reference."""
    if reference is None:
        reference = np.nanmean(data)
    return data - reference


# === File I/O ===

def save_netcdf(data, filename):
    """Save xarray Dataset to NetCDF."""
    if isinstance(data, xr.DataArray):
        data = data.to_dataset(name="data")
    data.to_netcdf(filename)
    print(f"Saved to {filename}")


def load_netcdf(filename):
    """Load NetCDF file."""
    return xr.open_dataset(filename)