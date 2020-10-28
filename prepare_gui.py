import os
from os import scandir, getcwd
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

def prepare_click():
        #Prevent the use of two methods in one calculus
        if (chkbox1.get() == 1 and chkbox2.get() == 1 and chkbox3.get() ==1):
                messagebox.showerror("Error", "Select only one method!")
        elif (chkbox1.get() == 1 and chkbox2.get() == 1):
                messagebox.showerror("Error", "Select only one method!")
        elif (chkbox2.get() == 1 and chkbox3.get() == 1):
                messagebox.showerror("Error", "Select only one method!")
        elif (chkbox1.get() == 1 and chkbox3.get() == 1):
                messagebox.showerror("Error", "Select only one method!")

        #Check that one of the bases are checked
        if (chkbox5.get() == 1 and chkbox6.get() == 1):
             messagebox.showerror("Error", "Select only one base!")
        elif (chkbox5.get() == 0 and chkbox6.get() == 0):
             messagebox.showerror("Error", "Select one base!")

        #Actions if MP2 is requested
        if chkbox1.get() == 1:
            n_completed = 0

            #Create a list with all arch names in path_entry route and look for .xyz extensions
            filepaths = [arch.name for arch in scandir(path_entry.get()) if arch.is_file()]
            for fp in filepaths:               
                ext = os.path.splitext(fp)[-1].lower()
                if ext == ".xyz":
                    #Count the files preparated
                    n_completed = n_completed +1

                    #Create the .com file
                    full_path = path_entry.get() + "/" + fp
                    com = full_path.replace(".xyz", ".com")
                    com_file = open(com, "w")
                    #Write down the parameters of the calculation in the .com file
                    com_file.write("%mem=" + mem_entry.get() + "mb\n")
                    com_file.write("%nproc=" + proc_entry.get() + "\n")
                    com_file.write("%chk=" + fp.replace(".xyz", ".chk") + "\n")

                    if chkbox5.get() == 1:
                        base = "6-31++G(d,p)"
                    if chkbox6.get() == 1:
                        base = "6-311++G(d,p)"

                    com_file.write("#MP2/" + base + " opt freq output=pickett\n")
                    com_file.write(os.linesep)
                    com_file.write(fp + "\n")
                    com_file.write(os.linesep)
                    com_file.write("0 1")
                    com_file.write(os.linesep)
                    #Get the info of the .xyz file and write it down in the file
                    mylines = []
                    with open (full_path, "r") as xyz:
                        for myline in xyz:
                            mylines.append(myline)
                    n = 2
                    m = len(mylines)
                    while n<m:
                        com_file.write(mylines[n])
                        n=n+1
                    #Finish the file with spaces to prevent bad termination of Gaussian
                    com_file.write(os.linesep*10)
                    com_file.close()

        #Actions if B3LYP is requested
        elif chkbox2.get() == 1:
            n_completed = 0

                #Inform that the program is using Empirical Dispersion with B3LYP to obtain better results
            messagebox.showinfo("Info", "Using Empirical Dispersion = GD3")
                #Create a list with all arch names in path_entry route and look for .xyz extensions
            filepaths = [arch.name for arch in scandir(path_entry.get()) if arch.is_file()]
            for fp in filepaths:
                ext = os.path.splitext(fp)[-1].lower()
                if ext == ".xyz":
                    #Count the files preparated
                    n_completed = n_completed +1

                    full_path = path_entry.get() + "/" + fp
                    com = full_path.replace(".xyz", ".com")
                    com_file = open(com, "w")
                    #Write down the parameters of the calculation in the .com file
                    com_file.write("%mem=" + mem_entry.get() + "mb\n")
                    com_file.write("%nproc=" + proc_entry.get() + "\n")
                    com_file.write("%chk=" + fp.replace(".xyz", ".chk") + "\n")

                    if chkbox5.get() == 1:
                        base = "6-31++G(d,p)"
                    if chkbox6.get() == 1:
                        base = "6-311++G(d,p)"
                    com_file.write("#B3LYP/" + base + " opt Freq EmpiricalDispersion=GD3 output=pickett\n")
                    com_file.write(os.linesep)
                    com_file.write(fp + "\n")
                    com_file.write(os.linesep)
                    com_file.write("0 1")
                    com_file.write(os.linesep)
                    #Get the info of the .xyz file and write it down in the file
                    mylines = []
                    with open (full_path, "r") as xyz:
                        for myline in xyz:
                            mylines.append(myline)
                    n = 2
                    m = len(mylines)
                    while n<m:
                        com_file.write(mylines[n])
                        n=n+1
                    #Finish the file with spaces to prevent bad termination of Gaussian
                    com_file.write(os.linesep*10)
                    com_file.close()

        #Actions if WFN calc is requested
        elif chkbox3.get() == 1:
            n_completed = 0

            #Inform that the program is using B3LYP to obtain results (MP2 is not necessary here)
            messagebox.showinfo("Info", "Using B3LYP to WFN calculation")
                #Create a list with all arch names in path_entry route and look for .xyz extensions
            filepaths = [arch.name for arch in scandir(path_entry.get()) if arch.is_file()]
            for fp in filepaths:
                ext = os.path.splitext(fp)[-1].lower()
                if ext == ".xyz":
                    #Count the files preparated
                    n_completed = n_completed +1

                    full_path = path_entry.get() + "/" + fp
                    com = full_path.replace(".xyz", ".com")
                    com_file = open(com, "w")
                    #Write down the parameters of the calculation in the .com file
                    com_file.write("%mem=" + mem_entry.get() + "mb\n")
                    com_file.write("%nproc=" + proc_entry.get() + "\n")
                    com_file.write("%chk=" + fp.replace(".xyz", ".chk") + "\n")

                    if chkbox5.get() == 1:
                        base = "6-31G++(d,p)"
                    if chkbox6.get() == 1:
                        base = "6-311G++(d,p)"

                    com_file.write("#B3LYP/" + base + " opt output=(pickett,wfn)")
                    com_file.write(os.linesep)
                    com_file.write(fp)
                    com_file.write(os.linesep)
                    com_file.write("0 1\n")
                    #Get the info of the .xyz file and write it down in the file
                    mylines = []
                    with open (full_path, "r") as xyz:
                        for myline in xyz:
                            mylines.append(myline)
                    n = 2
                    m = len(mylines)
                    while n<m:
                        com_file.write(mylines[n])
                        n=n+1
                    #Finish the file with spaces to prevent bad termination of Gaussian
                    com_file.write(os.linesep)
                    com_file.write(fp.replace(".xyz",".wfn") + "\n")
                    com_file.write(os.linesep*10)
                    com_file.close()

        messagebox.showinfo("Info", "Completed " + str(n_completed) + " files")

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
