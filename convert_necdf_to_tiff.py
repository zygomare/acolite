import xarray as xr
from osgeo import gdal, osr
import numpy as np

def netcdf_to_geotiff_all_bands(netcdf_file, geotiff_file):
    # Open the NetCDF file using xarray
    netcdf_ds = xr.open_dataset(netcdf_file)

    # Get the dimensions and number of bands
    y_size, x_size = netcdf_ds.sizes['y'], netcdf_ds.sizes['x']
    num_bands = len(netcdf_ds.data_vars)

    # Get the geotransform and projection from the NetCDF file
    lat = netcdf_ds['lat'].values
    lon = netcdf_ds['lon'].values
    geotransform = (lon.min(), (lon.max() - lon.min()) / (x_size - 1), 0, lat.max(), 0, (lat.min() - lat.max()) / (y_size - 1))

    # Create the GeoTIFF file
    driver = gdal.GetDriverByName('GTiff')
    geotiff_ds = driver.Create(geotiff_file, x_size, y_size, num_bands, gdal.GDT_Float32)

    # Set the geotransform and projection on the GeoTIFF file
    geotiff_ds.SetGeoTransform(geotransform)
    srs = osr.SpatialReference()
    srs.ImportFromEPSG(32618)  # Assuming WGS84 latitude/longitude
    geotiff_ds.SetProjection(srs.ExportToWkt())

    # Iterate over all bands and write them to the GeoTIFF file
for band_index, band_name in enumerate(netcdf_ds.data_vars, start=1):
    data = netcdf_ds[band_name].values
    geotiff_ds.GetRasterBand(band_index).WriteArray(data)
    geotiff_ds.GetRasterBand(band_index).SetNoDataValue(np.nan)

    # Flush the cache to write the data to disk
    geotiff_ds.FlushCache()

    # Close the datasets
    netcdf_ds.close()
    geotiff_ds = None

# Example usage
netcdf_to_geotiff_all_bands('/mnt/0_ARCTUS_Projects/19_SAGE-Port/dataset/L2/PNEO3_2024_09_03_15_46_21_L1R.nc', '/mnt/0_ARCTUS_Projects/19_SAGE-Port/dataset/L2/output.tif')