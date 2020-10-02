import tkinter as tk
from tkinter.filedialog import askopenfilenames, asksaveasfile
import sys
from PyPDF2 import PdfFileMerger

root = tk.Tk()
root.withdraw()
merger = PdfFileMerger()
filename = askopenfilenames()
if len(filename) == 0:
    sys.exit()
for x in filename:
    if x.endswith(".pdf"):
        merger.append(x)
outputname = asksaveasfile(mode="w", defaultextension=".pdf")
merger.write(outputname.name)
merger.close()
