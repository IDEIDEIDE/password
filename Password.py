#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 10:11:51 2021

@author: clockshield
"""

from tkinter import *
import random
root=Tk()
root.title("lol")
root.geometry("400x400")

Label = Label(root)
array_3d = [[["Andrew Garfield ", "TomHalland", "TOBYMCY"], ["Fan", "Hater"], [1,2,3,4,5,6]]]

def Password420():
    random_1 = random.randint(0, 2)
    random_2 = random.randint(0, 1)
    random_3 = random.randint(0, 5)
    letter1 = array_3d[0][0][random_1]
    letter2 = array_3d[0][1][random_2]
    letter3 = str(array_3d[0][2][random_3])
    Label["text"] = "Your new password is: " + letter1 + letter2 + letter3

btn = Button(root,text="spiderman",command=Password420)
btn.place(relx = 0.5, rely = 0.4, anchor=CENTER)
Label.place(relx = 0.5, rely = 0.5, anchor=CENTER)
root.mainloop()