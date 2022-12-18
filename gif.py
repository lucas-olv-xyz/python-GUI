import tkinter as tk
from tkinter import PhotoImage

# Create the main window
window = tk.Tk()

# Create a PhotoImage object from the GIF image file
image = PhotoImage(file="outrun.gif", format="gif")

# Create a Label widget to display the image
label = tk.Label(window, image=image)

# Place the label in the center of the window
label.pack(side="top", fill="both", expand=True)

# Run the Tkinter event loop
window.mainloop()
