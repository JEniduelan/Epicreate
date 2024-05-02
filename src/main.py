# External Packages
from colored import Fore, Back, Style
from rich import emoji

# App functions
from New_char import new_Char
from csv_function import remove_Char, view_Char

# ---------- Main Application ----------
print(f"\n|============ {Fore.green_4}Welcome{Style.reset} ============|")
print(f"|====🔥======== {Fore.orange_4a}To{Style.reset} =========🔥====|")
print(f"|=========== {Fore.blue}Epicreate{Style.reset} ===========|\n")
print(f"🏰 {Fore.yellow}A RPG Character Creation System Application{Style.reset} 🏰")

while True:
            user_input = input(f"{Fore.light_cyan}\nPress Enter to continue...{Style.reset}")
            if user_input == "":
                    break

# ---------- Main menu ----------
def main_menu():
    # Display the main menu and get user input
    while True:
        print(f"\n----------📜 {Fore.magenta}Main Menu{Style.reset} 📜----------\n")
        print(f"▶ Enter {Fore.cyan}1{Style.reset} to {Fore.cyan}Create{Style.reset} a character ")
        print(f"▶ Enter {Fore.red}2{Style.reset} to {Fore.red}Delete{Style.reset} created character ")
        print(f"▶ Enter {Fore.aquamarine_1b}3{Style.reset} to {Fore.aquamarine_1b}View{Style.reset} created character ")
        print(f"▶ Enter {Fore.green}4{Style.reset} to {Fore.green}Exit{Style.reset} the application ")

        choice = input("\nEnter your choice: ")
        return choice



# ---------- Implementation of the main logic of the application ----------

choice = ""

# Continuously prompt the user until they choose to exit
while choice != "4":
      choice = main_menu()

      # Call the function to create a new character and automatically added in csv file
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
            print(f"\n{Fore.blue}Thank you for using Epicreate!{Style.reset}🌟")
      # Handle invalid input
      else:
            print(f"\n{Back.red}🚨 Please only enter a number between 1 - 4 🚨{Style.reset}")

# Exit message
print(f"\n{Fore.yellow}👋 Goodbye...{Style.reset}\n")