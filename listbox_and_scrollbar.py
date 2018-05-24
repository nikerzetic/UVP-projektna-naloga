import tkinter as tk


class ListboxAndScrollbar:
    def __init__(self, master, items=[]):
        self.master = master
        self.items = items
        self.selected = set()
        self.listbox = tk.Listbox(self.master, selectmode=tk.MULTIPLE)  # worth sacrificing this offense for cleaner code?
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self.master)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        for item in self.items:
            self.listbox.insert(tk.END, item)

        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

    def refresh_listbox(self):
        self.listbox.delete(0, tk.END)
        for item in self.items:
            self.listbox.insert(tk.END, item)

    def select(self):
        for i in self.listbox.curselection():
            self.selected.add(self.items[i])
        return self.selected
