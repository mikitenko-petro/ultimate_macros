import pyautogui
from .actions.click_on_image import ClickOnImage
from ..json_manage import read_json

turn = 0
is_capcha = False
old_actions_list = []

def main_macros(macros_id):
    global turn
    global is_capcha
    global old_actions_list
    pyautogui.FAILSAFE = False

    actions_list = read_json(path = "static/json/macros_list.json")
    actions_list = actions_list[macros_id]["actions"]

    current_actions_list = []

    if old_actions_list != actions_list:
        turn = 0
        old_actions_list = actions_list

    for index in range(len(actions_list)):
        if actions_list[index]["type"] == "click_on_image":
            current_actions_list.append(ClickOnImage(action_properties = actions_list[index]))

    current_actions_list[turn].perform()

    turn += 1

    if turn == len(actions_list):
        turn = 0