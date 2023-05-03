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
![image](./doc/roadmap2.drawio.png)

#### Prepare your data
- If you already have 3D mesh data that you want to segment, make sure it is in .ply file format. If not, you will need to convert it to this format.
- You can also obtain a spatial mesh from the Hololens web portal, which will be in .obj file format. To use this mesh for segmentation, you will need to convert it to .ply format. The Data Adaptor module can assist you in converting the data.
- If the data is not still available, you can use the Spatial Mesh Collector module to collect spatial mesh data in real-time. To do this, deploy a Unity app with the provided package to the Hololens device, and set up the Python server provided in the module. The app will send the captured mesh data to the backend, where it will be saved as a .ply file.
#### Perform 3D segmentation
- To perform 3D segmentation, first determine what you want to segment from the data.
- Geometric segmentation involves segmenting based on the geometry and topology of the 3D mesh. This approach is useful for segmenting space boundaries and other geometric features.
- Semantic segmentation involves segmenting based on the labels or categories of objects in the 3D mesh. This approach is useful for segmenting specific types of objects (e.g. furniture) or features (e.g. windows, doors).
- Follow the instructions provided in the module to perform the segmentation.
#### Apply Segmentation Result to Your Application
- The segmented result is provided in the form of multiple .ply files, each representing a segment of the 3D mesh.
- If further data processing is needed, you can use the Python code and the plyfile library to access the features of the segmented data.
- To apply segmentation to your AR application, modules are provided in the toolkit to load the segmented result into the Unity engine. The segmented data can be loaded as a mesh object or point cloud, depending on the specific needs of your application.
The module also provides a batch loading function for loading multiple segments at once.
## Modules
### Spatial Mesh Collector
This module is designed to facilitate the collection of 3D mesh data from real-world environments. 
The module provides runtime data collection Unity package and a local TCP server.
#### Python Server
The Python server receives data from the Hololens client and saves it locally in .ply format. It acts as a bridge between the client and backend processing tools, allowing for real-time data capture and processing.

##### Setup:
- In [./SpatialMeshCollector/server.py](./SpatialMeshCollector/server.py), set the `HOST` constant to your local ip address. Set the `output` constant to your designated filepath.
- Run `./SpatialMeshCollector/server.py` to start receiving connections.
- When the 3D spatial data is received and saved, the server will stop automatically.

#### Unity Package
##### Setup:
- In a unity project, use `Assets > Import Package > Custom Package` to import the [VisionARy_MeshCollector.unitypackage](./SpatialMeshCollector/UnityExample/VisionARy_MeshCollector.unitypackage) for collecting and sending 3D spatial mesh.

![image](./doc/import_package.png)
- Then in the `Project` window, under `Asset > Scenes`, open the `MeshCollect.unity` scene.

![image](./doc/collectorscene.png)
- In the `TCP client` game object, set the `Host IP address` to your python server IP.

![image](./doc/tcpsetting.png)
- Save the change, deploy the scene to your Hololens.
##### In the Application:
- You will see the following AR interface. Use `Connect to Server` button to connect to python server. When success, the button will turn green.

![image](./doc/interface.png)
- Use the headset to scan your environment. The `suspend` and `resume` button can control the update of spatial mesh.
- When the immersive environment is well covered by mesh, use `send mesh` to save the mesh data to server.

### Data Adaptor

The Data Adaptor converts 3D models in OBJ format to PLY format for segmentation.

cr: This code is developed based on nabeel3133's file-converter-.obj-to-.ply repository, which can be found at https://github.com/nabeel3133/file-converter-.obj-to-.ply
#### How to use
```commandline
python ./DataAdaptor/convert.py --input [objfilename.obj] --output [plyfilename.ply]
```
### Geometric Segmentation

One sample task that can be performed using the Geometric Segmentation module is the segmentation of the ceiling and floor from 3D mesh data. By using algorithms to identify the horizontal surfaces in the mesh, the module can isolate the ceiling and floor segments and generate separate .ply files.
### How to use
```commandline
python ./GeometricSegment/Geometric.py --mesh_file [yourmesh.ply] --threshold [threshold] --output_file [plyfilename.ply]
```
### Semantic Segmentation

The Semantic Segmentation module is designed to enable segmentation of 3D mesh data based on semantic labels or categories. This module utilizes a Mask3D(https://github.com/JonasSchult/Mask3D) model and the [ScanNet200](https://kaldir.vc.in.tum.de/scannet_benchmark/) dataset to perform segmentation.
#### How to use
By making HTTP requests to the Mask3D demo backend(https://francisengelmann.github.io/mask3d/), the Semantic Segmentation module obtains predictions of vertex of indoor data from the Mask3D server in single command.

```commandline
python .\SemanticSegment\segment_via_HTTP.py --mesh_file [your_mesh.ply] --output_folder [output_folder]
```
This command will obtain the prediction maps in plain text format. The following command can then be used to map the prediction back to the original mesh.

- for getting all labeled instances from the result
```commandline
python .\SemanticSegment\SegmentationMap\semantics_to_mesh.py --pred_zip [filename.zip] --mesh_file [your_mesh.ply] --output_folder [output_folder]
put_folder
```
- for getting single instance of your choice
```commandline
python .\SemanticSegment\SegmentationMap\visualize_labels_on_mesh.py --pred_file [predict.txt] --mesh_file .[your_mesh.ply] --output_file [output.ply]
```
or
```commandline
python .\SemanticSegment\SegmentationMap\visualize_labels_on_mesh.py --pred_file [predict.txt] --mesh_file .[your_mesh.ply] --output_file [output.ply]
```
### Segmented Mesh Generator

This module helps you load segmented data into the Unity development platform with just one click.
#### How to use:
```commandline
cp .\UnityPlugins\editorMeshLoad\. [your_project\Assets\Scripts\]
```
Then add the script to any gameobject.

![image](./doc/loadmesh.png)

You can put the path to single .ply file or a folder containing multiple files to the corresponding box, and click the button to load it in the scene.
### Point Cloud Generator

The usage of point cloud generator is similar to mesh generator

```commandline
cp .\UnityPlugins\editorPointCloudLoad\. [your_project\Assets\Scripts\]
```

![image](./doc/loadpointcloud.png)
