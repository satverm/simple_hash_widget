'''
the aim of this file to create a ui with many windows and the desired workflow

Steps for ui
Open a main window with two buttons one for selecting a database file and second to create a new database file
Select database: use filedialog to open a file and then make use of the filename for all operatoins
once the file is selected then we can open the new window (main window storing and retrieving)
Store and Retrieve buttons in the new main window
store Window layout:
    Title: Store an input
    Label: Enter the input to store: Entry widget
    Label: Enter the input again to confirm: Entry widget
    Button: Click to get input hash: 
    Label: Input hash will be shown here, it will change to input hash on clicking the button above
        If the inputs don't match, a messagebox would be opened to enter the inputs again
        and the inputs would be reset

    Label: Enter the passphrase: Entry widget for passphrase
    Label: Enter the passphrase again to confirm: Entry widget for passphrase
    Button: to get the hash of passphrase
    Label: Passphrase hahs would be shown here, input again if not same
    Caution: for noting the passphrase for future use
    Button to genrate the hash list for the input
    Button to store the hash list in the database
Go the main window for storing more inputs or retrieving input from hash list

All the functions shoule be in one file and made so generic that they can be called by
the widgets as per requirement from the ui file

## Lessons learnt 
    For a gui with multiwidow workflow we should plan as under:
        - Making the modules for standard functions: This will include all standard functions and without the need for any user input. Like hash(input), read_yn() etc.
        - every window should be an independent window with it's widgets in teh window design as a group and the related functions immediately above the widgets design. This way everty window can be made modular and can be used at more than one place or can be copied and modified for similar requirements.
        - For a fully gui based application, there should not be any input from the user in the terminal like app and thinking that the terminal is not available.
        - The widget names should be as per teh task which they are doing

Title
'''
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox