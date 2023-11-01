from tkinter import *

window = Tk()
window.title("First GUI tk")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

my_label = Label(text="Label test", font=("Arial", 24, "bold"))
# my_label.pack()
#
my_label["text"] = "New text"
my_label.config(text="New text")
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)

def button_clicked():
    print("Clicked")
    button.config(text="Clicked")
    print(input.get())

button = Button(text="Click me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

input = Entry(width=10)
# input.pack()
input.grid(column=2, row=2)

window.mainloop()
