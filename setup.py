import tkinter as tk
import listbox_and_scrollbar as las


class LeftFrame:

    def __init__(self, master, h, w, op, ip, items=[]):
        self.left_frame = tk.Frame(master, height=h, width=w)
        self.left_frame.grid(row=0, column=0, padx=op, pady=op, ipadx=ip, ipady=ip)
        self.left_frame.propagate(False)

        self.left_frame_title = tk.Label(self.left_frame, text='Škatle')
        self.left_frame_title.pack(side=tk.TOP)

        self.left_frame_listbox_and_scrollbar = las.ListboxAndScrollbar(self.left_frame, items, tk.SINGLE)

    def refresh(self):
        self.left_frame_listbox_and_scrollbar.refresh_listbox()


class MiddleFrame:

    def __init__(self, master, h, w, op, ip, items=[]):
        self.middle_frame = tk.Frame(master, height=h, width=w)
        self.middle_frame.grid(row=0, column=1, padx=op, pady=op, ipadx=ip, ipady=ip)
        self.middle_frame.propagate(False)

        self.middle_frame_title = tk.Label(self.middle_frame, text='Listki')
        self.middle_frame_title.pack(side=tk.TOP)

        self.middle_frame_listbox_and_scrollbar = las.ListboxAndScrollbar(self.middle_frame, items)


class RightFrame:

    def __init__(self, master, h, w, op, ip, commands=[]):
        self.right_frame = tk.Frame(master, height=h, width=w)
        self.right_frame.grid(row=0, column=2, padx=op, pady=op, ipadx=ip, ipady=ip)
        self.right_frame.propagate(False)

        self.button_box_label = tk.Label(self.right_frame, text='Škatle', bg='silver')
        self.button_box_label.pack(fill=tk.X)

        self.button_new_box = tk.Button(self.right_frame, text='Nova škatla', command=commands[0])
        self.button_new_box.pack(fill=tk.X)

        self.button_delete_box = tk.Button(self.right_frame, text='Izbriši škatlo', command=commands[1])
        self.button_delete_box.pack(fill=tk.X)

        self.button_open_box = tk.Button(self.right_frame, text='Odpri škatlo', command=commands[2])
        self.button_open_box.pack(fill=tk.X)

        self.button_box_label = tk.Label(self.right_frame, text='Listki', bg='silver')
        self.button_box_label.pack(fill=tk.X)

        self.button_new_note = tk.Button(self.right_frame, text='Nov listek', command=commands[3])
        self.button_new_note.pack(fill=tk.X)

        self.button_edit_note = tk.Button(self.right_frame, text='Uredi listek', command=commands[4])
        self.button_edit_note.pack(fill=tk.X)

        self.button_delete_note = tk.Button(self.right_frame, text='Izbriši listke', command=commands[5])
        self.button_delete_note.pack(fill=tk.X)

        self.button_move_note = tk.Button(self.right_frame, text='Premakni listke', command=commands[6])
        self.button_move_note.pack(fill=tk.X)
