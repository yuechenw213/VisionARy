import os, sys, argparse
import numpy as np
import plyfile

parser = argparse.ArgumentParser()
parser.add_argument('--mesh_file', required=True, help='path to the *.ply mesh')
parser.add_argument('--threshold', help='the threshold to be considered as boundary')
parser.add_argument('--output_file', required=True, help='output file for segment result')
opt = parser.parse_args()

def get_vertical_bounderies(file, threshold, output):
    with open(file) as f:
        mesh_data = plyfile.PlyData.read(f)

    vertices = np.vstack([mesh_data['vertex']['x'], mesh_data['vertex']['y'], mesh_data['vertex']['z']]).T

    max_y = np.max(vertices[:, 1])
    min_y = np.min(vertices[:, 1])
    th = threshold * (max_y - min_y)  # 10% of the height range

    selected_indices = set()
    vertex_dict = {}
    index = 0
    new_vertex = []

    for i, v in enumerate(mesh_data['vertex']):
        if v[1] > max_y - th or v[1] < min_y + th:
            selected_indices.add(i)
            vertex_dict[i] = index
            index += 1
            new_vertex.append(v)

    selected_faces = []
    for i, face in enumerate(mesh_data['face']):
        faceset = set(face[0])
        intersect = selected_indices.intersection(faceset)
        if intersect and len(intersect) == 3:

            face[0][0] = vertex_dict[face[0][0]]
            face[0][1] = vertex_dict[face[0][1]]
            face[0][2] = vertex_dict[face[0][2]]
            selected_faces.append(face)

    selected_faces = np.array(selected_faces)
    print(selected_faces,np.array(selected_faces))

    mesh_data['face'].data = selected_faces
    mesh_data['vertex'].data = np.array(new_vertex)

    with open(output, "wb") as f:
        mesh_data.write(f)

def main():
    get_vertical_bounderies(opt.mesh_file, opt.threshold, opt.output_file)

if __name__ == '__main__':
    main()