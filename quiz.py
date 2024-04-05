import _tkinter as tk
from tkinter import StringVar

root=tkinter.tkinter()
root .geometry("500x500")
questions=["25+25=?," "25*4 =?","4-2=?","5/5=?","20*4=?"]
options=['A','B','50'],['C','D','90'],['A','B','2'],['20','25','80']
questions=["what is the opposite of girl ?"]
options=['boy','girl','woman','mother']

frame =tkinter.frame(root, padx=10,pady=10,)
questions_labe1 = tk.label(frame,height=5,width=20)

options=tk.Radiobutton(frame,bg="efff")
option1=tk.Radiobutton(frame,bg="efff")
option2=tk.Radiobutton(frame,bg="efff")


button_next=tk.button(frame,text='next')

frame-__package__(fill='both',expand=true)