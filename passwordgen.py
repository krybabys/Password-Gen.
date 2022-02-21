from curses.panel import bottom_panel
import importlib
import random
import string
import secrets
import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, width =400 ,height = 200, bg = 'white')

e = tk.Entry(root)
lng = tk.Label(root, text ="The Number of Chars.", bg = 'grey',)
canvas.create_window(200 ,  100 , window = e)

def pas():
    num = e.get()
    num = int(num)
    if num > 20 :
        num = 20
    global p
    p = "".join(secrets.choice(string.punctuation + string.digits + string.ascii_letters) for x in range (num))
    root = tk.Tk()
    lbl2 = tk.Label(root , text = 'Your password is : ' + p )
    lbl2.pack()
    root.mainloop()


btn = tk.Button(root, text = 'Generate', command =pas,)
lng.pack()
btn.pack()
canvas.pack()
root.mainloop()