'''
A simple tkinter widget for hashing
Get sha256 hash of any input
Get sha256 hash by adding a salt(any text which acts as a pass phrase or your secret code )which further generates a hash of input string joined with haah of secret passphrase or pin 
You can store first four to five digits of the generated hash for any password or input and later use this code to test if you are using the correct password for something.
Caution: If you forget the passphrase then there is no way to get the same digits.
Storing obly first four to five digits ensures that no one can guess both either the input or the pass phrase as there will be almost unlimited possibilities for getting the same digits which you have stored.
You can even modify the code to get so many variations for hashing to have even more complexity but this code is for demonstarting the concept
get_smallest_hash function used to store the characters of your password using the same basic concept and you can get back the password or input uaing the same passphrase you used to store them.

'''
import tkinter as tk
import hashlib as hs
root = tk.Tk()
root.title("SHA256 Hash Generator")
root.geometry('1280x1900')

#a frame to kewp input data
frm1 = tk.Frame(root)
frm1.pack(padx=10, pady=100)

# reusable hash function
def get_sha256(input_str= None):
	if input_str is None:
		input_str= input("Enter any text to get sha256 hash: ")
	hash_op = hs.sha256(input_str.encode('utf-8')).hexdigest()
	return(hash_op)
		
# This funcion runs whwn btn1 is pressed to chwxk if inputa are same and generate thw haah of thw input oe caution if inpits sont match
def get_hash_btn1():
	hsh_input = e1.get()
	hsh_confirm = e2.get()
	if hsh_input == hsh_confirm:
		hsh_output = get_sha256(hsh_input)

		label_ip_hash.configure(text= hsh_output)
		lbl_match.configure(text='Inputs matching')
	else:
		
		lbl_match.configure(text="The inputs dont't match !!")
		label_ip_hash.configure(text='Try again', fg= 'red')
		#lbl_match.configure(text="Matching inputs..")
		

		

# Hash ( hash(input)+ hash(passphrase) )		
def get_salted_hash():
	ip_text_hsh = get_sha256(e1.get())
	salt_hsh=   get_sha256(e_salt.get())
	salted_ip = ip_text_hsh + salt_hsh
	hsh_salted_ip = get_sha256(salted_ip)
	lbl_salted.configure(text= hsh_salted_ip)

	
# hash(pass_hash +  ip_char + sequence + pass_hash)	
def get_char_hash():
	pass

def get_smallest_hash(pass_phrase= None, input_data= None, pack_sequence= None, external_key= None):
	
	pass
	
label1 = tk.Label(frm1, text="Lets have fun with hashing", padx=20, pady=20, fg='blue')
label1.pack()
label2=tk.Label(frm1, text="Enter the input to get hash")
label2.pack()
e1= tk.Entry(frm1,  show= '*', width= 30)
e1.pack(pady=(10,40))

label3 = tk.Label(frm1, text="Enter the input again to confirm:")
label3.pack()

e2= tk.Entry(frm1, show= '*', width =30)
e2.pack(pady=(10, 20))

lbl_match = tk.Label(frm1, text=" Testing inputs..", bg= 'grey', fg='yellow')
lbl_match.pack(padx=5,pady=10)

btn1= tk.Button(frm1, text="Click to get  hash of input ", padx=10, pady=10,command= get_hash_btn1, bg= 'red', fg= 'white')
btn1.pack()

label_ip_hash = tk.Label(frm1, text= "Input hash will be shown here", padx= 6, relief='raised', fg='blue', border=5)
label_ip_hash.pack(pady= (10,20))
label4= tk.Label(root, text="Add a passphrase or pin (salt) for more security", pady=10)
label4.pack()
e_salt= tk.Entry(root, show='*', width=30)
e_salt.pack(pady=20)
btn2 = tk.Button(root, text= 'Click to get hash of hashed input+hashed passphrase ', command= get_salted_hash, bg ='red', fg= 'white', padx=5, pady= 20)
btn2.pack()
lbl_salted= tk.Label(root, text=" Salted hash will be displayed here", relief="raised", border=7,padx=5,pady=20)
lbl_salted.pack()

btn_ext = tk.Button(root, text= 'Exit', fg= 'white',  bg= 'red', command= root.destroy)
btn_ext.pack(padx =5, pady=(30,10))


root.mainloop()
