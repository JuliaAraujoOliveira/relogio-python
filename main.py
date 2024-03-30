import tkinter as tk
from  tkinter import *

import os 
from time import strftime

root = tk.Tk()
root.title('Relogio da Julinha')
root.geometry("600X320")
root.maxsize(600,320)
root.minsize(600,320)

root.configure(background= '#1d1d1d')

def get_saudacao():
    nome_usuario = os.getlogin()
    saudacao.config(text='Olá, '+nome_usuario)

def get_data():
    data_atual =strftime('%a, %d, %Y')
    data.config(text=data_atual)
    
def get_horas():
    hora_atual= strftime('%H:%M:%S')
    horas.config(text=hora_atual)
    horas.after(1000, get_horas)
    
margem = tk.Canvas(root, width=600, height=60, bg='#d1d1d1', bd=0, highlightthickness=0,relief='ridge' )
margem.pack()  
  
saudacao = Label(root, background='#1d1d1d', fg='#8e27ea', font=('Arial', 16))
saudacao.pack()

data = Label(root, background='#1d1d1d', fg='#8e27ea', font=('Arial', 14))
data.pack(pady=2)

horas = Label(root, background='#1d1d1d', fg='#8e27ea', font=('Arial', 64, 'bold'))
horas.pack(pady=2)



get_saudacao()
get_data()
get_horas()
root.mainloop()
