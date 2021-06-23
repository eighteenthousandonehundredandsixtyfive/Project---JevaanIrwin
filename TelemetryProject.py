#Telemtry process
#Use pyinstaller to package as exe, must be done on hime pc
from tkinter import * #imports everything form tkinter
import time  #imports time functality
import math
import json
import datetime
from types import LambdaType
#https://zetcode.com/tkinter/introduction/ temp

class Flight_sim():
    def __init__ (self):

        print("simulating flight") #for troublehsooting and to be removed in the final program. 
        Sim_window = Tk()
        Sim_window.title('Flight Simulation')
        Sim_window.geometry(f'{screen_width}x{screen_height}')
        Sim_window.configure(bg = "white")

        def Simulation(): 
            thrust = Thrust_text.get()
            weight = Weight_text.get()
            r_time = Time_text.get()

            warned = False
            File_warn = Label(Sim_window, text = "Cannot be empty, or word", bg = 'white', fg = 'red')
            File_warn_2 = Label(Sim_window, text = "Cannot be empty", bg = 'white', fg = 'red')

            if len(thrust) == 0 or thrust.isdigit() == False or  len(weight) == 0 or  weight.isdigit() == False or len(r_time) == 0 or  r_time.isdigit() == False: #checks to make sure each field contains values else the program wont work
                warned = True
                if len(thrust) == 0 or thrust.isdigit() == False: # it then indiviually checks each entry feild to see where a warning needs to be placed
                    File_warn.place(x = 210 * rw, y = 40 * rh)
                elif len(weight) == 0 or  weight.isdigit() == False:
                    File_warn.place(x = 210 * rw, y = 60 * rh)
                elif len(r_time) == 0 or  r_time.isdigit() == False:
                    File_warn.place(x = 210 * rw, y = 80 * rh)
            else:
                if warned == True: #not working as intended though not vital to functionality
                    File_warn.delete()
                    warned = False

                print ("simulating")
                i = float(thrust)  # this is impulse # all the entry boxes must be filled in or else error will be returned. Need to add featrues sucha seasier navigation with tab, pressing enter etc. 
                w = float(weight)
                t = float(r_time)
    
                T = i / t #T = thrust
                m = w / 9.81
                a = (T - w) / m
                d_b = (0.5) * (a) * (t ** 2) # distance during the burn time . 
                v = a * t # v being the time after burn
                E = (0.5) * (m) * (v ** 2)
                d_c = E / (m * 9.81) # d_c being the distance coasted to apoapsis
                print (d_b, d_c, d_b + d_c) 
                d_m = d_c + d_b # maximum height theoretically.

                File_name = Data_name.get()

                if len(File_name) == 0: # checks to make sure there is an entry for the data. 
                    File_warn_2.place(x = 210 * rw, y = 118 * rh)
                else:
                    if len(File_name) == 0:
                        File_warn_2.delete()
                    
                    Burn_distance = "d_b"
                    Coast_distance = 'd_c'
                    Max_distance = 'd_m'  
                    
                    Flight_data = {
                        Burn_distance :  d_b, Coast_distance: d_c, Max_distance: d_m
                    }

                    with open("flight_data.json", "w") as write_file:
                        json.dump(Flight_data, write_file)


        Thrust_text = Entry(Sim_window, width = 5, bg = 'white', fg = 'black')
        Thrust_label= Label(Sim_window, text = 'Avg. Thrust', width = 10, height = 1, bg = 'white', fg = "black")
        Thrust_text.place(x = 150 * rw, y = 40 * rh)
        Thrust_label.place(x = 70 * rw, y = 42 * rh)

        Weight_text = Entry(Sim_window, width = 5, bg = 'white', fg = "black")
        Weight_label = Label(Sim_window, text = 'Total Weight', width = 10, bg = 'white', fg = 'black')
        Weight_text.place(x = 150 * rw, y = 60 * rh)
        Weight_label.place(x = 70 * rw, y = 62 * rh)

        Time_text = Entry(Sim_window, width = 5, bg = 'white', fg = "black")
        Time_label = Label(Sim_window, text = 'Burn Time', width = 10, bg = 'white', fg = 'black')
        Time_text.place(x = 150 * rw, y = 80 * rh)
        Time_label.place(x = 70 * rw, y = 82 * rh)

        Simulate_button = Button(Sim_window, text = "simulate", width = 30, height= 1, bg = "white", fg = 'black', command = lambda:[Simulation()])
        Simulate_button.place(x = 60 * rw, y = 140 * rh)

        Data_name = Entry(Sim_window, width = 30, bg = "white", fg = 'black')
        Data_name_label = Label(Sim_window, text = "Data Name", fg = "black", bg = "white", width = 29)
        Data_name.place(x = 58 * rw, y = 118 * rh)
        Data_name_label.place(x = 60 * rw, y = 100 * rh)

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


