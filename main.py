from tkinter import *
from winsound import *


def toggle():
    if loop_btn.config("relief")[-1] == "sunken":
        loop_btn.config(relief="raised")
    else:
        loop_btn.config(relief="sunken")


def play1():
    if loop_btn.config("relief")[-1] == "sunken":
        PlaySound("Sounds/DrumKit.wav", SND_FILENAME | SND_ASYNC | SND_LOOP)
    else:
        PlaySound("Sounds/DrumKit.wav", SND_FILENAME | SND_ASYNC)


def play2():
    PlaySound("Sounds/Snare.wav", SND_FILENAME | SND_ASYNC)


def play3():
    PlaySound("Sounds/DrumKit2.wav", SND_FILENAME | SND_ASYNC)


def play4():
    PlaySound("Sounds/DrumLoop.wav", SND_FILENAME | SND_ASYNC)


def play5():
    PlaySound("Sounds/BassDrum.wav", SND_FILENAME | SND_ASYNC)


def play6():
    PlaySound("Sounds/HHSuperShort.wav", SND_FILENAME | SND_ASYNC)


def play7():
    PlaySound("Sounds/ShortSnare.wav", SND_FILENAME | SND_ASYNC)


def play8():
    PlaySound("Sounds/ClosedHihat.wav", SND_FILENAME | SND_ASYNC)


def play9():
    PlaySound("Sounds/MBase.wav", SND_FILENAME | SND_ASYNC)


def play10():
    PlaySound("Sounds/TranceBass.wav", SND_FILENAME | SND_ASYNC)


def play11():
    PlaySound("Sounds/MiniKickLoop.wav", SND_FILENAME | SND_ASYNC)


def play12():
    PlaySound("Sounds/DrumKit3.wav", SND_FILENAME | SND_ASYNC)


# Create blank window
root = Tk()

# Rename window
root.title("Soundboard")

label = Label(root, text="Welcome to the soundboard!")
label.grid(row=0, column=1, columnspan=3, pady=10)

# Create loop button
loop_btn = Button(height=3, width=15, text="Loop", relief="raised", command=toggle)
loop_btn.grid(row=0, column=0, pady=3, padx=2)

# Create buttons
btn1 = Button(height=5, width=15, command=play1)
btn2 = Button(height=5, width=15, command=play2)
btn3 = Button(height=5, width=15, command=play3)
btn4 = Button(height=5, width=15, command=play4)

btn5 = Button(height=5, width=15, command=play5)
btn6 = Button(height=5, width=15, command=play6)
btn7 = Button(height=5, width=15, command=play7)
btn8 = Button(height=5, width=15, command=play8)

btn9 = Button(height=5, width=15, command=play9)
btn10 = Button(height=5, width=15, command=play10)
btn11 = Button(height=5, width=15, command=play11)
btn12 = Button(height=5, width=15, command=play12)

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

