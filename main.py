from tkinter import *
import tkinter.messagebox
from tkinter.constants import SUNKEN

window = Tk()
window.title("Calculator")
my_frame = Frame(master=window, bg="#4F186B", padx=10, pady=10)
my_frame.pack()
my_entry = Entry(master=my_frame, relief=SUNKEN, borderwidth=5, width=45)
my_entry.grid(row=0, column=0, columnspan=3, ipady=3, pady=3)

def my_click(num):
    my_entry.insert(END, num)

def equal():
    try:
        y = str(eval(my_entry.get()))
        my_entry.delete(0, END)
        my_entry.insert(0, y)
    except:
        tkinter.messagebox.showinfo("Error", "Syntax Error")

def clear():
    my_entry.delete(0, END)

def calculate_percentage():
    try:
        result = float(my_entry.get()) * 0.01
        my_entry.delete(0, END)
        my_entry.insert(0, result)
    except ValueError:
        tkinter.messagebox.showinfo("Error", "Invalid Input")

def delete_last_char():
    current_text = my_entry.get()
    new_text = current_text[:-1]
    my_entry.delete(0, END)
    my_entry.insert(0, new_text)

button_1 = Button(master=my_frame, text="1", padx=5, pady=5, width=10, command=lambda: my_click(1))
button_1.grid(row=1, column=0, pady=3)
button_2 = Button(master=my_frame, text="2", padx=5, pady=5, width=10, command=lambda: my_click(2))
button_2.grid(row=1, column=1, pady=3)
button_3 = Button(master=my_frame, text="3", padx=5, pady=5, width=10, command=lambda: my_click(3))
button_3.grid(row=1, column=2, pady=3)
button_4 = Button(master=my_frame, text="4", padx=5, pady=5, width=10, command=lambda: my_click(4))
button_4.grid(row=2, column=0, pady=3)
button_5 = Button(master=my_frame, text="5", padx=5, pady=5, width=10, command=lambda: my_click(5))
button_5.grid(row=2, column=1, pady=3)
button_6 = Button(master=my_frame, text="6", padx=5, pady=5, width=10, command=lambda: my_click(6))
button_6.grid(row=2, column=2, pady=3)
button_7 = Button(master=my_frame, text="7", padx=5, pady=5, width=10, command=lambda: my_click(7))
button_7.grid(row=3, column=0, pady=3)
button_8 = Button(master=my_frame, text="8", padx=5, pady=5, width=10, command=lambda: my_click(8))
button_8.grid(row=3, column=1, pady=3)
button_9 = Button(master=my_frame, text="9", padx=5, pady=5, width=10, command=lambda: my_click(9))
button_9.grid(row=3, column=2, pady=3)
button_0 = Button(master=my_frame, text="0", padx=5, pady=5, width=10, command=lambda: my_click(0))
button_0.grid(row=4, column=1, pady=3)
button_plus = Button(master=my_frame, text="+", padx=5, pady=5, width=10, command=lambda: my_click("+"))
button_plus.grid(row=5, column=0, pady=3)
button_clear = Button(master=my_frame, text="C", bg="red", padx=5, pady=5, width=10, command=clear)
button_clear.grid(row=5, column=1, pady=3)
button_minus = Button(master=my_frame, text="-", padx=5, pady=5, width=10, command=lambda: my_click("-"))
button_minus.grid(row=5, column=2, pady=3)
button_multiply = Button(master=my_frame, text="*", padx=5, pady=5, width=10, command=lambda: my_click("*"))
button_multiply.grid(row=6, column=0, pady=3)
button_equal = Button(master=my_frame, text="=", bg="green", padx=5, pady=5, width=10, command=equal)
button_equal.grid(row=6, column=1, pady=3)
button_divide = Button(master=my_frame, text="/", padx=5, pady=5, width=10, command=lambda: my_click("/"))
button_divide.grid(row=6, column=2, pady=3)
button_power = Button(master=my_frame, text="^", padx=5, pady=5, width=10, command=lambda: my_click("**"))
button_power.grid(row=7, column=0, pady=3)
button_del = Button(master=my_frame, text="←", padx=5, pady=5, width=10, command=delete_last_char)
button_del.grid(row=7, column=1, pady=3)
button_percentage = Button(master=my_frame, text="%", padx=5, pady=5, width=10, command=calculate_percentage)
button_percentage.grid(row=7, column=2, pady=3)

window.mainloop()