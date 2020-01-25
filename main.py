import tkinter


# Create blank window
window = tkinter.Tk()

# Rename window
window.title("Soundboard")

label = tkinter.Label(window, text="Welcome to the soundboard!")

btn1 = tkinter.Button(text="Button1", fg="red").grid(row=0, column=0)
btn2 = tkinter.Button(text="Button2", fg="green").grid(row=0, column=1)
btn3 = tkinter.Button(text="Button3", fg="purple").grid(row=0, column=2)
btn4 = tkinter.Button(text="Button4", fg="red").grid(row=1, column=0)
btn5 = tkinter.Button(text="Button5", fg="green").grid(row=1, column=1)
btn6 = tkinter.Button(text="Button6", fg="purple").grid(row=1, column=2)
btn7 = tkinter.Button(text="Button7", fg="red").grid(row=2, column=0)
btn8 = tkinter.Button(text="Button8", fg="green").grid(row=2, column=1)
btn9 = tkinter.Button(text="Button9", fg="purple").grid(row=2, column=2)

window.mainloop()