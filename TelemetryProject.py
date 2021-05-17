#Telemtry process
#Use pyinstaller to package as exe, must be done on hime pc
from tkinter import * #imports everything form tkinter
import time  #imports time functality
#https://zetcode.com/tkinter/introduction/ 
   
class Main_menu():
    def __init__(self, parent):
        print("Intro_text start")

        global screen_ratio_h 
        global screen_ratio_w 
        screen_ratio_h = screen_height/1080 # determines the ratio between the screen dimensiosn that the program is designed for and the demensions of the screen 
        screen_ratio_w = screen_width/1920  # in use, so that the ui elements can be scaled appropriatly
        print(screen_ratio_h)
        print(screen_ratio_w)

        intro_text = Label(parent, text = "MRGS Telemetry Monitor", fg = "Black", bg = "white", width = "20")
        intro_text.place(y = 10 * screen_ratio_h, x = 10 * screen_ratio_w)

        telemetry_button = Button (parent, text = "Telemetry processing", width = 25, height = 1, bg = "white", fg = "black")
        Raw_data_button = Button (parent, text = "Raw Data Processing", width = 25, height = 1, bg = "white", fg = "black")

        telemetry_button.place(y= 20 * screen_ratio_h)
       

main_window = Tk()
screen_height = main_window.winfo_screenheight()
screen_width = main_window.winfo_screenwidth()
main_window.geometry(f'{screen_width}x{screen_height}')
print(screen_height)
print(screen_width)
main_window.configure(bg = "white")
Main_menu(main_window)
main_window.mainloop()


