import csv
import os.path


# Add character function to csv file
def add_char(character):
    Header = ["Name", "Race", "Class", "Attributes", "Abilities"]
    file_exists = os.path.isfile("characters.csv")

    with open("characters.csv", "a", newline="") as f:
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


    



