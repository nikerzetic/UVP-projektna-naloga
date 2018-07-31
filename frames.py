import tkinter as tk
import listbox_and_scrollbar as las


class LeftFrame:

    def __init__(self, master, h, w, op, ip, items=[]):
        self.frame = tk.Frame(master, height=h, width=w)
        self.frame.grid(row=0, column=0, padx=op, pady=op, ipadx=ip, ipady=ip)
        self.frame.propagate(False)

        self.frame_title = tk.Label(self.frame, text='Škatle')
        self.frame_title.pack(side=tk.TOP)

        self.listbox_and_scrollbar = las.ListboxAndScrollbar(self.frame, items, tk.SINGLE)

    def refresh(self):
        self.listbox_and_scrollbar.refresh_listbox()


class MiddleFrame:

    def __init__(self, master, h, w, op, ip, items=[]):
        self.frame = tk.Frame(master, height=h, width=w)
        self.frame.grid(row=0, column=1, padx=op, pady=op, ipadx=ip, ipady=ip)
        self.frame.propagate(False)

        self.frame_title = tk.Label(self.frame, text='Listki')
        self.frame_title.pack(side=tk.TOP)

        self.frame_listbox_and_scrollbar = las.ListboxAndScrollbar(self.frame, items)


class RightFrame:

    def __init__(self, master, h, w, op, ip, commands=[]):
        self.frame = tk.Frame(master, height=h, width=w)
        self.frame.grid(row=0, column=2, padx=op, pady=op, ipadx=ip, ipady=ip)
        self.frame.propagate(False)

        self.button_box_label = tk.Label(self.frame, text='Škatle', bg='silver')
        self.button_box_label.pack(fill=tk.X)

        self.button_new_box = tk.Button(self.frame, text='Nova škatla', command=commands[0])
        self.button_new_box.pack(fill=tk.X)

        self.button_delete_box = tk.Button(self.frame, text='Izbriši škatlo', command=commands[1])
        self.button_delete_box.pack(fill=tk.X)

        self.button_open_box = tk.Button(self.frame, text='Odpri škatlo', command=commands[2])
        self.button_open_box.pack(fill=tk.X)

        self.button_box_label = tk.Label(self.frame, text='Listki', bg='silver')
        self.button_box_label.pack(fill=tk.X)

        self.button_new_note = tk.Button(self.frame, text='Nov listek', command=commands[3])
        self.button_new_note.pack(fill=tk.X)

        self.button_edit_note = tk.Button(self.frame, text='Uredi listek', command=commands[4])
        self.button_edit_note.pack(fill=tk.X)

        self.button_delete_note = tk.Button(self.frame, text='Izbriši listke', command=commands[5])
        self.button_delete_note.pack(fill=tk.X)

        self.button_move_note = tk.Button(self.frame, text='Premakni listke', command=commands[6])
        self.button_move_note.pack(fill=tk.X)
