from tkinter import *
from PIL import Image, ImageTk

class PhotoViewer:
    def __init__(self, master):
        self.master = master
        self.master.title("Photo Viewer")
        self.master.iconbitmap('test_axe.ico')

        self.image_list = [Image.open("test.png"), Image.open("test2.png")]
        self.current_image = 0

        self.my_label = Label(self.master)
        self.my_label.grid(row=0, column=0, columnspan=3)

        self.status_bar = Label(self.master, text="Image 1 of {}".format(len(self.image_list)), bd=1, relief=SUNKEN, anchor=E)
        self.status_bar.grid(row=2, column=0, columnspan=3, sticky=W+E)

        self.button_back = Button(self.master, text="<<", command=self.back, state=DISABLED)
        self.button_quit = Button(self.master, text="Exit", command=root.quit)
        self.button_forward = Button(self.master, text=">>", command=lambda: self.forward(1))

        self.button_back.grid(row=1, column=0)
        self.button_quit.grid(row=1, column=1)
        self.button_forward.grid(row=1, column=2)

        self.update_image()

    def update_image(self):
        image = ImageTk.PhotoImage(self.image_list[self.current_image])
        self.my_label.grid_forget()
        self.my_label = Label(self.master, image=image)
        self.my_label.image = image
        self.my_label.grid(row=0, column=0, columnspan=3)

    def back(self):
        if self.current_image > 0:
            self.current_image -= 1
            self.update_image()
            self.update_buttons()

    def forward(self, num):
        if self.current_image < len(self.image_list) - 1:
            self.current_image += num
            self.update_image()
            self.update_buttons()

    def update_buttons(self):
        if self.current_image == 0:
            self.button_back.config(state=DISABLED)
        else:
            self.button_back.config(state=NORMAL)

        if self.current_image == len(self.image_list) - 1:
            self.button_forward.config(state=DISABLED)
        else:
            self.button_forward.config(state=NORMAL)

root = Tk()
app = PhotoViewer(root)
root.mainloop()