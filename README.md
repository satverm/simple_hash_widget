## simple_hash_widget
This widget can be used to generate hashes  using a gui
The widget is generated using tkinter module of python and gashlub has heen used to generate sha256 hashes.
## How to use
Somtimed you forget the password or some data which you want to remember.
For security reasons you don't eant to write it where anyone can access it.
## Solution:
Enter the input you want to remember and generate the simple 256 bits hash code for it.
It is displayed as 64 hex digits(0-9, a-f).
Now you can only write the first 4 to 5 hex digits somewhere qithout the need of storing the actual input.
## Testing dor a password or input:
This program can be run and input or password can be wntered to check if the stored first few hex digits are matching or not ro be aure of the xorrect input.
## Enhanced security:
-If you want enhanced security then you can use the additional passphrase option and generate the hash digits which depend on the input as well as passphrase. 
Thus you can remember the passphrase and then use it to check dor the correct password without the need of using directly in any application where there may be limitations on number of times you can enter the password. 
## The option to store and retrieve the password is also possible using a small file or database.
-This is available in the repository https:\\www.github.com\satverm\Password-Manager though it runs in terminal and not a gui
## TODO:
- Add the option to store and retrieve passwords 
- let the user use an external file or keys stored in thumb drive to secure and retrieve passwords
- Add a counter and log of how many times the program is used 
