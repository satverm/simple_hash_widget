'''
Update:
This is an updated widget where the user can retrieve teh input from the stored hashes of the input
[This is a modified simple tkinter widget for use as a personal file where you can modify the code to generate hash based on your sequence entered in the code itself.
To be precise, you can use your own value of the variable seq which is part of the create_sequence() function. This will generate a hash of the input joined with the sequence and the passphrase]

Browse the python code below and modify the code or sequence as per your imagination

A simple tkinter widget for hashing.
Get sha256 hash of any input
Get sha256 hash by adding a salt(any text which acts as a pass phrase or your secret code )which further generates a hash of input string joined with haah of secret passphrase or pin 
You can store first four to five digits of the generated hash for any password or input and later use this code to test if you are using the correct password for something.
Caution: If you forget the passphrase then there is no way to get the same digits.
Storing only first four to five digits ensures that no one can guess both either the input or the pass phrase as there will be almost unlimited possibilities for getting the same digits which you have stored.
You can even modify the code to get so many variations for hashing to have even more complexity but this code is for demonstarting the concept
get_smallest_hash function used to store the characters of your password using the same basic concept and you can get back the password or input uaing the same passphrase you used to store them.

'''
import tkinter as tk
import hashlib as hs
import random as rd
import os

root = tk.Tk()
root.title("SHA256 Personal Hash Generator")
#oot.geometry('1280x2400')

#todo: add a window to select the file to store the data and aslo to retrive if required
# we can use any text file but using a database file is more useful as we can do add, apend, edit and delete operations on the database.
# Also we can have multiple columns to add fields like id, userid, remark, user, the hashlist itself etc
# For this we need to create a main window to select options such as create database file, select database file, retrieve input or store new input and then use the different windows for each of these options. 

def get_ip_back(): #under development
	ret_win = tk.Tk()
	lbl_ret_pw = tk.Label(ret_win, text = 'Retrieve input')
	lbl_ret_pw.pack()
	e_ret_ip = tk.Entry(ret_win)
	e_ret_ip.pack()
	e_pp = tk.Entry(ret_win)
	e_pp.pack()
	
	
	ret_win.mainloop()
	
#a frame to keep input data
frm1 = tk.Frame(root, border=5)
frm1.pack(padx=5, pady=10)

# reusable hash function
def get_sha256(input_str= None):
	if input_str is None:
		input_str= input("Enter any text to get sha256 hash: ")
	hash_op = hs.sha256(input_str.encode('utf-8')).hexdigest()
	return(hash_op)
		
# This function runs when btn1 is pressed to checkk if inputs are same and generate thw hash of the input or show caution if inputs don't match
def get_input_hash():
	hsh_input = e_input.get()
	hsh_confirm = e_input_cnf.get()
	
	if hsh_input == hsh_confirm:
		hsh_output = get_sha256(hsh_input)

		label_ip_hash.configure(text= hsh_output, fg= 'blue')
		lbl_match.configure(text='Inputs matching', bg= 'green')
		
	else:
		lbl_match.configure(text="The inputs dont't match !!", bg='red')
		label_ip_hash.configure(text="Inputs don't match Enter input again", fg= 'red')
		e_input.delete(0, tk.END)
		e_input_cnf.delete(0, tk.END)

# Hash of passphrase
def get_pp_hash():
		pass_phrase = e_pass_phrase.get()
		pp_hash = get_sha256(pass_phrase)
		lbl_pp_hsh.configure(text= pp_hash)
		
# Hash ( hash(input)+ hash(passphrase) )		
def get_salted_hash():
	ip_text_hsh = get_sha256(e_input.get())
	salt_hsh=   get_sha256(e_pass_phrase.get())
	salted_ip = ip_text_hsh + salt_hsh
	hsh_salted_ip = get_sha256(salted_ip)
	lbl_salted.configure(text= hsh_salted_ip)


# Get Personal hash
# hash( hash(input)+ yoursequence + hash(passphrase))
def get_pers_hash():
		ip_text_hsh = get_sha256(e_input.get())
		salt_hsh=   get_sha256(e_pass_phrase.get())
		pers_salted_ip = ip_text_hsh + create_sequence() + salt_hsh
		hsh_pers_salted_ip = get_sha256(pers_salted_ip)
		lbl_salted.configure(text= hsh_pers_salted_ip)



# hash(pass_hash +  ip_char + sequence + pass_hash)

## define a sequence ##
#Create your own sequence which is put between the inp_hash and the pp_hash. This can be part of your modified code or it can be created as an entry box to get the sequence from the user. To get back the input using the passphrase we can store all tge characters of the input by securing it with a sequence and a passphrase. Then the same passphrase is used to get back the characters.
def create_sequence():
	
	seq= 'anything you want of any length but it should be a string'    #you can change the value of seq but it should be string
	return(seq)

# A function to return smallest hash digits for storing the input characteres and reteieving later when needed	
def inp_char_pp_hash_lst():
	inp= e_input.get()
	pp = e_pass_phrase.get()
	c_ser = 0 # we can choose this intiger as any high value to make it a unique personal code
	inp_char_lst_hsh = []
	inp_char_lst = [x for x in inp]
	for char in inp_char_lst:
		c_ser += 1
		tmp_ch_str = pp + char + str(c_ser) + get_sha256(pp)
		tmp_ch_str_hsh = get_sha256(tmp_ch_str)
		hsh_len = 1
		sml_hsh_len = 1
		for i in range(32, 144):
			test_chr_str = pp + str(chr(i)) + str(c_ser) + get_sha256(pp)
			test_chr_str_hsh = get_sha256(test_chr_str)
			if test_chr_str_hsh != tmp_ch_str_hsh:
				
				for j in range(hsh_len,64):
					if test_chr_str_hsh[1:j] == tmp_ch_str_hsh[1:j]:
						tmp_hsh_len = j
						if sml_hsh_len < tmp_hsh_len:
							sml_hsh_len = tmp_hsh_len
							
					else:
						hsh_len = sml_hsh_len
						break
						
		sml_inp_chr_hsh = tmp_ch_str_hsh[0:sml_hsh_len+1]
		inp_char_lst_hsh.append(sml_inp_chr_hsh)
		
	return(inp_char_lst_hsh)
		
