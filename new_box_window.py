import tkinter as tk
import model


class NewBoxWindow:
    def __init__(self):
        self.mainframe = model.Mainframe()
        self.window = tk.Tk()
        self.window.title('Nova škatla')
        self.enter_new_box_name = tk.Entry(self.window)
        self.enter_new_box_name.pack(fill=tk.X)
        self.confirm_new_box = tk.Button(self.window, text='Ustvari novo škatlo', command=self.create)  # how to destroy button afterwards?
        self.confirm_new_box.pack()

    def create(self):
        self.mainframe.new_box(self.enter_new_box_name.get())
        self.window.destroy()
