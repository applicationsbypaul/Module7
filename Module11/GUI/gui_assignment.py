"""
Program: gui_assignment.py
Author: Paul Ford
Last date modified: 06/27/2020
Purpose: Game to select between 1 and 10
"""

import random
import tkinter
from tkinter import messagebox
from Module13.classes.number_guesser import NumberGuesser

MAX = 10  # number of buttons in the game
winner = 0  # winner value
game = NumberGuesser()  # instance of the game
buttons = []  # list of buttons to manipulate


def start_game():
    """
    Generates a random number between 1 and MAX.
    Resets games
    :return:
    """
    global winner, game, buttons
    # reset the game , clear the list. create new winner
    game.guessed_list.clear()
    winner = random.randint(1, 10)
    # set all the buttons back to active
    for i in range(MAX):
        buttons[i].config(state="active")


def try_number(num):
    """
    If correct guess
    Create a WINNER window or messagebox to pop up
    Reset game
    Else
    Set the button to visible but not clickable
    Add guessed number to guessed_list in object of type NumberGuesser
    :param num:
    """
    global buttons, game, winner
    if num == winner:
        tkinter.messagebox._show('Winner', 'Congratulations you won. The answer was ' + str(num))
        tkinter.messagebox._show('Guesses', 'You guessed\n' + str(game.guessed_list))
        start_game()
    else:
        game.guessed_list.append(num)
        buttons[num - 1].config(state="disabled")


# command= lambda guess = i,
m = tkinter.Tk()  # where m is the name of the main window object
m.title('Number Game')
for index in range(MAX):
    guess_button = tkinter.Button(m, text=index + 1, command=lambda guess=index + 1: try_number(guess))
    guess_button.grid(row=index + 1)
    buttons.append(guess_button)

exit_button = tkinter.Button(m, text='Exit', width=25, command=m.destroy)
exit_button.grid(row=12)
exit_button = tkinter.Button(m, text='Start', width=25, command=start_game)
exit_button.grid(row=0)
start_game()
m.mainloop()  # infinite loop that waits for events to happen
