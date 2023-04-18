# VisionARy: An Open Source 3D Environment Segmentation Toolkit for Augmented Reality

![image](./doc/banner.png)
VisionARy is an open-source toolkit designed to make 3D indoor segmentation technologies accessible to Augmented Reality (AR) developers and researchers. With a strong emphasis on developer experience, the toolkit expands the potential of AR spatial mesh in conjunction with 3D segmentation, providing various modules for geometric and semantic segmentation, data adaptation, AR platform integration, and APIs.

[[video](https://www.youtube.com/playlist?list=PLrYVDrNwUVZA4m67fYLc22FMmgH0v85ib)]
## Getting Started
### Download the Toolkit
```commandline
git clone https://github.com/yuechenw213/VisionARy.git
```
### Get Your Developer Roadmap


## Modules
### Spatial Mesh Collector
### Data Adaptor
### Geometric Segmentation
### Semantic Segmentation

```commandline
python .\segment_via_HTTP.py --mesh_file=D:/thesis/ac
cessability/test_docs/spatialMappingWithRGB.ply --output_folder=D:/thesis/accessability/
test_docs/output_folder/
```
```commandline
python .\semantics_to_mesh.py --pred_zip .\20230414_192339_room.zip --mesh_file .\test_docs\spatialMappingWithRGB.ply --output_folder .\test_docs\out
put_folder
```

```commandline
python .\visualize_labels_on_mesh.py --pred_file .\test_docs\20230414_192339_room\pred_mask\20230414_192339_room_2.txt --mesh_file .\test_docs\spatia
lMappingWithRGB.ply --output_file .\test_docs\output2.ply
```

### Segmented Mesh Generator

### Point Cloud Generator


