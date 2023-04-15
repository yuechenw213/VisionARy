## Mask3D: Mask Transformer for 3D Instance Segmentation

The format is the same as ScanNet (https://kaldir.vc.in.tum.de/scannet_benchmark/documentation#format-instance3d)


### Format for 3D Semantic Instance Prediction

Results are provided as a text file for each test scan.
Each text file contains a line for each instance, containing the relative path to a binary mask of the instance, the predicted label id, and the confidence of the prediction.
Predicted instance mask files live in a subdirectory `pred_mask`. For instance, a submission should look like:

```
unzip_root/
 |-- scene_name.txt
 |-- pred_mask/
    |-- scene_name_0.txt
    |-- scene_name_1.txt
         ⋮
```

Each prediction file for a scan contains a list of instances, where an instance is:
(1) the relative path to the predicted mask file,
(2) the integer class label id,
(3) the float confidence score.
Each line in the prediction file corresponds to one instance,
and the three values above separated by spaces.
The predicted instance mask file provides a mask over the vertices of the scan mesh in the same order as the uploaded .ply vertices.
Each instance mask file contains one line per vertex,
with each line containing an integer value, with non-zero values indicating part of the instance.
E.g., `scene_name.txt` is of the format:

```
pred_masks/scene_name_0.txt 10 0.7234
pred_masks/scene_name_1.txt 36 0.9038
     ⋮
```

and `pred_mask/scene_name_0.txt` could look like:

```
0
0
0
1
1
⋮
0
```

### BibTex

If you find this work useful, please consider citing:

```
@article{Schult23,
  title     = {{Mask3D for 3D Semantic Instance Segmentation}},
  author    = {Schult, Jonas and Engelmann, Francis and Hermans, Alexander and Litany, Or and Tang, Siyu and Leibe, Bastian},
  booktitle = {{International Conference on Robotics and Automation (ICRA)}},
  year      = {2023}
}
```
