import tkinter as tk 
# for gui we use this module
# import time module
from time  import strftime
# root window -to display elements
root=tk.Tk()
root.title("Digital Clock")

def time():
    string = strftime('%H:%M:%S %p \n %D')
    label.config(text= string)
    label.after(1000,time)
    
label=tk.Label(root,font=('calibri',50,'bold'),background='black',foreground='purple')
label.pack(anchor='center')    
time()   
root.mainloop() 
    