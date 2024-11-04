from ..json_manage import read_json, write_json
from .main_macros import main_macros

macros = None

def macros_mode(macros_id):
    global macros

    if read_json("static/json/create_macros_window_status.json") == False and read_json("static/json/edit_macros_window_status.json") == False:
        macros = macros_id
    
def macros_manager():
    global macros

    process = 0

    while process < 10:
        if read_json(path = "static/json/main_macros_window_status.json") == False:
            write_json("static/json/macros_status.json", False)
            print("stopping macros")
            break

        if read_json(path = "static/json/main_macros_window_status.json") == False:
            macros = None

        if macros != None:
            write_json("static/json/macros_status.json", True)
            main_macros(macros)

        process += 1

        if process == 10:
            process = 0