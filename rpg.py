import sys
import time
from tkinter import *

root = Tk()

def testFunction():
    l.insert(INSERT, 'time!' + '\n')

def quitGame():
    sys.exit()

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.attributes("-fullscreen", True)
root.bind("<Escape>", (lambda event: quitGame()))
root.configure(background='#333333')

w2 = root.winfo_reqwidth()
h2 = root.winfo_reqheight()

l = Text(root)
l.configure(highlightthickness=0, background='#000000', foreground='#ffffff', borderwidth=0)
l.configure(width=w2, height=h2)
l.place(x=0)
l.pack()

def parseInput(input):
    if (not input):
        return
    if (input == 'quit'):
        root.destroy()
    elif (input == 'timer'):
        root.after(2000, func=testFunction)
    else:
        l.insert(INSERT, input + '\n')
    e.delete(0, 'end')

e = Entry(root)
e.configure(background='#000000', foreground='#fff000', borderwidth=0, width=w2-12)
e.focus_set()
e.place(x=0, y=h-35)
e.bind('<Return>', (lambda event: parseInput(e.get())))

root.mainloop()