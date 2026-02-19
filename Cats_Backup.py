from pathlib import Path
import sys
import subprocess
from abc import ABC, abstractmethod
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\shiba\Desktop\DogCat Information System\assets\frame1")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()

# =====================================================
# Setting the Window Properties
# =====================================================

window.title("Cats Page") # Window Title

screen_width = window.winfo_screenwidth() # Screen/Monitor Width
screen_height = window.winfo_screenheight() # Screen/Monitor Height

# Calculate x and y coordinates to center the window
x_coordinate = (screen_width - 1024) // 2
y_coordinate = (screen_height - 576) // 2

window.geometry(f"1024x576+{x_coordinate}+{y_coordinate}")
window.configure(bg = "#FFFFFF")


# =====================================================
# Initializing the Background of the Window
# =====================================================
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
canvas.create_rectangle(
    199.0,
    0.0,
    1024.0,
    99.0,
    fill="#337EEE",
    outline="")

canvas.create_rectangle(
    0.0,
    0.0,
    199.0,
    576.0,
    fill="#5A5D64",
    outline="")

# DogCat Label
canvas.create_text(
    224.0,
    28.0,
    anchor="nw",
    text="Keayon.DogCat",
    fill="#FFFFFF",
    font=("KronaOne Regular", 40 * -1)
)

# Cat Label
canvas.create_text(
    60.0,
    28.0,
    anchor="nw",
    text="Cats",
    fill="#FFFFFF",
    font=("KronaOne Regular", 40 * -1)
)

# Search Text
canvas.create_text(
    12.0,
    111.0,
    anchor="nw",
    text="Search",
    fill="#FFFFFF",
    font=("Karla Regular", 20 * -1)
)



def clear_entries():
    entry_1.delete(1.0, "end")
    entry_2.delete(1.0, "end")
    entry_3.delete(1.0, "end")
    entry_4.delete(1.0, "end")
    entry_5.delete(1.0, "end")
    
    

# ENCAPSULATION: The class CatBreed encapsulates the attributes and methods related to cat breeds. 
#                The data (breed) is encapsulated within the class, and methods like update_entry are used to control access to the data.

# ABSTRACTION: The abstract base class CatBreed provides a blueprint with abstract methods (set_cat_profile, set_cat_health_information, etc.), 
#              which are meant to be overridden by concrete subclasses. This enforces abstraction, allowing you to define a common interface without 
#              specifying the implementation details.

# INHERITANCE: The CatInformation class inherits from CatBreed, establishing an "is-a" relationship. 
#              This allows CatInformation to inherit the attributes and methods of CatBreed and extend or override them as needed.

# POLYMORPHISM: The abstract methods in CatBreed (e.g., set_cat_profile, set_cat_health_information) are implemented differently in the CatInformation class. 
#               This is an example of polymorphism, where different classes can provide their own unique implementations of the same methods defined in a common interface.


# =====================================================
# Cat Class
# =====================================================

class CatBreed(ABC):
    def __init__(self, breed):
        self.breed = breed
        self.update_entry(entry_1, f"Breed: {breed}")


    # To update to the Entries
    def update_entry(self, entry, text):
        entry.config(state="normal")
        entry.delete("1.0", "end")
        entry.insert("insert", text)
        entry.config(state="disabled")

    @abstractmethod
    def set_cat_profile(self):
        pass

    @abstractmethod
    def set_cat_health_information(self):
        pass

    @abstractmethod
    def set_cat_behavior_and_training(self):
        pass

    @abstractmethod
    def set_cat_maintenance(self):
        pass



