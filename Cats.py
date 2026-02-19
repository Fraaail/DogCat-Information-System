from pathlib import Path
import sys
import subprocess
import sqlite3
from abc import ABC, abstractmethod
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\School\College\Codes\DogCat Information System\assets\frame1")


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

canvas.create_rectangle(
    0.0,
    150.0,
    199.0,
    99.0,
    fill="black",
    outline=""
)

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
    80.0,
    111.0,
    anchor="nw",
    text="List",
    fill="#FFFFFF",
    font=("Karla Regular", 20 * -1)
)



def clear_entries():
    entry_1.delete(1.0, "end")
    entry_2.delete(1.0, "end")
    entry_3.delete(1.0, "end")
    entry_4.delete(1.0, "end")
    entry_5.delete(1.0, "end")
    
    

# 1. ENCAPSULATION
# We encapsulate the information related to a cat breed within the CatBreed class. Each instance of CatBreed contains a specific breed, and 
# we manage this data through the self.breed attribute. Additionally, we encapsulate the behavior of updating entry information in the 
# update_entry method. This method ensures a consistent approach to updating GUI entries, maintaining a clean separation between the implementation 
# details and the rest of the program.

# 2. ABSTRACTION
# Our use of abstraction is evident through the creation of an abstract class, CatBreed. This class serves as a blueprint, defining a common method, 
# set_cat_info, as an abstract method. By doing so, we enforce that each subclass must implement this method, ensuring that specific cat information 
# is set according to the category (profile, health, behavior, maintenance).

# 3. INHERITANCE
# Inheritance plays a crucial role in our design. We have several subclasses, such as CatProfile, CatHealthInfo, CatBehaviorAndTraining, and CatMaintenance, 
# which inherit from the abstract class CatBreed. This inheritance mechanism allows us to reuse the common functionality defined in CatBreed across all subclasses. 
# Each subclass then specializes in setting information specific to its category, promoting code reuse and a hierarchical structure.

# 4. POLYMORPHISM
# Polymorphism is demonstrated through method polymorphism. The set_cat_info method is declared in the abstract class CatBreed, and each subclass provides its own 
# unique implementation. This enables us to treat objects of different types (subclasses) uniformly when calling the set_cat_info method. For instance, when we create 
# an instance of CatProfile, we can seamlessly set profile information specific to that breed.


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
    def set_cat_info(self):
        pass


# Inheritance of the Class CatBreed
class CatProfile(CatBreed):
    def __init__(self, breed):
        super().__init__(breed)

    def set_cat_info(self, average_lifespan, size, weight_range, coat_type, color):
        self.update_entry(entry_2, f"Average Lifespan: {average_lifespan}")
        self.update_entry(entry_3, f"Size: {size}")
        self.update_entry(entry_4, f"Weight Range: {weight_range}")
        self.update_entry(entry_5, f"Coat Type {coat_type}")
        self.update_entry(entry_6, f"Color: {color}")

class CatHealthInfo(CatBreed):
        def set_cat_info(self, recommended_diet, common_health_issues, exercise_needs, regular_check_up_schedule):
            self.update_entry(entry_19, f"Recommended Diet: {recommended_diet}")
            self.update_entry(entry_20, f"Common Health Issues: {common_health_issues}")
            self.update_entry(entry_21, f"Exercise Needs: {exercise_needs}")
            self.update_entry(entry_22, f"Regular Check Up Schedule: {regular_check_up_schedule}")

class CatBehaviorAndTraining(CatBreed):
        def set_cat_info(self, intelligence_level, trainability, socialization_needs, behavior_traits):
            self.update_entry(entry_7, f"Intelligence Level: {intelligence_level}")
            self.update_entry(entry_8, f"Trainability: {trainability}")
            self.update_entry(entry_9, f"Socialization Needs: {socialization_needs}")
            self.update_entry(entry_10, f"Behavior Traits: {behavior_traits}")

class CatMaintenance(CatBreed):
        def set_cat_info(self, hygiene_practices, feeding_schedule, grooming_routine, environment):
            self.update_entry(entry_13, f"Hygiene Practices: {hygiene_practices}")
            self.update_entry(entry_14, f"Feeding Schedule: {feeding_schedule}")
            self.update_entry(entry_15, f"Grooming Routine: {grooming_routine}")
            self.update_entry(entry_16, f"Environment: {environment}")


        
    
