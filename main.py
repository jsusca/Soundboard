from tkinter import *
from winsound import *


def play():
    PlaySound("SystemExit", SND_ASYNC)


# Create blank window
root = Tk()
# Rename window
root.title("Soundboard")

label = Label(root, text="Welcome to the soundboard!").grid(row=0, column=0, columnspan=4, pady=10)

# Create buttons
btn1 = Button(height=5, width=15, command=play)
btn2 = Button(height=5, width=15)
btn3 = Button(height=5, width=15)
btn4 = Button(height=5, width=15)
btn5 = Button(height=5, width=15)
btn6 = Button(height=5, width=15)
btn7 = Button(height=5, width=15)
btn8 = Button(height=5, width=15)
btn9 = Button(height=5, width=15)
btn10 = Button(height=5, width=15)
btn11 = Button(height=5, width=15)
btn12 = Button(height=5, width=15)

# Place buttons on root window
btn1.grid(row=1, column=0, padx=2, pady=2)
btn2.grid(row=1, column=1, padx=2, pady=2)
btn3.grid(row=1, column=2, padx=2, pady=2)
btn4.grid(row=1, column=3, padx=2, pady=2)
btn5.grid(row=2, column=0, padx=2, pady=2)
btn6.grid(row=2, column=1, padx=2, pady=2)
btn7.grid(row=2, column=2, padx=2, pady=2)
btn8.grid(row=2, column=3, padx=2, pady=2)
btn9.grid(row=3, column=0, padx=2, pady=2)
btn10.grid(row=3, column=1, padx=2, pady=2)
btn11.grid(row=3, column=2, padx=2, pady=2)
btn12.grid(row=3, column=3, padx=2, pady=2)

root.mainloop()