# Inheritance of the Class CatBreed
class CatInformation(CatBreed):
    def __init__(self, breed):
        super().__init__(breed)

    # Polymorphism and Inhertitance of the method "update_entry"
    def set_cat_profile(self, average_lifespan, size, weight_range, coat_type, color):
        self.update_entry(entry_2, f"Average Lifespan: {average_lifespan}")
        self.update_entry(entry_3, f"Size: {size}")
        self.update_entry(entry_4, f"Weight Range: {weight_range}")
        self.update_entry(entry_5, f"Coat Type {coat_type}")
        self.update_entry(entry_6, f"Color: {color}")

    def set_cat_health_information(self, recommended_diet, common_health_issues, exercise_needs, regular_check_up_schedule):
        self.update_entry(entry_19, f"Recommended Diet: {recommended_diet}")
        self.update_entry(entry_20, f"Common Health Issues: {common_health_issues}")
        self.update_entry(entry_21, f"Exercise Needs: {exercise_needs}")
        self.update_entry(entry_22, f"Regular Check Up Schedule: {regular_check_up_schedule}")

    def set_cat_behavior_and_training(self, intelligence_level, trainability, socialization_needs, behavior_traits):
        self.update_entry(entry_7, f"Intelligence Level: {intelligence_level}")
        self.update_entry(entry_8, f"Trainability: {trainability}")
        self.update_entry(entry_9, f"Socialization Needs: {socialization_needs}")
        self.update_entry(entry_10, f"Behavior Traits: {behavior_traits}")

    def set_cat_maintenance(self, hygiene_practices, feeding_schedule, grooming_routine, environment):
        self.update_entry(entry_13, f"Hygiene Practices: {hygiene_practices}")
        self.update_entry(entry_14, f"Feeding Schedule: {feeding_schedule}")
        self.update_entry(entry_15, f"Grooming Routine: {grooming_routine}")
        self.update_entry(entry_16, f"Environment: {environment}")

    
# =====================================================
# Cat Button Click Methods
# =====================================================      
def abyssinian_button_click():
    clear_entries()
    abyssinian = CatInformation("Abyssinian")
    abyssinian.set_cat_profile("12 to 16 years", "Medium-sized", "6 to 12 pounds", "Soft, silky, fine in texture", "Ruddy, red, blue, and fawn")
    abyssinian.set_cat_health_information("High-quality cat food", "Gingivitis and Patellar Luxation", "Moderate", "Annual check-ups")
    abyssinian.set_cat_behavior_and_training("4 out of 5", "Can learn tricks and commands", "High", "They are active, playful, and enjoy climbing")
    abyssinian.set_cat_maintenance("Provide a clean litter box, groom regularly, and ensure they have access to clean water", "2 to 3 times a day", "Brush their short coat to reduce shedding and hairballs", "Plenty of vertical spaces for climbing and exploring")

def american_bobtail_button_click():
    clear_entries()
    american_bobtail = CatInformation("American Bobtail")
    american_bobtail.set_cat_profile("12 to 16 years", "Medium to Large", "7 to 16 pounds", "Semi-long to longhair, with a shaggy appearance", "Come in a variety of colors and patterns")
    american_bobtail.set_cat_health_information("High-quality cat food", "Spinal issues", "Moderate", "Annual check-ups")
    american_bobtail.set_cat_behavior_and_training("4 out of 5", "Enjoys learning tricks or playing fetch", "Moderate", "Friendly and playful nature")
    american_bobtail.set_cat_maintenance("Regular grooming, especially for longhaired Bobtails. Ensure access to a clean litter box and fresh water", "2 to 3 times a day", "Brush the coat regularly, particularly for longhaired Bobtails. Trim nails and clean ears as needed", "Provide enough space for play and climbing")

def bengal_button_click():
    clear_entries()
    bengal = CatInformation("Bengal")
    bengal.set_cat_profile("12 to 16 years", "Medium to large", "6 to 15 pounds", "Dense and luxurious", "Brown tabby, seal sepia tabby, seal mink tabby, black silver tabby")
    bengal.set_cat_health_information("")

def british_shorthair_button_click():
    clear_entries()
    british_shorthair = CatInformation("British Shorthair")
    british_shorthair.set_cat_profile("12 to 20 years", "Medium to large", "8 to 20 pounds", "Very dense. Not double-coated or wooly", "Any other color or pattern with the exception of those showing evidence of hybridization resulting in the colors chocolate, lavender, the Himalayan pattern, or these combinations with white.")

def burmese_button_click():
    clear_entries()
    burmese = CatInformation("Burmese")
    burmese.set_cat_profile("12 to 16 years", "Medium-sized", "6 to 12 pounds", "Fine-glossy, latin-like texture", "Sable, champagne, blue, or platinum")

def cornish_rex_button_click():
    clear_entries()
    cornish_rex = CatInformation("Cornish Rex")
    cornish_rex.set_cat_profile("11 to 15 years", "Small to medium", "6 to 10 pounds", "Extremely soft, silky. Relatively dense", "All colors and patterns")