# =====================================================
# Cat Button Click Methods
# =====================================================      
def abyssinian_button_click():
    clear_entries()
    breed = "Abyssinian"
    abyssinian_profile = CatProfile(breed)
    abyssinian_profile.set_cat_info("12 to 16 years", "Medium-sized", "6 to 12 pounds", "Soft, silky, fine in texture", "Ruddy, red, blue, and fawn")

    abyssinian_health_info = CatHealthInfo(breed)
    abyssinian_health_info.set_cat_info("High-quality cat food", "Gingivitis and Patellar Luxation", "Moderate", "Annual")

    abyssinian_behavior_and_training = CatBehaviorAndTraining(breed)
    abyssinian_behavior_and_training.set_cat_info("4 out of 5", "Highly trainable", "High", "Active and playful")

    abyssinian_maintenance = CatMaintenance(breed)
    abyssinian_maintenance.set_cat_info("Provide a clean litterbox and some freshwater", "2 to 3 times a day", "Occasional brushing", "Enriched indoor space")

def american_bobtail_button_click():
    clear_entries()
    breed = "American Bobtail"
    american_bobtail_profile = CatProfile(breed)
    american_bobtail_profile.set_cat_info("12 to 16 years", "Medium to Large", "7 to 16 pounds", "Semi-long to longhair, with a shaggy appearance", "Various colors and patterns")
    
    american_bobtail_health_info = CatHealthInfo(breed)
    american_bobtail_health_info.set_cat_info("High-quality cat food", "Spinal issues", "Moderate", "Annual")

    american_bobtail_behavior_and_training = CatBehaviorAndTraining(breed)
    american_bobtail_behavior_and_training.set_cat_info("4 out of 5", "Moderately trainable", "Moderate", "Friendly and playful nature")

    american_bobtail_maintenance = CatMaintenance(breed)
    american_bobtail_maintenance.set_cat_info("Ensure access to a clean litter box and some freshwater", "2 to 3 times a day", "Regular brushing", "Spacious indoor environment")

def bengal_button_click():
    clear_entries()
    breed = "Bengal"
    bengal_profile = CatProfile(breed)
    bengal_profile.set_cat_info("12 to 16 years", "Medium to large", "6 to 15 pounds", "Dense and luxurious", "Spotted or marbled patterns")

    bengal_health_info = CatHealthInfo(breed)
    bengal_health_info.set_cat_info("High-quality cat food", "Hypertrophic cardiomyopathy", "High", "Semi-annual")

    bengal_behavior_and_training = CatBehaviorAndTraining(breed)
    bengal_behavior_and_training.set_cat_info("5 out of 5", "Highly Trainable", "Very High", "Energetic and Playful")

    bengal_maintenance = CatMaintenance(breed)
    bengal_maintenance.set_cat_info("Provide clean enviroment. Monitor for dental issues", "2 to 3 times a day", "Regular brushing", "Stimulating indoor space")


def british_shorthair_button_click():
    clear_entries()
    breed = "British Shorthair"
    british_shorthair_profile = CatProfile(breed)
    british_shorthair_profile.set_cat_info("12 to 20 years", "Medium to large", "8 to 20 pounds", "Very dense. Not double-coated or wooly", " Various solid colors")

    british_shorthair_health_info = CatHealthInfo(breed)
    british_shorthair_health_info.set_cat_info("High-quality cat food", " Obesity and dental issues", "Moderate", "Semi-annual")

    british_shorthair_behavior_and_training = CatBehaviorAndTraining(breed)
    british_shorthair_behavior_and_training.set_cat_info("4 out of 5", "Moderately trainable", "Low", "Easygoing and laid-back")

    british_shorthair_maintenenace = CatMaintenance(breed)
    british_shorthair_maintenenace.set_cat_info("Provide a clean litter box and some freshwater", "2 to 3 times a day", "Regular brushing", "Comfortable indoor setting")

def burmese_button_click():
    clear_entries()
    breed = "Burmese"
    burmese_profile = CatProfile(breed)
    burmese_profile.set_cat_info("12 to 16 years", "Medium-sized", "6 to 12 pounds", "Fine-glossy, latin-like texture", "Sable, champagne, blue, or platinum")

    burmese_shorthair_health_info = CatHealthInfo(breed)
    burmese_shorthair_health_info.set_cat_info("High-quality cat food", "Gingivitis and respiratory issues", "Moderate", "Annual")

    burmese_behavior_and_training = CatBehaviorAndTraining(breed)
    burmese_behavior_and_training.set_cat_info("4 out of 5", "Moderately trainable", "Moderate", "Affectionate and people-oriented")

    burmese_maintenance = CatMaintenance(breed)
    burmese_maintenance.set_cat_info("Regular dental care is important", "2 to 3 times a day", "Minimal grooming needs", "Indoor with play areas")

