#imported for the rolls
import random

#for the GUI
from tkinter import *

#give the amount of d6 needed to roll for an attack and return the array
def roll_normal(rolls):
    roll_block = []
    for i in range(rolls):
        roll_block.append(random.randint(1,6))
    
    return roll_block

#adds the pilots die to every score
def add_pilot_roll(pilot_roll, roll):
    new_array = []

    for i in pilot_roll:
        new_array.append(i + roll)

    return new_array

def total_roll(rolls):
    total = 0
    for i in rolls:
        total += i

    return total

#command for the roll button
def roll_button():
    display.delete(1.0, END)
    roll_number = roll.get()

    pilot_roll = random.randint(1, 6)

    roll_array = roll_normal(roll_number)
    pilot_array = add_pilot_roll(roll_array, pilot_roll)






#Base GUI code

#creates the root screen
root = Tk()
root.title('Battletech Dice Roller')

#sets the size of the GUI
root.geometry("500x300")

#Label for spinner
Label(master=root, text='D6 to Roll:').grid(row=0, column=0)

#Spinner for D6 to roll
roller = Spinbox(root, from_=1, to=100, width=10, wrap=True).grid(row=0, column=1)

#adding a confirm button
roll = Button(root, text="Roll", width=20, command=roll_button).grid(row=1, column=0)

#display for rolls
display = Text(root, height=2, width=60, state='disabled', relief=SUNKEN).grid(row=2,column=0)


#initalizes main window - NOTE: put widgets before this
root.mainloop()