def devon_rex_button_click():
    clear_entries()
    devon_rex = CatInformation("Devon Rex")
    devon_rex.set_cat_profile("9 to 15 years", "Small to medium", "5 to 9 pounds", "Well-covered with fur", "All colors and patterns including bi-color and the pointed pattern")

def egyptian_mau_button_click():
    clear_entries()
    egyptian_mau = CatInformation("Egyptian Mau")
    egyptian_mau.set_cat_profile("12 to 16 years", "Medium-sized", "6 to 16 pounds", "Spotted coat", "Silver, bronze, or smoke")

def himalayan_button_click():
    clear_entries()
    himalayan = CatInformation("Himalayan")
    himalayan.set_cat_profile("9 to 15 years", "Medium to large", "7 to 14 pounds", "Dense undercoat, giving the coat full volume", "Come in a variety of colors")

def japanese_bobtail_button_click():
    clear_entries()
    japanese_bobtail = CatInformation("Japanese Bobtail")
    japanese_bobtail.set_cat_profile("9 to 15 years", "Small to medium", "5 to 10 pounds", "Soft and Silky Coat", "Come in a variety of colors and patterns")




# =====================================================
# Buttons
# =====================================================

# Back Button Method
def go_back():
    window.destroy()
    subprocess.run([sys.executable, r"C:\Users\shiba\Desktop\DogCat Information System\Main.py"])

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
back_button = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=go_back,
    relief="flat"
)
back_button.place(
    x=920.0,
    y=533.0,
    width=85.5111083984375,
    height=35.302734375
)

# Abyssinian Cat
abyssinian_button = Button(
    text="Abyssinian",
    background="#424242",
    foreground="white",
    borderwidth=1,
    highlightthickness=0,
    command=abyssinian_button_click,
    relief="flat"
)
abyssinian_button.place(
    x=0.0,
    y=146.0,
    width=199.0,
    height=43.0
)

# American Bobtail Cat
american_bobtail_button = Button(
    text="American Bobtail",
    background="#424242",
    foreground="white",
    borderwidth=1,
    highlightthickness=0,
    command=american_bobtail_button_click,
    relief="flat"
)
american_bobtail_button.place(
    x=0.0,
    y=189.0,
    width=199.0,
    height=43.0
)

# Bengal Cat
bengal_button = Button(
    text="Bengal",
    background="#424242",
    foreground="white",
    borderwidth=1,
    highlightthickness=0,
    command=bengal_button_click,
    relief="flat"
)
bengal_button.place(
    x=0.0,
    y=232.0,
    width=199.0,
    height=43.0
)

# British Shorthair Cat
british_short_hair_button = Button(
    text="British Short Hair",
    background="#424242",
    foreground="white",
    borderwidth=1,
    highlightthickness=0,
    command=british_shorthair_button_click,
    relief="flat"
)
british_short_hair_button.place(
    x=0.0,
    y=275.0,
    width=199.0,
    height=43.0
)

# Burmese Cat
burmese_button = Button(
    text="Burmese",
    background="#424242",
    foreground="white",
    borderwidth=1,
    highlightthickness=0,
    command=burmese_button_click,
    relief="flat"
)
burmese_button.place(
    x=0.0,
    y=318.0,
    width=199.0,
    height=43.0
)

# Cornish Rex Cat
cornish_rex_button = Button(
     text="Cornish Rex",
    background="#424242",
    foreground="white",
    borderwidth=1,
    highlightthickness=0,
    command=cornish_rex_button_click,
    relief="flat"
)
cornish_rex_button.place(
    x=0.0,
    y=361.0,
    width=199.0,
    height=43.0
)

# Devon Rex Cat
devon_rex_button = Button(
    text="Devon Rex",
    background="#424242",
    foreground="white",
    borderwidth=1,
    highlightthickness=0,
    command=devon_rex_button_click,
    relief="flat"
)
devon_rex_button.place(
    x=0.0,
    y=404.0,
    width=199.0,
    height=43.0
)

