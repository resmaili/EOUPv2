from pathlib import Path
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import argparse

def main(cmap, width, height):
    data_dir = Path("./data/blended-hydro")
    files = sorted(data_dir.glob("BHP-TPW_v04r0_blend*.nc"))

    # Open all files
    df = []
    for file in files:
      df.append(xr.open_dataset(file, decode_timedelta=True))

    # Combime files across the time dimension and calculate the daily average
    combined_ds = xr.concat(df, dim='time')
    daily_average_tpw = combined_ds['TPW'].mean(dim='time')

    # Interpolate any missing values
    daily_average_tpw_filled = daily_average_tpw.interpolate_na(\
      dim='lat', method='nearest')
    daily_average_tpw_filled = daily_average_tpw_filled.interpolate_na(\
      dim='lon', method='nearest')

    # Extract time for filename
    time_str = combined_ds.time_coverage_start[0:10]
    output_file = Path("./") / f"Blended-Hydro-{time_str}-{cmap}-{width}x{height}.png"

    # Generate and save plot
    plt.figure(figsize=[width, height])
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.coastlines(resolution='50m', color="white", linewidth=0.5)
    plt.pcolormesh(daily_average_tpw.lon, daily_average_tpw.lat, \
        daily_average_tpw_filled, cmap=cmap, vmin=1, vmax=65)
    plt.savefig(output_file, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate blended hydro daily average plot")
    parser.add_argument("--cmap", type=str, default="magma", help="Colormap name (default: magma)")
    parser.add_argument("--width", type=int, default=20, help="Figure width in inches (default: 20)")
    parser.add_argument("--height", type=int, default=20, help="Figure height in inches (default: 20)")
    
    args = parser.parse_args()
    main(args.cmap, args.width, args.height)