from tkinter import *

class test():
    def __init__(self, parent):

        frame = Frame(root, height = 10, width = 5)
        frame.place (x = 100, y = 10)

        # listbox = Listbox(frame, height=10)
        # listbox.insert(1,"jevaan")
        # listbox.insert(2,"Jasper")
        # listbox.insert(3,"Yuv")
        # listbox.insert(4,"Arnav")
        # listbox.insert(5,'Josh')
        # listbox.insert(6,'John')
        # listbox.insert(7,'Ryan')
        # listbox.insert(8,'Aliyah')
        # listbox.insert(9,'Irwin')
        # listbox.insert(10,'benjamin')
        # listbox.insert(11,'11')
        # listbox.insert(12,'12')
        # listbox.insert(13,'13')
        
        # listbox.pack(side = 'left', fill = 'y')

        # scroll = Scrollbar(frame)
        # scroll.pack(side = RIGHT, fill = Y)
        # listbox.config(yscrollcommand = scroll.set)

        # scroll.config( command = listbox.yview )

        but = Button(text = 'destroy', command = lambda:[listbox.destroy()])
        but.place(x = 100, y = 160)

        but2 = Button(text = 'get', command = lambda:[print(listbox.get(ANCHOR))])
        but2.place(x = 150, y = 160)

root = Tk()
root.geometry("400x250+300+300")
test(root)
root.mainloop()