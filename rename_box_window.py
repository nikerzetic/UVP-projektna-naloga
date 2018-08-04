import tkinter as tk


class RenameBoxWindow:

    def __init__(self, master, command1, command2):
        self.command1 = command1
        self.command2 = command2

        self.window = tk.Toplevel(master)
        self.window.title('Preimenuj škatlo')

        self.enter_new_box_name = tk.Entry(self.window)
        self.enter_new_box_name.pack(fill=tk.X)

        self.confirm_button = tk.Button(self.window, text='Preimenuj škatlo', command=self.rename)
        self.confirm_button.pack()

    def rename(self):
        if self.enter_new_box_name.get():
            self.command1(self.enter_new_box_name.get())
            self.command2()
            self.window.destroy()
        else:
            self.window.destroy()
