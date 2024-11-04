import customtkinter
from ...macros.macros_manager import macros_mode
from ...json_manage import read_json, write_json
from ..edit_macros.edit_macros_window import edit_macros_window

class MacrosFrame(customtkinter.CTkFrame):
    def __init__(self, macros_list, index, **kwargs):
        super().__init__(**kwargs)

        name_macros_text = customtkinter.CTkLabel(
        master = self,
        text = macros_list[index]["name"],
        font= ('Roboto Slab', 20, "bold"),
        anchor = "w",
        width = 100,
        height = 20)

        name_macros_text.place(x = 5, y = 5)

        edit_macros_button = customtkinter.CTkButton(
        master = self,
        text = "edit",
        hover = False,
        width = 100,
        fg_color = "#1e77f6",
        command = lambda: edit_macros_window(index))

        edit_macros_button.place(x = 5, y = 65)

        play_macros_button = customtkinter.CTkButton(
        master = self,
        text = "play",
        hover = False,
        width = 100,
        fg_color = "#1e77f6",
        command = lambda: macros_mode(index))

        play_macros_button.place(x = 110, y = 65)

        delete_macros_button = customtkinter.CTkButton(
        master = self,
        text = "delete",
        hover = False,
        width = 100,
        fg_color = "#1e77f6",
        command = lambda: self.delete_macros(index = index))

        delete_macros_button.place(x = 1075, y = 65)
    
    def delete_macros(self, index : int):
        data = read_json(path = "static/json/macros_list.json")
        data.pop(index)
        write_json(path = "static/json/macros_list.json", data = data)

class MacrosListFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.macros_frame_list = []
        self.old_macros_list = []

    def frame_update(self):
        macros_list = read_json(path = "static/json/macros_list.json")

        if self.old_macros_list != macros_list:
            for i in range(len(self.macros_frame_list)):
                self.macros_frame_list[i].destroy()
            self.macros_frame_list = []

            for index in range(len(macros_list)):
                macros_frame = MacrosFrame(
                macros_list = macros_list,
                index = index,
                master = self,
                height = 100,
                fg_color = "#cfcfcf")

                macros_frame.pack(fill = "x", pady = 5)
                self.macros_frame_list.append(macros_frame)

        self.old_macros_list = macros_list

        self.after(50, lambda: self.frame_update())