from pathlib import Path
import sys
import subprocess
import sqlite3
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\School\College\Codes\DogCat Information System\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

# =====================================================
# Setting the Window Properties
# =====================================================

window.title("Dog Page") # Window Title

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

# List rectangle
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

# Dog Label
canvas.create_text(
    60.0,
    28.0,
    anchor="nw",
    text="Dogs",
    fill="#FFFFFF",
    font=("KronaOne Regular", 40 * -1)
)

# List Text
canvas.create_text(
    80.0,
    111.0,
    anchor="nw",
    text="List",
    fill="#FFFFFF",
    font=("Karla Regular", 20 * -1)
)

# =====================================================
# Database
# =====================================================

conn = sqlite3.connect("dogs_database.db")

cursor = conn.cursor()

create_dog_profile_table = ('''
                            CREATE TABLE IF NOT EXISTS dog_profile (
                                breed TEXT NOT NULL PRIMARY KEY,
                                average_lifespan TEXT NOT NULL,
                                size TEXT NOT NULL,
                                weight_range TEXT NOT NULL,
                                coat_type TEXT NOT NULL,
                                color TEXT NOT NULL
                            )
                            ''')

create_dog_health_information_table = ('''
                                    CREATE TABLE IF NOT EXISTS dog_health_information (
                                        breed TEXT NOT NULL,
                                        recommended_diet TEXT NOT NULL,
                                        common_health_issues TEXT NOT NULL,
                                        exercise_needs TEXT NOT NULL,
                                        regular_check_up_schedule TEXT NOT NULL,
                                        FOREIGN KEY (breed) REFERENCES dog_profile (breed)
                                    )
                                        ''')

create_dog_behavior_and_training_table = ('''
                                    CREATE TABLE IF NOT EXISTS dog_behavior_and_training (
                                          breed TEXT NOT NULL,
                                          intelligence_level TEXT NOT NULL,
                                          trainability TEXT NOT NULL,
                                          socialization_needs TEXT NOT NULL,
                                          behavior_traits TEXT NOT NULL,
                                          FOREIGN KEY (breed) REFERENCES dog_profile (breed)
                                        )
                                        ''')

create_dog_maintenance_table = ('''
                            CREATE TABLE IF NOT EXISTS dog_maintenance (
                                breed TEXT NOT NULL,
                                hygiene_practices TEXT NOT NULL,
                                feeding_schedule TEXT NOT NULL,
                                grooming_routine TEXT NOT NULL,
                                environment TEXT NOT NULL,
                                FOREIGN KEY (breed) REFERENCES dog_profile (breed)
                            )
                                ''')


cursor.execute(create_dog_profile_table)
cursor.execute(create_dog_health_information_table)
cursor.execute(create_dog_behavior_and_training_table)
cursor.execute(create_dog_maintenance_table)

conn.commit()

def clear_entries():
    for i in range(1, 25):
        entry = globals().get(f'entry_{i}', None)
        if entry is not None:
            entry.delete(1.0, "end")

