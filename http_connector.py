import requests

prediction_url = 'https://mix3d-demo.nekrasov.dev/mask3d/predictions/'
prediction_end = '.zip'

test_dir = "D:/thesis/accessability/"
test_string = '20230411_201545_AnyConv.com__SpatialMapping'


def get_data(data_string, output_dir):

    r = requests.get(prediction_url + data_string + prediction_end)

    if r.status_code == 200:
        filename = r.headers.get("content-disposition", "").split("filename=")[-1]

        with open(output_dir+data_string+prediction_end, "wb") as f:
            f.write(r.content)

        print("file: ", filename)
    else:
        print("error")


# get_data(test_string, test_dir)

def upload_file():
    url = 'https://mix3d-demo.nekrasov.dev/mask3d/upload.php'
    filepath = 'D:/thesis/accessability/test_docs/spatialMappingWithRGB.ply'

    with open (filepath, "rb") as f:
        filecontents = f.read()

    file_data = {"userfile":("room.ply", filecontents)}
    form_data = {"label_set":200, "up_axis":"y"}

    response = requests.post(url, files=file_data, data=form_data)

    if response.status_code == 200:
        print(response.content)
        test_string = response.content
    else:
        print("error")
        print(response.content)

# upload_file()
get_data("20230414_192339_room", test_dir)