import os
import tkinter as tk
from tkinter import messagebox
top = tk.Tk()
top.title('QQ登录')
banner = tk.Label(top, width=25, text='QQ', fg='white', bg='green')
banner.grid(row=0, columnspan=4)

usernameLabel = tk.Label(top, text='用户名')
usernameLabel.grid(row=1, column=0)
username = tk.StringVar()
usernameEntry = tk.Entry(top, textvariable=username)
usernameEntry.grid(row=1, column=1)

passwordLabel = tk.Label(top, text='密码')
passwordLabel.grid(row=2, column=0)
password = tk.StringVar()
passwordEntry = tk.Entry(top, textvariable=password, show='*')
passwordEntry.grid(row=2, column=1)

mp = dict()
f = open(f'{os.path.dirname(__file__)}/e5-5.txt', 'r', encoding='utf-8')
f.seek(0)
lines = f.read().splitlines()
for line in lines:
  un, pwd = map(str,line.split(' '))
  mp[un] = pwd

def login():
    if username.get() == '' or password.get() == '':
        messagebox.showerror('错误','用户名或密码不能为空')
        return
    pwd = mp.get(username.get(),None)
    if pwd == None:
        messagebox.showerror('错误','用户名不存在')
        return
    if pwd != password.get():
        messagebox.showerror('错误','密码错误')
        return 
    messagebox.showinfo('成功','登录成功')

loginButton = tk.Button(top, text = '登录', command = login)
loginButton.grid(row=3, columnspan=4)

top.mainloop()