def display_afghan_hound_info():
    # Fetch data if it exists in the dog_profile table
    cursor.execute("SELECT * FROM dog_profile WHERE breed = 'Afghan Hound'")
    profile_info = cursor.fetchone()

    if profile_info:
        breed = profile_info[0]

        # Fetch information using the breed obtained from dog_profile
        cursor.execute("SELECT * FROM dog_behavior_and_training WHERE breed = ?", (breed,))
        behavior_info = cursor.fetchone()
        cursor.execute("SELECT * FROM dog_maintenance WHERE breed = ?", (breed,))
        mainte_info = cursor.fetchone()
        cursor.execute("SELECT * FROM dog_health_information WHERE breed = ?", (breed,))
        health_info = cursor.fetchone()

        # Clear display in entry widgets
        clear_entries()

        # Displaying in entry widgets (Modify for other fields)
        entry_1.insert('end', f"Breed: {profile_info[0]}")
        entry_2.insert('end', f"Average Lifespan: {profile_info[1]}")
        entry_3.insert('end', f"Size: {profile_info[2]}")
        entry_4.insert('end', f"Weight Range: {profile_info[3]}")
        entry_5.insert('end', f"Coat Type: {profile_info[4]}")
        entry_6.insert('end', f"Color: {profile_info[5]}")

        entry_7.insert('end', f"Intelligence Level: {behavior_info[1]}")
        entry_8.insert('end', f"Trainability: {behavior_info[2]}")
        entry_9.insert('end', f"Socialization Needs: {behavior_info[3]}")
        entry_10.insert('end', f"Behavior Traits: {behavior_info[4]}")  

        entry_13.insert('end', f"Hygiene Practices: {mainte_info[1]}")
        entry_14.insert('end', f"Feeding Schedule: {mainte_info[2]}")
        entry_15.insert('end', f"Grooming Routine: {mainte_info[3]}")
        entry_16.insert('end', f"Environment: {mainte_info[4]}") 

        entry_19.insert('end', f"Recommended Diet: {health_info[1]}")
        entry_20.insert('end', f"Common Health Issues: {health_info[2]}")
        entry_21.insert('end', f"Exercise Needs: {health_info[3]}")
        entry_22.insert('end', f"Regular Check Up Schedule: {health_info[4]}")  

    else:
        # If entry doesn't exist, add new data
        messagebox.showinfo("Failed", "No Afghan Hound data found. Adding new data...")
        profile_info = ('Afghan Hound', '12 to 14 years', 'Large', '50 to 60 pounds', 'Long and silky', 'Black, cream, red, and brindle')
        behavior_info = (profile_info[0], '3 out of 5', 'Independent but trainable', 'Moderate', 'Aloof with strangers, gentle and dignified')
        mainte_info = (profile_info[0], 'Regular brushing and bathing as needed', '2 to 3 times a day', 'Daily brushing', 'A spacious home with room to move')
        health_info = (profile_info[0], 'High-quality dog food', 'Hip dysplasia and Sensitivity to anesthesia', 'Moderate', 'Annual')
        cursor.execute("INSERT OR REPLACE INTO dog_profile VALUES (?, ?, ?, ?, ?, ?)", profile_info)
        cursor.execute("INSERT OR REPLACE INTO dog_behavior_and_training VALUES (?, ?, ?, ?, ?)", behavior_info)
        cursor.execute("INSERT OR REPLACE INTO dog_maintenance VALUES (?, ?, ?, ?, ?)", mainte_info)
        cursor.execute("INSERT OR REPLACE INTO dog_health_information VALUES (?, ?, ?, ?, ?)", health_info)
        conn.commit()
        messagebox.showinfo("Success", "New Afghan Hound information added to the database.")

