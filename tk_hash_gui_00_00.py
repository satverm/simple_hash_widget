'''
This code is for a fully gui based inputs and outputs
'''
import tkinter as tk
import hashlib as hs
import random as rd
from tkinter import filedialog
from tkinter import messagebox
import os

## Standard Fuctions  ##

# get teh sha256 hash of any input string
def get_sha256(input_str):
    hash_op = hs.sha256(input_str.encode('utf-8')).hexdigest()
    return(hash_op)

# This function is used to create a personal sequence in the code itself to make the hash unique for the user
def create_pers_sequence():
    # you can change the value of seq but it should be string
    seq = 'anything you want of any length but it should be a string'
    return(seq)

# A function to return smallest hash digits for storing the input characteres and reteieving later when needed
# This function will be converted to a standard function without the need to  get input from a widget
def inp_char_pp_hash_lst(inp, pp, c_ser):
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
                for j in range(hsh_len, 64):
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

# Fuction to get back the input string back from the input hash list
def get_back_inp(c_ser, inp_list, pp):
    inp_list = []
    c_ser = 0  # should be same as used in the code to encode input to hash
    inp_word = ''
    for ip_ch_hsh in inp_list:
        c_ser += 1
        tmp_inp = ''
        for i in range(32, 144):
            test_chr_str = pp + str(chr(i)) + str(c_ser) + get_sha256(pp)
            test_chr_str_hsh = get_sha256(test_chr_str)
            if test_chr_str_hsh[1:len(ip_ch_hsh)] == ip_ch_hsh[1:-1]:
                tmp_inp = str(chr(i))
                break
            else:
                continue
        if tmp_inp == '':
            return("incorrect hash input or passphrase")
        else:
            inp_word += tmp_inp
    return(inp_word)



