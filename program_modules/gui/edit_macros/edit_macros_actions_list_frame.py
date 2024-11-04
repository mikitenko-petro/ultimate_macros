import customtkinter
from ...image_loader import image_loader
from ...json_manage import read_json, write_json

class MacrosActionFrame(customtkinter.CTkFrame):
    def __init__(self, macros_list, macros_index, action_index, **kwargs):
        super().__init__(**kwargs)


        if macros_list[action_index]["type"] == "click_on_image":
            action_name = "click on image"

            self.tracking_image = customtkinter.CTkLabel(
            master = self,
            text = None,
            image = image_loader(image_path = macros_list[action_index]["tracking_image"],
            width = 30,
            height = 30),
            width = 30,
            height = 30)

            self.tracking_image.place(x = 150, y = 5)

        self.name_macros_text = customtkinter.CTkLabel(
        master = self,
        text = action_name,
        font= ('Roboto Slab', 20, "bold"),
        anchor = "w",
        width = 100,
        height = 20)

        self.name_macros_text.place(x = 5, y = 5)

        self.delete_action_button = customtkinter.CTkButton(
        master = self,
        text = "delete",
        hover = False,
        width = 100,
        fg_color = "#1e77f6",
        command = lambda: self.delete_action(macros_index = macros_index, action_index = action_index))

        self.delete_action_button.place(x = 425, y = 65)

    def delete_action(self, macros_index, action_index):
        data = read_json(path = "static/json/macros_list.json")

        data[macros_index]["actions"].pop(action_index)

        write_json(path = "static/json/macros_list.json", data = data)


class EditMacrosActionsListFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, macros_index, **kwargs):
        super().__init__(**kwargs)

        self.macros_actions_frame_list = []
        self.old_macros_list = []
        self.macros_index = macros_index

    def frame_update(self):
        macros_list = read_json(path = "static/json/macros_list.json")
        macros_list = macros_list[self.macros_index]["actions"]

        if self.old_macros_list != macros_list:
            for i in range(len(self.macros_actions_frame_list)):
                self.macros_actions_frame_list[i].destroy()
            self.macros_actions_frame_list = []

            for index in range(len(macros_list)):
                macros_action_frame = MacrosActionFrame(
                macros_list = macros_list,
                macros_index = self.macros_index,
                action_index = index,
                master = self,
                height = 100,
                fg_color = "#cfcfcf")

                macros_action_frame.pack(fill = "x", pady = 5)
                self.macros_actions_frame_list.append(macros_action_frame)

        self.old_macros_list = macros_list

        self.after(50, lambda: self.frame_update())