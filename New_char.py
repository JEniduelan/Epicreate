
# Character dictionary
class Character:

    class_attributes = {
        "Warrior": {"Strength": 10, "Dexterity": 5, "Intelligence": 3},
        "Mage": {"Strength": 3, "Dexterity": 5, "Intelligence": 10},
        "Rogue": {"Strength": 5, "Dexterity": 10, "Intelligence": 5}
    }

    def __init__(self, name, race, char_class):
        self.name = name
        self.race = race
        self.char_class = char_class
        self.attributes = self.assign_attributes()
        self.abilities = {}
        self.assign_abilities()

    def assign_attributes(self):
        return self.class_attributes.get(self.char_class, {})
    
    def assign_abilities(self):
        if self.char_class == "Warrior":
            self.abilities["Taunt"] = "Make nearby enemies to attack you"
            self.abilities["Berserker Rage"] = "Makes the user deal additional damage and reduce incoming damage"
        elif self.char_class == "Mage":
            self.abilities["Fireball"] = "Launch a ball of fire at enemies"
            self.abilities["Teleport"] = "Instantly teleport short distances"
        elif self.char_class == "Rogue":
            self.abilities["Backstab"] = "Sneak behind enemies and deal extra damage"
            self.abilities["Stealth"] = "Become invisible temporarily"

    def display_details(self):
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
def create_character():
    name = input("Enter character name: ")

    race = input("Enter character race (Human/Elf/Drawf): ")
    while race not in ["Human", "Elf", "Drawf"]:
        print ("Sorry invalid race. Please choose only from Human, Elf or Drawf.")
        race = input("Enter character race (Human/Elf/Drawf): ")

    char_class = input("Enter character class (Warrior/Mage/Rogue): ")
    while char_class not in ["Warrior", "Mage", "Rogue"]:
        print("Invalid class. Please choose from Warrior, Mage, or Rogue.")
        char_class = input("Enter character class (Warrior/Mage/Rogue): ")

    character = Character(name, race, char_class)
    character.display_details()