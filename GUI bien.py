from tkinter import * 
from PIL import ImageTk, Image
import subprocess

root = Tk()
root.title("Gaussian2FTMW")

def click1():
	subprocess.run(['python.exe', 'prepare_gui.py'])

def click2():
	subprocess.run(['python.exe', 'check_gui.py'])

def click3():
	subprocess.run(['python.exe', 'search_gui.py'])


img = ImageTk.PhotoImage(Image.open("image.jpg"))
img_label = Label(image = img)


#label1 =  Label(root, text = "Welcome to Gaussian2FTMW")
label2 =  Label(root, text = "Select a task:")
space_label = Label(root, text = " ")
button1 = Button(root, text = "Prepare .COM from .xyz files", command = click1)
button2 = Button(root, text = "Gaussian .log files check", command = click2)
button3 = Button(root, text = "Extract information from Gaussian .log files", command = click3)

#label1.pack()
img_label.grid(row = 0, column = 0, rowspan = 4)
label2.grid(row =0, column =1)
button1.grid(row = 1, column = 1)
button2.grid(row = 2, column = 1)
button3.grid(row = 3, column = 1)



root.mainloop()
