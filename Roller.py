#imported for the rolls
import random

#for the GUI
from tkinter import *
import tkinter as tk

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
    
    roll_number = int(Spinbox.get(roller))

    pilot_roll = random.randint(1, 6)

    roll_array = roll_normal(roll_number)
    pilot_array = add_pilot_roll(roll_array, pilot_roll)

    output = ("Roll: " + str(roll_array) + "\nPilot Roll: " + str(pilot_roll) + 
        "\nRolls with pilot Die: " + str(pilot_array) + "\nTotal: " + str(total_roll(pilot_array)))
    display.config(text=output)

    

    






#Base GUI code

#creates the root screen
root = Tk()
root.title('Battletech Dice Roller')

#sets the size of the GUI
root.geometry("1200x300")

#Label for spinner
roll_label = tk.Label(master=root, text='D6 to Roll:')
roll_label.grid(row=0, column=0)

#Spinner for D6 to roll
roller = tk.Spinbox(root, from_=1, to=100, width=10, wrap=True)
roller.grid(row=0, column=1)

#adding a confirm button
roll = tk.Button(root, text="Roll", width=20, command=roll_button)
roll.grid(row=0, column=3)

#display for rolls
display = Label(master=root, font=('Ariel', 16))
display.grid(row=3, column=4)

roll_lab2 = Label(master=root, text='Rolls: ', font=('Ariel', 16))
roll_lab2.grid(row=2, column=3)
#initalizes main window - NOTE: put widgets before this
root.mainloop()