# Egyptian Mau Cat
egyptian_mau_button = Button(
    text="Egyptian Mau",
    background="#424242",
    foreground="white",
    borderwidth=1,
    highlightthickness=0,
    command=egyptian_mau_button_click,
    relief="flat"
)
egyptian_mau_button.place(
    x=0.0,
    y=447.0,
    width=199.0,
    height=43.0
)

# Himalayan Cat
himalayan_button = Button(
    text="Himalayan",
    background="#424242",
    foreground="white",
    borderwidth=1,
    highlightthickness=0,
    command=himalayan_button_click,
    relief="flat"
)
himalayan_button.place(
    x=0.0,
    y=490.0,
    width=199.0,
    height=43.0
)

# Japanese Bobtail Cat
japanese_bobtail_button = Button(
    text="Japanese Bobtail",
    background="#424242",
    foreground="white",
    borderwidth=1,
    highlightthickness=0,
    command=japanese_bobtail_button_click,
    relief="flat"
)
japanese_bobtail_button.place(
    x=0.0,
    y=533.0,
    width=199.0,
    height=43.0
)

searchbBar = Entry(
    font="Arial",
    foreground="black",
    background="#D9D9D9",
    )

searchbBar.place(
    x=87.0,
    y=111.0,
    width=101.0,
    height=23.0,
)

canvas.create_rectangle(
    621.0,
    326.0,
    1006.0,
    526.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    224.0,
    326.0,
    609.0,
    526.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    621.0,
    111.0,
    1006.0,
    311.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    224.0,
    111.0,
    609.0,
    311.0,
    fill="#D9D9D9",
    outline="")

# =====================================================
# Entries - Cat Profile
# =====================================================

# Breed Entry
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    320.5,
    173.5,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    font=("Cascadia Mono", 8),
    bg="#D9D9D9",
    fg="#000716",
    wrap="word",
    highlightthickness=0
)
entry_1.place(
    x=224.0,
    y=146.0,
    width=193.0,
    height=53.0
)

# Average Lifespan Entry
entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    320.5,
    228.5,
    image=entry_image_2
)
entry_2 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    font=("Cascadia Mono", 8),
    wrap="word",
    highlightthickness=0
)
entry_2.place(
    x=224.0,
    y=201.0,
    width=193.0,
    height=53.0
)

# Size Entry
entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    320.5,
    283.5,
    image=entry_image_3
)
entry_3 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    font=("Cascadia Mono", 8),
    wrap="word",
    highlightthickness=0
)
entry_3.place(
    x=224.0,
    y=256.0,
    width=193.0,
    height=53.0
)

# Weight Range Entry
entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    512.5,
    173.5,
    image=entry_image_4
)
entry_4 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    font=("Cascadia Mono", 8),
    wrap="word",
    highlightthickness=0
)
entry_4.place(
    x=416.0,
    y=146.0,
    width=193.0,
    height=53.0
)

# Coat Type Entry
entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    512.5,
    228.5,
    image=entry_image_5
)
entry_5 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    font=("Cascadia Mono", 8),
    wrap="word",
    highlightthickness=0
)
entry_5.place(
    x=416.0,
    y=201.0,
    width=193.0,
    height=53.0
)

# Color Entry
entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    512.5,
    283.5,
    image=entry_image_6
)
entry_6 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    font=("Cascadia Mono", 8),
    wrap="word",
    highlightthickness=0
)
entry_6.place(
    x=416.0,
    y=256.0,
    width=193.0,
    height=53.0
)

# =====================================================
# Entries - Cat Behavior and Training
# =====================================================

# Intelligence Level Entry
entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    320.5,
    388.5,
    image=entry_image_7
)
entry_7 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    font=("Cascadia Mono", 8),
    wrap="word",
    highlightthickness=0
)
entry_7.place(
    x=224.0,
    y=361.0,
    width=193.0,
    height=53.0
)

# Trainability Entry
entry_image_8 = PhotoImage(
    file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(
    320.5,
    443.5,
    image=entry_image_8
)
entry_8 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    font=("Cascadia Mono", 8),
    wrap="word",
    highlightthickness=0
)
entry_8.place(
    x=224.0,
    y=416.0,
    width=193.0,
    height=53.0
)

# Socialization Needs Entry
entry_image_9 = PhotoImage(
    file=relative_to_assets("entry_9.png"))
