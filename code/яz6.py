import tkinter as tk
from tkinter import Label, Button
from PIL import ImageTk, Image
from pathlib import Path


# Функция для обновления изображения и кнопок пролистывания
def update_image(image_number):
    global my_label
    global button_forward
    global button_back

    # Загрузка нового изображения
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    my_label.grid(row=0, column=0, columnspan=3)

    # Обновление информации о текущей фотографии
    status_label = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1,
                         relief=tk.SUNKEN, anchor=tk.E)
    status_label.grid(row=2, column=0, columnspan=3, sticky=tk.W + tk.E)

    # Обновление кнопки вперед
    if image_number == len(image_list):
        button_forward.config(state=tk.DISABLED)
    else:
        button_forward.config(state=tk.NORMAL)

    # Обновление кнопки назад
    if image_number == 1:
        button_back.config(state=tk.DISABLED)
    else:
        button_back.config(state=tk.NORMAL)


# Функция для перелистывания вперед
def forward(image_number):
    global current_image
    current_image += image_number
    update_image(current_image)


# Функция для перелистывания назад
def back(image_number):
    global current_image
    current_image -= image_number
    update_image(current_image)


# Создание основного окна
root = tk.Tk()
root.title("Photo Viewer")

# Установка иконки приложения
path = Path(__file__).parent.resolve()
file = path.joinpath("test_axe.ico")
root.iconbitmap(file)

# Создание списка изображений
image_list = [ImageTk.PhotoImage(Image.open(path.joinpath("images", file))) for file in
              sorted(Path("images").glob("*.jpg"))]

# Изначально отображается первое изображение
current_image = 1
my_label = Label(image=image_list[current_image - 1])
my_label.grid(row=0, column=0, columnspan=3)

# Создание кнопок для пролистывания и выхода
button_back = Button(root, text="<<", command=lambda: back(1), state=tk.DISABLED)
button_exit = Button(root, text="Exit", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(1))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

# Вывод информации о текущей фотографии
status_label = Label(root, text="Image " + str(current_image) + " of " + str(len(image_list)), bd=1, relief=tk.SUNKEN,
                     anchor=tk.E)
status_label.grid(row=2, column=0, columnspan=3, sticky=tk.W + tk.E)

# Запуск основного цикла обработки событий
root.mainloop()
