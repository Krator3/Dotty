# Библиотеки
import os
# Файлы программы
import config
from detect import *

def add_func(path):
    file = path.split("/")
    data = file[3:]

    if data[-1] == "":
        file = data[-2]
        data = "~/" + "/".join(data[:-1])
    else:
        file = data[-1]
        data = "~/" + "/".join(data)

    with open(f"{os.path.expanduser(config.need_folder)}/links.dotty", "a+") as links:
        links.seek(0)
        if data in [link.strip() for link in links]:
            print(tracking_file)
        elif os.path.exists(path):
            os.system(f"mv {path} {config.need_folder}")
            os.system(f"ln -s {config.need_folder}/{file} {data}")
            links.write(f"{data}\n")
        else:
            print(incorrect_path)
# Добавить возможность указать несколько путей и обработать их

