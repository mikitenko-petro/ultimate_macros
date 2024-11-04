import pyautogui
from ...search_path import search_path

class ClickOnImage():
    def __init__(self, action_properties):
        self.path_to_image = action_properties["tracking_image"]

    def perform(self):
        try:
            image_location = pyautogui.locateOnScreen(search_path(self.path_to_image), confidence=0.9)
            
            # if button_location_left_list[turn] == "":
            #     button_location_left_param = button_location.width/2
            # else:
            #     button_location_left_param = button_location_left_list[turn]

            # if button_location_top_list[turn] == "":
            #     button_location_top_param = button_location.height/2
            # else:
            #     button_location_top_param = button_location_top_list[turn]

            pyautogui.moveTo(
            image_location.left,
            image_location.top)

            pyautogui.click()
        except:
            pass
