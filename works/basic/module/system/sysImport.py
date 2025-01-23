import os
import sys


def path_append_on_cwd(path):
    if '' == path:
        return

    cwd = os.getcwd()
    new_path = path
    if new_path[0] != '/':
        new_path = cwd + '/' + path
    else:
        new_path = cwd + path
    sys.path.append(new_path)
