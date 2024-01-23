# NDWI-WaterAnalysis

## Overview
NDWI-WaterAnalysis is a Python-based tool designed for environmental scientists, geographers, and remote sensing professionals. It focuses on calculating the Normalized Difference Water Index (NDWI) from satellite remote sensing images. This tool enables the extraction of water-related features, including water bodies and water surfaces, and facilitates the calculation of water surface areas using geospatial reprojection techniques.

## Features
- **NDWI Calculation**: Compute the NDWI from satellite imagery to highlight water bodies.
- **Water Surface Extraction**: Extract water surfaces from NDWI data.
- **Area Calculation Before and After Reprojection**: Calculate the water surface area before and after reprojection to a different coordinate system.

## Prerequisites
Before you begin, ensure you have met the following requirements:
- Python 3.x installed
- Libraries: GDAL, NumPy, Rasterio (see `requirements.txt` for versions)

## Installation
Clone the repository to your local machine:
```bash
git clone https://github.com/waveletswave/NDWI-WaterAnalysis.git
cd NDWI-WaterAnalysis
