import tkinter as tk
import webbrowser
import random

def generate_random_wikipedia_link():
    random_page_id = random.randint(1, 1700000)  # Генерация случайного ID страницы Википедии
    random_link = f"https://ru.wikipedia.org/wiki/index.html?curid={random_page_id}"  # Формирование случайной ссылки на Википедию
    link_label.config(text=random_link)  # Обновление текста метки для отображения случайной ссылки

def open_link():
    link = link_label.cget("text")  # Получение текста из метки
    webbrowser.open_new(link)  # Открытие ссылки в браузере

app = tk.Tk()  # Создание главного окна приложения
app.title("Случаяная страница Википедии")
app.geometry("350x150")

link_label = tk.Label(app, text="", wraplength=250, justify="center")
link_label.pack(pady=10)

generate_button = tk.Button(app, text="Сгенерировать случайную ссылку", command=generate_random_wikipedia_link)  # Создание кнопки для генерации случайной ссылки
generate_button.pack(pady=5)

open_button = tk.Button(app, text="Перейти по ссылке", command=open_link)  # Создание кнопки для открытия ссылки
open_button.pack(pady=5)

app.mainloop()