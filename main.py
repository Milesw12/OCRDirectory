import os
import tkinter as tk
from tkinter import filedialog
import shutil
import ocrmypdf
#import OCRmyPDF

root = tk.Tk()
root.withdraw()

directory = filedialog.askdirectory()
for root, dirs, files in os.walk(directory):
    for file in files:
        print(file)
        name = file
        output = file + "_OCR"
        ocrmypdf(file, output)
        shutil.move(output, 'PDF')
        