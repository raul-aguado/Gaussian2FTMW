import os
from os import scandir, getcwd
import sys
from tkinter import *
from tkinter import messagebox
import time

root = Tk()

root.title("Gaussian2FTMW")

def path_error_popup():
    messagebox.showerror("Error", "Path not found")

def atoms_error_popup():
    messagebox.showerror("Error", "Error in atom number")

def search_click():
    path = path_entry.get()

    try:
        n_atoms = int(atoms_entry.get())
    except:
        atoms_error_popup()

    n_incorrect = 0
    n_correct = 0

    try:
        filepaths = [arch.name for arch in scandir(path) if arch.is_file()]
    except:
        path_error_popup()
        
    for fp in filepaths:
        ext = os.path.splitext(fp)[-1].lower()
    
        if ext == ".log":
            full_path = path + "/" + fp

            #First, the program checks that the last line in the log file is "NormalterminationofGaussian"
            with open (full_path, "r") as log:
                mylines = []
                chars = []
                for myline in log:
                    mylines.append(myline)

            n = int(((len(mylines))-1))

                
            for char in mylines[n]:
                chars.append(char)

            linea_final = ''.join([str(elem) for elem in chars[0:31] if elem!=" "])

            
            if linea_final == "NormalterminationofGaussian":
                #If the last line in the log file is "NormalterminationofGaussian", the program checks that all the frequencies calculated are positives
                print(n)
                while mylines[n] != " and normal coordinates:\n":
                    n=n-1
                else:
                    n=n+3
                    while mylines[n] != " - Thermochemistry -\n":
                        chars = []
                        for char in mylines[n]:
                            chars.append(char)
                        freq_1 = ''.join([str(elem) for elem in chars[18:33] if elem!=" "])
                        freq_2 = ''.join([str(elem) for elem in chars[34:60] if elem!=" "])
                        freq_3 = ''.join([str(elem) for elem in chars[60:74] if elem!=" "])
            
                        if (float(freq_1) < 0 or float(freq_2) < 0 or float(freq_3) < 0):
                            print("Error with the frequencies in " + full_path)
                            break
                            
                    
                        else:
                            n = (n + n_atoms + 7)
                            
                    print("Frequencies for " + fp + " are CORRECT")
                    n_correct = n_correct + 1

            else:
                n_incorrect = n_incorrect + 1 
                incorrect_label = Label(root, text = ("Bad termination of " + fp + " file."))
                incorrect_label.grid(row = 5, column = 0, columnspan = 2)

    result_label = Label(root, text = (str(n_correct) + " files are CORRECT and " + str(n_incorrect) + " files have a BAD termination"))
    result_label.grid(row = 6, column = 0, columnspan = 2)



def exit_click():
    raise SystemExit

path_entry = Entry(root, width = 50)
atoms_entry = Entry(root, width = 50)

path_label =  Label(root, text = "Select the path of LOG files:")
atoms_label = Label(root, text = "Number of atoms in the molecule...")

search_button = Button(root, text = "Run check", command = search_click)
exit_button = Button(root, text = "Exit", command = exit_click)

path_label.grid(row = 0, column = 0, columnspan = 2)
atoms_label.grid(row = 2, column = 0, columnspan = 2)
search_button.grid(row = 4, column = 0)
exit_button.grid(row = 4, column = 1)
path_entry.grid(row = 1, column = 0, columnspan = 2)
atoms_entry.grid(row = 3, column = 0, columnspan = 2)

root.mainloop()
