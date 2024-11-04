import threading
from .keyboard_listener import keyboard_listener
from .json_manage import read_json, write_json
from program_modules.gui.main_window.main_window import frame_start
from program_modules.macros.macros_manager import macros_manager

frame = threading.Thread(target = frame_start)
macros = threading.Thread(target = macros_manager)
listener = threading.Thread(target = keyboard_listener)

write_json("static/json/macros_status.json", False)

write_json("static/json/main_macros_window_status.json", True)

frame.start()

macros.start()

# listener.start()