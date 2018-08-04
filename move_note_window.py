import tkinter as tk
import model


class MoveNoteWindow:
    def __init__(self, master, box, content, command):
        self.master = master
        self.box = box
        self.content = content
        self.command = command

        self.window = tk.Toplevel(self.master)
        self.window.title('Premakni listke')

        self.move_from_label = tk.LabelFrame(self.window, text='Premakni iz:')
        self.move_from_label.pack(fill=tk.BOTH, expand=tk.YES)

        self.move_from_box = tk.Label(self.move_from_label, text=str(self.box))
        self.move_from_box.pack()

        self.move_to_label = tk.LabelFrame(self.window, text='Premakni v:')
        self.move_to_label.pack(fill=tk.BOTH, expand=tk.YES)

        self.tk_variable = tk.StringVar(self.move_to_label)
        self.tk_variable.set(self.content[0])
        self.option_menu = tk.OptionMenu(self.move_to_label, self.tk_variable, *self.content)
        self.option_menu.pack(fill=tk.X)

        self.button_frame = tk.Frame(self.move_to_label)
        self.button_frame.pack(fill=tk.X)

        self.cancel_button = tk.Button(self.button_frame, text='Prekliči', command=self.cancel)
        self.cancel_button.grid(row=0, column=0)

        self.move_button = tk.Button(self.button_frame, text='Premakni', command=self.move)
        self.move_button.grid(row=0, column=1)

    def cancel(self):
        self.window.destroy()

    def move(self):
        if model.Box(self.tk_variable.get()) != self.box:
            self.box.move_notes(model.Box(self.tk_variable.get()))
            self.command(self.box)
            self.window.destroy()
