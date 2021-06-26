#Telemtry process
#Use pyinstaller to package as exe, must be done on hime pc
from tkinter import * #imports everything form tkinter
import time  #imports time functality
import math
import json
import datetime

class Flight_sim():
    def __init__ (self):

        print("simulating flight") #for troublehsooting and to be removed in the final program. 
        Sim_window = Tk()
        Sim_window.title('Flight Simulation')
        Sim_window.geometry(f'{int(screen_width/1.25)}x{int(screen_height/2)}')
        Sim_window.configure(bg = "white")

        def Simulation(): 
            thrust = Thrust_text.get()
            weight = Weight_text.get()
            r_time = Time_text.get()

            warned = False
            File_warn = Label(Sim_window, text = "Cannot be empty, or a word", bg = 'white', fg = 'red')

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
                global i
                global w
                global t

                global d_b
                global d_c
                global d_m

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
                d_m = d_c + d_b #maximum height theoretically.

                Terminal.config(state = NORMAL)
                Terminal.insert(INSERT, '\n***Simiulated Data*** \n Burn Distance: ' + str(d_b) + '\n Coast Distance: ' + str(d_c) + '\n Maximum Distance: ' + str(d_m))
                Terminal.config(state = DISABLED)
                 
        def Save(): #Button that saves the simulated Data to a JSON file. 
            File_warn_2 = Label(Sim_window, text = "Cannot be empty", bg = 'white', fg = 'red')
            File_name = Data_name.get()

            if len(File_name) == 0: # checks to make sure there is an entry for the data. 
                File_warn_2.place(x = 210 * rw, y = 118 * rh)
            else:
            
                read_file = open("flight_data.json", "r")
                data = json.load(read_file)

                Index_no_new = data["Flight_data"]["Index"]["Index_no"]
                Index_no_new += 1

                Index_new = {
                    "Index" : {'Index_no' : Index_no_new}
                }
                
                Temp_no = 1

                while Temp_no < Index_no_new:
                    Index_new["Index"].update({str(Temp_no): data['Flight_data']['Index'][str(Temp_no)]})
                    Temp_no += 1

                if Temp_no == Index_no_new:
                    Index_new["Index"].update({Index_no_new: File_name})
                    
                del data['Flight_data']['Index']

                data['Flight_data'].update({str(File_name): {"Burn_distance" : d_b, 'Coast_distance' : d_c, 'Max_distance': d_m, 'i': i, 'w': w, 't': t }})
                data['Flight_data'].update(Index_new)

                with open('flight_data.json', "w") as write_file:
                    json.dump(data, write_file, indent = 2)
        
        def List_data(): #lists the data and adds to list box, in fucntion so that the listbox can be refreshed. 
            read_file = open("flight_data.json", "r")
            data = json.load(read_file)

            Index_no = data['Flight_data']['Index']['Index_no']
            Temp_no = 1

            while Temp_no < Index_no or Temp_no == Index_no:
                Frame_data.insert(int(Temp_no), str(data['Flight_data']['Index'][str(Temp_no)]))
                Temp_no += 1

        def Data_delete(): #for deleting data from 
            Name = Frame_data.get(ANCHOR)

            read_file = open("flight_data.json", "r")
            data = json.load(read_file)
            Index_new = data['Flight_data']['Index']

            print(data)
            print('\n' , Index_new)
            Temp_no = 1
            Index_no = data['Flight_data']['Index']['Index_no']
            del data['Flight_data']['Index']

            while Temp_no < Index_no or Temp_no == Index_no:
                print(Temp_no)
                Name_temp = data['Flight_data']['Index'][str(Temp_no)]

                if Name_temp == Name:
                    #del Index_new[Temp_no]
                    #del data['Flight_data'][Name]

                    val = 1
                    Data_list = []
                    while Temp_no < Index_no or Temp_no == Index_no:
                        Data_list[val] = Index_new[Temp_no]

                        

                Temp_no += 1







        #Below all(most) the GUI elements are created and added to the window          
        var = IntVar() #not entirely sure what this does, though i belevie it could simple be substituted for a interger pr string within the radio button declaration itself
        Radio_but_1 = Radiobutton(Sim_window, variable = var, value = 1,  text = 'Input Data', command = lambda:[print('Inputting data')])
        Radio_but_2 = Radiobutton(Sim_window, variable = var, value = 2, text = 'Load data', command = lambda:[print('loading data')])

        Radio_but_1.place(x = 150 * rw, y = 10 * rh)
        Radio_but_2.place(x = 250 * rw, y = 10 * rh)

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
        Simulate_button.place(x = 60 * rw, y = 100 * rh)

        Data_name = Entry(Sim_window, width = 30, bg = "white", fg = 'black')
        Data_name_label = Label(Sim_window, text = "Data Name", fg = "black", bg = "white", width = 29)
        Data_name.place(x = 58 * rw, y = 148 * rh)
        Data_name_label.place(x = 60 * rw, y = 130 * rh)

        Save_button = Button(Sim_window, text = 'Save', width = 30, height= 1, bg = "white", fg = 'black', command = lambda:[Save()])
        Save_button.place(x = 60 * rw, y = 170 * rh)

        Data_frame = Frame(Sim_window, height = 10, width = 10)
        Data_frame.place(x = 300 *rw, y = 40 * rh)

        Frame_data = Listbox(Data_frame, height = 10)
        Frame_data.pack(side = 'left', fill = 'y')
        List_data()
        Data_scroll = Scrollbar(Data_frame)
        Data_scroll.pack(side = RIGHT, fill = Y)
        Frame_data.config(yscrollcommand = Data_scroll.set)
        Data_scroll.config(command = Frame_data.yview)

        Data_del = Button(Sim_window, text = 'delete', command = lambda:[Data_delete()])
        Data_del.place(x = 300 * rw, y = 180 * rh)

        Terminal_frame = Frame(Sim_window, height = 50, width = 40, relief = GROOVE, bd = 2)
        Terminal_frame.place(x = 450 * rw, y = 40 * rh)

        Terminal_text = 'Output Terminal'
        Terminal = Text(Terminal_frame, height = 50, width = 30)
        Terminal.pack(side = 'left', fill = 'y')
        Terminal.insert(INSERT, Terminal_text)
        Terminal.config(state = DISABLED) 






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

        #print(rh) #for troublehsooting
        #print(rw) #for troublehsooting

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


