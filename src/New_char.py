from colored import Fore, Back, Style
from rich import emoji

from rich.console import Console
from rich.table import Table

# App functions
from csv_function import add_char

#  ---------- Create Character Feature ----------
class Character:
    # Class attribute defining attributes for each character class
    class_attributes = {
        "Warrior": {"Str": 10, "Dex": 5, "Int": 3},
        "Mage": {"Str ":3, "Dex ": 5, "Int ": 10},
        "Rogue": {"Str": 5, "Dex": 10, "Int": 5}
    }

    # Constructor method to initialize a character object
    def __init__(self, name, race, char_class):
        self.name = name
        self.race = race
        self.char_class = char_class
        # Assign attributes based on class
        self.attributes = self.assign_attributes() 
        # Empty dictionary for abilities
        self.abilities = {}
        # Assign abilities based on class
        self.assign_abilities()

    # Method to assign attributes based on character class
    def assign_attributes(self):
        # Retrieve attributes from class_attributes dictionary
        return self.class_attributes.get(self.char_class, {})
    
    # Method to assign abilities based on character class
    def assign_abilities(self):
        # Assign abilities based on character class
        if self.char_class == "Warrior":
            self.abilities["Taunt"] = "Make nearby enemies to attack you"
            self.abilities["Berserker Rage"] = "Makes the user deal additional damage and reduce incoming damage"
        elif self.char_class == "Mage":
            self.abilities["Fireball"] = "Launch a ball of fire at enemies"
            self.abilities["Teleport"] = "Instantly teleport short distances"
        elif self.char_class == "Rogue":
            self.abilities["Backstab"] = "Sneak behind enemies and deal extra damage"
            self.abilities["Stealth"] = "Become invisible temporarily"

    # Method to display character details
    def display_details(self):
        # Create a rich Table
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Category", style="cyan", width=15)
        table.add_column("Detail", style="green")

        # Add character details to the table
        table.add_row("Name:", self.name)
        table.add_row("Race:", self.race)
        table.add_row("Class:", self.char_class)

        # Add a separator row
        table.add_row(" ", " ")

        # Add attributes to the table
        attributes_text = "\n".join([f"{attr}: {value}" for attr, value in self.attributes.items()])
        table.add_row("Attributes:", attributes_text)

        # Add abilities to the table
        abilities_text = "\n".join([f"{ability}: {description}" for ability, description in self.abilities.items()])
        table.add_row("Abilities:", abilities_text)
        
        # Print the table
        console = Console()
        console.print(table)

# Function to create a new character
def new_Char():
    # Prompt the user to enter character details
    name = input(f"Enter character's name: ")
    race = input(f"Enter character's race (👨 {Fore.yellow}Human{Style.reset} 🧝 {Fore.blue}Elf{Style.reset} 🧔 {Fore.green}Drawf{Style.reset}): ")
    # Validate the entered race
    while race not in ["Human", "Elf", "Drawf"]:
        print(f"\n🚨{Back.red}Sorry invalid race{Style.reset}🚨")
        print(f"🚨Please choose only from {Fore.yellow}Human{Style.reset}, {Fore.blue}Elf{Style.reset} or {Fore.green}Drawf{Style.reset} 🚨")
        race = input(f"\nEnter character's race (👨 {Fore.yellow}Human{Style.reset} 🧝 {Fore.blue}Elf{Style.reset} 🧔 {Fore.green}Drawf{Style.reset}): ")

    char_class = input(f"Enter character's class (🛡️ {Fore.red}Warrior{Style.reset} 🧙{Fore.blue}Mage{Style.reset} 🗡️ {Fore.cyan}Rogue{Style.reset}): ")
    # Validate the entered class
    while char_class not in ["Warrior", "Mage", "Rogue"]:
        print(f"\n🚨{Back.red}Invalid class{Style.reset}🚨")
        print(f"Please choose from {Fore.red}Warrior{Style.reset}, {Fore.blue}Mage{Style.reset}, or {Fore.cyan}Rogue{Style.reset}.")
        char_class = input(f"\nEnter character's class (🛡️ {Fore.red}Warrior{Style.reset} 🧙{Fore.blue}Mage{Style.reset} 🗡️ {Fore.cyan}Rogue{Style.reset}): ")
    # Create a Character object with the entered details
    character = Character(name, race, char_class)
    # Display character details
    character.display_details()
    # Add character to CSV file
    add_char(character)