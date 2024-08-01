from tkinter import *
from tkinter import ttk


def open_new_window():
    """
    opens a new window 
    """
    new_window = Toplevel(master)
    new_window.title("New Window")
    new_window.geometry("1280x720")
    Label(new_window, text = "this is a new window").pack()

master = Tk() # I guess I can't put this in a function without opening more tabs than desired?
master.geometry("1280x720")
label = Label(master, text = "this is the main window")
label.pack(pady=10)
button = Button(master, text = "Click to open a new window", command = open_new_window)
button2 = Button(master, text = "Exit", command = master.quit)
button.pack(pady=10)
button2.pack(pady=10)
master.mainloop()
# need to figure out how to store whichever option is picked from the drop down menu



def openwindow():
    root = Tk()
    root.config(width=1280, height=720)
    root.title("Conversions")
    combo = ttk.Combobox(
        state="readonly", values=["800m",
        "1500m",
        "1600m",
        "Mile",
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
    continuebutton = Button(root, text = "Continue", command=open_new_window(root, combo.get())) #need to figure out how to have the user selection returned and another window opened where the user will then input a time
    continuebutton.pack(pady=10)
    continuebutton.place(x=xcombo+(xcombo*0.333), y=ycombo+50)
    root.mainloop()

