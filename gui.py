import tkinter as tk
import webbrowser

# Create the main window
window = tk.Tk()
window.title("????????????????????????????????????")
window.geometry("900x600")
window.configure(bg='black')

def open_url():
    # Open the URL in the user's default web browser
    webbrowser.open("https://www.youtube.com/watch?v=OzBPyATdG-c&list=PLnh-TZzbBdaAMOm7sexgpBr01u3uFnjmA&index=4")
    
# Create a label and a button
label = tk.Label(window, text="???????????????", bg='black')
label.configure(fg='red', font=('Inter', 20))

button = tk.Button(window, text="????????????", command=open_url)
button.configure(fg='pink', bg='black', font=('Inter', 12))
button.pack(side='bottom')

image = tk.PhotoImage(file='dream.gif')

label.pack(side='top', fill='both', expand=True)
label.configure(image=image)

# Arrange the widgets using a layout manager
label.pack()
button.pack()

# Run the main loop
window.mainloop()

