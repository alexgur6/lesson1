import tkinter as tk
import webbrowser
import random

def generate_random_wikipedia_link():
    random_page_id = random.randint(1, 1000000)  # случайный ID страницы
    random_link = f"https://en.wikipedia.org/wiki/index.html?curid={random_page_id}"
    link_label.config(text=random_link)  # обновляем текст метки

def open_link():
    link = link_label.cget("text")  # получаем текст метки
    webbrowser.open_new(link)  # открываем ссылку в браузере

app = tk.Tk()
app.title("Random Wikipedia Link")
app.geometry("300x150")

link_label = tk.Label(app, text="", wraplength=250, justify="center")
link_label.pack(pady=10)

generate_button = tk.Button(app, text="Generate Random Link", command=generate_random_wikipedia_link)
generate_button.pack(pady=5)

open_button = tk.Button(app, text="Open Link", command=open_link)
open_button.pack(pady=5)

app.mainloop()
