# Импортируем модуль tkinter для создания графического интерфейса
import tkinter as tk

# Объявляем глобальные переменные
f_num = ""
math = ""

# Функция обработки нажатия на кнопку с числом
def button_click(number):
    global f_num
    current = entry.get()
    entry.delete(0, "end") # для удаления текста из поля ввода entry с индекса 0 (начала) до индекса "end" (конца).
    entry.insert(0, str(current) + str(number))

# Функции обработки нажатия на кнопки операций
def button_add():
    global f_num
    global math
    math = "addition"
    f_num = float(entry.get())
    entry.delete(0, "end")
def button_subtract():
    global f_num
    global math
    math = "subtraction"
    f_num = float(entry.get())
    entry.delete(0, "end")

def button_multiply():
    global f_num
    global math
    math = "multiplication"
    f_num = float(entry.get())
    entry.delete(0, "end")

def button_divide():
    global f_num
    global math
    math = "division"
    f_num = float(entry.get())
    entry.delete(0, "end")

# Функция обработки нажатия на кнопку "равно"
def button_equal():
    second_num = float(entry.get())
    entry.delete(0, "end")

    if math == "addition":
        result = f_num + second_num
    elif math == "subtraction":
        result = f_num - second_num
    elif math == "multiplication":
        result = f_num * second_num
    elif math == "division":
        result = f_num / second_num

    entry.insert(0, str(result))

# Функция обработки нажатия на кнопку "очистить"
def button_clear():
    entry.delete(0, "end")



# Создаем главное окно
root = tk.Tk()
root.title("Calculator")

# Создаем поле ввода
entry = tk.Entry(root, width=20, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

# Создаем кнопки для цифр
for i in range(1, 10):
    btn = tk.Button(root, text=str(i), command=lambda i=i: button_click(i))
    btn.grid(row=(i-1)//3 + 1, column=(i-1)%3) #. При делении (i-1)//3 мы разделяем значения i на группы по 3 кнопки.
    # Затем добавляем 1, чтобы сдвинуть индексацию строк с 0 на 1.
    # column=(i-1)%3: Это определяет столбец, в котором будет размещена кнопка.
    # Операция (i-1)%3 позволяет вычислить остаток от деления i-1 на 3, что дает значения 0, 1 или 2

# Создаем кнопку для нуля
btn_zero = tk.Button(root, text="0", command=lambda: button_click(0))
btn_zero.grid(row=4, column=1)

# Создаем кнопки для операций
btn_add = tk.Button(root, text="+", command=button_add)
btn_subtract = tk.Button(root, text="-", command=button_subtract)
btn_multiply = tk.Button(root, text="*", command=button_multiply)
btn_divide = tk.Button(root, text="/", command=button_divide)
btn_equal = tk.Button(root, text="=", command=button_equal)
btn_clear = tk.Button(root, text="C", command=button_clear)

# Позиционируем кнопки операций
btn_add.grid(row=1, column=3)
btn_subtract.grid(row=2, column=3)
btn_multiply.grid(row=3, column=3)
btn_divide.grid(row=4, column=3)
btn_equal.grid(row=4, column=0)
btn_clear.grid(row=4, column=2)

# Запускаем главный цикл обработки событий
root.mainloop()
