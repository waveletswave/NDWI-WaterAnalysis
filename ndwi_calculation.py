from osgeo import gdal
import numpy as np

def calculate_ndwi(green_band_path, nir_band_path, output_path):
    # Open the TIFF file for the green spectral band using GDAL
    green_band_tiff = gdal.Open(green_band_path)

    # Open the TIFF file for the near-infrared (NIR) spectral band using GDAL
    nir_band_tiff = gdal.Open(nir_band_path)

    # Read the green band as an array and convert it to float type
    green_band_array = green_band_tiff.GetRasterBand(1).ReadAsArray().astype(float)

    # Read the NIR band as an array and convert it to float type
    nir_band_array = nir_band_tiff.GetRasterBand(1).ReadAsArray().astype(float)

    # Calculate the Normalized Difference Water Index (NDWI)
    # NDWI = (Green - NIR) / (Green + NIR)
    ndwi = (green_band_array - nir_band_array) / (green_band_array + nir_band_array)

    # Replace NaN values in NDWI array with -999
    ndwi[np.isnan(ndwi)] = -999

    # Get the GDAL driver for GeoTIFF format
    driver = gdal.GetDriverByName('GTiff')

    # Create a new GeoTIFF file to store the NDWI result
    ndwi_tiff = driver.Create(output_path, green_band_tiff.RasterXSize, green_band_tiff.RasterYSize, 1, gdal.GDT_Float32)

    # Set the geotransform and projection information for the NDWI TIFF based on the green band TIFF
    ndwi_tiff.SetGeoTransform(green_band_tiff.GetGeoTransform())
    ndwi_tiff.SetProjection(green_band_tiff.GetProjection())

    # Write the NDWI array to the first band of the new TIFF
    ndwi_tiff.GetRasterBand(1).WriteArray(ndwi)

    # Set the no data value for the NDWI TIFF to -999
    ndwi_tiff.GetRasterBand(1).SetNoDataValue(-999)

    # Write the data to disk
    ndwi_tiff.FlushCache()

    # Print a confirmation message with the output file path
    print(f"NDWI calculation complete. Output saved at '{output_path}'")