def display_akita_info():
    # Fetch data if it exists in the dog_profile table
    cursor.execute("SELECT * FROM dog_profile WHERE breed = 'Akita'")
    profile_info = cursor.fetchone()

    if profile_info:
        breed = profile_info[0]

        # Fetch information using the breed obtained from dog_profile
        cursor.execute("SELECT * FROM dog_behavior_and_training WHERE breed = ?", (breed,))
        behavior_info = cursor.fetchone()
        cursor.execute("SELECT * FROM dog_maintenance WHERE breed = ?", (breed,))
        mainte_info = cursor.fetchone()
        cursor.execute("SELECT * FROM dog_health_information WHERE breed = ?", (breed,))
        health_info = cursor.fetchone()

        # Clear display in entry widgets
        clear_entries()

        # Displaying in entry widgets (Modify for other fields)
        entry_1.insert('end', f"Breed: {profile_info[0]}")
        entry_2.insert('end', f"Average Lifespan: {profile_info[1]}")
        entry_3.insert('end', f"Size: {profile_info[2]}")
        entry_4.insert('end', f"Weight Range: {profile_info[3]}")
        entry_5.insert('end', f"Coat Type: {profile_info[4]}")
        entry_6.insert('end', f"Color: {profile_info[5]}")

        entry_7.insert('end', f"Intelligence Level: {behavior_info[1]}")
        entry_8.insert('end', f"Trainability: {behavior_info[2]}")
        entry_9.insert('end', f"Socialization Needs: {behavior_info[3]}")
        entry_10.insert('end', f"Behavior Traits: {behavior_info[4]}")  

        entry_13.insert('end', f"Hygiene Practices: {mainte_info[1]}")
        entry_14.insert('end', f"Feeding Schedule: {mainte_info[2]}")
        entry_15.insert('end', f"Grooming Routine: {mainte_info[3]}")
        entry_16.insert('end', f"Environment: {mainte_info[4]}") 

        entry_19.insert('end', f"Recommended Diet: {health_info[1]}")
        entry_20.insert('end', f"Common Health Issues: {health_info[2]}")
        entry_21.insert('end', f"Exercise Needs: {health_info[3]}")
        entry_22.insert('end', f"Regular Check Up Schedule: {health_info[4]}")  

    else:
        # If entry doesn't exist, add new data
        messagebox.showinfo("Failed", "No Akita data found. Adding new data...")
        profile_info = ('Akita', '10 to 15 years', 'Large to Giant', '100 to 130 pounds', 'Thick and dense', 'Red, brindle, and pinto')
        behavior_info = (profile_info[0], '3 out of 5', 'Intelligent and responds well to consistent training', 'Early and consistent', 'Dignified, reserved and protective')
        mainte_info = (profile_info[0], 'Regular brushing and bathing as needed', '2 to 3 times a day', 'Weekly brushing', 'A home with a secure yard')
        health_info = (profile_info[0], 'Protein-rich diet', 'Hip dysplasia and Progressive retinal atrophy (PRA)', 'Moderate', 'Annual')
        cursor.execute("INSERT OR REPLACE INTO dog_profile VALUES (?, ?, ?, ?, ?, ?)", profile_info)
        cursor.execute("INSERT OR REPLACE INTO dog_behavior_and_training VALUES (?, ?, ?, ?, ?)", behavior_info)
        cursor.execute("INSERT OR REPLACE INTO dog_maintenance VALUES (?, ?, ?, ?, ?)", mainte_info)
        cursor.execute("INSERT OR REPLACE INTO dog_health_information VALUES (?, ?, ?, ?, ?)", health_info)
        conn.commit()
        messagebox.showinfo("Success", "New Akita information added to the database.")

def display_australian_sheperd_info():
    # Fetch data if it exists in the dog_profile table
    cursor.execute("SELECT * FROM dog_profile WHERE breed = 'Australian Shepherd'")
    profile_info = cursor.fetchone()

    if profile_info:
        breed = profile_info[0]

        # Fetch information using the breed obtained from dog_profile
        cursor.execute("SELECT * FROM dog_behavior_and_training WHERE breed = ?", (breed,))
        behavior_info = cursor.fetchone()
        cursor.execute("SELECT * FROM dog_maintenance WHERE breed = ?", (breed,))
        mainte_info = cursor.fetchone()
        cursor.execute("SELECT * FROM dog_health_information WHERE breed = ?", (breed,))
        health_info = cursor.fetchone()

        # Clear display in entry widgets
        clear_entries()

        # Displaying in entry widgets (Modify for other fields)
        entry_1.insert('end', f"Breed: {profile_info[0]}")
        entry_2.insert('end', f"Average Lifespan: {profile_info[1]}")
        entry_3.insert('end', f"Size: {profile_info[2]}")
        entry_4.insert('end', f"Weight Range: {profile_info[3]}")
        entry_5.insert('end', f"Coat Type: {profile_info[4]}")
        entry_6.insert('end', f"Color: {profile_info[5]}")

        entry_7.insert('end', f"Intelligence Level: {behavior_info[1]}")
        entry_8.insert('end', f"Trainability: {behavior_info[2]}")
        entry_9.insert('end', f"Socialization Needs: {behavior_info[3]}")
        entry_10.insert('end', f"Behavior Traits: {behavior_info[4]}")  

        entry_13.insert('end', f"Hygiene Practices: {mainte_info[1]}")
        entry_14.insert('end', f"Feeding Schedule: {mainte_info[2]}")
        entry_15.insert('end', f"Grooming Routine: {mainte_info[3]}")
        entry_16.insert('end', f"Environment: {mainte_info[4]}") 

        entry_19.insert('end', f"Recommended Diet: {health_info[1]}")
        entry_20.insert('end', f"Common Health Issues: {health_info[2]}")
        entry_21.insert('end', f"Exercise Needs: {health_info[3]}")
        entry_22.insert('end', f"Regular Check Up Schedule: {health_info[4]}")  

    else:
        # If entry doesn't exist, add new data
        messagebox.showinfo("Failed", "No Australian Shepherd data found. Adding new data...")
        profile_info = ('Australian Shepherd', '12 to 15 years', 'Medium to Large', '40 to 65 pounds', 'Docked tails and smooth coats', 'Black, blue merle, red, and red merle')
        behavior_info = (profile_info[0], '5 out of 5', 'Highly trainable, excels in obedience and agility', 'High', 'Intelligent and energetic')
        mainte_info = (profile_info[0], 'Regular brushing and bathing as needed', '2 to 3 times a day', 'Weekly brushing', 'A home with space to move and a yard to play')
        health_info = (profile_info[0], 'High-quality dog food', 'Collie eye anomaly', 'Moderate', 'Annual')
        cursor.execute("INSERT OR REPLACE INTO dog_profile VALUES (?, ?, ?, ?, ?, ?)", profile_info)
        cursor.execute("INSERT OR REPLACE INTO dog_behavior_and_training VALUES (?, ?, ?, ?, ?)", behavior_info)
        cursor.execute("INSERT OR REPLACE INTO dog_maintenance VALUES (?, ?, ?, ?, ?)", mainte_info)
        cursor.execute("INSERT OR REPLACE INTO dog_health_information VALUES (?, ?, ?, ?, ?)", health_info)
        conn.commit()
        messagebox.showinfo("Success", "New Australian Shepherd information added to the database.")

