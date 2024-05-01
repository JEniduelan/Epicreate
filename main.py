# System Packages
import csv

# External Packages
from colored import Fore, Back, Style
from rich import emoji
# App functions
from New_char import new_Char
from csv_function import remove_Char, view_Char

# ---------- Main Application ----------

# ---------- Application title ----------
print("\nWelcome to Epicreate")

# ---------- Main menu ----------
def main_menu():
    # Display the main menu and get user input
    while True:
        print("\nMain Menu:")
        print("> Enter 1 to create a character ")
        print("> Enter 2 to delete created character ")
        print("> Enter 3 to view created character ")
        print("> Enter 4 to exit ")

        choice = input("\nEnter your choice: ")
        return choice



# ---------- Implementation of the main logic of the application ----------

choice = ""

# Continuously prompt the user until they choose to exit
while choice != "4":
      choice = main_menu()

      # Call the function to create a new character
      if choice == "1":
           new_Char()
      # Call the function to remove a character
      elif choice == "2":
            remove_Char()
      # Call the function to view characters
      elif choice == "3":
            view_Char()
      # Exit the program
      elif choice == "4":
            print("\nThank you for using Epicreate!")
      # Handle invalid input
      else:
            print("\nPlease only enter a number between 1 - 4. Thank you")

# Exit message
print("Goodbye...\n")














