# T1A3 - Terminal Application - Epicreate

---

## Link to GitHub Repositry

https://github.com/JEniduelan/Epicreate

---

## Style Guide

I will be following the Pep8 Python Style Guide while coding my application.

### Reference for Style Guide:

Van Rossum, G., Warsaw, B., & Coghlan, N. 2001, PEP 8 - Style guide for Python code, PEPS Python, accessed 1 May 2023, https://peps.python.org/pep-0008/.

---

## Introduction

My application, called "Epicreate," is designed to allow users to create, delete, and view RPG characters. It's a text-based interface where users can interact by selecting options from a menu.

---

## Packages

The application runs on built in Python system packages and external packages. 

 - colored: This package is used for adding colored text to the console output.
 - rich: This package is used for adding emojis and formatting to the console output.
 - csv: This is a built-in Python module used for reading and writing CSV files.
 - os.path: This is a built-in Python module used for common pathname manipulation.
 - ast: This is a built-in Python module used for parsing and processing Python abstract syntax trees.

---

## Features

### Create a Character Feature:

#### User Input Prompt: 

The application prompts the user to enter details for the new character, such as name, race, and class.

#### Data Validation:

It validates the user's inputs, ensuring they are within the expected ranges or values (e.g., valid race and class options).

#### Character Creation:

 Upon receiving valid inputs, the application creates a Character object representing the new character.

#### Attribute Assignment:

 Based on the chosen class, the Character object is assigned specific attributes (e.g., strength, dexterity, intelligence).

#### Ability Assignment: 

Similarly, the character is assigned abilities corresponding to their class (e.g., special skills or spells).

#### Display Details: 

The application then displays the details of the newly created character in a visually appealing format, such as a rich table with colored text.

#### Persistence: 

Finally, the created character is stored in a CSV file for future reference, ensuring it persists across sessions.

### Delete a Character Feature:

#### Character Selection: 

Upon selecting the delete option from the main menu, the application retrieves existing characters from the CSV file.

#### User Interaction: 

It displays a list of characters and prompts the user to select one for deletion.

#### Confirmation: 

Once the user selects a character for deletion, the application confirms the action and proceeds accordingly.

#### File Update:

 After deletion, the selected character is removed from the CSV file, ensuring the file remains updated.

#### Feedback: 

The application provides feedback to the user, confirming the successful deletion of the character.

### View Characters Feature:

#### Data Retrieval: 

Upon selecting the view option from the main menu, the application reads existing characters from the CSV file.

#### Display: 

It then displays the characters' details in a visually organized format, such as a rich table with colored text and emojis.

#### User Interaction: 

The application waits for the user to review the displayed characters before proceeding.

#### Persistence: 

The characters remain stored in the CSV file for future viewing and reference.

### Exit the Application Feature:

#### User Interaction: 

  When the user selects the exit option from the main menu, the application provides a farewell message.

#### Termination: 

 It then gracefully terminates the program, ending the execution and returning control to the user.

 ### Additional Notes:

 - My application uses external packages like colored for colored text and rich for emoji and formatting.
 - Characters are stored in a CSV file named "characters.csv" for persistence.
 - Validation is implemented for race and class inputs to ensure they are within predefined options.
 - Error handling is in place for invalid inputs and missing CSV files.

 Please refer to # comments in the main.py, new_char.py, csv_function.py for futher explanation of the code with visual representation.

---

## How to play the app

---

### Main Menu

When you start the application, you are greeted with a main menu. Here are the options:

 - Create a character (Option 1): Allows you to create a new RPG character. You'll be prompted to enter the character's name, race (Human, Elf, or Dwarf), and class (Warrior, Mage, or Rogue).
 - Delete created character (Option 2): Lets you remove a character that you previously created. You'll see a list of your characters and can choose which one to delete.
 - View created characters (Option 3): Displays a list of all characters you've created along with their details, such as name, race, class, attributes, and abilities.
 - Exit the application (Option 4): Allows you to exit the application.

### Creating a Character

 To create a character:

 - Choose option 1 from the main menu.
 - Enter the character's name, race, and class.
 - The application will then display the details of the created character, including their attributes and abilities.
 - The character is automatically saved to a CSV file for future reference.

### Deleting a Character

 To delete a character:

 - Choose option 2 from the main menu.
 - You'll see a list of your characters with corresponding numbers.
 - Enter the number of the character you want to delete.
 - The selected character will be removed from the list, and the updated list will be displayed.
 - The removed character is deleted from the CSV file.

### Viewing Characters

 To view all created characters:

 - Choose option 3 from the main menu.
 - The application will display a table with details of each character, including name, race, class, attributes, and abilities.
 - You can review the information for all characters you've created.

### Exiting the Application

 To exit the application:

 - Choose option 4 from the main menu.
 - You'll see a farewell message indicating that you're exiting the application.

That's the basic overview of how to play my RPG Character Creation System Application! Enjoy creating and managing your characters! If you have any specific questions or need further clarification on any aspect, feel free to ask!

---

## Implementation Plan

## Installation




