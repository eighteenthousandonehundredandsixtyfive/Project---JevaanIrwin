#Telemtry process
#Use pyinstaller to package as exe, must be done on hime pc
from tkinter import * #imports everything form tkinter
import time  #imports time functality
import math
import json
from types import LambdaType
#https://zetcode.com/tkinter/introduction/ 

class Flight_sim():
    def __init__ (self):
        print("simulating flight") #for troublehsooting and to be removed in the final program. 
        Sim_window = Tk()
        Sim_window.title('Flight Simulation')
        Sim_window.geometry(f'{screen_width}x{screen_height}')

        Thrust_text = Entry(Sim_window, width = 5, bg = 'white', fg = 'black')
        Thrust_label= Label(Sim_window, text = 'Avg. Thrust', width = 10, height = 1, bg = 'white', fg = "black")
        Thrust_text.place(x = 100 * rw, y = 40 * rh)
        Thrust_label.place(x = 20 * rw, y = 42 * rh)

        Weight_text = Entry(Sim_window, width = 5, bg = 'white', fg = "black")
        Weight_label = Label(Sim_window, text = 'Total Weight', width = 10, bg = 'white', fg = 'black')
        Weight_text.place(x = 100 * rw, y = 60 * rh)
        Weight_label.place(x = 20 * rw, y = 62 * rh)
        global w
        w = Weight_text.get()

        Time_text = Entry(Sim_window, width = 5, bg = 'white', fg = "black")
        Time_label = Label(Sim_window, text = 'Burn Time', width = 10, bg = 'white', fg = 'black')
        Time_text.place(x = 100 * rw, y = 80 * rh)
        Time_label.place(x = 20 * rw, y = 82 * rh)

        Simulate_button = Button(Sim_window, text = "simulate", width = 30, height= 1, bg = "white", fg = 'black', command = lambda:[Simulate()])
        Simulate_button.place(x = 100 * rw, y = 100 * rh)

class Simulate():
    def __init__(self):
        m = w / 9.81
        print (w)


class Raw_data(): #this class contains the code for the raw_data window
    def __init__(self):
        print("Raw data processing") #for troublehsooting
        Raw_data_window = Tk()
        Raw_data_window.title("Raw Data Processing") #for troublehsooting
        Raw_data_window.geometry(f'{screen_width}x{screen_height}')

class Tele_data(): # this class manages the code for the telemetry window
    def __init__(self):
        print("telemetry processing") #for troublehsooting
        Tele_data_window = Tk()
        Tele_data_window.title("Telemetry Data Processing") 
        Tele_data_window.geometry(f'{screen_width}x{screen_height}')

class About(): #This class contains the code for the about window.
    def __init__ (self):
        About_window = Tk()
        About_window.title('About')
        About_window.geometry(f'{int(screen_width/2)}x{int(screen_height/2)}')

        About_label = Label(About_window, text = "This is a python program created by Jevaan Irwin \n It is for interfacing a arduino microcontroller with a computer \n and transfering telemetry data cotained within", bg = 'white', fg = 'black')
        About_label.place (x = 5 * rw, y = 10 * rh)

class Main_menu(): #this class contains the appropriate code for the main screen at the start of the porgram
    def __init__(self, parent):
        print("Intro_text start") #for troublehsootingb

        print(rh) #for troublehsooting
        print(rw) #for troublehsooting

        intro_text = Label(parent, text = "MRGS Telemetry Monitor", fg = "red", bg = "white", width = 25)
        discription_text = Label(parent, text = "Made by Jevaan Irwin", fg = "red", bg= "white", width = 25)
        place_holder_text = Label(parent, text = "MRGS logo/rocket", fg = "white", bg = "red")

        intro_text.place(x = 200 * rw, y = 15 * rh)
        discription_text.place(x = 200 * rw, y= 30 * rh)
        place_holder_text.place(x = 50 * rw, y = 50 * rh)


        telemetry_button = Button (parent, text = "Telemetry processing", width = 25, height = 1, bg = "white", fg = "black", command = lambda:[print("telemetry button pressed"), Tele_data(), main_window.destroy()])  #print statements within are for troubleshooting and will require removal
        raw_data_button = Button (parent, text = "Raw Data Processing", width = 25, height = 1, bg = "white", fg = "black", command = lambda:[print("raw_data_pressed"), Raw_data(), main_window.destroy()])
        about_button = Button (parent, text = 'about', width = 25, height = 1, bg = 'white', fg = 'black', command = lambda:[print('About'), About()])
        sim_button = Button (parent, text = "Flight Simulation", width = 25, height = 1, bg = "white", fg = "black", command = lambda:[print('Flight sim'), Flight_sim(), main_window.destroy()])

        telemetry_button.place(x = 200 * rw, y= 70 * rh)
        raw_data_button.place(x = 200 * rw, y = 50 * rh)
        sim_button.place(x = 200 * rw, y = 90 * rh)
        about_button.place(x = 200 * rw, y = 110 * rh)

main_window = Tk()
main_window.title('Start Menu')
global cur_window
cur_window = 'main_window'
screen_height = (main_window.winfo_screenheight())
screen_width = (main_window.winfo_screenwidth())
global rh #rh being the ratio of the computer resoulotion to 1080p, and rw is the widths ratio
global rw 
rh = 1080/screen_height # determines the ratio between the screen dimensiosn that the program is designed for and the demensions of the screen 
rw = 1920/screen_width  # in use, so that the ui elements can be scaled appropriatly
main_window.geometry(f'{int(screen_width/3 * rw)}x{int(screen_height/5 * rh)}')
print(screen_height)
print(screen_width)
main_window.configure(bg = "white")
Main_menu(main_window)
main_window.mainloop()


