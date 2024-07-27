from tkinter import *
from tkinter import ttk

#I copied the basis for this code from the tkinter documentation and have no idea how to use this
def openwindow():
    root = Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text="Welcome. This program will show you equivalent performances to any given race time.").grid(column=0, row=0)
    ttk.Button(frm, text="Choose distance") #haven't implemented drop-down menu yet but once an option is clicked a new interface 
                                            #should show up that allows the user to enter their time
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=1)
    root.mainloop()