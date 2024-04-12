import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + str(number))

def button_add():
    global f_num
    global math
    math = "addition"
    f_num = float(entry.get())
    entry.delete(0, tk.END)

def button_subtract():
    global f_num
    global math
    math = "subtraction"
    f_num = float(entry.get())
    entry.delete(0, tk.END)

def button_multiply():
    global f_num
    global math
    math = "multiplication"
    f_num = float(entry.get())
    entry.delete(0, tk.END)

def button_divide():
    global f_num
    global math
    math = "division"
    f_num = float(entry.get())
    entry.delete(0, tk.END)

def button_equal():
    second_num = float(entry.get())
    entry.delete(0, tk.END)

    if math == "addition":
        result = f_num + second_num
    elif math == "subtraction":
        result = f_num - second_num
    elif math == "multiplication":
        result = f_num * second_num
    elif math == "division":
        result = f_num / second_num

    entry.insert(0, str(result))

def button_clear():
    entry.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=20, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

# Create number buttons
button_1 = tk.Button(root, text="1", command=lambda: button_click(1))
button_2 = tk.Button(root, text="2", command=lambda: button_click(2))
button_3 = tk.Button(root, text="3", command=lambda: button_click(3))
button_4 = tk.Button(root, text="4", command=lambda: button_click(4))
button_5 = tk.Button(root, text="5", command=lambda: button_click(5))
button_6 = tk.Button(root, text="6", command=lambda: button_click(6))
button_7 = tk.Button(root, text="7", command=lambda: button_click(7))
button_8 = tk.Button(root, text="8", command=lambda: button_click(8))
button_9 = tk.Button(root, text="9", command=lambda: button_click(9))
button_0 = tk.Button(root, text="0", command=lambda: button_click(0))

buttons = [button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9, button_0]

# Position number buttons
for i, button in enumerate(buttons):
    button.grid(row=(i // 3) + 1, column=i % 3)

# Create operation buttons
button_add = tk.Button(root, text="+", command=button_add)
button_subtract = tk.Button(root, text="-", command=button_subtract)
button_multiply = tk.Button(root, text="*", command=button_multiply)
button_divide = tk.Button(root, text="/", command=button_divide)
button_equal = tk.Button(root, text="=", command=button_equal)
button_clear = tk.Button(root, text="C", command=button_clear)

# Position operation buttons
button_add.grid(row=4, column=0)
button_subtract.grid(row=4, column=1)
button_multiply.grid(row=4, column=2)
button_divide.grid(row=4, column=3)
button_equal.grid(row=5, column=0)
button_clear.grid(row=5, column=1)

root.mainloop()