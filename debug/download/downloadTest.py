from requests import get


def download(url_address, save_file_name):
    response = get(url_address)
    if response.status_code == 200:
        with open(save_file_name, "wb") as file:
            file.write(response.content)
        return True
    else:
        return False


url = "https://2.img-dpreview.com/files/p/TS1200x900~sample_galleries/1600733718/8738305624.jpg"
base_directory = "/Users/kook/Pictures/"
file_name = "img.jpg"
save_path = base_directory + file_name

status = download(url, save_path)

if status:
    print("success")
else:
    print("Fail")