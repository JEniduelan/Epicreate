print("Welcome to Epicreate")

# Menu function
def menu():
    while True:
        print("\nMain Menu:")
        print("> Enter 1 to create a character ")
        print("> Enter 2 to delete customised character ")
        print("> Enter 3 to view customised character ")
        print("> Enter 4 to exit ")

        choice = input("Enter your choice: ")
        return choice
    
choice = ""

while choice != "4":
      choice = menu()

      if choice == "1":
            print(1)
      elif choice == "2":
            print(2)
      elif choice == "3":
            print(3)
      elif choice == "4":
            print("\nThank you for using Epicreate")
      else:
            print("Invalid choice. Please enter a number between 1 and 4.")

print("Exiting...\n")