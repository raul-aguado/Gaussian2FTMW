import os
from os import scandir, getcwd
import sys
from tkinter import *
from tkinter import messagebox
import time

root = Tk()
root.title("Gaussian2FTMW")

def popup():
    messagebox.showerror("Error", "Path not found")

def search_click():
    path = path_entry.get()
    n_incorrect = 0
    n_correct = 0

    try:
        filepaths = [arch.name for arch in scandir(path) if arch.is_file()]
        for fp in filepaths:
            ext = os.path.splitext(fp)[-1].lower()
        
            if ext == ".log":
                full_path = path + "/" + fp
                with open (full_path, "r") as log:
                    for myline in log:
                        mylines = []
                        chars = []

                        mylines.append(myline)

                    n = (int(len(mylines))-1)

                    for char in mylines[n]:
                        chars.append(char)

                    linea_final = ''.join([str(elem) for elem in chars[0:31] if elem!=" "])
                
                    if linea_final == "NormalterminationofGaussian":
                        n_correct = n_correct + 1

                    else:
                        n_incorrect = n_incorrect + 1 
                        incorrect_label = Label(root, text = ("Bad termination of " + fp + " file."))
                        incorrect_label.pack()
        result_label = Label(root, text = (str(n_correct) + " files are CORRECT and " + str(n_incorrect) + " files have a BAD termination"))
        result_label.pack()

    except:
        popup()


def exit_click():
    raise SystemExit

path_entry = Entry(root, width = 50)

label =  Label(root, text = "Select the path of LOG files:")
search_button = Button(root, text = "Run check", command = search_click)
exit_button = Button(root, text = "Exit", command = exit_click)

label.pack()
search_button.pack()
exit_button.pack()
path_entry.pack()

root.mainloop()
