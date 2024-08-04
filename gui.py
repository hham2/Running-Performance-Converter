from tkinter import *
from tkinter import ttk


def open_new_window():
    """
    opens a new window 
    """
    master.destroy()
    master1 = Tk()
    master1.withdraw() #hides the blank window while still allowing master1 to be used to create the labeled new window
    new_window = Toplevel(master1)
    new_window.title("New Window")
    new_window.geometry("1280x720")
    Label(new_window, text = f"Distance: {distance_selection}\nTime: [todo: time_input]").pack()
    print(hours_selection)

def list_of_options():
    """
    returns a list of valid distances
    """
    options = [
        "800m",
        "1500m",
        "1600m",
        "Mile",
        "3000m",
        "3200m",
        "2 mile",
        "5000m",
        "10000m",
        "Half marathon",
        "Marathon"]
    return options

def click(event): #this function will cause a TypeError when used as an argument for the combobox bind() function if "event" is not used as an argument, for some reason
    """
    used to assign the user's selection to a variable that will be used in the next window 
    and for that selection to be made when a user clicks a given option from the drop down menu
    """
    global distance_selection
    distance_selection = cb.get()

def retrievehours():
    """
    Retrieves the number of hours in the user's entered time. By default this value is 0
    """


master = Tk() #opens main (initial) window
master.geometry("1280x720")                                                          
label = Label(master, text = "Please select a distance")
label.pack(pady=10)

#drop down menu code
cb = ttk.Combobox(master, state = "readonly", values = list_of_options())
cb.current(0) #default selection is "800m"
distance_selection = "800m" #default selection value is 800m - will be changed if user selects a different option from drop down menu
cb.bind("<<ComboboxSelected>>", click)
cb.pack()

# text box code
# probably going to have three separate text boxes labeled "hours","minutes", and "seconds" that will each store input
# that will then be converted to seconds using a function I'll make
textbox = Text(master, height=1, width=10)
textbox.pack()
hours_selection = textbox.get #need to figure out how to store user input - this isn't quite doing it 



button = Button(master, text = "Confirm", command = open_new_window)
button2 = Button(master, text = "Exit", command = master.quit)
button.pack(pady=10)
button2.pack(pady=10)
master.mainloop()
# need to figure out how to store whichever option is picked from the drop down menu