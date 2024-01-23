# NDWI水体分析

## 概述
NDWI水体分析是一个基于Python的工具，专为环境科学家、地理学家和遥感专业人士设计。它主要用于从卫星遥感图像计算归一化差异水体指数（NDWI）。此工具能够提取与水体相关的特征，包括水体和水面，并使用地理空间重投影技术计算水面面积。

## 特点
- **NDWI计算**：从卫星图像计算NDWI，以突出水体。
- **水面提取**：从NDWI数据中提取水面。
- **重投影前后的面积计算**：在不同坐标系统中重投影前后计算水面面积。

## 前提条件
开始之前，请确保满足以下要求：
- 安装了Python 3.x
- 已安装库：GDAL、NumPy、Rasterio（详见`requirements.txt`中的版本）

## 安装
克隆仓库到本地机器：
```
git clone https://github.com/waveletswave/NDWI-WaterAnalysis.git
cd NDWI-WaterAnalysis
```

安装必要的Python包：
```
pip install -r requirements.txt
```

## 使用方法
该工具分为几个模块，每个模块负责NDWI处理和水体提取工作流程的一部分。

1. **NDWI计算**： 
   ```python
   from ndwi_calculation import calculate_ndwi
   calculate_ndwi('<绿色波段路径>', '<近红外波段路径>', '<NDWI输出路径>')
   ```

2. **水面提取**：
   ```python
   from water_extraction import extract_water_surfaces
   extract_water_surfaces('<NDWI路径>', '<水面输出路径>')
   ```

3. **水面面积计算**：
   ```python
   from water_area_calculation import calculate_water_area_before_reprojection, reproject_and_calculate_area
   calculate_water_area_before_reprojection('<水面路径>')
   reproject_and_calculate_area('<输入栅格>', '<输出重投影栅格>')
   ```

将占位符（`<路径...>`）替换为实际的文件路径。

## 贡献
欢迎对NDWI水体分析进行贡献。要贡献：
1. Fork仓库。
2. 创建新分支（`git checkout -b feature_branch`）。
3. 进行更改。
4. 提交更改（`git commit -am 'Add some feature'`）。
5. 推送到分支（`git push origin feature_branch`）。
6. 创建新的Pull Request。

## 许可证
此项目根据[MIT许可证](LICENSE)授权。

## 联系方式
如有任何疑问或需要进一步协助，请联系[waveletswave](mailto:yiyuns@andrew.cmu.edu)。

---

### 注意事项
- 将 `<路径...>` 及其他占位符替换为与您的项目相关的具体说明或示例。
- 如果您在README中引用了 `LICENSE` 文件，请确保您的仓库中有此文件。
- 根据您的偏好调整联系信息。
- 您可以根据项目的具体情况添加或修改部分内容，例如如果您想指定或推荐特定的卫星数据集，可以添加“数据来源”部分。
