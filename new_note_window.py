import tkinter as tk


class NewNoteWindow:
    def __init__(self, master, content, command):
        self.master = master
        self.command = command
        self.content = content

        self.window = tk.Toplevel(self.master)
        self.window.title('Nov listek')

        self.enter_new_note_content = tk.Text(self.window)
        self.enter_new_note_content.pack(fill=tk.X)

        self.tk_variable = tk.StringVar(self.window)
        self.tk_variable.set(self.content[0])
        self.option_menu = tk.OptionMenu(self.window, self.tk_variable, *self.content)
        self.option_menu.pack(fill=tk.X)

        self.confirm_new_box = tk.Button(self.window, text='Ustvari novo škatlo', command=self.create)  # how to destroy button afterwards?
        self.confirm_new_box.pack()

    def create(self):
        if self.enter_new_note_content.get():
            self.command(self.tk_variable, self.enter_new_note_content.get())
            self.window.destroy()
        else:
            self.window.destroy()

