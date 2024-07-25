from tkinter import *
from tkinter import ttk

#I copied the basis for this code from the tkinter documentation and have no idea how to use this
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Welcome. This program will show you equivalent performances to any given race time.").grid(column=0, row=0)
ttk.Button(frm, text="Choose distance")
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=1)
root.mainloop()