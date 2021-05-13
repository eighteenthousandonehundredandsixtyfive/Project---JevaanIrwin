from tkinter import *      
root = Tk()      
canvas = Canvas(root, width = 2000, height = 1000, bg= "white")      
canvas.pack()      
img = PhotoImage(file="Logo.ppm")      
canvas.create_image(950,300,image=img)      
mainloop()   
