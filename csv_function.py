import csv
import os.path

Character_list = "characters.csv"

#  ---------- Add Character Feature ----------
def add_char(character):
    Header = ["Name", "Race", "Class", "Attributes", "Abilities"]
    file_exists = os.path.isfile(Character_list)

    with open(Character_list, "a", newline="") as f:
        writer = csv.DictWriter(f, Header)

        if not file_exists:
            writer.writeheader()

        writer.writerow({
            "Name": character.name,
            "Race": character.race,
            "Class": character.char_class,
            "Attributes": character.attributes,
            "Abilities": character.abilities
         })
        
    print("\nCharacter created successfully")

# ---------- Remove Character Feature ----------
def remove_Char():
    if (not os.path.isfile(Character_list)):
        print("\nYou have not created any characters yet!")
        return
    
    with open(Character_list, "r", newline="") as f:
        reader = csv.DictReader(f)
        characters = list(reader)

    if not characters:
        print("No characters found! Please create a character first")
        return
    
    print("\nHere are the list of your characters\n")
    for Char_num, character in enumerate(characters, start=1):
        print(f"{Char_num}. {character['Name']} - {character['Race']} - {character['Class']}")

    try:
        Char_num = int(input("\nEnter the number of the character you wish to remove: "))
        if Char_num < 1 or Char_num > len(characters):
            print("Invalid index number.")
            return
        
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    removed_char = characters.pop(Char_num - 1)
    with open(Character_list, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=removed_char.keys())
        writer.writeheader()
        writer.writerows(characters)

    print(f"\nYour character '{removed_char["Name"]}' has been removed.")

# ---------- View Character Feature ----------
def view_Char():
    try:
        with open(Character_list,"r") as f:
            reader = csv.DictReader(f)
            if not reader.fieldnames:
                print("\nSorry, There are no characters found.")
                return
            
            for row in reader:
                print(row)

    except FileNotFoundError:
        print("\nPlease create a character first before continuing")





    
