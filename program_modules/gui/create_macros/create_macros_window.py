import customtkinter
from ...json_manage import read_json, write_json

class CreateMacrosWindow(customtkinter.CTkToplevel):
    def __init__(self, **kwargs):
        super().__init__( **kwargs)

        width = 600
        height = 600

        x_cor = (self.winfo_screenwidth() // 2) - (width // 2) 
        y_cor = (self.winfo_screenheight() // 2) - (height // 2)

        self.title("create macros")
        self.geometry(f"{width}x{height}+{x_cor}+{y_cor}")
        # self.iconbitmap(search_path("static/images/cosmetic/icon.ico"))
        self.resizable(False, False)
        self.attributes('-topmost',True)
        self.protocol("WM_DELETE_WINDOW", self.window_destoy)

        self.new_macros_label = customtkinter.CTkLabel(master = self,
        text = "macros name",
        font= ('Roboto Slab', 20, "normal"),
        width = 50,
        height = 30)
        self.new_macros_label.place(x = 25, y = 10)

        self.macros_name_input = customtkinter.CTkTextbox(master = self, width = 550, height = 30)
        self.macros_name_input.place(x = 25, y = 50)

        self.create_button = customtkinter.CTkButton(master = self,
        text = "create macros",
        hover = False,
        width = 560,
        fg_color = "#1e77f6",
        command = lambda: self.create_macros(name = self.macros_name_input.get(0.1, customtkinter.END).replace("\n", '')))
        self.create_button.place(x = 20, y = 550)

        self.mainloop()

    def create_macros(self, name):
        if name != "":
            data = read_json(path = "static/json/macros_list.json")
            data.append({"name": name, "actions": []})
            write_json(path = "static/json/macros_list.json", data = data)
            self.window_destoy()

    def window_destoy(self):
        write_json("static/json/create_macros_window_status.json", False)
        self.destroy()

windows_open_error = True

def create_macros_window():
    global windows_open_error
    window_status = None
    try:
        window_status = read_json("static/json/create_macros_window_status.json")
    except:
        write_json("static/json/create_macros_window_status.json", False)

    if read_json("static/json/create_macros_window_status.json") == True and windows_open_error == True:
        write_json("static/json/create_macros_window_status.json", True)
        windows_open_error = False
        window = CreateMacrosWindow()
    
    if window_status == False:
        write_json("static/json/create_macros_window_status.json", True)
        window = CreateMacrosWindow()