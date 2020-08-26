import os
import sys
from tkinter import *
from tkinter import messagebox
import time

root = Tk()
root.title("Gaussian2FTMW")


chkbox1 = IntVar()
chkbox2 = IntVar()
chkbox3 = IntVar()
chkbox4 = IntVar()
chkbox5 = IntVar()
chkbox6 = IntVar()

#def prepare_click():
	#Codificar esto, que va a tener tela

def exit_click():
	raise SystemExit

top_label = Label(root, text = "Select the calculation to process:")
proc_label = Label(root, text = "Select the number of processors to use in the calculation process:")
mem_label = Label(root, text = "Select the memory to use in the calculation process:")
base_label = Label(root, text = "Select the base functions to use in the calculation process:")
path_label =  Label(root, text = "Select the path of XYZ files to prepare:")
checkbox1 = Checkbutton(root, text = "MP2", var = chkbox1)
checkbox2 = Checkbutton(root, text = "B3LYP", var = chkbox2)
checkbox3 = Checkbutton(root, text = "WFN calculation", var = chkbox3)
checkbox4 = Checkbutton(root, text = "Scan", var = chkbox4)
checkbox5 = Checkbutton(root, text = "Doble Zeta (++ G(d,p))", var = chkbox5)
checkbox6 = Checkbutton(root, text = "Triple Zeta (++ G(d,p))", var = chkbox6)
path_entry = Entry(root, width = 50)
proc_entry = Entry(root, width = 20)
mem_entry = Entry(root, width = 20)
prepare_button = Button(root, text = "Prepare .COM files", command = prepare_click)
exit_button = Button(root, text = "Exit", command = exit_click)



top_label.grid(row = 0, column = 0)
proc_label.grid(row = 1, column = 1)
mem_label.grid(row = 3, column = 1)
base_label.grid(row = 5, column = 0)
path_label.grid(row = 8, column = 0, columnspan = 2)
checkbox1.grid(row = 1, column = 0)
checkbox2.grid(row = 2, column = 0)
checkbox3.grid(row = 3, column = 0)
checkbox4.grid(row = 4, column = 0)
checkbox5.grid(row = 6, column = 0)
checkbox6.grid(row = 7, column = 0)
path_entry.grid(row = 9, column = 0, columnspan = 2)
proc_entry.grid(row = 2, column = 1)
mem_entry.grid(row = 4, column = 1)
prepare_button.grid(row = 10, column = 0)
exit_button.grid(row = 10, column = 1)

root.mainloop()
