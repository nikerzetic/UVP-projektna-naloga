import tkinter as tk


class NewBoxWindow:
    def __init__(self, master, command):
        self.master = master
        self.command = command
        self.window = tk.Toplevel(self.master)
        self.window.title('Nova škatla')
        self.enter_new_box_name = tk.Entry(self.window)
        self.enter_new_box_name.pack(fill=tk.X)
        self.confirm_new_box = tk.Button(self.window, text='Ustvari novo škatlo', command=self.create)  # how to destroy button afterwards?
        self.confirm_new_box.pack()

    def create(self):
        if self.enter_new_box_name.get():
            self.command(self.enter_new_box_name.get())
            self.window.destroy()
        else:
            self.window.destroy()