def open_hash_win():
    ## get the input hash window
    
    get_hash_win = tk.Toplevel(root)
    get_hash_win.title("SHA256 Personal Hash Generator")

    # This function runs when btn1 is pressed to checkk if inputs are same and generate thw hash of the input or show caution if inputs don't match
    def get_input_hash():
        hsh_input = e_input.get()
        hsh_confirm = e_input_cnf.get()
        if hsh_input == hsh_confirm:
            hsh_output = get_sha256(hsh_input)
            label_ip_hash.configure(text=hsh_output, fg='blue')
            lbl_match.configure(text='Inputs matching', bg='green')
        else:
            lbl_match.configure(text="The inputs dont't match !!", bg='red')
            label_ip_hash.configure(
                text="Inputs don't match Enter input again", fg='red')
            e_input.delete(0, tk.END)
            e_input_cnf.delete(0, tk.END)

    # Hash of passphrase
    def get_pp_hash():
        pass_phrase = e_pass_phrase.get()
        pp_hash = get_sha256(pass_phrase)
        lbl_pp_hsh.configure(text=pp_hash)

    # Hash ( hash(input)+ hash(passphrase) )
    def get_salted_hash():
        ip_text_hsh = get_sha256(e_input.get())
        salt_hsh = get_sha256(e_pass_phrase.get())
        salted_ip = ip_text_hsh + salt_hsh
        hsh_salted_ip = get_sha256(salted_ip)
        lbl_salted.configure(text=hsh_salted_ip)

    # Get Personal hash
    # hash( hash(input)+ yoursequence + hash(passphrase))
    def get_pers_hash():
        ip_text_hsh = get_sha256(e_input.get())
        salt_hsh = get_sha256(e_pass_phrase.get())
        pers_salted_ip = ip_text_hsh + create_pers_sequence() + salt_hsh
        hsh_pers_salted_ip = get_sha256(pers_salted_ip)
        lbl_salted.configure(text=hsh_pers_salted_ip)


    # command for small hash button
    def get_sml_hsh_lst():
        pp = e_pass_phrase.get()
        inp = e_input.get()
        c_ser = 0
        inp_char_pp_hash_lst_str = inp_char_pp_hash_lst(inp,pp,c_ser)
        # code required for all arguments to be passed to following function
        lbl_sml_hsh_lst.configure(text= inp_char_pp_hash_lst_str)

    # Reset all the boxes
    def reset_all():
        e_input.delete(0, tk.END)
        e_input_cnf.delete(0, tk.END)
        e_pass_phrase.delete(0, tk.END)
        lbl_match.configure(text='Testing inputs', bg='grey', fg='yellow')
        label_ip_hash.configure(text='Input hash will be displayed here')
        lbl_salted.configure(text='Personal hash will be displayed here')
        lbl_pp_hsh.configure(text='Passphrase hash will be displayed here')
        lbl_sml_hsh_lst.configure(text='Smallest hash list')


    title_label = tk.Label(get_hash_win, text="Personal Hash Generator".upper(),
                    padx=10, pady=5, fg='purple')
    title_label.pack()
    inp_label = tk.Label(get_hash_win, text="Enter the input to get hash")
    inp_label.pack()
    e_input = tk.Entry(get_hash_win,  show='*', width=30)
    e_input.pack(pady=5)
    inp_conf_label = tk.Label(get_hash_win, text="Enter the input again to confirm:")
    inp_conf_label.pack()
    e_input_cnf = tk.Entry(get_hash_win, show='*', width=30)
    e_input_cnf.pack(pady=10)
    lbl_match = tk.Label(get_hash_win, text=" Testing inputs..", bg='grey', fg='yellow')
    # lbl_match.pack(padx=5,pady=10)
    btn_input_hsh = tk.Button(get_hash_win, text="Click to get  hash of input", padx=5, pady=0,
                            command=get_input_hash, relief="raised", bg='grey', fg='white', border=2, width=20)
    btn_input_hsh.pack(pady=10)
    label_ip_hash = tk.Label(get_hash_win, text="Input hash will be displayed here", wraplength=198,
                            padx=5, pady=0, relief='sunken', width=32, height=2, fg='blue', border=5)
    label_ip_hash.pack(pady=0)
    pass_phr_label = tk.Label(
        get_hash_win, text="Add a passphrase or pin (salt) for more security", pady=0)
    pass_phr_label.pack()
    e_pass_phrase = tk.Entry(get_hash_win, show='*', width=30)
    e_pass_phrase.pack(pady=10)
    btn_hash_pp = tk.Button(get_hash_win, text='Click to get hash of  passphrase ', command=get_pp_hash,
                            bg='grey', fg='white', relief="raised", padx=5, pady=0, border=3, width=30)
    btn_hash_pp.pack(pady=4)
    lbl_pp_hsh = tk.Label(get_hash_win, text="Passphrase hash will be diaplayed here", fg="blue",
                        relief="sunken", border=7, padx=5, pady=0, wraplength=198, height=2, width=32)
    lbl_pp_hsh.pack()
    btn_hash_ip_pers_pp = tk.Button(get_hash_win, text='Click to get Personal hash', command=get_pers_hash,
                                    bg='grey', fg='white', relief="raised", padx=5, pady=0, border=4)
    btn_hash_ip_pers_pp.pack(pady=5)
    lbl_salted = tk.Label(get_hash_win, text="Personal hash will be diaplayed here", fg="blue",
                        relief="sunken", border=7, padx=5, pady=0, wraplength=198, height=2, width=32)
    lbl_salted.pack(pady=0)
    btn_sml_hsh_lst = tk.Button(get_hash_win, text='Get smallest hash list', fg='white',
                                bg='blue', relief="raised", command=get_sml_hsh_lst, border=10)
    btn_sml_hsh_lst.pack(padx=5, pady=10)
    lbl_sml_hsh_lst = tk.Label(get_hash_win, text="Smallest hash list", fg='blue', relief='sunken',
                            border=7, padx=5, pady=10, wraplength=1000, height=3, width=50)
    lbl_sml_hsh_lst.pack(pady=0)
    btn_reset = tk.Button(get_hash_win, text='Reset', fg='red',  bg='yellow',
                        relief="raised", command=reset_all, padx=10, border=2)
    btn_reset.pack(padx=15, pady=10)
    btn_exit = tk.Button(get_hash_win, text='Exit', fg='white',  bg='red',
                        relief="raised", padx=10, command=get_hash_win.destroy, border=2)
    btn_exit.pack(padx=15, pady=(10, 10))

#


## main window widget(UI) design ##
root = tk.Tk()
root.title("Hash Generator")
root.geometry('800x600')
hash_input_btn = tk.Button(root, text= "Get Input Hash List", command= open_hash_win)
hash_input_btn.pack(padx= 10, pady= 20)

root.mainloop()
