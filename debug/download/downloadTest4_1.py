import progressbar
import urllib.request


progress_bar = None


def show_progress(block_num, block_size, total_size):
    global progress_bar
    if progress_bar is None:
        progress_bar = progressbar.ProgressBar(maxval=total_size)

    downloaded = block_num * block_size
    if downloaded < total_size:
        progress_bar.update(downloaded)
    else:
        progress_bar.finish()
        progress_bar = None


def sub_string(target, word):
    return target[target.rfind(word) + 1: len(target)]


def remove_string(target, word):
    return target[0: target.rfind(word)]


def make_url(url_address_head, object_file_name, object_extension):
    return url_address_head + "/" + object_file_name + "." + object_extension


def download_all(url_root, file_extension, start, end):
    for idx in range(start, end + 1):
        buffer = ""
        if idx < 10:
            buffer = "00"
        else:
            buffer = "0"

        object_name = buffer + str(idx)
        file_name = str(idx) + "." + file_extension
        save_path = base_directory + file_name
        url_address = make_url(url_root, object_name, file_extension)

        print(url_address, " -> ", save_path)
        urllib.request.urlretrieve(url_address, save_path, show_progress)


url = " "
base_directory = "/Users/kook/temp/"

last = sub_string(url, '/')
extension = sub_string(last, '.')
name = remove_string(last, '.')
lastIndex = int(name)
url_head = remove_string(url, '/')

download_all(url_head, extension, 1, lastIndex)
