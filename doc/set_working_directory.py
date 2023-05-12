"""sets as working directory the parent of data/

Assumes this file is distributed inside COGENT3_ROOT/doc directory"""
import os
import pathlib


def get_data_dir():
    """returns path to cogent3 doc data directory"""
    current = pathlib.Path(".").absolute().parent
    for path in current.glob("**/*"):
        if "doc" not in path.parts:
            continue

        if path.is_dir() and str(path.name) == "data":
            return path.parent

    raise RuntimeError(f"could not find data dir from {current}")


def get_thumbnail_dir():
    """returns path to directory for writing html thumbnail images"""
    thumbdir = pathlib.Path(__file__).parent / "_build" / "html" / "_images"
    thumbdir.mkdir(exist_ok=True, parents=True)
    return thumbdir


data_dir = get_data_dir()
os.chdir(data_dir)
