#Telemtry process
#Use pyinstaller to package as exe, must be done on hime pc
from tkinter import * #imports everything form tkinter
import time  #imports time functality

class main_menu():
    def __init__(self, parent):
        intro_text = Label(
            parent,
            text = "MRGS Telemetry Monitor",
            fg = "Black",
            bg = "white",
            width = "20"
        )
        

        logo = PhotoImage(file="Logo.ppm")

        intro_text.grid(column=1, row = 10)
        first_window.create_image(950,300, image=img)
        print ("hello world")

root = Tk()
first_window = Tk()
first_window.geometry("1000x1000+100+100")
root.geometry("400x250+300+300")
root.configure(bg="white")
main_menu(root)
root.mainloop()

