#Telemtry process
#Use pyinstaller to package as exe, must be done on hime pc
#%%
from tkinter import * #imports everything form tkinter
import time  #imports time functality

class main_menu():
    def __init__(self, parent):
        intro_text = Label(
            parent,
            text = "MRGS Telemetry Monitor",
            fg = "Black",
            bg = "white"
        )

        intro_text.place(#...)

        print ("hello world")

root = Tk()
root.geometry("400x250+300+300")
main_menu(root)
root.mainloop()
# %%
