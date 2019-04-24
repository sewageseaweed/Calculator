from Tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("400x700")


def printName(num):
    print(num)


def printName2(Event):
    print("2")


button1 = Button(root, text="1", width=5, height=4, command=lambda: printName(1))

button2 = Button(text="2", width=5, height=4)
button2.bind("<Button-1>", printName2)
button3 = Button(text="3", width=5, height=4)
button3.bind("<Button-1>", printName2)
button4 = Button(text="4", width=5, height=4)
button4.bind("<Button-1>", printName2)
button5 = Button(text="5", width=5, height=4)
button5.bind("<Button-1>", printName2)
button6 = Button(text="6", width=5, height=4)
button6.bind("<Button-1>", printName2)
button7 = Button(text="7", width=5, height=4)
button7.bind("<Button-1>", printName2)
button8 = Button(text="8", width=5, height=4)
button8.bind("<Button-1>", printName2)
button9 = Button(text="9", width=5, height=4)
button9.bind("<Button-1>", printName2)
button0 = Button(text="0", width=5, height=4)
button0.bind("<Button-1>", printName2)
button_plus = Button(text="+", width=5, height=4)
button_plus.bind("<Button-1>", printName2)
button_minus = Button(text="-", width=5, height=4)
button_minus.bind("<Button-1>", printName2)

button1.grid(row=1, column=0, sticky="sew")
button2.grid(row=1, column=1, sticky="sew")
button3.grid(row=1, column=2, sticky="sew")
button4.grid(row=2, column=0, sticky="nsew")
button5.grid(row=2, column=1, sticky="nsew")
button6.grid(row=2, column=2, sticky="nsew")
button7.grid(row=3, column=0, sticky="nsew")
button8.grid(row=3, column=1, sticky="nsew")
button9.grid(row=3, column=2, sticky="nsew")
button0.grid(row=4, column=1, sticky="nsew")
button_plus.grid(row=4, column=0, sticky="nsew")
button_minus.grid(row=4, column=2, sticky="nsew")

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)

root.mainloop()
