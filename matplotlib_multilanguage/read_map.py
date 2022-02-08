from yaml import load, FullLoader
from os.path import join, split, realpath



def read_map():
    filename = join(split(realpath(__file__))[0], "fontmap.yaml")
    with open(filename) as file:
        config = load(file, FullLoader)
    return config["fontmap"]