def display_beagle_info():
    # Fetch data if it exists in the dog_profile table
    cursor.execute("SELECT * FROM dog_profile WHERE breed = 'Beagle'")
    profile_info = cursor.fetchone()

    if profile_info:
        breed = profile_info[0]

        # Fetch information using the breed obtained from dog_profile
        cursor.execute("SELECT * FROM dog_behavior_and_training WHERE breed = ?", (breed,))
        behavior_info = cursor.fetchone()
        cursor.execute("SELECT * FROM dog_maintenance WHERE breed = ?", (breed,))
        mainte_info = cursor.fetchone()
        cursor.execute("SELECT * FROM dog_health_information WHERE breed = ?", (breed,))
        health_info = cursor.fetchone()

        # Clear display in entry widgets
        clear_entries()

        # Displaying in entry widgets (Modify for other fields)
        entry_1.insert('end', f"Breed: {profile_info[0]}")
        entry_2.insert('end', f"Average Lifespan: {profile_info[1]}")
        entry_3.insert('end', f"Size: {profile_info[2]}")
        entry_4.insert('end', f"Weight Range: {profile_info[3]}")
        entry_5.insert('end', f"Coat Type: {profile_info[4]}")
        entry_6.insert('end', f"Color: {profile_info[5]}")

        entry_7.insert('end', f"Intelligence Level: {behavior_info[1]}")
        entry_8.insert('end', f"Trainability: {behavior_info[2]}")
        entry_9.insert('end', f"Socialization Needs: {behavior_info[3]}")
        entry_10.insert('end', f"Behavior Traits: {behavior_info[4]}")  

        entry_13.insert('end', f"Hygiene Practices: {mainte_info[1]}")
        entry_14.insert('end', f"Feeding Schedule: {mainte_info[2]}")
        entry_15.insert('end', f"Grooming Routine: {mainte_info[3]}")
        entry_16.insert('end', f"Environment: {mainte_info[4]}") 

        entry_19.insert('end', f"Recommended Diet: {health_info[1]}")
        entry_20.insert('end', f"Common Health Issues: {health_info[2]}")
        entry_21.insert('end', f"Exercise Needs: {health_info[3]}")
        entry_22.insert('end', f"Regular Check Up Schedule: {health_info[4]}")  

    else:
        # If entry doesn't exist, add new data
        messagebox.showinfo("Failed", "No Beagle data found. Adding new data...")
        profile_info = ('Beagle', '12 to 15 years', 'Small to Medium', '18 to 30 pounds', 'Short, dense and smooth', 'Tricolor (black, white, and brown), red and white, lemon and white')
        behavior_info = (profile_info[0], '2 out of 5', 'Responsive to positive reinforcement, particularly food rewards', 'Moderate', 'Friendly and curious. Has a strong sense of smell')
        mainte_info = (profile_info[0], 'Regular brushing and bathing as needed', '2 to 3 times a day', 'Regular brushing', 'A home with a yard or access to outdoor spaces')
        health_info = (profile_info[0], 'Balanced diet to prevent obesity', 'Obesity and ear infection', 'Moderate', 'Annual')
        cursor.execute("INSERT OR REPLACE INTO dog_profile VALUES (?, ?, ?, ?, ?, ?)", profile_info)
        cursor.execute("INSERT OR REPLACE INTO dog_behavior_and_training VALUES (?, ?, ?, ?, ?)", behavior_info)
        cursor.execute("INSERT OR REPLACE INTO dog_maintenance VALUES (?, ?, ?, ?, ?)", mainte_info)
        cursor.execute("INSERT OR REPLACE INTO dog_health_information VALUES (?, ?, ?, ?, ?)", health_info)
        conn.commit()
        messagebox.showinfo("Success", "New Beagle information added to the database.")

