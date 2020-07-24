import os
import sys
import tkinter as tk
import time

class Application(tk.Frame):
    
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Gaussian 2 FTMW")
        
        self.run_button = tk.Button(self, text = "   Run   ")
        self.checkbox = tk.Checkbutton(self, text="Search for thermochemistry")
        self.checkbox2 = tk.Checkbutton(self, text="Search for frequencies")
        self.checkbox3 = tk.Checkbutton(self, text="Search for rotational constants")


        self.checkbox.place(x=10, y=30)
        self.checkbox2.place(x=10, y=50)
        self.checkbox3.place(x=10, y=70)
        self.run_button.place(x=125, y=150)

        self.place(width=400, height=300)
        
main_window = tk.Tk()
app = Application(main_window)
app.mainloop()
