#Telemtry process
#Use pyinstaller to package as exe, must be done on hime pc
from tkinter import * #imports everything form tkinter
import time  #imports time functality
#https://zetcode.com/tkinter/introduction/ 
   
class Main_menu():
    def __init__(self, parent):
        print("Intro_text start")

        global rh #rh being the ratio of the computer resoulotion to 1080p, and rw is the widths ratio
        global rw 
        rh = 1080/screen_height # determines the ratio between the screen dimensiosn that the program is designed for and the demensions of the screen 
        rw = 1920/screen_width  # in use, so that the ui elements can be scaled appropriatly
        print(rh)
        print(rw)

        intro_text = Label(parent, text = "MRGS Telemetry Monitor", fg = "Black", bg = "white", width = "20")
        intro_text.place(y = 10 * rh, x = 25 * rw)

        telemetry_button = Button (parent, text = "Telemetry processing", width = 25, height = 1, bg = "white", fg = "black")
        raw_data_button = Button (parent, text = "Raw Data Processing", width = 25, height = 1, bg = "white", fg = "black")

        telemetry_button.place(x = 10 * rw, y= 30 * rh)
        raw_data_button.place(x = 200 * rw, y = 30 * rh)
       

main_window = Tk()
screen_height = main_window.winfo_screenheight()
screen_width = main_window.winfo_screenwidth()
main_window.geometry(f'{screen_width}x{screen_height}')
print(screen_height)
print(screen_width)
main_window.configure(bg = "white")
Main_menu(main_window)
main_window.mainloop()


