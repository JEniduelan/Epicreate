# System Packages
import csv
import os

# External Packages

# App functions
from New_char import create_character
# Main App

print("Welcome to Epicreate")

# Menu function
def main_menu():
    while True:
        print("\nMain Menu:")
        print("> Enter 1 to create a character ")
        print("> Enter 2 to delete created character ")
        print("> Enter 3 to view created character ")
        print("> Enter 4 to exit ")

        choice = input("Enter your choice: ")
        return choice


csv_file = "Characters.csv"

choice = ""

while choice != "4":
      choice = main_menu()

      if choice == "1":
           create_character()
      elif choice == "2":
            print(2)
      elif choice == "3":
            print(3)
      elif choice == "4":
            print("\nThank you for using Epicreate!")
      else:
            print("Please only enter a number between 1 - 4. Thank you")

print("Goodbye...\n")