entry_bg_9 = canvas.create_image(
    320.5,
    498.5,
    image=entry_image_9
)
entry_9 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    font=("Cascadia Mono", 8),
    wrap="word",
    highlightthickness=0
)
entry_9.place(
    x=224.0,
    y=471.0,
    width=193.0,
    height=53.0
)

# Behavior Traits
entry_image_10 = PhotoImage(
    file=relative_to_assets("entry_10.png"))
entry_bg_10 = canvas.create_image(
    512.5,
    388.5,
    image=entry_image_10
)
entry_10 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    font=("Cascadia Mono", 8),
    wrap="word",
    highlightthickness=0
)
entry_10.place(
    x=416.0,
    y=361.0,
    width=193.0,
    height=53.0
)

# ------------------ UNUSED BEHAVIOR AND TRAINING ENTRY ------------------
entry_image_11 = PhotoImage(
    file=relative_to_assets("entry_11.png"))
entry_bg_11 = canvas.create_image(
    512.5,
    443.5,
    image=entry_image_11
)
entry_11 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    font=("Cascadia Mono", 8),
    wrap="word",
    highlightthickness=0
)
entry_11.place(
    x=416.0,
    y=416.0,
    width=193.0,
    height=53.0
)

# ------------------ UNUSED BEHAVIOR AND TRAINING ENTRY ------------------
entry_image_12 = PhotoImage(
    file=relative_to_assets("entry_12.png"))
entry_bg_12 = canvas.create_image(
    512.5,
    498.5,
    image=entry_image_12
)
entry_12 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    font=("Cascadia Mono", 8),
    wrap="word",
    highlightthickness=0
)
entry_12.place(
    x=416.0,
    y=471.0,
    width=193.0,
    height=53.0
)

# =====================================================
# Entries - Cat Maintenance
# =====================================================

# Hygiene Practices Entry
entry_image_13 = PhotoImage(
    file=relative_to_assets("entry_13.png"))
entry_bg_13 = canvas.create_image(
    717.5,
    388.5,
    image=entry_image_13
)
entry_13 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    font=("Cascadia Mono", 8),
    wrap="word",
    highlightthickness=0
)
entry_13.place(
    x=621.0,
    y=361.0,
    width=193.0,
    height=53.0
)

# Feeding Schedule Entry
entry_image_14 = PhotoImage(
    file=relative_to_assets("entry_14.png"))
entry_bg_14 = canvas.create_image(
    717.5,
    443.5,
    image=entry_image_14
)
entry_14 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    font=("Cascadia Mono", 8),
    wrap="word",
    highlightthickness=0
)
entry_14.place(
    x=621.0,
    y=416.0,
    width=193.0,
    height=53.0
)

# Grooming Routine Entry
entry_image_15 = PhotoImage(
    file=relative_to_assets("entry_15.png"))
entry_bg_15 = canvas.create_image(
    717.5,
    498.5,
    image=entry_image_15
)
entry_15 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    font=("Cascadia Mono", 8),
    wrap="word",
    highlightthickness=0
)
entry_15.place(
    x=621.0,
    y=471.0,
    width=193.0,
    height=53.0
)

# Environment Entry
entry_image_16 = PhotoImage(
    file=relative_to_assets("entry_16.png"))
entry_bg_16 = canvas.create_image(
    909.5,
    388.5,
    image=entry_image_16
)
entry_16 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    font=("Cascadia Mono", 8),
    wrap="word",
    highlightthickness=0
)
entry_16.place(
    x=813.0,
    y=361.0,
    width=193.0,
    height=53.0
)

# ------------------ UNUSED MAINTENANCE ENTRY ------------------
entry_image_17 = PhotoImage(
    file=relative_to_assets("entry_17.png"))
entry_bg_17 = canvas.create_image(
    909.5,
    443.5,
    image=entry_image_17
)
entry_17 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    font=("Cascadia Mono", 8),
    wrap="word",
    highlightthickness=0
)
entry_17.place(
    x=813.0,
    y=416.0,
    width=193.0,
    height=53.0
)

# ------------------ UNUSED MAINTENANCE ENTRY ------------------
entry_image_18 = PhotoImage(
    file=relative_to_assets("entry_18.png"))
