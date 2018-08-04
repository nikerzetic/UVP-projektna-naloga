import tkinter as tk


class ConfirmationWindow:

    def __init__(self, master, question, command1, command2):
        self.command1 = command1
        self.command2 = command2

        self.window = tk.Toplevel(master)
        self.window.title('Potrdi izbiro')

        self.label = tk.Label(self.window, text=question)
        self.label.pack()

        self.frame = tk.Frame(self.window)
        self.frame.pack()

        self.confirm_button = tk.Button(self.frame, text='Da', command=self.confirm)
        self.confirm_button.grid(row=0, column=0)

        self.cancel_button = tk.Button(self.frame, text='Prekliči', command=self.window.destroy)
        self.cancel_button.grid(row=0, column=1)

    def confirm(self):
        self.command1()
        self.command2()
        self.window.destroy()
