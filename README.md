## simple_hash_widget
This widget can be used to generate hashes  using a gui.
The widget is generated using tkinter module of python and hashlib has heen used to generate sha256 hashes.
If youbwant to use any other hash like sha512, the get hash function can be modified.
## Updates:
 - tk_hash_pers_widget.py is a version where you can add your sequence in the code itself and have a unique file to generate a unique hash. 
Since the sequence is part of the code and not seen in the widget window, it can be considered as a hard coded code which can be accessed only by having the access to the file.
Though comments have been added to create your own coded sequence, but some working knowledge of python will be useful. 

## Concept:
Sometimes you forget the password or some data which you want to remember.
For security reasons you don't want to store or write it where anyone can access it.
One of the solution is to write the first few digits of the hash of the input data.
For more security you can use a pass-phrase with the input and get the hash by using the input and the passphrase in multiple ways.
The simplest way is to just join the hashes of input and the passphrase and generate a new hash.
Then you can store or write the first few digits.
## How to get the python file from github:
 - Download the python file using curl https:\\www.github.com\satverm\simple_hash_widget in linux os.
 - Use git clone or wget, you can google to know how to downlod files from github.
 - You can fork the repository if you jave a github account  and play withe program  and send your pull request to improve the program.
 - install python in windows if not done, linux has it installed by default.
 - For use in Android phones you can install Pydroid or any other app to run python in mobiles.
 - Run the downloaded python file and it will show up the window to enter the input and passphrase 
 - You are free to modify the program and play around with it. For example, if you remove the show='*' from the input entry widgets then the inputs will be visible to you in place of ***... when you enter any data.
## Using the python program:
On running the python program a window will popup with the entry boxes and text labels.
You have to enter the input two times to be sure that you have entered correct input.
You can click on the button below the input entry boxes to generate the hash digits.
Please note there is a hash of blank entry box also, so you can generate hashes even without any input. 
In case the two inputs don't match, you have to enter the inputs again. 
Next, you can enter the passphrase in the third entry box and generate its hash using the button below it.
Finally you can click the Button for generating the hash of the hashes of input and passphrase.
You can store or write the first four to five hex digits in a secure place to test your input or password with the same passphrase to  test if it is correct or not.remember the 
The Reset Button can be used to reset all data and enter new details.
Clicking the exit button exits the program.

## Testing for a password or input:
This program can be run again and input or password and the passphrase if used earlier can be entered to check if the stored first few hex digits are matching or not.
## Enhanced security:
-If you want enhanced security then you can use the passphrase option and generate the hash digits which depend on the input as well as passphrase. 
Thus you can remember the passphrase and then use it to check for the correct password without the need of using directly in any application where there may be limitations on number of times you can enter the password. 
This will avoid resetting and generating new password by exhausting your attempts to enter the password. 
Using the pass-phrase is a good idea to store your PIN codes' as few hashes if you use many PINs in various applications. 
## The option to store and retrieve the password is also possible using a small file or database.
-This is available in the repository https:\\www.github.com\satverm\Password-Manager though it runs in terminal and not a gui
##Caution: The application is for learning and not a fully developed solution for security of critical information. 

## TODO:
- Add the option to store and retrieve passwords 
- let the user use an external file or keys stored in thumb drive to secure and retrieve passwords
- Add a counter and log of how many times the program is used 
- Make it an exe file( Don't know how to do it !!)
