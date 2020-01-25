import tkinter


# Create blank window
window = tkinter.Tk()

# Rename window
window.title("Soundboard")

label = tkinter.Label(window, text="Welcome to the soundboard!").pack()
window.mainloop()