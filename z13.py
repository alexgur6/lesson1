if 2**2 > 4:
    print("yes")
#ничего


import tkinter as tk  # Импорт библиотеки Tkinter для создания графического интерфейса
import webbrowser  # Импорт модуля webbrowser для открытия ссылок в браузере
import random  # Импорт модуля random для генерации случайных чисел

def generate_random_wikipedia_link():
    random_page_id = random.randint(1, 1000000)  # Генерация случайного ID страницы Википедии
    random_link = f"https://en.wikipedia.org/wiki/index.html?curid={random_page_id}"  # Формирование случайной ссылки на Википедию
    link_label.config(text=random_link)  # Обновление текста метки для отображения случайной ссылки

def open_link():
    link = link_label.cget("text")  # Получение текста из метки
    webbrowser.open_new(link)  # Открытие ссылки в браузере

app = tk.Tk()  # Создание главного окна приложения
app.title("Random Wikipedia Link")  # Установка заголовка окна
app.geometry("300x150")  # Установка размеров окна

link_label = tk.Label(app, text="", wraplength=250, justify="center")  # Создание метки для отображения ссылки
link_label.pack(pady=10)  # Размещение метки в окне с некоторым отступом сверху и снизу

generate_button = tk.Button(app, text="Generate Random Link", command=generate_random_wikipedia_link)  # Создание кнопки для генерации случайной ссылки
generate_button.pack(pady=5)  # Размещение кнопки в окне с некоторым отступом сверху и снизу

open_button = tk.Button(app, text="Open Link", command=open_link)  # Создание кнопки для открытия ссылки
open_button.pack(pady=5)  # Размещение кнопки в окне с некоторым отступом сверху и снизу

app.mainloop()  # Запуск главного цикла приложения для отображения окна и обработки событий