def display_boxer_info():
    # Fetch data if it exists in the dog_profile table
    cursor.execute("SELECT * FROM dog_profile WHERE breed = 'Boxer'")
    profile_info = cursor.fetchone()

    if profile_info:
        breed = profile_info[0]

        # Fetch information using the breed obtained from dog_profile
        cursor.execute("SELECT * FROM dog_behavior_and_training WHERE breed = ?", (breed,))
        behavior_info = cursor.fetchone()
        cursor.execute("SELECT * FROM dog_maintenance WHERE breed = ?", (breed,))
        mainte_info = cursor.fetchone()
        cursor.execute("SELECT * FROM dog_health_information WHERE breed = ?", (breed,))
        health_info = cursor.fetchone()

        # Clear display in entry widgets
        clear_entries()

        # Displaying in entry widgets (Modify for other fields)
        entry_1.insert('end', f"Breed: {profile_info[0]}")
        entry_2.insert('end', f"Average Lifespan: {profile_info[1]}")
        entry_3.insert('end', f"Size: {profile_info[2]}")
        entry_4.insert('end', f"Weight Range: {profile_info[3]}")
        entry_5.insert('end', f"Coat Type: {profile_info[4]}")
        entry_6.insert('end', f"Color: {profile_info[5]}")

        entry_7.insert('end', f"Intelligence Level: {behavior_info[1]}")
        entry_8.insert('end', f"Trainability: {behavior_info[2]}")
        entry_9.insert('end', f"Socialization Needs: {behavior_info[3]}")
        entry_10.insert('end', f"Behavior Traits: {behavior_info[4]}")  

        entry_13.insert('end', f"Hygiene Practices: {mainte_info[1]}")
        entry_14.insert('end', f"Feeding Schedule: {mainte_info[2]}")
        entry_15.insert('end', f"Grooming Routine: {mainte_info[3]}")
        entry_16.insert('end', f"Environment: {mainte_info[4]}") 

        entry_19.insert('end', f"Recommended Diet: {health_info[1]}")
        entry_20.insert('end', f"Common Health Issues: {health_info[2]}")
        entry_21.insert('end', f"Exercise Needs: {health_info[3]}")
        entry_22.insert('end', f"Regular Check Up Schedule: {health_info[4]}")  

    else:
        # If entry doesn't exist, add new data
        messagebox.showinfo("Failed", "No Boxer data found. Adding new data...")
        profile_info = ('Boxer', '10 to 12 years', 'Medium to Large', '50 to 80 pounds', 'Short and smooth', 'Fawn or brindle with a black mask')
        behavior_info = (profile_info[0], '4 out of 5', 'Energetic and trainable with consistent, positive methods', 'High', 'Playful and energetic')
        mainte_info = (profile_info[0], 'Minimal brushing and bathing as needed', '2 to 3 times a day', 'Weekly brushing', 'A home with room to play')
        health_info = (profile_info[0], 'High-quality dog food with moderate protein levels', 'Heart conditions (aortic stenosis)', 'Moderate', 'Annual')
        cursor.execute("INSERT OR REPLACE INTO dog_profile VALUES (?, ?, ?, ?, ?, ?)", profile_info)
        cursor.execute("INSERT OR REPLACE INTO dog_behavior_and_training VALUES (?, ?, ?, ?, ?)", behavior_info)
        cursor.execute("INSERT OR REPLACE INTO dog_maintenance VALUES (?, ?, ?, ?, ?)", mainte_info)
        cursor.execute("INSERT OR REPLACE INTO dog_health_information VALUES (?, ?, ?, ?, ?)", health_info)
        conn.commit()
        messagebox.showinfo("Success", "New Boxer information added to the database.")

