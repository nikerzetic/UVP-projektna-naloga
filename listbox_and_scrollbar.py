import tkinter as tk


class ListboxAndScrollbar:
    def __init__(self, master, items=[], selection_method=tk.MULTIPLE):
        self.master = master
        self.items = items
        self.selected = set()
        self.selection_method = selection_method
        self.listbox = tk.Listbox(self.master, selectmode=self.selection_method)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self.master)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        for item in self.items:
            self.listbox.insert(tk.END, item)

        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

    def refresh_listbox(self):
        self.listbox.destroy()

        self.listbox = tk.Listbox(self.master, selectmode=self.selection_method)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        for item in self.items:
            self.listbox.insert(tk.END, item)

    def select(self):
        for i in self.listbox.curselection():
            self.selected.add(self.items[i])
        return self.selected
