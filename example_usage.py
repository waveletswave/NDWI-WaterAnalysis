from ndwi_calculation import calculate_ndwi
from water_extraction import extract_water_surfaces
from water_area_calculation import calculate_water_area_before_reprojection, reproject_and_calculate_area

# Define paths for the input images and output results
green_band_path = '/path/to/your/PGH_Sentinel2_Image_BAND3.tif'
nir_band_path = '/path/to/your/PGH_Sentinel2_Image_BAND8.tif'
ndwi_output_path = '/path/to/your/output/ndwi.tif'
water_surface_output_path = '/path/to/your/output/water_surface.tif'
reprojected_output_path = '/path/to/your/output/reprojected_water_surface.tif'

# Step 1: NDWI Calculation
calculate_ndwi(green_band_path, nir_band_path, ndwi_output_path)

# Step 2: Water Surface Extraction
extract_water_surfaces(ndwi_output_path, water_surface_output_path)

# Step 3: Water Area Calculation Before Reprojection
calculate_water_area_before_reprojection(water_surface_output_path)

# Step 4: Reproject and Calculate Water Surface Area After Reprojection
reproject_and_calculate_area(water_surface_output_path, reprojected_output_path)
