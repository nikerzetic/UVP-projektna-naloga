import tkinter as tk
import model


class MoveNoteWindow:
    def __init__(self, master, box, content):
        self.master = master
        self.box = box
        self.content = content

        self.window = tk.Toplevel(self.master)
        self.window.title('Nov listek')

        self.move_from_label = tk.LabelFrame(self.master, text='Premakni iz:')
        self.move_from_label.pack(fill=tk.X)

        self.move_from_box = tk.Label(self.master, text=str(self.box))
        self.move_from_box.pack()

        self.move_to_label = tk.LabelFrame(self.master, text='v:')
        self.move_to_label.pack(fill=tk.X)

        self.tk_variable = tk.StringVar(self.window)
        self.tk_variable.set(self.content[0])
        self.option_menu = tk.OptionMenu(self.window, self.tk_variable, *self.content)
        self.option_menu.pack(fill=tk.X)

        self.cancel_button = tk.Button(self.window, text='Prekliči', command=self.cancel)

        self.move_button = tk.Button(self.window, text='Premakni', command=self.move)
        self.move_button.pack(tk.RIGHT)

    def cancel(self):
        self.window.destroy()

    def move(self):
        if model.Box(self.tk_variable.get()) != self.box:
            self.box.move_notes(model.Box(self.tk_variable.get()))
            self.window.destroy()
