#Telemtry process
#Use pyinstaller to package as exe, must be done on hime pc
from tkinter import * #imports everything form tkinter
import time  #imports time functality
import math
#https://zetcode.com/tkinter/introduction/ 
   
global  int button_check
 
class Main_menu():
    def __init__(self, parent):
        print("Intro_text start")

        global rh #rh being the ratio of the computer resoulotion to 1080p, and rw is the widths ratio
        global rw 
        global  int button_check 
        rh = 1080/screen_height # determines the ratio between the screen dimensiosn that the program is designed for and the demensions of the screen 
        rw = 1920/screen_width  # in use, so that the ui elements can be scaled appropriatly
        print(rh)
        print(rw)

        intro_text = Label(parent, text = "MRGS Telemetry Monitor", fg = "red", bg = "white", width = "20")
        intro_text.place(y = 10 * rh, x = 25 * rw)

        telemetry_button = Button (parent, text = "Telemetry processing", width = 25, height = 1, bg = "white", fg = "black", command = lambda:[print("telemetry button pressed", button_check = 2)])
        raw_data_button = Button (parent, text = "Raw Data Processing", width = 25, height = 1, bg = "white", fg = "black", command = lambda:[print("raw data pressed", button_check = 1)])

        telemetry_button.place(x = 10 * rw, y= 30 * rh)
        raw_data_button.place(x = 200 * rw, y = 30 * rh)

main_window = Tk()
screen_height = (main_window.winfo_screenheight())
screen_width = (main_window.winfo_screenwidth())
main_window.geometry(f'{int(screen_width/2)}x{int(screen_height/8)}')
print(screen_height)
print(screen_width)
main_window.configure(bg = "white")
Main_menu(main_window)
if button_check == 1:   
    new_window = Tk()

main_window.mainloop()


