# NDWI-WaterAnalysis

## 概述
NDWI-WaterAnalysis 是一个基于 Python 的工具，专为环境科学家、地理学家和遥感专业人员设计。它专注于从卫星遥感图像中计算归一化差异水指数（NDWI）。该工具能够提取与水有关的特征，包括水体和水面，并利用地理空间重投影技术计算水面面积。

## 特点
- **NDWI 计算**：从卫星图像中计算 NDWI，以突出显示水体。
- **水面提取**：从 NDWI 数据中提取水面。
- **重投影前后的面积计算**：计算重投影前后的水面面积。

## 先决条件
在开始之前，请确保您已满足以下要求：
- 安装了 Python 3.x
- 库：GDAL、NumPy、Rasterio（请参见 `requirements.txt` 了解版本信息）

## 安装
克隆仓库到您的本地机器：
```
git clone https://github.com/waveletswave/NDWI-WaterAnalysis.git
cd NDWI-WaterAnalysis
```

安装必要的 Python 包：
```
pip install -r requirements.txt
```

## 使用方法
该工具分为几个模块，每个模块负责 NDWI 处理和水面提取工作流的一部分。

1. **NDWI 计算**： 
   ```python
   from ndwi_calculation import calculate_ndwi
   calculate_ndwi('<绿波段路径>', '<近红外波段路径>', '<ndwi输出路径>')
   ```

2. **水面提取**：
   ```python
   from water_extraction import extract_water_surfaces
   extract_water_surfaces('<ndwi路径>', '<水面输出路径>')
   ```

3. **水面面积计算**：
   ```python
   from water_area_calculation import calculate_water_area_before_reprojection, reproject_and_calculate_area
   calculate_water_area_before_reprojection('<水面路径>')
   reproject_and_calculate_area('<输入栅格>', '<输出重投影水面>')
   ```

### 示例使用
为了演示如何使用 NDWI-WaterAnalysis 工具，请参考 `example_usage.py` 脚本。此脚本提供了使用所提供模块处理卫星图像以计算 NDWI、提取水面和计算水面面积的实际示例。确保使用您自己的卫星图像文件和期望输出位置的实际路径来更新脚本。

## 贡献
欢迎对 NDWI-WaterAnalysis 进行贡献。要贡献：
1. Fork 仓库。
2. 创建一个新分支（`git checkout -b feature_branch`）。
3. 进行您的更改。
4. 提交您的更改（`git commit -am '添加一些功能'`）。
5. 推送到分支（`git push origin feature_branch`）。
6. 创建一个新的 Pull Request。

## 许可
此项目根据 [MIT 许可证](LICENSE) 授权。

## 联系
如有任何疑问或需要进一步的帮助，请联系 [waveletswave](mailto:yiyuns@andrew.cmu.edu)。

---

### 注意事项
- 请将 `<路径>` 等占位符替换为与您的项目相关的具体指示或示例。
- 根据您项目的具体情况，随时添加或修改部分内容，例如如果您想指定或推荐特定的卫星数据集，可以添加“数据来源”部分。