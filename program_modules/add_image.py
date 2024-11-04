import os
import shutil
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from PIL import UnidentifiedImageError

def add_image():
    try:
        image_path = askopenfilename()
        target = f"static/images/downloaded_images/{os.path.basename(image_path).split('/')[-1]}"
        shutil.copyfile(image_path, target)

    except UnidentifiedImageError:
        messagebox.showinfo(
        title='Upload Error',
        message='Image could not be read, please make sure the selected is an image file')