from tkinter import *
from tkinter import ttk

#I copied the basis for this code from the tkinter documentation and have no idea how to use this
# def openwindow():
    
#     root = Tk()
#     frm = ttk.Frame(root, padding=10)
#     frm.grid()
#     ttk.Label(frm, text="Welcome. This program will show you equivalent performances to any given race time.").grid(column=0, row=0)
    
#     ttk.Button(frm, text="Choose distance") 
#     ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=1)
#     root.mainloop()

def entertimewindow():
    root=Tk()
    frame = ttk.Frame(root, padding=10)
    frame.grid()
    ttk.Label(frame, text="Thanks for making it this far.")
    root.mainloop()

def openwindow():
    root = Tk()
    root.config(width=1280, height=720)
    root.title("Conversions")
    combo = ttk.Combobox(
        state="readonly", values=["800m",
        "1500m",
        "1600m",
        "3000m",
        "3200m",
        "5000m",
        "10000m",
        "Half marathon",
        "Marathon"]
    )
    xcombo = 415
    ycombo=50
    combo.place(x=xcombo, y=ycombo)
    combo.config(width=50)
    continuebutton = Button(root, text = "Continue", command=combo.get()) #need to figure out how to have the user selection returned and another window opened where the user will then input a time
    continuebutton.pack()
    continuebutton.place(x=xcombo+(xcombo*0.333), y=ycombo+50)
    root.mainloop()

# openwindow()

