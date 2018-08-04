import tkinter as tk
import model


class NewNoteWindow:
    def __init__(self, master, content):
        self.master = master
        self.content = content

        self.window = tk.Toplevel(self.master)
        self.window.title('Nov listek')

        self.enter_new_note_content = tk.Entry(self.window)
        self.enter_new_note_content.pack(fill=tk.X)

        self.tk_variable = tk.StringVar(self.window)
        self.tk_variable.set(self.content[0])
        self.option_menu = tk.OptionMenu(self.window, self.tk_variable, *self.content)
        self.option_menu.pack(fill=tk.X)

        self.confirm_new_box = tk.Button(self.window, text='Ustvari nov listek', command=self.create)
        self.confirm_new_box.pack()

    def create(self):
        if self.enter_new_note_content.get():
            model.Box(self.tk_variable.get()).add_note(self.enter_new_note_content.get())
            self.window.destroy()
        else:
            self.window.destroy()
