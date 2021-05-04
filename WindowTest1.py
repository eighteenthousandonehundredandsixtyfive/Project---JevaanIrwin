#Python hello
#https://realpython.com/python-gui-tkinter/
#for mplotting data
#%%
from tkinter import *
import time

class data():
        def __init__(self, parent):
                self.main_page = Frame(parent, width=750, height=350)
                self.main_page.pack()

                intro = Label(
                        self.main_page,
                        text = "Welcome to Jevaan's Grapher",
                        fg = "white",
                        bg = "blue")
                
                intro.place(x=100,y=0)

                metu_button = Button (
                        root,
                        text = "Click For Metu pic",
                        width = 18,
                        height = 1,
                        bg = "purple",
                        foreground = "black")
                
                metu_button.place(x=100, y = 30)
                
class methu():
        def __init__(self, parent):
                metu = Label(
                        window,
                        text = "metu ,metu, metu!!!!",
                        fg = "white",
                        bg = "red")
                
                metu.place(x = 100, y = 10)

                metu_text = Entry(
                        window,
                        fg = "yellow",
                        bg = "blue",
                        width = 50,)

                metu_text_button = Button(
                        window,
                        fg = "yellow",
                        bg = "blue",
                        command = lambda:[metu_text.place(x=100, y = 30)])

                metu_text_button.place(x =100, y = 60)
                
                metu_words = metu_text.get()
                metu_words

                
                

class adrian():
        def __init__(self, parent):
                adrian_label = Label(
                        parent,
                        text = "Hello I am ADRiAN",
                        fg = "white",
                        bg = "black")
                adrian_label.place(x = 100, y = 0)
                        
                


if __name__ == '__main__':
        window = Tk()
        adrian_window = Tk()
        adrian_window.geometry("400x250")
        window.geometry("400x250+300+300")
        root = Tk()
        root.geometry("400x250+300+300")
        data(root)
        adrian(adrian_window)
        methu(root)
        root.mainloop()
        


# %%
