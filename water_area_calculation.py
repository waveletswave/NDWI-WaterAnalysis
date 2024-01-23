from osgeo import gdal, osr
import numpy as np

# Calculate the water surface area before reprojection
def calculate_water_area_before_reprojection(water_surface_path):
    # Open the raster file
    ds = gdal.Open(water_surface_path)
    # Get the first band of the raster
    band = ds.GetRasterBand(1)
    # Read the band's data as an array
    water_surface_array = band.ReadAsArray()
    # Count the number of pixels that represent water (value == 1)
    water_pixel_count = np.count_nonzero(water_surface_array == 1)
    # Get the pixel dimensions from the geotransform
    transform = ds.GetGeoTransform()
    pixel_width = transform[1]
    pixel_height = -transform[5]  # Negative as pixel height is usually negative
    # Calculate the area per pixel
    area_per_pixel = pixel_width * pixel_height
    # Calculate the total water surface area
    total_water_area = water_pixel_count * area_per_pixel

    # Print and return the total water area before reprojection
    print(f"Total water surface area (BEFORE reprojection): {total_water_area}")
    return total_water_area

# Reproject the raster and calculate the water surface area after reprojection
def reproject_and_calculate_area(input_raster, output_raster):
    # Open the source raster file
    src_ds = gdal.Open(input_raster)
    # Get the projection and geotransform of the source raster
    src_proj = src_ds.GetProjection()
    src_geotrans = src_ds.GetGeoTransform()

    # Create a spatial reference object for the source projection
    src_osr = osr.SpatialReference(wkt=src_proj)
    # Calculate the UTM zone based on the longitude
    src_lon = src_geotrans[0]
    src_lat = src_geotrans[3]
    utm_zone = int(1 + (src_lon + 180.0) / 6.0)

    # Create a spatial reference object for the UTM projection
    utm_osr = osr.SpatialReference()
    utm_osr.SetProjCS(f"UTM Zone {utm_zone}N")
    utm_osr.SetWellKnownGeogCS("WGS84")
    utm_osr.SetUTM(utm_zone, src_lat >= 0)

    # Create a virtual raster (VRT) in the desired target projection
    vrt_ds = gdal.AutoCreateWarpedVRT(src_ds, src_proj, utm_osr.ExportToWkt())
    # Create a copy of the VRT as a new raster file
    gdal.GetDriverByName('GTiff').CreateCopy(output_raster, vrt_ds)

    # Open the reprojected raster file
    ds = gdal.Open(output_raster)
    # Get the first band
    band = ds.GetRasterBand(1)
    # Read the band's data as an array
    water_surface_array = band.ReadAsArray()
    # Count the number of water pixels (value == 1)
    water_pixel_count = np.count_nonzero(water_surface_array == 1)
    # Assume a fixed pixel area (e.g., 30m x 30m)
    area_per_pixel = 30 * 30
    # Calculate the total water area
    total_water_area = water_pixel_count * area_per_pixel

    # Print and return the total water area after reprojection
    print(f"Total water surface area (AFTER reprojection): {total_water_area} square meters ({total_water_area / 1e6:.2f} square kilometers)")
    return total_water_area
