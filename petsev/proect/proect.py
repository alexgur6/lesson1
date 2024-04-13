import tkinter as tk
import webbrowser


def open_random_article():
    webbrowser.open("https://ru.wikipedia.org/wiki/Special:Random")


app = tk.Tk()
app.title("Случайная страница")
app.geometry("300x100")

label = tk.Label(app, text="Хотите увидеть случайную страницу Википедии?")
label.pack()

open_button = tk.Button(app, text="Открыть", command=open_random_article)
open_button.pack()

app.mainloop()

