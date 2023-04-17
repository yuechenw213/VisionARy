```commandline
python .\semantics_to_mesh.py --pred_zip .\20230414_192339_room.zip --mesh_file .\test_docs\spatialMappingWithRGB.ply --output_folder .\test_docs\out
put_folder
```

```commandline
python .\visualize_labels_on_mesh.py --pred_file .\test_docs\20230414_192339_room\pred_mask\20230414_192339_room_2.txt --mesh_file .\test_docs\spatia
lMappingWithRGB.ply --output_file .\test_docs\output2.ply
```

```commandline
python .\ply_to_obj.py .\test_docs\output2.ply .\test_docs\output2.obj
```

```commandline
python .\segment_via_HTTP.py --mesh_file=D:/thesis/ac
cessability/test_docs/spatialMappingWithRGB.ply --output_folder=D:/thesis/accessability/
test_docs/output_folder/
```