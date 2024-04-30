
# App functions
from csv_function import add_char

#  ---------- Create Character Feature ----------
class Character:
    # Class attribute defining attributes for each character class
    class_attributes = {
        "Warrior": {"Str": 10, "Dex": 5, "Int": 3},
        "Mage": {"Str": 3, "Dex": 5, "Int": 10},
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
        # Print character details
        print(f"Name: {self.name}")
        print(f"Race: {self.race}")
        print(f"Class: {self.char_class}")
        print("Attributes:")
        for attr, value in self.attributes.items():
            print(f"- {attr}: {value}")
        print("Abilities:")
        for ability, description in self.abilities.items():
            print(f"- {ability}: {description}")

# Function to create a new character
def new_Char():
    # Prompt the user to enter character details
    name = input("Enter character name: ")
    race = input("Enter character race (Human/Elf/Drawf): ")
    # Validate the entered race
    while race not in ["Human", "Elf", "Drawf"]:
        print ("Sorry invalid race. Please choose only from Human, Elf or Drawf.")
        race = input("Enter character race (Human/Elf/Drawf): ")

    char_class = input("Enter character class (Warrior/Mage/Rogue): ")
    # Validate the entered class
    while char_class not in ["Warrior", "Mage", "Rogue"]:
        print("Invalid class. Please choose from Warrior, Mage, or Rogue.")
        char_class = input("Enter character class (Warrior/Mage/Rogue): ")
    # Create a Character object with the entered details
    character = Character(name, race, char_class)
    # Display character details
    character.display_details()
    # Add character to CSV file
    add_char(character)