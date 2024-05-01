


# App functions
import csv
import os.path

Character_list = "characters.csv"

#  ---------- Add Character Feature ----------

# Function to add a character
def add_char(character):
    # Define the header for the CSV file
    Header = ["Name", "Race", "Class", "Attributes", "Abilities"]
    # Check if the CSV file already exists
    file_exists = os.path.isfile(Character_list)

    # Open the CSV file in append mode
    with open(Character_list, "a", newline="") as f:
        # Create a CSV writer object
        writer = csv.DictWriter(f, Header)

        # If the file doesn't exist, write the header
        if not file_exists:
            writer.writeheader()

        # Write a new row to the CSV file with character details
        writer.writerow({
            "Name": character.name,
            "Race": character.race,
            "Class": character.char_class,
            "Attributes": character.attributes,
            "Abilities": character.abilities
         })
    # Print a success message 
    print("\nCharacter created successfully")

# ---------- Remove Character Feature ----------

# Function to remove a character
def remove_Char():
    # Check if the CSV file exists
    if (not os.path.isfile(Character_list)):
        print("\nYou have not created any characters yet!")
        return
    # Read character data from the CSV file
    with open(Character_list, "r", newline="") as f:
        reader = csv.DictReader(f)
        characters = list(reader)
    # Check if there are any characters in the list then print
    if not characters:
        print("No characters found! Please create a character first")
        return
    # Display the list of characters
    print("\nHere are the list of your characters\n")
    for Char_num, character in enumerate(characters, start=1):
        print(f"{Char_num}. {character['Name']} - {character['Race']} - {character['Class']}")

    try:
        # Prompt the user to select a character to remove
        Char_num = int(input("\nEnter the number of the character you wish to remove: "))
        if Char_num < 1 or Char_num > len(characters):
            print("Invalid index number.")
            return
        
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    # Remove the selected character from the list
    removed_char = characters.pop(Char_num - 1)
    # Write the updated list of characters back to the CSV file
    with open(Character_list, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=removed_char.keys())
        writer.writeheader()
        writer.writerows(characters)
    # Print confirmation message
    print(f"\nYour character '{removed_char["Name"]}' has been removed.")

# ---------- View Character Feature ----------

# Function to view characters stored in the CSV file
def view_Char():
    try:
        # Attempts to open the CSV file and read character data
        with open(Character_list,"r") as f:
            reader = csv.DictReader(f)
            # Checks if the file is empty or characters exist, and prints them
            if not reader.fieldnames:
                print("\nSorry, There are no characters found.")
                return
            
            for row in reader:
                print(row)
    # Handles FileNotFoundError if the file does not exist
    except FileNotFoundError:
        print("\nPlease create a character first before continuing")





    