# Function to getback input from earlier stored small hashes


def get_back_inp(pw_list=[], passphrase= None):
	
	inp_lst = pw_list
	pp = passphrase
	c_ser = 0 # should be same as used in the code to encode input to hash
	inp_word = ''
	for ip_ch_hsh in inp_lst:
		c_ser += 1
		tmp_inp = ''
		for i in range(32, 144):
			test_chr_str = pp + str(chr(i)) + str(c_ser) + get_sha256(pp)
			test_chr_str_hsh = get_sha256(test_chr_str)
			if test_chr_str_hsh[1:len(ip_ch_hsh)] == ip_ch_hsh[1:-1]:
				tmp_inp = str(chr(i))
				break
			else:
				print("continue checking other characters")
		if tmp_inp == '':
			return("incorrect hash input or passphrase")
		else:
			inp_word += tmp_inp
	return(inp_word)
				

		

#command for small hash button
def get_sml_hsh_lst():
	
	lbl_sml_hsh_lst.configure(text= inp_char_pp_hash_lst())
	

def get_smallest_hash(inp_chr_hsh= None):
	
	inp_chr_lst = inp_char_pp_hash_lst()
	
	pass

# Reset all the boxes
def reset_all():
	e_input.delete(0, tk.END)
	e_input_cnf.delete(0, tk.END)
	e_pass_phrase.delete(0,tk.END)
	lbl_match.configure(text= 'Testing inputs', bg='grey', fg='yellow')
	label_ip_hash.configure(text='Input hash will be displayed here')
	lbl_salted.configure(text='Personal hash will be displayed here')
	lbl_pp_hsh.configure(text= 'Passphrase hash will be displayed here')
	lbl_sml_hsh_lst.configure(text= 'Smallest hash list')

# main widget window design
label1 = tk.Label(frm1, text="Personal Hash Generator".upper(), padx=10, pady=5, fg='purple')
label1.pack()

label2=tk.Label(frm1, text="Enter the input to get hash")
label2.pack()

e_input= tk.Entry(frm1,  show= '*', width= 30)
e_input.pack(pady=5)

label3 = tk.Label(frm1, text="Enter the input again to confirm:")
label3.pack()

e_input_cnf= tk.Entry(frm1, show= '*', width =30)
e_input_cnf.pack(pady= 10)

lbl_match = tk.Label(frm1, text=" Testing inputs..", bg= 'grey', fg='yellow')
#lbl_match.pack(padx=5,pady=10)

btn_input_hsh= tk.Button(frm1, text="Click to get  hash of input", padx=5, pady=0,command= get_input_hash, relief= "raised", bg= 'grey', fg= 'white', border=2, width=20)
btn_input_hsh.pack(pady=10)

label_ip_hash = tk.Label(frm1, text= "Input hash will be displayed here", wraplength=198, padx= 5, pady=0, relief='sunken', width=32, height=2, fg='blue', border=5)
label_ip_hash.pack(pady=0)

label4= tk.Label(root, text="Add a passphrase or pin (salt) for more security", pady=0)
label4.pack()

e_pass_phrase= tk.Entry(root, show='*', width=30)
e_pass_phrase.pack(pady=10)

#add a button for passphrase hash
#and passphrase hash label

btn_hash_pp= tk.Button(root, text= 'Click to get hash of  passphrase ', command= get_pp_hash, bg ='grey', fg= 'white', relief= "raised", padx=5, pady= 0, border=3, width=30)
btn_hash_pp.pack(pady=4)

lbl_pp_hsh =tk.Label(root, text="Passphrase hash will be diaplayed here", fg="blue", relief="sunken", border=7,padx=5,pady=0, wraplength=198, height =2, width=32)
lbl_pp_hsh.pack()


btn_hash_ip_pers_pp= tk.Button(root, text= 'Click to get Personal hash', command= get_pers_hash, bg ='grey', fg= 'white', relief= "raised", padx=5, pady= 0, border=4)
btn_hash_ip_pers_pp.pack(pady=5)

lbl_salted= tk.Label(root, text="Personal hash will be diaplayed here", fg="blue", relief="sunken", border=7,padx=5,pady=0, wraplength=198, height =2, width=32)
lbl_salted.pack(pady=0)


btn_sml_hsh_lst = tk.Button(root, text= 'Get smallest hash list', fg= 'white',  bg= 'blue', relief="raised", command= get_sml_hsh_lst, border=10)
btn_sml_hsh_lst.pack(padx =5, pady=10)

lbl_sml_hsh_lst = tk.Label(root, text= "Smallest hash list", fg= 'blue', relief= 'sunken', border= 7, padx=5, pady =10,wraplength= 1000, height=3, width=50)
lbl_sml_hsh_lst.pack(pady=0)

btn_reset = tk.Button(root, text= 'Reset', fg= 'red',  bg= 'yellow', relief="raised", command= reset_all, padx= 10, border=2)
btn_reset.pack(padx =15, pady=10)


btn_exit = tk.Button(root, text= 'Exit', fg= 'white',  bg= 'red', relief="raised", padx= 10, command= root.destroy, border=2)
btn_exit.pack(padx =15, pady=(10,10))


root.mainloop()
