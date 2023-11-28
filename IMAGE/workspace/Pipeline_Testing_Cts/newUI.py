# -*- coding: utf-8 -*-
import os
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askdirectory
from tkinter import filedialog as fd
from time import sleep
import subprocess
# from tqdm import tqdm
UsrName = subprocess.check_output('whoami')
UsrName = UsrName.decode().strip()
try : 
    os.remove('path.txt')
except:
    print()

# create the root window
root = tk.Tk()
root.title('GMS Auto Test')
root.resizable(False, False)
root.geometry('550x250')
var = tk.StringVar()


def select_dir():
    path = askdirectory(title ='Select your folder')
    # path = path.replace('/','\\')
    var.set(path)
    with open('path.txt', 'w') as f:
        f.write(path)

var = tk.StringVar()
retry=tk.StringVar()
reboot=tk.StringVar()
reset=tk.StringVar()
mylabel = tk.Label(root, text='                 GMS Auto Test',font = ('Bahnschrift',20,'bold'),pady=10)
mylabel.grid()

llabel = tk.Label(root,text='Retry')
llabel.place(x = 150, y = 100)
retry1 = tk.Entry(root,textvariable=retry)
retry1.place(x = 200, y = 100)


lllabel = tk.Label(root,text='Reboot')
lllabel.place(x = 150, y = 130)
reboot1 = tk.Entry(root,textvariable=reboot)
reboot1.place(x = 200, y = 130)


llllabel = tk.Label(root,text='Reset')
llllabel.place(x = 150, y = 160)
reset1 = tk.Entry(root,textvariable=reset)
reset1.place(x = 200, y = 160)

def start():
    with open(f'/home/{UsrName}/Desktop/IMAGE/workspace/Pipeline_Testing/runfre.txt','w')as f:       
        f.write(str(retry1.get())+'\n')
        f.write(str(reboot1.get())+'\n')
        f.write(str(reset1.get()))
        f.close

    with open('record_disconnect.txt','r+') as a:
        a.truncate(0)
        root.destroy()

def close_window():
    root.destroy()

start_button = tk.Button(
    root,
    text='Start',
    font = ('Arial',9),
    width=10,
    command=start
)
close_button = tk.Button(
    root,
    text='Close',
    font = ('Arial',9),
    width=10,
    command = close_window
)

b_select = tk.Button(root, text = 'select folder', command = select_dir,width = 20)
b_select.place(x = 170, y = 60)

start_button.place(x = 170, y = 200)
close_button.place(x = 260, y = 200)

root.mainloop()


