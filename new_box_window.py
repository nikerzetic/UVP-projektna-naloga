import tkinter as tk


class NewBoxWindow:
    def __init__(self, master, command1, command2):
        self.master = master
        self.command1 = command1
        self.command2 = command2
        self.window = tk.Toplevel(self.master)
        self.window.title('Nova škatla')
        self.enter_new_box_name = tk.Entry(self.window)
        self.enter_new_box_name.pack(fill=tk.X)
        self.confirm_new_box = tk.Button(self.window, text='Ustvari novo škatlo', command=self.create)
        self.confirm_new_box.pack()

    def create(self):
        if self.enter_new_box_name.get():
            self.command1(self.enter_new_box_name.get())
            self.command2()
            self.window.destroy()
        else:
            self.window.destroy()
