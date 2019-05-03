from Tkinter import *


root = Tk()
root.title("Calculator")
root.geometry("500x700")

values = []


def clear():
    entry.delete(0, END)
    del values[:]


def sum(num):
    values.append(num)
    values.append('+')
    entry.delete(0, END)


def subtract(num):
    values.append(num)
    values.append('-')
    entry.delete(0, END)


def multiply(num):
    values.append(num)
    values.append('x')
    entry.delete(0, END)


def divide(num):
    values.append(num)
    values.append('/')
    entry.delete(0, END)


def store_to_total():
    num = entry.get()
    values.append(num)
    entry.delete(0, END)
    total = float(values[0])
    length = len(values)
    for i in xrange(1, length, 2):
        if values[i] == '+':
            total += float(values[i+1])
        if values[i] == '-':
            total -= float(values[i+1])
        if values[i] == 'x':
            total *= float(values[i+1])
        if values[i] == '/':
            total /= float(values[i+1])

    entry.insert(END, total)

#def store_to_total(values=[]):
    #entry.delete(0, END)
    #for i in enumerate(values):
    #    if not i.isalpha():
    #        values = map(str, values)
    #    else:
    #        values = map(float, values)
        #print(i)



#total = Label(root, width=10, height=8, bg="red")
#total.config(font=("Courier", 18))

entry = Entry(root, width=10)
entry.config(font=("Courier", 18))

#Creating buttons in GUI

button1 = Button(text="1", width=3, height=4, command=lambda: entry.insert(END,1))

button2 = Button(text="2", width=3, height=4, command=lambda: entry.insert(END,2))

button3 = Button(text="3", width=3, height=4, command=lambda: entry.insert(END,3))

button4 = Button(text="4", width=3, height=4, command=lambda: entry.insert(END,4))

button5 = Button(text="5", width=3, height=4, command=lambda: entry.insert(END,5))

button6 = Button(text="6", width=3, height=4, command=lambda: entry.insert(END,6))

button7 = Button(text="7", width=3, height=4, command=lambda: entry.insert(END,7))

button8 = Button(text="8", width=3, height=4, command=lambda: entry.insert(END,8))

button9 = Button(text="9", width=3, height=4, command=lambda: entry.insert(END,9))

button0 = Button(text="0", width=3, height=4, command=lambda: entry.insert(END,0))

button_dot = Button(text=".", width = 3, height=4, command=lambda: entry.insert(END, '.'))

button_plus = Button(text="+", width=3, height=4, command=lambda: sum(entry.get()))

button_minus = Button(text="-", width=3, height=4, command=lambda: subtract(entry.get()))

button_divide = Button(text='/', width=3, height=4, command=lambda: divide(entry.get()))

button_multiplication = Button(text='X', width=3, height=4, command=lambda: multiply(entry.get()))

button_equals = Button(text="=", width=3, height=4, command=lambda: store_to_total())

button_clear_entry = Button(text="Clear All", width=3, height=4, command=lambda: clear())

#Formatting Button Layout in APP

entry.grid(row=0, stick="nsew", columnspan=6)

button_clear_entry.grid(row=1, columnspan=3, sticky="nsew")
button1.grid(row=2, column=0, sticky="nsew", pady=1)
button2.grid(row=2, column=1, sticky="nsew", pady=1)
button3.grid(row=2, column=2, sticky="nsew", pady=1)
button4.grid(row=3, column=0, sticky="nsew", pady=1)
button5.grid(row=3, column=1, sticky="nsew", pady=1)
button6.grid(row=3, column=2, sticky="nsew", pady=1)
button7.grid(row=4, column=0, sticky="nsew", pady=1)
button8.grid(row=4, column=1, sticky="nsew", pady=1)
button9.grid(row=4, column=2, sticky="nsew", pady=1)
button0.grid(row=5, columnspan=2, sticky="nsew", pady=1)
button_dot.grid(row=5, column=2, sticky="nsew", pady=1)
button_divide.grid(row=1, column=3, sticky="nsew", pady=1)
button_multiplication.grid(row=2, column=3, sticky="nsew", pady=1)
button_minus.grid(row=3, column=3, sticky="nsew", pady=1)
button_plus.grid(row=4, column=3, sticky="nsew", pady=1)
button_equals.grid(row=5, column=3, sticky="nsew", pady=1)

#total.grid(row=0, stick="ew", columnspan=3)

#Giving a set size for each row/column

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
root.rowconfigure(0, weight=2)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)
root.rowconfigure(5, weight=1)

root.mainloop()
