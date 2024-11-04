import customtkinter
from PIL import Image
from .search_path import search_path

def image_loader(image_path, scale = None, mirror = None, width = None, height = None):
    image = Image.open(search_path(image_path))

    if mirror == True:
        image = image.transpose(Image.ROTATE_180)

    if scale != None:
        ctk_image = customtkinter.CTkImage(light_image=image, dark_image=image, size=(image.width*scale, image.height*scale))
        return ctk_image
    
    if width != None and height != None:
        ctk_image = customtkinter.CTkImage(light_image=image, dark_image=image, size=(width, height))
        return ctk_image
