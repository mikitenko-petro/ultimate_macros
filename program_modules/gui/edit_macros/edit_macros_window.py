import customtkinter
from tkinter.filedialog import askopenfilename
from .edit_macros_actions_list_frame import EditMacrosActionsListFrame
from ...json_manage import read_json, write_json
from ...search_path import search_path

class EditMacrosWindow(customtkinter.CTkToplevel):
    def __init__(self, index, **kwargs):
        super().__init__(**kwargs)

        self.index = index

        width = 600
        height = 600

        x_cor = (self.winfo_screenwidth() // 2) - (width // 2) 
        y_cor = (self.winfo_screenheight() // 2) - (height // 2)

        self.title("edit macros")
        self.geometry(f"{width}x{height}+{x_cor}+{y_cor}")
        # self.iconbitmap(search_path("static/images/cosmetic/icon.ico"))
        self.resizable(False, False)
        self.attributes('-topmost',True)
        self.protocol("WM_DELETE_WINDOW", self.window_destoy)

        self.new_macros_name_label = customtkinter.CTkLabel(master = self,
        text = "macros name",
        font= ('Roboto Slab', 20, "normal"),
        width = 50,
        height = 30)
        self.new_macros_name_label.place(x = 25, y = 10)

        self.macros_name_input = customtkinter.CTkTextbox(master = self, width = 550, height = 30)
        self.macros_name_input.place(x = 25, y = 50)

        self.edit_macros_actions_list_farme = EditMacrosActionsListFrame(
        master = self,
        macros_index = self.index,
        width = 530,
        height = 300)
        self.edit_macros_actions_list_farme.frame_update()
        self.edit_macros_actions_list_farme.place(x = 25, y = 100)

        self.edit_button = customtkinter.CTkButton(master = self,
        text = "edit macros",
        hover = False,
        width = 560,
        fg_color = "#1e77f6",
        command = lambda: self.edit_macros(
            name = self.macros_name_input.get(0.1, customtkinter.END).replace("\n", '')))
        self.edit_button.place(x = 20, y = 550)

        self.add_image_for_clicking_button = customtkinter.CTkButton(
        master = self,
        text = "add image for clicking",
        hover = False,
        fg_color = "#1e77f6",
        width = 100,
        command = lambda: self.add_image_for_clicking())

        self.add_image_for_clicking_button.place(x = 20, y = 420)

        self.mainloop()

    def edit_macros(self, name):
        data = read_json(path = "static/json/macros_list.json")

        if name != "":
            data[self.index]["name"] = name
        
        write_json(path = "static/json/macros_list.json", data = data)
        self.window_destoy()

    def add_image_for_clicking(self):
        image_path = askopenfilename(initialdir = search_path("static/images/downloaded_images"))

        if image_path != "":

            data = read_json(path = "static/json/macros_list.json")

            data[self.index]["actions"].append({
                    "type": "click_on_image",
                    "tracking_image": image_path
                })
            
            write_json(path = "static/json/macros_list.json", data = data)

    def window_destoy(self):
        write_json("static/json/edit_macros_window_status.json", False)
        self.destroy()

windows_open_error = True

def edit_macros_window(index):
    global windows_open_error
    window_status = None
    try:
        window_status = read_json("static/json/edit_macros_window_status.json")
    except:
        write_json("static/json/edit_macros_window_status.json", False)

    if read_json("static/json/edit_macros_window_status.json") == True and windows_open_error == True:
        write_json("static/json/edit_macros_window_status.json", True)
        windows_open_error = False
        window = EditMacrosWindow(index)
    
    if window_status == False:
        write_json("static/json/edit_macros_window_status.json", True)
        window = EditMacrosWindow(index)