from tkinter import *
win = Tk()

#buttons
b1 = Button(win, text='one')
b2 = Button(win, text='two')

b1.grid(row=0, column=0)
b2.grid(row=1, column=1)

b1.configure(text='uno')

def but1():
    print('this button was pressed')

b1.configure(command=but1)


