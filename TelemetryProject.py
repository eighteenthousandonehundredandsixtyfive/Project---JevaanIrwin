#Telemtry process
#Use pyinstaller to package as exe, must be done on hime pc
from tkinter import * #imports everything form tkinter
import time  #imports time functality
import math
#https://zetcode.com/tkinter/introduction/ 

action = 'main' 
print(action)

class Raw_data():
    def __init__(self):
        print("Raw data processing")
        Raw_data_window = Tk()
        Raw_data_window.title("Raw Data Processing")
        Raw_data_window.geometry(f'{screen_width}x{screen_height}')

class Tele_data():
    def __init__(self):
        print("telemetry processing")
        Tele_data_window = Tk()
        Tele_data_window.title("Telemetry Data Processing")
        Tele_data_window.geometry(f'{screen_width}x{screen_height}')

class About():
    def __init__ (self):
        About_window = Tk()
        About_window.title('About')
        About_window.geometry(f'{int(screen_width/2)}x{int(screen_height/2)}')

        About_label = Label(About_window, text = "This is a python program created by Jevaan Irwin \n It is for interfacing a arduino microcontroller with a computer \n and transfering telemetry data cotained within", bg = 'white', fg = 'black')
        About_label.place (x = 5 * rw, y = 10 * rh)
class Main_menu():
    def __init__(self, parent):
        print("Intro_text start")

        global rh #rh being the ratio of the computer resoulotion to 1080p, and rw is the widths ratio
        global rw 
        rh = 1080/screen_height # determines the ratio between the screen dimensiosn that the program is designed for and the demensions of the screen 
        rw = 1920/screen_width  # in use, so that the ui elements can be scaled appropriatly
        print(rh)
        print(rw)

        intro_text = Label(parent, text = "MRGS Telemetry Monitor", fg = "red", bg = "white", width = "20")
        discription_text = Label(parent, text = "Made by Jevaan Irwin", fg = "red", bg= "white")
        intro_text.place(x = 25 * rw, y = 10 * rh)
        discription_text.place(x = 228 * rw, y= 10 * rh)


        telemetry_button = Button (parent, text = "Telemetry processing", width = 25, height = 1, bg = "white", fg = "black", command = lambda:[print("telemetry button pressed"), Tele_data(), main_window.destroy()])
        raw_data_button = Button (parent, text = "Raw Data Processing", width = 25, height = 1, bg = "white", fg = "black", command = lambda:[print("raw_data_pressed"), Raw_data(), main_window.destroy()])
        about_button = Button (parent, text = 'about', width = 5, height = 1, bg = 'white', fg = 'black', command = lambda:[print('About'), About()])

        telemetry_button.place(x = 10 * rw, y= 30 * rh)
        raw_data_button.place(x = 200 * rw, y = 30 * rh)
        about_button.place(x = 370 * rw, y = 30 * rh)

main_window = Tk()
main_window.title('Start Menu')
screen_height = (main_window.winfo_screenheight())
screen_width = (main_window.winfo_screenwidth())
main_window.geometry(f'{int(screen_width/2)}x{int(screen_height/8)}')
print(screen_height)
print(screen_width)
main_window.configure(bg = "white")
Main_menu(main_window)
main_window.mainloop()


