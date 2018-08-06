import tkinter as tk
import model


class EditNoteWindow:
    def __init__(self, master, box, note, command):
        self.master = master
        self.box = box
        self.note = note
        self.command = command

        self.window = tk.Toplevel(self.master)
        self.window.title('Nov listek')

        self.enter_new_note_content = tk.Entry(self.window)
        self.enter_new_note_content.insert(tk.END, note)
        self.enter_new_note_content.pack(fill=tk.X)

        self.confirm_new_box = tk.Button(self.window, text='Uredi listek', command=self.edit)
        self.confirm_new_box.pack()

    def edit(self):
        if self.enter_new_note_content.get() and self.enter_new_note_content.get() != self.note:
            self.box.delete_selected()
            self.box.add_note(self.enter_new_note_content.get())
            self.command(self.box)
            self.window.destroy()
        else:
            self.window.destroy()
