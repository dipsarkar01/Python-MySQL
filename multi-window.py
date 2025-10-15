from tkinter import *

root = Tk()
root.title("First window")
root.geometry("500x400")

def window1():
    root1 = Tk()
    root1.title("Second window")
    root1.geometry("400x300")
    button1 = Button(root1, text="Back to main window", command=root1.destroy)
    button1.pack(pady=20)

label = Label(root, text="Welcome to multi-window")
label.pack(pady=20)

button = Button(root, text="New window", command=window1)
button.pack()

root.mainloop()