import tkinter 
from tkinter import *
from tkinter import ttk

import tkinter.messagebox



def F():
  global notepad
  
  files = Tk()

  notepad += 1;
    
  files.title('Notepad #' + str(notepad))
  
  canvas = Canvas(files, width=550, height=820, bg='#f4dc72')
  canvas.pack()
  
  canvas.create_rectangle(10, 0, 8, 500, fill='#ff2c2c', outline="")
  
  files.geometry('400x400')
  
  current_var = tkinter.StringVar()
  combobox = ttk.Combobox(files, textvariable=current_var)
  
  File=ttk.Button(files,text="File" , command=F).place(x=100, y=20)
  
  
  
  Help=ttk.Button(files,text="Help", command=H).place(x=220, y=20)
  
  t = tkinter.Text(files, width=52, height=50, bg='#f4dc72',highlightthickness=0,bd=0).place(x=15, y=60)
  
  files.configure(bg='#f4dc72')
  
  files.mainloop()

notepad = 1;

def H():
  tkinter.messagebox.showinfo("Help","Press File to Create a new Notepad")

  
root= Tk()

root.title('Notepad #1')

canvas = Canvas(root, width=550, height=820, bg='#f4dc72')
canvas.pack()

canvas.create_rectangle(10, 0, 8, 500, fill='#ff2c2c', outline="")

root.geometry('400x400')

current_var = tkinter.StringVar()
combobox = ttk.Combobox(root, textvariable=current_var)

File=ttk.Button(root,text="File" , command=F).place(x=100, y=20)


Help=ttk.Button(root,text="Help", command=H).place(x=220, y=20)

t = tkinter.Text(root, width=52, height=50, bg='#f4dc72',highlightthickness=0,bd=0).place(x=15, y=60)

root.configure(bg='#f4dc72')

root.mainloop()



