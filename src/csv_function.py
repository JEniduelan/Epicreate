
# App functions
import csv
import os.path
import ast

from colored import Fore, Back, Style
from rich.console import Console
from rich.table import Table


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
    print(f"\n{Fore.yellow}You have successfully created your character!{Style.reset} ✅")

    while True:
            user_input = input(f"{Fore.light_cyan}\nPress Enter to continue...{Style.reset}")
            if user_input == "":
                    break
    

# ---------- Remove Character Feature ----------

# Function to remove a character
def remove_Char():
    # Check if the CSV file exists
    if (not os.path.isfile(Character_list)):
        print(f"\n🚨{Fore.red}You have not created any characters yet!{Style.reset}🚨")
        return
    # Read character data from the CSV file
    with open(Character_list, "r", newline="") as f:
        reader = csv.DictReader(f)
        characters = list(reader)
    # Check if there are any characters in the list then print
    if not characters:
        print(f"\n🚨{Back.red}No characters found!{Style.reset}🚨")
        print(f"{Fore.yellow}Please create a character first{Style.reset}\n")
        return
    # Create a rich Table
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Character Number", style="cyan")
    table.add_column("Name", style="green")
    table.add_column("Race", style="blue")
    table.add_column("Class", style="yellow")

    # Add rows to the table
    for Char, character in enumerate(characters, start=1):
        table.add_row(
            str(Char),
            character['Name'],
            character['Race'],
            character['Class']
        )

    # Print the table
    console = Console()
    console.print("\nHere are the list of your characters\n",style="yellow")
    console.print(table)

    try:
        # Prompt the user to select a character to remove
        Char_num = int(input(f"\nEnter the number of the character you wish to {Fore.red}remove{Style.reset}: "))
        if Char_num < 1 or Char_num > len(characters):
            print(f"\n🚨{Fore.yellow}Please enter the character number{Style.reset}🚨")
            return remove_Char()
        
    except ValueError:
        print(f"\n🚨{Back.red}Invalid input{Style.reset}🚨")
        print(f"{Fore.yellow}Please enter the character number!{Style.reset}\n")
        return remove_Char()
    # Remove the selected character from the list
    removed_char = characters.pop(Char_num - 1)
    # Write the updated list of characters back to the CSV file
    with open(Character_list, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=removed_char.keys())
        writer.writeheader()
        writer.writerows(characters)
    # Print confirmation message
    print(f"\n{Fore.yellow}Your character '{removed_char["Name"]}' has been removed{Style.reset} ✅")

    while True:
            user_input = input(f"{Fore.light_cyan}\nPress Enter to continue...{Style.reset}")
            if user_input == "":
                    break


# ---------- View Character Feature ----------

def view_Char():
    try:
        # Attempt to open the CSV file for reading
        with open(Character_list, "r", newline="") as f:
            # Create a CSV reader object
            reader = csv.DictReader(f)
            rows = list(reader)
            if not rows:
                print(f"\n🚨{Fore.red}Sorry, There are no characters found.{Style.reset}🚨")
                return
            
            # Create a rich Table
            table = Table(show_header=True, header_style="bold magenta")
            table.add_column("Name", style="cyan")
            table.add_column("Race", style="green")
            table.add_column("Class", style="blue")
            table.add_column("Attributes", style="yellow")
            table.add_column("Abilities", style="red")
            
            # Add rows to the table
            for row in rows:
                attributes = ast.literal_eval(row["Attributes"])
                abilities = ast.literal_eval(row["Abilities"])
                table.add_row(
                    row["Name"], 
                    row["Race"], 
                    row["Class"], 
                    "\n".join([f"{key}: {value}" for key, value in attributes.items()]), 
                    "\n".join([f"{key}: {value}" for key, value in abilities.items()])
                )
            
            # Print the table
            console = Console()
            console.print(table)

        while True:
            user_input = input(f"{Fore.light_cyan}\nPress Enter to continue...{Style.reset}")
            if user_input == "":
                    break
            
        
                    
    except FileNotFoundError:
        print(f"\n🚨{Fore.red}Please create a character first before viewing.{Style.reset}🚨")