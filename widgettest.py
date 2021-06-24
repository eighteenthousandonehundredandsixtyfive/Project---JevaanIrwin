from tkinter import *

class test():
    def __init__(self, parent):
        listbox = Listbox(root, height=3)
        listbox.insert(1,"jevaan")
        listbox.insert(2,"Jasper")
        listbox.insert(3,"Yuv")
        listbox.place(x = 100, y = 100)

        but = Button(text = 'destroy', command = lambda:[listbox.destroy()])
        but.place(x = 100, y = 160)


root = Tk()
root.geometry("400x250+300+300")
test(root)
root.mainloop()