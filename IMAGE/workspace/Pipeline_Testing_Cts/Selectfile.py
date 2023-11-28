# -*- coding: utf-8 -*-
import os
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askdirectory
from tkinter import filedialog as fd
from time import sleep
from tqdm import tqdm

try : 
    os.remove('path.txt')
except:
    print()

# create the root window
root = tk.Tk()
root.title('CPU Mitigation')
root.resizable(False, False)
root.geometry('300x150')

def select_dir():
    path = askdirectory(title ='Select your folder')
    path = path.replace('/','\\')
    print("Path:"+path)
    with open('path.txt', 'w') as f:
        f.write(path)


openfile_button = tk.Button(
    root,
    text = "Select your folder",
    font = ('Arial',12,'bold'),
    command=select_dir
)

openfile_button.pack(expand=True)
root.mainloop()