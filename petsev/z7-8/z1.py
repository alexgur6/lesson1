from tkinter import*


root = Tk()
root.geometry("250x200")
root.configure(bg="orange")
myLabel = Label(root, text = "Hello World!", fg="white", bg="lightblue", width=20, height=5,borderwidth=1, relief="solid")
myLabel.pack(padx=6, pady=20)

myLabel.pack()
root.mainloop()

