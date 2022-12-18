import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("My GUI")
window.geometry("500x500")
window.configure(bg='black')

# Create a label and set its font color and size
label = tk.Label(window, text="Hello, world!")
label.configure(fg='red', font=('Arial', 16))
label.configure(bg='black')

# Arrange the widget using a layout manager
label.pack()

# Run the main loop
window.mainloop()
