import tkinter

window = tkinter.Tk()
window.title("First GUI tk")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="Label test", font=("Arial", 24, "bold"))
my_label.pack()



window.mainloop()
