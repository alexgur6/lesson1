import tkinter as tk
from PIL import Image, ImageTk

class PhotoViewer:
    def __init__(self, master):
        self.master = master
        self.master.title("Photo Viewer")
        self.master.iconbitmap('test_axe.ico')

        self.image_paths = ['test.png', 'test2.png']
        self.current_image = 0

        self.canvas = tk.Canvas(master, width=400, height=400)
        self.canvas.pack()

        self.load_image()

        next_button = tk.Button(master, text="Next", command=self.next_image)
        next_button.pack(side=tk.LEFT)

        prev_button = tk.Button(master, text="Previous", command=self.prev_image)
        prev_button.pack(side=tk.LEFT)

        exit_button = tk.Button(master, text="Exit", command=master.quit)
        exit_button.pack(side=tk.RIGHT)

    def load_image(self):
        image_path = self.image_paths[self.current_image]
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        self.canvas.image = photo

    def next_image(self):
        self.current_image = (self.current_image + 1) % len(self.image_paths)
        self.load_image()

    def prev_image(self):
        self.current_image = (self.current_image - 1) % len(self.image_paths)
        self.load_image()

if __name__ == "__main__":
    root = tk.Tk()
    app = PhotoViewer(root)
    root.mainloop()
