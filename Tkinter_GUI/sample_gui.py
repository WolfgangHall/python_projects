from tkinter import *

window = Tk()

def km_to_miles():
    # get method
    miles = float(e1_value.get()) * 1.6
    # put the text at the END
    t1.insert(END, miles)

b1 = Button(window, text="Execute", command=km_to_miles)
b1.grid(row=0, column=0)

# need to declare the variable returned
e1_value = StringVar()
# gets variable depending on what user puts in entry widget
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

t1 = Text(window, height=1, width=15)
t1.grid(row=0, column=2)

window.mainloop()
