import tkinter as tk
from tkinter import ttk

# Create the main window
window = tk.Tk()
window.title("Minha interface")
window.geometry("900x600")
window.configure(bg='black')

def say_hello():
    print("Hello,world!")
    
# Create a label and a button
label = tk.Label(window, text="Bem vindo..!", bg='black')
label.configure(fg='red', font=('Inter', 20))

button = tk.Button(window, text="Entrar no abismo!", command=say_hello)
button.configure(fg='red', bg='black', font=('Inter', 12))
button.pack(side='bottom')

image = tk.PhotoImage(file='outrun.gif')

label.pack(side='top', fill='both', expand=True)
label.configure(image=image)

# Arrange the widgets using a layout manager
label.pack()
button.pack()

# Run the main loop
window.mainloop()

