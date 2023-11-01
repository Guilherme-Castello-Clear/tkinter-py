from tkinter import *

window = Tk()
window.title("First GUI tk")
window.minsize(width=500, height=300)

my_label = Label(text="Label test", font=("Arial", 24, "bold"))
my_label.pack(side="left")

my_label["text"] = "New text"
my_label.config(text="New text")


def button_clicked():
    print("Clicked")
    button.config(text="Clicked")
    print(input.get())

button = Button(text="Click me", command=button_clicked)
button.pack()

input = Entry(width=10)
input.pack()

window.mainloop()
