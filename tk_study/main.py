import tkinter as tk
import time
import random

COLORS = [('#e53935', '#fff'), ('#4a148c', '#fff'), ('#bbdefb', 'black'), ('#ff9800', 'black')]

root = tk.Tk()
root.title('Button Widget')
root.geometry('500x300+700+300')

def get_label():
   #print(label.cget('text'))
    print(label_text.get())

def set_label():
    label_text.set('Hello, world!!!!!!')

def change_label_color():
    idx = random.randint(0, len(COLORS) - 1)
    color = COLORS[idx]
    label['bg'] = color[0]
    label['fg'] = color[1 ]




btn = tk.Button(root, text='Get', font="Verdana 10 bold", width=12, pady=5, padx=5, command=get_label)
btn.pack(pady=10)

btn2 = tk.Button(root, text='Set', font="Verdana 10 bold", width=8, pady=5, padx=5, command=get_label)
btn2.pack(pady=10)

btn3 = tk.Button(root, text='Change color', font="Verdana 10 bold", width=12, pady=5, padx=5, command=change_label_color)
btn3.pack(pady=10)

s = 'vsyciy text!!!!'

label_text = tk.StringVar()
label_text.set(s)


label = tk.Label(root, textvariable=label_text, bg='#000', fg='#fff')
label.pack(pady=10)

root.mainloop()