def display_bulldog_info():
    # Fetch data if it exists in the dog_profile table
    cursor.execute("SELECT * FROM dog_profile WHERE breed = 'Bulldog'")
    profile_info = cursor.fetchone()

    if profile_info:
        breed = profile_info[0]

        # Fetch information using the breed obtained from dog_profile
        cursor.execute("SELECT * FROM dog_behavior_and_training WHERE breed = ?", (breed,))
        behavior_info = cursor.fetchone()
        cursor.execute("SELECT * FROM dog_maintenance WHERE breed = ?", (breed,))
        mainte_info = cursor.fetchone()
        cursor.execute("SELECT * FROM dog_health_information WHERE breed = ?", (breed,))
        health_info = cursor.fetchone()

        # Clear display in entry widgets
        clear_entries()

        # Displaying in entry widgets (Modify for other fields)
        entry_1.insert('end', f"Breed: {profile_info[0]}")
        entry_2.insert('end', f"Average Lifespan: {profile_info[1]}")
        entry_3.insert('end', f"Size: {profile_info[2]}")
        entry_4.insert('end', f"Weight Range: {profile_info[3]}")
        entry_5.insert('end', f"Coat Type: {profile_info[4]}")
        entry_6.insert('end', f"Color: {profile_info[5]}")

        entry_7.insert('end', f"Intelligence Level: {behavior_info[1]}")
        entry_8.insert('end', f"Trainability: {behavior_info[2]}")
        entry_9.insert('end', f"Socialization Needs: {behavior_info[3]}")
        entry_10.insert('end', f"Behavior Traits: {behavior_info[4]}")  

        entry_13.insert('end', f"Hygiene Practices: {mainte_info[1]}")
        entry_14.insert('end', f"Feeding Schedule: {mainte_info[2]}")
        entry_15.insert('end', f"Grooming Routine: {mainte_info[3]}")
        entry_16.insert('end', f"Environment: {mainte_info[4]}") 

        entry_19.insert('end', f"Recommended Diet: {health_info[1]}")
        entry_20.insert('end', f"Common Health Issues: {health_info[2]}")
        entry_21.insert('end', f"Exercise Needs: {health_info[3]}")
        entry_22.insert('end', f"Regular Check Up Schedule: {health_info[4]}")  

    else:
        # If entry doesn't exist, add new data
        messagebox.showinfo("Failed", "No Bulldog data found. Adding new data...")
        profile_info = ('Bulldog', '8 to 12 years', 'Medium', '40 to 50 pounds', 'Short and smooth', 'Brindle, fawn, and white')
        behavior_info = (profile_info[0], '3 out of 5', 'May be laid-back but responds to positive reinforcement', 'Moderate', 'Calm, gentle, and affectionate. Also good with children')
        mainte_info = (profile_info[0], 'Regular cleaning of facial wrinkles and bathing as needed.', '2 to 3 times a day', 'Regular facial fold cleaning', 'Indoor living. Comfortable with limited outdoor exercise')
        health_info = (profile_info[0], 'Balanced diet', 'Brachycephalic airway syndrome', 'Moderate', 'Annual')
        cursor.execute("INSERT OR REPLACE INTO dog_profile VALUES (?, ?, ?, ?, ?, ?)", profile_info)
        cursor.execute("INSERT OR REPLACE INTO dog_behavior_and_training VALUES (?, ?, ?, ?, ?)", behavior_info)
        cursor.execute("INSERT OR REPLACE INTO dog_maintenance VALUES (?, ?, ?, ?, ?)", mainte_info)
        cursor.execute("INSERT OR REPLACE INTO dog_health_information VALUES (?, ?, ?, ?, ?)", health_info)
        conn.commit()
        messagebox.showinfo("Success", "New Bulldog information added to the database.")

