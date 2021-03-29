# BIOT670 Capstone Group 3
# Thom Hart & Myeisha Johnson

# Import all packages 
from tkinter import * 
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
import tkinter as tk

# Set the window to execute Tk()

window = tk.Tk()

# Establish the window size as a 400 pixel square
window.geometry('400x400')

# Create the instructions for how to use this GUI

greeting = tk.Label(text="Welcome to the EEG analog signal processing tool. \n \n"
                    "Please only process one .tiff file at a time.")

# Execute the label

greeting.pack()
  
# Open file function that allows us to open and read the file
def open_file(): 
    file = askopenfile(mode ='r', filetypes =[('Image Files', '.tiff', '.tif')]) 
    if file is not None: 
        content = file.read() 
        print(content)

# Create the button that allows us to select the .tiff file
  
btn = Button(window, text ='Select EEG', command = lambda:open_file()) 
btn.pack(side = TOP, pady = 10) 

#Myeisha Johnson - text widget to capture notes
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import asksaveasfile

root = Tk()
root.title('EEG Notes')
root.geometry("500x450")

# Create Clear Function
def clear():
	eeg_text.delete(1.0, END)

# Grab the text from the text box
def get_text():
	my_label.config(text=eeg_text.get(1.0, END))

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

#save text entered in text widget as a file
def save():
    files = [('All Files', '*.*'), 
             ('Text Document', '*.txt')]
    file = asksaveasfile(filetypes = files, defaultextension = files)
  
btn = ttk.Button(root, text = 'Save', command = lambda : save())
btn.pack(side = TOP, pady = 20)



root.mainloop()
