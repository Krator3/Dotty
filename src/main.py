#!/usr/bin/env python3

# Библиотеки
import argparse
import sys
# Файлы программы
from detect import *
import functions.init as init
import functions.add as add
import functions.restore as restore
import functions.deploy as deploy

parser = argparse.ArgumentParser(prog=prog, description=description)

parser.add_argument("init", nargs="*", help=help_init)
parser.add_argument("add", nargs="*", help=help_add)
parser.add_argument("restore", nargs="*", help=help_restore)
parser.add_argument("-v","--version", action="store_true", help=help_version)
parser.add_argument("deploy", nargs="*", help=help_deploy)

args = parser.parse_args()

try:
    if args.version:
        print("Dotty v1.0.0")

    elif len(sys.argv) < 2:
        print(no_data)

    elif "init" in sys.argv:
        init.init_func()

    elif "add" in sys.argv:
        if len(sys.argv) >= 3:
            add.add_func(sys.argv[2])
        else:
            print(error_path)

    elif "restore" in sys.argv:
        if len(sys.argv) >= 3:
            restore.restore_func(sys.argv[2])
        else:
            print(error_path)

    elif "deploy" in sys.argv:
        deploy.deploy_func()

    else:
        print(arguments_not_supported)
except:
    print(error_base)
finally:
    print(done)

