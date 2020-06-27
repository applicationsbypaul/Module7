"""
Program: gui.py
Author: Paul Ford
Last date modified: 06/27/2020
Purpose: Working on my first GUI
"""
import tkinter


def pick_cis():
    label.config(text="Nice choice")


def pick_bis():
    label.config(text="Are you sure?")


m = tkinter.Tk()  # where m is the name of the main window object
m.title('Major Decision')
label = tkinter.Label(m, text="No Selection Made")
label.grid(row=5)
var1 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="CIS", variable=var1, command=pick_cis).grid(row=0)
var2 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="BIS", variable=var2, command=pick_bis).grid(row=1)
exit_button = tkinter.Button(m, text='Exit', width=25, command=m.destroy)
exit_button.grid(row=6)
m.mainloop()  # infinite loop that waits for events to happen
