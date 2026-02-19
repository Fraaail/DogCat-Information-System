from pathlib import Path
import sys
import subprocess
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\School\College\Codes\DogCat Information System\assets\frame2")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

# =====================================================
# Setting the Window Properties
# =====================================================

window.title("Home Page") # Window Title

screen_width = window.winfo_screenwidth() # Screen/Monitor Width
screen_height = window.winfo_screenheight() # Screen/Monitor Height

# Calculate x and y coordinates to center the window
x_coordinate = (screen_width - 1024) // 2
y_coordinate = (screen_height - 576) // 2

window.geometry(f"1024x576+{x_coordinate}+{y_coordinate}")
window.configure(bg = "#FFFFFF")


def open_dog_window():
    window.destroy()
    subprocess.run([sys.executable, r"D:\School\College\Codes\DogCat Information System\Dogs.py"])

def open_cat_window():
    window.destroy()
    subprocess.run([sys.executable, r"D:\School\College\Codes\DogCat Information System\Cats.py"])

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 576,
    width = 1024,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    512.0,
    288.0,
    image=image_image_1
)

canvas.create_text(
    266.0,
    67.0,
    anchor="nw",
    text="Keayon.DogCat",
    fill="#000000",
    font=("KronaOne Regular", 48 * -1)
)

canvas.create_text(
    256.0,
    141.0,
    anchor="nw",
    text="Your personal Dog and Cat Information System",
    fill="#000000",
    font=("Karla Regular", 24 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
dog_button = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=open_dog_window,
    relief="flat"
)
dog_button.place(
    x=266.0,
    y=253.0,
    width=218.0,
    height=90.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
cat_button = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=open_cat_window,
    relief="flat"
)
cat_button.place(
    x=540.0,
    y=253.0,
    width=218.0,
    height=90.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=928.4888916015625,
    y=535.0,
    width=85.5111083984375,
    height=35.302734375
)
window.resizable(False, False)
window.mainloop()
