# Библиотеки
import os
# Файлы программы
import config

def init_func():
    os.system(f"mkdir {config.need_folder}")
    os.system(f"touch {config.need_folder}/links.dotty")

