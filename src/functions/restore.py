# Библиотеки
import os
# Файлы программы
import config

def restore_func(path):
    with open(f"{os.path.expanduser(config.need_folder)}/links.dotty", "r") as links:
        i = 1
        for link in links:
            link = link.strip()
            path_file = path.strip().split("/")[-1]
            check_link = "".join(path)
            if check_link[-1] == "/":
                link = link.rstrip("/")
                path_file = path.strip().split("/")[-2]
            if path_file.rstrip("/") in link.split("/"):
                os.system(f"rm -rf {link}")
                os.system(f"mv {config.need_folder}/{path_file} {link}")
                os.system(f"sed -i '{i}d' {config.need_folder}/links.dotty")
                break
            else:
                i += 1

# Добавить возможность указать несколько путей и обработать их

