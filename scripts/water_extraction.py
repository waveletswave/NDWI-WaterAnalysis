from osgeo import gdal, gdalconst
import numpy as np

# Function to extract water surfaces based on NDWI values
def extract_water_surfaces(ndwi_path, water_surface_path):
    # Open the NDWI raster file in read-only mode
    ndwi_ds = gdal.Open(ndwi_path, gdalconst.GA_ReadOnly)

    # Access the first band of the NDWI raster
    ndwi_band = ndwi_ds.GetRasterBand(1)

    # Read the NDWI data into an array
    ndwi_array = ndwi_band.ReadAsArray()

    # Define the threshold value to classify water
    # (water is typically represented by NDWI values greater than 0)
    threshold = 0.0

    # Create an array where NDWI values greater than the threshold are marked as water (1), else non-water (0)
    water_surface_array = np.where(ndwi_array > threshold, 1, 0)

    # Get the GDAL driver for GeoTIFF format
    driver = gdal.GetDriverByName('GTiff')

    # Create a new GeoTIFF file for the water surface extraction result
    water_surface_ds = driver.Create(water_surface_path, ndwi_band.XSize, ndwi_band.YSize, 1, gdal.GDT_Byte)

    # Set the geotransform and projection for the new file based on the NDWI raster
    water_surface_ds.SetGeoTransform(ndwi_ds.GetGeoTransform())
    water_surface_ds.SetProjection(ndwi_ds.GetProjection())

    # Write the water surface array to the first band of the new GeoTIFF
    water_surface_ds.GetRasterBand(1).WriteArray(water_surface_array)

    # Set the no data value for the output raster to 0
    water_surface_ds.GetRasterBand(1).SetNoDataValue(0)

    # Write the data to disk
    water_surface_ds.FlushCache()

    # Print a confirmation message with the output file path
    print(f"Water surface extraction complete. Output saved at '{water_surface_path}'")
