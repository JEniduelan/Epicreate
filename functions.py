import os
import csv

# Function to create a new character
def create_character():
    name = input("Enter character name: ")
    race = input("Enter character race: ")
    character_class = input("Enter character class: ")
    attributes = input("Enter character attributes: ")
    abilities = input("Enter character abilities: ")

    return {"Name": name, "Race": race, "Class": character_class, "Attributes": attributes, "Abilities": abilities}