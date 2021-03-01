#Author: Obi Casel

import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
def eeg_o():
	"Please upload an tiff file"
	path = askopenfilename (
		filetypes = [("Tiff Files", "*.tiff"), ("All files", "*.*")]
	)
	if not path:
		return
	words.delete(1.0, tk.END)
	with open (path, "r") as tiff_input:
		tff = tiff_input.read()
		words.insert(tk.END, tiff)
	window.title(f"EEG 3.0 Reader - {path}")

	
def eeg_s():
	"Save tff file"
	path = asksaveasfilename (
		defaultextension = "tiff",
		filetypes = [("Tiff Files", "*.tiff"), ("All files", "*.*")]
	)
	if not path:
		return
	with open (path, "w") as tff_output:
		tff = words.get(1.0, tk.END)
		tff_output.write(tff)
	window.title(f"EEG 3.0 Reader - {path}")

window = tk.Tk()
window.title("EEG 3.0 Reader")
window.rowconfigure(0, minsize = 900, weight = 1)
window.columnconfigure(1, minsize = 900, weight = 1)
words = tk.Text(window)
sides = tk.Frame(window, relief = tk.RAISED, bd = 3)
eeg_new = tk.Button (sides, text = "New")
eeg_open = tk.Button (sides, text = "Open", command = eeg_o)
eeg_save = tk.Button (sides, text = "Save", command = eeg_s)
eeg_new.grid(row = 0, column = 0, sticky = "ew", padx = 5, pady = 5)
eeg_open.grid(row = 1, column = 0, sticky = "ew", padx = 5)
eeg_save.grid(row = 2, column = 0, sticky = "ew", padx = 5)
sides.grid(row = 0, column = 0, sticky = "ns")
window.mainloop()
