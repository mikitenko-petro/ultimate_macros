from .json_manage import write_json
import keyboard
import time

def keyboard_listener():
    while True:
        time.sleep(1)
        print('work')
        if keyboard.is_pressed('a'):
            print("stop")
            write_json("static/json/macros_status.json", False)



