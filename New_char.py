
# Creating Character function
class Character:
    class_attributes = {
        "Warrior": {"Strength": 10, "Dexterity": 5, "Intelligence": 3},
        "Mage": {"Strength": 3, "Dexterity": 5, "Intelligence": 10},
        "Rogue": {"Strength": 5, "Dexterity": 10, "Intelligence": 5}
    }






# Function to create a new character
def create_character():
    name = input("Enter character name: ")
    race = input("Enter character race (Human/Elf/Drawf): ")
    char_class = input("Enter character class (Warrior/Mage/Rogue): ")

    character = Character(name, race, char_class)