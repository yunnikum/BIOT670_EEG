#Myeisha Johnson
#Group 3 EEG

from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import asksaveasfile

root = Tk()
root.title('EEG Notes')
root.geometry("500x450")

# Clear button
def clear():
	eeg_text.delete(1.0, END)

# Grab the text from the text box
def get_text():
	my_label.config(text=eeg_text.get(1.0, END))

	
#save button - save text entered in text widget as a file
def save():
    files = [('All Files', '*.*'), 
             ('Text Document', '*.txt')]
    file = asksaveasfile(filetypes = files, defaultextension = files)
    file.write(eeg_text.get(1.0, END))


eeg_text = Text(root, width=40, height=10, font=("Arial", 16))
eeg_text.pack(pady=20)

button_frame = Frame(root)
button_frame.pack()

clear_button = Button(button_frame, text="Clear", command=clear)
clear_button.grid(row=0, column=0)

get_text_button = Button(button_frame, text="Get Text", command=get_text)
get_text_button.grid(row=0, column=1, padx=20)

my_label = Label(root, text='')
my_label.pack(pady=20)

  
btn = ttk.Button(root, text = 'Save', command = lambda : save())
btn.pack(side = TOP, pady = 20)



root.mainloop()
