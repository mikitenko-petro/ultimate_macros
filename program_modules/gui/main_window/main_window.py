import customtkinter
from ...json_manage import read_json, write_json
from ...image_loader import image_loader
from .macros_list_frame import MacrosListFrame
from ..create_macros.create_macros_window import create_macros_window
from ...add_image import add_image

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        config_data = read_json(path = "static/json/window_config.json")

        x_cor = (self.winfo_screenwidth() // 2) - (config_data['width'] // 2) 
        y_cor = (self.winfo_screenheight() // 2) - (config_data['height'] // 2)

        self.title(config_data["title"])
        self.geometry(f"{config_data['width']}x{config_data['height']}+{x_cor}+{y_cor}")
        # self.iconbitmap(search_path("static/images/cosmetic/icon.ico"))
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.window_destoy)

        self.macros_title = customtkinter.CTkLabel(
        master = self,
        text = "your macroses",
        anchor = "w",
        font= ('Roboto Slab', 30, "bold"),
        width = 100,
        height = 20)

        self.macros_title.place(x = 10, y = 10)

        self.macros_list_frame = MacrosListFrame(master = self, width = 1180, height = 500)
        self.macros_list_frame.frame_update()
        self.macros_list_frame.place(x = 0, y = 50)

        self.add_macros_button = customtkinter.CTkButton(
        master = self,
        image = image_loader(image_path = "static/images/cosmetic/add_macros.png", scale = 0.02, mirror = False),
        text = "",
        hover = False,
        fg_color = "#1e77f6",
        width = 2.232,
        command = lambda: create_macros_window())

        self.add_macros_button.place(x = 1050, y = 570)

        self.add_image_button = customtkinter.CTkButton(
        master = self,
        image = image_loader(image_path = "static/images/cosmetic/add_image.png", scale = 0.64, mirror = False),
        text = "",
        hover = False,
        fg_color = "#1e77f6",
        width = 2.232,
        command = lambda: add_image())

        self.add_image_button.place(x = 930, y = 570)

        # self.macros_checking()


        self.mainloop()

    def window_destoy(self):
        write_json("static/json/main_macros_window_status.json", False)
        self.destroy()

    # def macros_checking(self):
    #     if read_json("static/json/macros_status.json") == True:
    #         self.withdraw()
    #     else:
    #         self.deiconify()
        
    #     self.after(50, lambda: self.macros_checking())

def frame_start():
    main = App()