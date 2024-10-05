# Библиотеки
import os
# Файлы программы
import config

def deploy_func():
    with open(f"{os.path.expanduser(config.need_folder)}/links.dotty", "r") as links:
        for link in links:
            link = link.strip()
            file = link.split("/")
            data = file[1::]
            if data[-1] == "":
                link = "/".join(file[:-1:])
                file = data[-2]
            else:
                file = data[-1]
            os.system(f"rm -rf {link}")
            os.system(f"ln -s {config.need_folder}/{file} {link}")
