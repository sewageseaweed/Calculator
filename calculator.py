from Tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("500x700")

values = []

entry = Entry(root, width=10)
entry.config(font=("Courier", 18))

label = Label(root, width=10)
label.config(font=("Courier", 15))


def show_numbers():     #Shows values list on label
    for i in xrange(0, len(values)):
        label.config(text=values)


def clear():
    entry.delete(0, END)
    del values[:]           #deletes all values in list


def operator(num, op):
    if num == '':
        num = '0'
    values.extend((num, op))     #works like append, but inserts more than 1 thing into the list
    entry.delete(0, END)
    show_numbers()


def store_to_total():
    num = entry.get()
    values.append(num)
    entry.delete(0, END)
    length = len(values)

    try:
        total = float(values[0])
    except ValueError:
        total = 0

    try:
        for i in xrange(1, length, 2):
            if values[i] == '+':
                total += float(values[i+1])
            elif values[i] == '-':
                total -= float(values[i+1])
            elif values[i] == 'x':
                total *= float(values[i+1])
            elif values[i] == '/':
                total /= float(values[i+1])
            elif values[i] == '%':
                total *= float(values[i+1])/100
            elif values[i] == '+%':
                total *= ((float(values[i+1])/100)+1)
            elif values[i] == '-%':
                percent = total*(float(values[i+1])/100)
                total -= percent
    except ValueError:
        pass

    try:
        if total.is_integer():
            entry.insert(END, int(total))
            label.config(text='= '+str(int(total)))
        else:
            entry.insert(END, total)
            label.config(text='= '+str(total))
    except AttributeError:
        entry.insert(END, 0)

    del values[:]


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

button_plus = Button(text="+", width=3, height=4, command=lambda: operator(entry.get(), '+'))

button_minus = Button(text="-", width=3, height=4, command=lambda: operator(entry.get(), '-'))

button_divide = Button(text='/', width=3, height=4, command=lambda: operator(entry.get(), '/'))

button_multiplication = Button(text='X', width=3, height=4, command=lambda: operator(entry.get(), 'x'))

button_equals = Button(text="=", width=3, height=4, command=lambda: store_to_total())

button_clear_entry = Button(text="Clear All", width=3, height=4, command=lambda: clear())

button_clear_line = Button(text="Clear Line", width=3, height=4, command=lambda: entry.delete(0, END))

button_sales_tax = Button(text="Sales Tax", width=3, height=4, command=lambda: operator(entry.get(), '+%'))

button_discount = Button(text="Discount", width=3, height=4, command=lambda: operator(entry.get(), '-%'))

button_percent = Button(text = "%", width=3, height=4, command=lambda: operator(entry.get(), '%'))


#Formatting Button Layout in APP

label.grid(row=0, columnspan=5, stick="new")
entry.grid(row=0, stick="nsew", columnspan=6)
button_clear_entry.grid(row=1, column=1, columnspan=2, sticky="nsew", pady=1)
button_clear_line.grid(row=1, column=0, sticky="nsew", pady=1)
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
button_sales_tax.grid(row=2, rowspan=2, column=3, sticky="nsew", pady=1)
button_discount.grid(row=4, rowspan=2, column=3, sticky="nsew", pady=1)
button_percent.grid(row=1, column=3, sticky="nsew", pady=1)
button_divide.grid(row=1, column=4, sticky="nsew", pady=1)
button_multiplication.grid(row=2, column=4, sticky="nsew", pady=1)
button_minus.grid(row=3, column=4, sticky="nsew", pady=1)
button_plus.grid(row=4, column=4, sticky="nsew", pady=1)
button_equals.grid(row=5, column=4, sticky="nsew", pady=1)


root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
root.columnconfigure(4, weight=1)
root.rowconfigure(0, weight=2)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)
root.rowconfigure(5, weight=1)

root.mainloop()
