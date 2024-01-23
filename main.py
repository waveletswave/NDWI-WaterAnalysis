# Import necessary functions from other scripts
from ndwi_calculation import calculate_ndwi
from water_extraction import extract_water_surfaces
from water_area_calculation import calculate_water_area_before_reprojection, reproject_and_calculate_area

# Define the main function of the application
def main():
    # Calculate the Normalized Difference Water Index (NDWI) 
    # from the given green and near-infrared (NIR) band paths, and save the output
    calculate_ndwi('/path/to/BAND3.tif', '/path/to/BAND5.tif', '/path/to/ndwi_output.tif')

    # Extract water surfaces from the calculated NDWI raster
    # and save the binary water surface raster
    extract_water_surfaces('/path/to/ndwi_output.tif', '/path/to/water_surface.tif')

    # Calculate the water surface area before reprojection
    # and print the calculated area
    calculate_water_area_before_reprojection('/path/to/water_surface.tif')

    # Reproject the water surface raster and calculate the water surface area
    # after reprojection, then print the calculated area
    reproject_and_calculate_area('/path/to/water_surface.tif', '/path/to/reprojected_water_surface.tif')

# Check if the script is run directly (as a script) and not imported as a module
if __name__ == "__main__":
    main()  # Execute the main function

