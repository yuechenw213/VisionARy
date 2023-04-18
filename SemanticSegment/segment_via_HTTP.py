import requests
import os, sys, argparse

parser = argparse.ArgumentParser()
parser.add_argument('--mesh_file', required=True, help='path to the *.ply mesh')
parser.add_argument('--output_folder', required=True, help='output folder of segment prediction')
opt = parser.parse_args()
print(opt)


prediction_url = 'https://mix3d-demo.nekrasov.dev/mask3d/predictions/'
prediction_end = '.zip'

test_dir = "D:/thesis/accessability/"
test_string = '20230411_201545_AnyConv.com__SpatialMapping'

filepath_toupload = 'D:/thesis/accessability/test_docs/spatialMappingWithRGB.ply'

def get_data(data_string, output_dir):

    r = requests.get(prediction_url + data_string + prediction_end)

    if r.status_code == 200:
        filename = r.headers.get("content-disposition", "").split("filename=")[-1]

        with open(output_dir+data_string+prediction_end, "wb") as f:
            f.write(r.content)

        print("file: ", output_dir+data_string+prediction_end)
    else:
        print("error")


# get_data(test_string, test_dir)

def upload_file(filepath):
    url = 'https://mix3d-demo.nekrasov.dev/mask3d/upload.php'


    with open (filepath, "rb") as f:
        filecontents = f.read()

    file_data = {"userfile":("room.ply", filecontents)}
    form_data = {"label_set":200, "up_axis":"y"}

    response = requests.post(url, files=file_data, data=form_data)

    if response.status_code == 200:
        print(response.content)
        return response.content.decode('utf-8')
    else:
        print("error")
        print(response.content)

def main():
    print("Server response:", "20230414_192339_room")
    get_data("20230414_192339_room", opt.output_folder)
    print("segment result save to", opt.output_folder)
# upload_file()
if __name__ == '__main__':
    main()