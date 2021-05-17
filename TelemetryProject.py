#Telemtry process
#Use pyinstaller to package as exe, must be done on hime pc
from tkinter import * #imports everything form tkinter
import time  #imports time functality
#https://zetcode.com/tkinter/introduction/ 
class Window_create():
        Main_window = Tk()
        Main_window.attributes = ('-fullscreen', True)
        
class Main_menu():
    def __init__(self, parent):
        print("Intro_text start")
        intro_text = Label(parent, text = "MRGS Telemetry Monitor", fg = "Black", bg = "white", width = "20")
        intro_text.grid(column=1, row = 10)

        telemetry_button = Button (parent, text = "Telemetry processing", width = 25, height = 1, bg = "white", fg = "black")
        Raw_data_button = Button (parent, text = "Raw Data Processing", width = 25, height = 1, bg = "white", fg = "black")
       
root = Tk()
root.configure (bg  = "white")
Window_create()
#root.attributes('-fullscreen', True)
root.mainloop()

