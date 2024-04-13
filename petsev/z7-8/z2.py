from tkinter import*


root = Tk()
root.geometry("500x400")
root.title("Задание 2")
root.configure(bg="orange")
myLabel1 = Label(root, text = "Hello World!", bg="lightblue", width=20, height=5, borderwidth=1, relief="solid").grid(row=0, column=0)
myLabel2 = Label(root, text = "Меня зовут \n Александр Пецев", bg="lightblue", width=20, height=5, borderwidth=1, relief="solid").grid(row=1, column=5)
myLabel3 = Label(root, bg="lightblue", width=20, height=5, borderwidth=1, relief="solid").grid(row=0, column=5)
myLabel4 = Label(root, bg="lightblue", width=20, height=5, borderwidth=1, relief="solid").grid(row=1, column=0)


root.mainloop()