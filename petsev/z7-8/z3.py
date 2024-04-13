from tkinter import *
root = Tk()
root.title("Задание 3")
root.configure(bg="orange")
root.geometry("250x150")
def myClick():
    #Обработчик событий при нажатии кнопки
    myLabel = Label(root, text="Нажата кнопка!")
    myLabel.pack()
myButton = Button(root, text = "Нажмите", command=myClick, fg="blue", bg="#ffffff", width=15, height=4)
myButton.pack()
root.mainloop()
