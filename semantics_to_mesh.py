import os, sys, argparse
import visualize_label_on_mesh_strict as segmesh
import zipfile
import csv
import scannet_200_labels


parser = argparse.ArgumentParser()
parser.add_argument('--pred_zip', required=True, help='path to predicted labels file as .txt evaluation format')
parser.add_argument('--mesh_file', required=True, help='path to the *.ply mesh')
parser.add_argument('--output_folder', required=True, help='output folder')
opt = parser.parse_args()
print(opt)

def segresult(pred_zip, mesh_file, output_folder):
    filename = os.path.splitext(os.path.basename(pred_zip))[0]
    extract_to = output_folder+'\\'+filename+'\\'
    if not os.path.exists(extract_to):
        os.makedirs(extract_to)
    with zipfile.ZipFile(pred_zip, "r") as zip_ref:
        zip_ref.extractall(output_folder)

    summary_filename = extract_to+filename+'.txt'
    rows = []
    # Open the file and create a CSV reader object
    with open(summary_filename, "r") as file:
        lines = file.readlines()
        for line in lines:
            items = line.strip().split()
            rows.append(items)

    dictionary = {key: value for key, value in zip(scannet_200_labels.VALID_CLASS_IDS_200, scannet_200_labels.CLASS_LABELS_200)}

    for i in range(0, len(rows)):
        pred_path = extract_to+rows[i][0]
        label_index = int(rows[i][1])
        label = dictionary[label_index]
        out_path = output_folder+"\\"+str(i)+"_"+label+'.ply'

        # segmesh.visualize(pred_path, mesh_file, out_path)
        label_color = scannet_200_labels.SCANNET_COLOR_MAP_200[label_index]
        segmesh.visualize(pred_path, mesh_file, out_path, label_color)

    for root, dirs, files in os.walk(extract_to, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))

    # Remove the folder itself
    os.rmdir(extract_to)

def main():
    segresult(opt.pred_zip, opt.mesh_file, opt.output_folder)

if __name__ == '__main__':
    main()