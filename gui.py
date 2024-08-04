from tkinter import *
from tkinter import ttk
import sys
import os
from conversions import *

def restart_program(): 
    """
    doesn't work right now but I want to use this to both allow the user to be able to re-enter
    a time if their input is invalid (not numeric) and be able to convert another time without
    having to close and re-open the program manually
    """
    python = sys.executable
    os.execl(python, python, * sys.argv)


def open_new_window():
    """
    opens a new window 
    """
    master.destroy()
    master1 = Tk()
    master1.withdraw() # hides the blank window while still allowing master1 to be used to create the labeled new window
    new_window = Toplevel(master1)
    new_window.title("New Window")
    new_window.geometry("1280x720")
    Label(new_window, text = f"Distance: {distance_selection}\nTime: {time_format(convert_user_input_time())}").pack()
    Label(new_window, text = conversionhubformatting(convert_user_input_time(), distance_selection)).pack() # just a test to make sure this works; not final
    # restartbutton = Button(new_window, text = "Convert another time", command = restart_program) # this doesn't work right now
    exitbutton= Button(new_window, text = "Exit", command = master.quit)
    # restartbutton.pack(pady=10)
    exitbutton.pack(pady=10)

def conversionhubformatting(time, distance):
    """
    formats the conversionhub() function to be displayed in the GUI by ensuring that 
    every time in the list of distance-time conversions is right-aligned 
    """
    dictionary = (conversionhub(time, distance)).items()
    bigstring = ""
    for item in dictionary:
        characters = len(f"{item[0]}:" + f"{item[1]}") # establishes number of characters based on the combined length of distance and time values
        spaces = ""
        spaces_count = 0
        while characters < 29: # stipulates that each distance-time conversion is 29 characters in length (in effect, this makes it right-aligned)
            spaces_count = 29 - characters # in effect, this makes the conversions right-aligned since I'm adding spaces between the distance and time values
            for i in range(spaces_count): # adds the number of spaces needed to make the distance-time conversion 29 characters long 
                spaces += " "
                characters += 1
        string = f"{item[0]}:" + spaces + f"{item[1]}" # this string is 29 characters long
        bigstring += f"{string}\n" #concatenates all of the newline-separated right-aligned strings
    return bigstring

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

def click(event): # this function will cause a TypeError when used as an argument for the combobox bind() function if "event" is not used as a parameter, for some reason
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
    hours_input = hourstextbox.get("1.0", "end-1c")
    if hours_input == "": # if nothing is entered in the text box
        hours_input = 0
    return hours_input

def retrieveminutes():
    """
    Retrieves the number of minutes in the user's entered time. By default this value is 0
    """
    minutes_input = minutestextbox.get("1.0", "end-1c")
    if minutes_input == "": # if nothing is entered in the text box
        minutes_input = 0
    return minutes_input

def retrieveseconds():
    """
    Retrieves the number of seconds in the user's entered time. By default this value is 0
    """
    seconds_input = secondstextbox.get("1.0", "end-1c")
    if seconds_input == "": # if nothing is entered in the text box
        seconds_input = 0
    return seconds_input


def pack_of_functions():
    """
    allows the "Confirm" button to execute multiple commands via the use of four other functions; 
    it stores the user input hours, minutes, and seconds values (by default they are 0) and opens a new
    window where those values have been used in conjunction with the code in the conversions file
    to create a list of equivalent performances at other distances
    """
    global hours_input
    hours_input = retrievehours()
    global minutes_input
    minutes_input = retrieveminutes()
    global seconds_input
    seconds_input = retrieveseconds()
    return open_new_window()

def convert_user_input_time():
    """
    converts the user input in the hours, minutes, and seconds text boxes to the sum of those inputs in seconds
    """
    total_time = convert_user_input_hours() + convert_user_input_minutes() + convert_user_input_seconds()
    return total_time

def convert_user_input_hours():
    """
    converts the user input in the hours text box to seconds. If input is invalid, then the program will restart (not yet implemented)
    """
    try:
        hours = float(hours_input)
        hours_in_seconds = hours * 3600
        return hours_in_seconds
    except ValueError:
        invalid_input = True
def convert_user_input_minutes():
    """
    converts the user input in the minutes text box to seconds. If input is invalid, then the program will restart (not yet implemented)
    """
    try:
        minutes = float(minutes_input)
        minutes_in_seconds = minutes * 60
        return minutes_in_seconds
    except ValueError:
        invalid_input = True
def convert_user_input_seconds():
    """
    returns the user input in the seconds text box. If input is invalid, then the program will restart (not yet implemented)
    """
    try:
        seconds = float(seconds_input)
        return seconds
    except ValueError: #will occur if seconds_input is not numeric
        invalid_input = True
        # while invalid_input: # will add this contingency once I get the main features working

master = Tk() # opens main (initial) window
master.geometry("1280x720")                
label = Label(master, text = "Please select a distance")
label.pack(pady=10)

# drop down menu code
distance_selection = "800m" # default selection value is 800m - will be changed if user selects a different option from drop down menu
cb = ttk.Combobox(master, state = "readonly", values = list_of_options())
cb.current(0) # default selection is "800m"
cb.bind("<<ComboboxSelected>>", click)
cb.pack()

# hours text box
hourstextbox = Text(master,height=1, width=10)
hourstextbox.pack()

# minutes text box
minutestextbox = Text(master, height=1, width=10)
minutestextbox.pack()

# seconds text box
secondstextbox = Text(master, height=1, width=10)
secondstextbox.pack()

button = Button(master, text = "Confirm", command = pack_of_functions)
button2 = Button(master, text = "Exit", command = master.quit)
button.pack(pady=10)
button2.pack(pady=10)
master.mainloop()
