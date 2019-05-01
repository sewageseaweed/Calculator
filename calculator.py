from Tkinter import *


root = Tk()
root.title("Calculator")
root.geometry("500x700")


def turn_to_float(values=[]):
    entry.delete(0, END)
    float_list = [float(i) for i in values]
    for i in float_list:
        print(i)


def addition(num):
    values = []
    values.append(num)
    turn_to_float(values)


#total = Label(root, width=10, height=8, bg="red")
#total.config(font=("Courier", 18))

entry = Entry(root, width=10)
entry.config(font=("Courier", 18))

button1 = Button(text="1", width=5, height=8, command=lambda: entry.insert(END,1))

button2 = Button(text="2", width=5, height=8, command=lambda: entry.insert(END,2))

button3 = Button(text="3", width=5, height=8, command=lambda: entry.insert(END,3))

button4 = Button(text="4", width=5, height=8, command=lambda: entry.insert(END,4))

button5 = Button(text="5", width=5, height=8, command=lambda: entry.insert(END,5))

button6 = Button(text="6", width=5, height=8, command=lambda: entry.insert(END,6))

button7 = Button(text="7", width=5, height=8, command=lambda: entry.insert(END,7))

button8 = Button(text="8", width=5, height=8, command=lambda: entry.insert(END,8))

button9 = Button(text="9", width=5, height=8, command=lambda: entry.insert(END,9))

button0 = Button(text="0", width=5, height=8, command=lambda: entry.insert(END,0))

button_dot = Button(text=".", width = 5, height=8, command=lambda: entry.insert(END, '.'))

button_plus = Button(text="+", width=5, height=8, command=lambda: addition(entry.get()))

button_minus = Button(text="-", width=5, height=8, command=lambda: turn_to_float())


button1.grid(row=1, column=0, sticky="sew", pady=1)
button2.grid(row=1, column=1, sticky="sew", pady=1)
button3.grid(row=1, column=2, sticky="sew", pady=1)
button4.grid(row=2, column=0, sticky="nsew", pady=1)
button5.grid(row=2, column=1, sticky="nsew", pady=1)
button6.grid(row=2, column=2, sticky="nsew", pady=1)
button7.grid(row=3, column=0, sticky="nsew", pady=1)
button8.grid(row=3, column=1, sticky="nsew", pady=1)
button9.grid(row=3, column=2, sticky="nsew", pady=1)
button0.grid(row=4, columnspan=2, sticky="nsew", pady=1)
button_dot.grid(row=4, column=2, sticky="sew", pady=1)
button_plus.grid(row=1, column=5, sticky="sew", pady=1)
button_minus.grid(row=2, column=5, sticky="nsew", pady=1)

#total.grid(row=0, stick="ew", columnspan=3)
entry.grid(row=0, stick="nsew", columnspan=6)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.rowconfigure(0, weight=2)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)

root.mainloop()
