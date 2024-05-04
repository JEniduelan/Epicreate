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


When you open the app, you'll see the main menu. It's pretty straightforward, offering four options to choose from. If you want to create a character, enter 1 to "Create a character." Just follow the prompts to give your hero a name, race (Human, Elf, or Dwarf), and class (Warrior, Mage, or Rogue). Your character will be ready to go with their stats and abilities.

If you need to say goodbye to a character you've created, go for the "Delete created character" option. It's a simple process to remove them from your roster.

For a quick look at all the characters you've created, choose "View created characters." You'll see their names, races, and classes, so you can admire your handiwork.

And when you're ready to call it a day, just select "Exit the application." No big deal, we'll wrap things up smoothly and let you get back to whatever you were doing.

That's the basic overview of how to play my RPG Character Creation System Application! Enjoy creating and managing your characters! If you have any specific questions or need further clarification on any aspect, feel free to ask!

---

## Implementation Plan



Link to Project Management Site:

 https://trello.com/b/bMkJBBMS/t1a3johnniduealn

## Help Documentation 

### Python

 - If you don't have the most recent version of Python installed, you can download it from the following link:
 https://www.python.org/downloads/

### Installing The Application

 ####  to install the application you need to do as follows:

 1. Open you terminal
![Screenshot1](https://github.com/JEniduelan/Epicreate/assets/161182890/71e483b7-e065-430c-81c5-3ce88cf0152f)

 2. Clone my reporistry

![Screenshot 2p2](https://github.com/JEniduelan/Epicreate/assets/161182890/f6e0fae6-3363-4acd-9a38-90d5bbe98a29)
![Screenshot2](https://github.com/JEniduelan/Epicreate/assets/161182890/be7aefea-5b05-43c6-98b6-adca407ffc09)

 3. Once you've cloned it, you need to navigate source directory in the repositry 

![Screenshot 3](https://github.com/JEniduelan/Epicreate/assets/161182890/28288f00-1f41-44c7-8a91-f6adb477bd57)

 4. You will need to add execute permission to the run.sh script

![screenshot4](https://github.com/JEniduelan/Epicreate/assets/161182890/2e68d2f5-2283-45cd-8488-bb264e23787b)

 4. And lastly, run the ./run.sh to start the application. Enjoy!

![Screenshot 5](https://github.com/JEniduelan/Epicreate/assets/161182890/bea946c2-f9d6-48df-84c0-48c5030ce80b)

 #### alternatively

 1. you can navigate through my Github repo
 2. click where it says <>Code.

![Screenshot 7](https://github.com/JEniduelan/Epicreate/assets/161182890/42483132-06cd-453d-aed5-a6d73e138feb)

 3. Select "Download ZIP" to download it
 4. once you have downloaded it, open the folder and locate the src folder then open this in VS Code.
 5. Using VS Code, open the terminal externally, not within the VS Code interface.

![Screenshot 8](https://github.com/JEniduelan/Epicreate/assets/161182890/7b4990bb-ca5d-4a71-99ad-e5f2ef250d2e)

 6. Then write the command bellow to execute permission to the script

![screenshot4](https://github.com/JEniduelan/Epicreate/assets/161182890/2e68d2f5-2283-45cd-8488-bb264e23787b)

 7. And simply, run the application by using this command.

![Screenshot 5](https://github.com/JEniduelan/Epicreate/assets/161182890/bea946c2-f9d6-48df-84c0-48c5030ce80b)

 8. Enjoy!


 




