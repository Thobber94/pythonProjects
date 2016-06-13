from tkinter import *


def set_val(val):
    print(val)


root = Tk()

# Variable scale
scale = Scale(orient='horizontal', from_=0, to=150, command=set_val)
scale.pack()

# Up button


root.mainloop()
