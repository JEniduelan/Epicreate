import csv
import os.path

Character_list = "characters.csv"

# Add character function to csv file
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
        
    print("Character created successfully")


def remove_Char():
    if (not os.path.isfile(Character_list)):
        print("You have not created any characters yet!")
        return




    
