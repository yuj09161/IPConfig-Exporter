import os,subprocess
import tkinter as tk
import tkinter.messagebox as msgbox

root=tk.Tk()

def default():
    k=1
    respond=subprocess.run('ipconfig /all',stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
    while True:
        if not os.path.isfile('out%d.txt' %k):
            with open('out%d.txt' %k,'ab') as file:
                file.write(respond.stdout)
            break
        k+=1
    root.destroy()

def set_name():
    name_str=name_in.get()
    if name_str:
        respond=subprocess.run('ipconfig /all',stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
        with open(name_str+'.txt','wb') as file:
            file.write(respond.stdout)
        root.destroy()
    else:
        msgbox.showerror('Error','Empty Name')

name_in=tk.StringVar()
tk.Label(root,text='ipconfig Saver').grid(row=0,column=0,columnspan=2)
tk.Entry(root,textvariable=name_in).grid(row=1,column=0,columnspan=2)
tk.Button(root,text='Export',command=set_name).grid(row=2,column=0)
tk.Button(root,text='+Default Name',command=default).grid(row=2,column=1)

tk.mainloop()