entry_bg_18 = canvas.create_image(
    909.5,
    498.5,
    image=entry_image_18
)
entry_18 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    font=("Cascadia Mono", 8),
    wrap="word",
    highlightthickness=0
)
entry_18.place(
    x=813.0,
    y=471.0,
    width=193.0,
    height=53.0
)

# =====================================================
# Entries - Cat Health Information
# =====================================================

# Recommended Diet Entry
entry_image_19 = PhotoImage(
    file=relative_to_assets("entry_19.png"))
entry_bg_19 = canvas.create_image(
    717.5,
    173.5,
    image=entry_image_19
)
entry_19 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    font=("Cascadia Mono", 8),
    wrap="word",
    highlightthickness=0
)
entry_19.place(
    x=621.0,
    y=146.0,
    width=193.0,
    height=53.0
)

# Common Health Issues Entry
entry_image_20 = PhotoImage(
    file=relative_to_assets("entry_20.png"))
entry_bg_20 = canvas.create_image(
    717.5,
    228.5,
    image=entry_image_20
)
entry_20 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    font=("Cascadia Mono", 8),
    wrap="word",
    highlightthickness=0
)
entry_20.place(
    x=621.0,
    y=201.0,
    width=193.0,
    height=53.0
)

# Exercise Needs Entry
entry_image_21 = PhotoImage(
    file=relative_to_assets("entry_21.png"))
entry_bg_21 = canvas.create_image(
    717.5,
    283.5,
    image=entry_image_21
)
entry_21 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    font=("Cascadia Mono", 8),
    wrap="word",
    highlightthickness=0
)
entry_21.place(
    x=621.0,
    y=256.0,
    width=193.0,
    height=53.0
)

# Regular Check-up Schedule Entry
entry_image_22 = PhotoImage(
    file=relative_to_assets("entry_22.png"))
entry_bg_22 = canvas.create_image(
    909.5,
    173.5,
    image=entry_image_22
)
entry_22 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    font=("Cascadia Mono", 8),
    wrap="word",
    highlightthickness=0
)
entry_22.place(
    x=813.0,
    y=146.0,
    width=193.0,
    height=53.0
)

# ------------------ UNUSED HEALTH INFORMATION ENTRY ------------------
entry_image_23 = PhotoImage(
    file=relative_to_assets("entry_23.png"))
entry_bg_23 = canvas.create_image(
    909.5,
    228.5,
    image=entry_image_23
)
entry_23 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    font=("Cascadia Mono", 8),
    wrap="word",
    highlightthickness=0
)
entry_23.place(
    x=813.0,
    y=201.0,
    width=193.0,
    height=53.0
)

# ------------------ UNUSED HEALTH INFORMATION ENTRY ------------------
entry_image_24 = PhotoImage(
    file=relative_to_assets("entry_24.png"))
entry_bg_24 = canvas.create_image(
    909.5,
    283.5,
    image=entry_image_24
)
entry_24 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    font=("Cascadia Mono", 8),
    wrap="word",
    highlightthickness=0
)
entry_24.place(
    x=813.0,
    y=256.0,
    width=193.0,
    height=53.0
)

# =====================================================
# Rectangles and Lables
# =====================================================
canvas.create_text(
    742.0,
    329.0,
    anchor="nw",
    text="Maintenance",
    fill="#000000",
    font=("Karla Regular", 24 * -1)
)

canvas.create_rectangle(
    223.0,
    145.0,
    609.0,
    146.00006103515625,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    223.0,
    360.0,
    609.0,
    361.00006103515625,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    620.0,
    360.0,
    1006.0,
    361.00006103515625,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    620.0,
    145.0,
    1006.0,
    146.00006103515625,
    fill="#000000",
    outline="")

canvas.create_text(
    340.0,
    115.0,
    anchor="nw",
    text="Animal Profile",
    fill="#000000",
    font=("Karla Regular", 24 * -1)
)

canvas.create_text(
    709.0,
    115.0,
    anchor="nw",
    text="Health Information",
    fill="#000000",
    font=("Karla Regular", 24 * -1)
)

canvas.create_text(
    297.0,
    329.0,
    anchor="nw",
    text="Behavior and Training",
    fill="#000000",
    font=("Karla Regular", 24 * -1)
)


window.resizable(False, False)
window.mainloop()
