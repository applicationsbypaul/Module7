"""
Program: basic_gui_assignment.py
Author: Paul Ford
Last date modified: 06/27/2020
Purpose: creating a gui
"""

import tkinter


def pick_breakfast():
    """
    Changes the label to reflect breakfast was selected
    """
    label.config(text="You selected breakfast")


def pick_second_breakfast():
    """
    Changes the label to reflect second breakfast was selected
    """
    label.config(text="You selected second breakfast")


def pick_lunch():
    """
    Changes the label to reflect lunch was selected
    """
    label.config(text="You selected Lunch.")


def pick_dinner():
    """
    Changes the label to reflect dinner was selected
    """
    label.config(text="You selected Dinner.")


m = tkinter.Tk()  # where m is the name of the main window object
m.title('Favorite Meal')
label = tkinter.Label(m, text="Waiting")
label.grid(row=5)
var1 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="Breakfast", variable=var1, command=pick_breakfast).grid(row=1)
var2 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="Second Breakfast", variable=var2, command=pick_second_breakfast).grid(row=2)
var3 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="Lunch", variable=var3, command=pick_lunch).grid(row=3)
var4 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="Dinner", variable=var4, command=pick_dinner).grid(row=4)

exit_button = tkinter.Button(m, text='Exit', width=25, command=m.destroy)
exit_button.grid(row=6)
m.mainloop()  # infinite loop that waits for events to happen