# =====================================================
# Buttons
# =====================================================

# Back Button
def go_back():
    window.destroy()
    subprocess.run([sys.executable, r"D:\School\College\Codes\DogCat Information System\Main.py"])

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=go_back,
    relief="flat"
)
button_1.place(
    x=920.0,
    y=533.0,
    width=85.5111083984375,
    height=35.302734375
)

button_3 = Button(
    text="Afghan Hound",
    background="#424242",
    foreground="white",
    borderwidth=1,
    highlightthickness=0,
    command=display_afghan_hound_info,
    relief="flat"
)
button_3.place(
    x=0.0,
    y=146.0,
    width=199.0,
    height=43.0
)

button_4 = Button(
    text="Akita",
    background="#424242",
    foreground="white",
    borderwidth=1,
    highlightthickness=0,
    command=display_akita_info,
    relief="flat"
)
button_4.place(
    x=0.0,
    y=189.0,
    width=199.0,
    height=43.0
)

button_5 = Button(
    text="Australian Shepherd",
    background="#424242",
    foreground="white",
    borderwidth=1,
    highlightthickness=0,
    command=display_australian_sheperd_info,
    relief="flat"
)
button_5.place(
    x=0.0,
    y=232.0,
    width=199.0,
    height=43.0
)

button_6 = Button(
    text="Beagle",
    background="#424242",
    foreground="white",
    borderwidth=1,
    highlightthickness=0,
    command=display_beagle_info,
    relief="flat"
)
button_6.place(
    x=0.0,
    y=275.0,
    width=199.0,
    height=43.0
)

button_7 = Button(
    text="Boxer",
    background="#424242",
    foreground="white",
    borderwidth=1,
    highlightthickness=0,
    command=display_boxer_info,
    relief="flat"
)
button_7.place(
    x=0.0,
    y=318.0,
    width=199.0,
    height=43.0
)

button_8 = Button(
    text="Bulldog",
    background="#424242",
    foreground="white",
    borderwidth=1,
    highlightthickness=0,
    command=display_bulldog_info,
    relief="flat"
)
button_8.place(
    x=0.0,
    y=361.0,
    width=199.0,
    height=43.0
)

button_9 = Button(
    text="PLACEHOLDER",
    background="#424242",
    foreground="white",
    borderwidth=1,
    highlightthickness=0,
    command=lambda: print("button_9 clicked"),
    relief="flat"
)
button_9.place(
    x=0.0,
    y=404.0,
    width=199.0,
    height=43.0
)

button_10 = Button(
    text="PLACEHOLDER",
    background="#424242",
    foreground="white",
    borderwidth=1,
    highlightthickness=0,
    command=lambda: print("button_10 clicked"),
    relief="flat"
)
button_10.place(
    x=0.0,
    y=447.0,
    width=199.0,
    height=43.0
)

button_11 = Button(
    text="PLACEHOLDER",
    background="#424242",
    foreground="white",
    borderwidth=1,
    highlightthickness=0,
    command=lambda: print("button_11 clicked"),
    relief="flat"
)
button_11.place(
    x=0.0,
    y=490.0,
    width=199.0,
    height=43.0
)

button_12 = Button(
    text="PLACEHOLDER",
    background="#424242",
    foreground="white",
    borderwidth=1,
    highlightthickness=0,
    command=lambda: print("button_12 clicked"),
    relief="flat"
)
button_12.place(
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

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    320.5,
    173.5,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    font=("Cascadia Mono", 8),
    wrap="word",
    highlightthickness=0
)
entry_1.place(
    x=224.0,
    y=146.0,
    width=193.0,
    height=53.0
)

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
    highlightthickness=0
)
entry_8.place(
    x=224.0,
    y=416.0,
    width=193.0,
    height=53.0
)

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
