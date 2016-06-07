# COPYRIGHT THOMAS BERGBY - ALL RIGHTS RESERVED

from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfile
import codecs


def remove_duplicates():
    global inputText

    if not textFrom.get:
        print("The input field is empty!")

    else:
        textTo.delete(1.0, END)
        getWords = textFrom.get(1.0, END)

        # Add to array
        inputText = [i.strip() for i in getWords.splitlines()]

        # Remove duplicates
        seen = set()
        seen_add = seen.add
        inputText = [x for x in inputText if not (x in seen or seen_add(x))]

        # Prints to output field
        textTo.insert(1.0, '\n'.join(inputText))


def getcontent():
    print(inputText)


def open_file():
    Tk().withdraw()
    input_file = askopenfilename()

    if not input_file:
        print("No file found")

    else:
        # Makes sure the program reads the file as utf-8
        open_textfile = codecs.open(input_file, "r", "utf-8")
        # Inserts all the text from the input file, and makes everything lowercase
        textFrom.insert(1.0, open_textfile.read().lower())
        global inputFileGlobal
        inputFileGlobal = input_file


def save_file():
    file = asksaveasfile(mode="w", defaultextension=".txt", filetypes=(("Text file", "*.txt"), ("All Files", "*.*")))
    if file is None:
        print("No file was opened")

    else:
        textToSave = str(textTo.get(1.0, END))
        file.write(textToSave)
        file.close()


def exit_program():
    root.destroy()


# Global variables
inputFileGlobal = "I'm empty"
inputText = "I am empty"

# The main GUI
root = Tk()
root.wm_title("Duplicate remover")

### Main GUI ###
menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Exit", command=exit_program)
menu_bar.add_cascade(label="File", menu=file_menu)

button = Button(root, text="Remove duplicates", command=remove_duplicates)
button.pack(side=BOTTOM)

# Textbox input-after
varTextAfter = StringVar()
L1 = Label(root, textvariable=varTextAfter)
varTextAfter.set("Output field")
L1.pack(side=RIGHT)
scrollbarAfter = Scrollbar(root)
textTo = Text(root, height=10, width=50)
scrollbarAfter.pack(side=RIGHT, fill=Y)
textTo.pack(side=RIGHT, fill=Y)
scrollbarAfter.config(command=textTo.yview)
textTo.config(yscrollcommand=scrollbarAfter.set)

# Textbox input-from
scrollbarFrom = Scrollbar(root)
textFrom = Text(root, height=10, width=50)
scrollbarFrom.pack(side=RIGHT, fill=Y)
textFrom.pack(side=RIGHT, fill=Y)
scrollbarFrom.config(command=textFrom.yview)
textFrom.config(yscrollcommand=scrollbarFrom.set)
varTextFrom = StringVar()
L2 = Label(root, textvariable=varTextFrom)
varTextFrom.set("Input field")
L2.pack(side=LEFT)

# Mainloop
root.config(menu=menu_bar)
root.mainloop()