def cornish_rex_button_click():
    clear_entries()
    breed = "Cornish Rex"
    cornish_rex_profile = CatProfile(breed)
    cornish_rex_profile.set_cat_info("11 to 15 years", "Small to medium", "6 to 10 pounds", "Extremely soft, silky. Relatively dense", "All colors and patterns")

    cornish_rex_health_info = CatHealthInfo(breed)
    cornish_rex_health_info.set_cat_info("High-quality cat food", "Skin issues and respiratory problems", "Moderate", "Annual")

    cornish_rex_behavior_and_training = CatBehaviorAndTraining(breed)
    cornish_rex_behavior_and_training.set_cat_info("4 out of 5", "Moderately trainable", "Moderate", "Affectoinate and social")

    cornish_rex_maintenance = CatMaintenance(breed)
    cornish_rex_maintenance.set_cat_info("Provide a clean litter box and some freshwater", "Frequent small meals", "Regular grooming required", "Indoor with warmth")

def devon_rex_button_click():
    clear_entries()
    breed = "Devon Rex"
    devon_rex_profile = CatProfile(breed)
    devon_rex_profile.set_cat_info("9 to 15 years", "Small to medium", "5 to 9 pounds", "Well-covered with fur", "All colors and patterns")

    devon_rex_health_info = CatHealthInfo(breed)
    devon_rex_health_info.set_cat_info("High-quality cat food", "Skin issues and respiratory problems", "Moderate", "Annual")

    devon_rex_behavior_and_training = CatBehaviorAndTraining(breed)
    devon_rex_behavior_and_training.set_cat_info("4 out of 5", "Moderately trainable", "Moderate", "Affectionate and playful")

    devon_rex_maintenance = CatMaintenance(breed)
    devon_rex_maintenance.set_cat_info("Provide a clean litter box and some freshwater", "2 to 3 times a day", "Regular grooming required", "Indoor with warmth")
    
def egyptian_mau_button_click():
    clear_entries()
    breed = "Egyptian Mau"
    egyptian_mau_profile = CatProfile(breed)
    egyptian_mau_profile.set_cat_info("12 to 16 years", "Medium-sized", "6 to 16 pounds", "Spotted coat", "Spotted or marbled patterns")

    egyptian_mau_health_info = CatHealthInfo(breed)
    egyptian_mau_health_info.set_cat_info("High-quality cat food", "Dental issues and certain genetic conditions", "Moderate to high", "Semi-annual")

    egyptian_mau_behavior_and_training = CatBehaviorAndTraining(breed)
    egyptian_mau_behavior_and_training.set_cat_info("4 out of 5", "Moderately trainable", "Moderate", "Friendly and social")

    egyptian_mau_maintenance = CatMaintenance(breed)
    egyptian_mau_maintenance.set_cat_info("Provide a clean litter box and some freshwater", "2 to 3 times a day", "Minimal grooming needs", "Safe outdoor access")

def himalayan_button_click():
    clear_entries()
    breed = "Himalayan"
    himalayan_profile = CatProfile(breed)
    himalayan_profile.set_cat_info("9 to 15 years", "Medium to large", "7 to 14 pounds", "Dense undercoat, giving the coat full volume", "Various color points")

    himalayan_health_info = CatHealthInfo(breed)
    himalayan_health_info.set_cat_info("High-quality cat food", "Respiratory problems, dental issues, and kidney disease", "Moderate", "Semi-annual",)

    himalayan_behavior_and_training = CatBehaviorAndTraining(breed)
    himalayan_behavior_and_training.set_cat_info("2 to 5", "Moderately trainable", "Moderate", "Affectionate and gentle")

    himalayan_maintenance = CatMaintenance(breed)
    himalayan_maintenance.set_cat_info("Provide a clean litter box and some freshwater", "2 to 3 times a day", "Daily brushing","Indoor with quiet surroundings")

def japanese_bobtail_button_click():
    clear_entries()
    breed = "Japanese Bobtail"
    japanese_bobtail_profile = CatProfile(breed)
    japanese_bobtail_profile.set_cat_info("9 to 15 years", "Small to medium", "5 to 10 pounds", "Soft and Silky Coat", "Various colors and patterns")

    japanese_bobtail_health_info = CatHealthInfo(breed)
    japanese_bobtail_health_info.set_cat_info("High-quality cat food", "Spinal issues due to unique tail structure", "Moderate", "Annual")

    japanese_bobtail_behavior_and_training = CatBehaviorAndTraining(breed)
    japanese_bobtail_behavior_and_training.set_cat_info("4 out of 5", "Moderately trainable", "Moderate", "Affectionate and friendly")

    japanese_bobtail_maintenance = CatMaintenance(breed)
    japanese_bobtail_maintenance.set_cat_info("Provide a clean litter box and some freshwater", "2 to 3 times a day", "Regular brushing", "Indoor with play opportunities")



# =====================================================
# Buttons
# =====================================================

# Back Button Method
def go_back():
    window.destroy()
    subprocess.run([sys.executable, r"D:\School\College\Codes\DogCat Information System\Main.py"])

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
