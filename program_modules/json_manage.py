import json
from .search_path import search_path

def read_json(path : str):
    with open(file = search_path(path), encoding = 'utf-8', mode= 'r') as file:
        return json.load(file)
    
def write_json(path : str, data):
    with open(file = search_path(path), encoding = 'utf-8', mode= 'w') as file:
        return json.dump(data, file, indent = 4)