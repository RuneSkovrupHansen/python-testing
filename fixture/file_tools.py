#!/bin/python3
import os
import shutil

def remove_file(file: str) -> bool:
    try:
        os.remove(file)
    except:
        return False

    return True

def remove_files(*args) -> bool:
    try:
        for file in args:
            os.remove(file)
    except:
        return False

    return True

def clear_folder(folder: str) -> bool:
    try:
        for f in os.listdir(folder): os.remove(os.path.join(folder, f))
    except:
        return False

    return True

def remove_folder(folder: str) -> bool:
    try:
        shutil.rmtree(folder)
    except:
        return False

    return True

def main():
    dir = "test_dir"
    remove_folder(dir)

if __name__ == "__main__":
    main()