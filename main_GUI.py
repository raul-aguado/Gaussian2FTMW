import os
import sys
import tkinter as tk
import time

class Application(tk.Frame):
    
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Gaussian 2 FTMW main")
        
        self.com_button = tk.Button(self, text = "Prepare .COM files from .xyz files")
        self.log_button = tk.Button(self, text = "Gaussian .log check")
        self.const_button = tk.Button(self, text = "Rotational constants")
        

        self.com_button.place(x=30, y=20)
        self.log_button.place(x=30, y=50)
        self.const_button.place(x=30, y=80)

        self.place(width=400, height=300)
        
main_window = tk.Tk()
app = Application(main_window)
app.mainloop()
