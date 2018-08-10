import tkinter as tk
import model
import listbox_and_scrollbar as las
import new_box_window as nbw
import new_note_window as nnw
import move_note_window as mnw
import rename_box_window as rbw
import edit_note_window as enw
import tkinter.messagebox
import ctypes

# Window constants
user32 = ctypes.windll.user32
WINDOW_HEIGHT = user32.GetSystemMetrics(1) - 130
WINDOW_WIDTH = user32.GetSystemMetrics(0) // 2
WINDOW_X = user32.GetSystemMetrics(0) // 4
WINDOW_Y = 20


class App:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Spominske škatle')
        self.root.configure(bg='gray')
        self.root.geometry('%dx%d+%d+%d' % (WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_X, WINDOW_Y))

        self.main = model.Main()

    # Left Frame and Content
        self.left_frame = tk.Frame(self.root)
        self.left_frame.pack(fill=tk.BOTH, side=tk.LEFT)

        self.left_frame_title = tk.Label(self.left_frame, text='Škatle')
        self.left_frame_title.pack(side=tk.TOP)

        self.left_frame_listbox_and_scrollbar = las.ListboxAndScrollbar(self.left_frame, self.main.boxes, tk.SINGLE)

    # Middle Frame and Content
        self.middle_frame = tk.Frame(self.root)
        self.middle_frame.pack(fill=tk.BOTH, expand=tk.YES, side=tk.LEFT)

        self.middle_frame_title = tk.Label(self.middle_frame, text='Listki')
        self.middle_frame_title.pack(side=tk.TOP)

        self.middle_frame_listbox_and_scrollbar = las.ListboxAndScrollbar(self.middle_frame, self.main.notes)

    # Right Frame and Content
        self.right_frame = tk.Frame(self.root)
        self.right_frame.pack(fill=tk.BOTH, side=tk.RIGHT)

        self.button_box_label_boxes = tk.Label(self.right_frame, text='Škatle', bg='silver')
        self.button_box_label_boxes.pack(fill=tk.X)

        self.button_new_box = tk.Button(self.right_frame, text='Nova škatla', command=self.ui_new_box)
        self.button_new_box.pack(fill=tk.X)

        self.button_delete_box = tk.Button(self.right_frame, text='Izbriši škatlo', command=self.ui_delete_box)
        self.button_delete_box.pack(fill=tk.X)

        self.button_rename_box = tk.Button(self.right_frame, text='Preimenuj škatlo', command=self.ui_rename_box)
        self.button_rename_box.pack(fill=tk.X)

        self.button_open_box = tk.Button(self.right_frame, text='Odpri škatlo', command=self.ui_open_box)
        self.button_open_box.pack(fill=tk.X)

        self.button_box_label_notes = tk.Label(self.right_frame, text='Listki', bg='silver')
        self.button_box_label_notes.pack(fill=tk.X)

        self.button_new_note = tk.Button(self.right_frame, text='Nov listek', command=self.ui_new_note)
        self.button_new_note.pack(fill=tk.X)

        self.button_delete_note = tk.Button(self.right_frame, text='Izbriši listke', command=self.ui_delete_notes)
        self.button_delete_note.pack(fill=tk.X)

        self.button_edit_note = tk.Button(self.right_frame, text='Uredi listek', command=self.ui_edit_note)
        self.button_edit_note.pack(fill=tk.X)

        self.button_move_note = tk.Button(self.right_frame, text='Premakni listke', command=self.ui_move_notes)
        self.button_move_note.pack(fill=tk.X)

        self.root.mainloop()

    # Box commands
    def ui_new_box(self):
        nbw.NewBoxWindow(self.root, self.main.new_box, self.left_frame_listbox_and_scrollbar.refresh_listbox)

    def ui_select_box(self):
        self.main.selected_box = self.left_frame_listbox_and_scrollbar.select()[0]

    def ui_delete_box(self):
        self.ui_select_box()
        result = tk.messagebox.askokcancel('Potrdi izbiro', 'Želite izbrisati izbrano škatlo?')
        if result:
            self.main.delete_selected_box()
            self.left_frame_listbox_and_scrollbar.refresh_listbox()

    def ui_open_box(self, selected_box=None):
        if selected_box:
            self.main.selected = selected_box
        else:
            self.ui_select_box()
        self.main.open_box()
        self.left_frame_listbox_and_scrollbar.refresh_listbox()
        self.middle_frame_listbox_and_scrollbar.refresh_listbox()

    def ui_rename_box(self):
        self.ui_select_box()
        rbw.RenameBoxWindow(self.root, self.main.rename_box, self.left_frame_listbox_and_scrollbar.refresh_listbox)

    # Note commands

    def ui_new_note(self):
        nnw.NewNoteWindow(self.root, self.main.boxes, self.ui_open_box)

    def ui_select_notes(self):
        self.main.selected_box.refresh_notes()
        self.main.selected_box.selected = set(self.middle_frame_listbox_and_scrollbar.select())

    def ui_delete_notes(self):
        self.ui_select_notes()
        result = tk.messagebox.askokcancel('Potrdi izbiro', 'Želite izbrisati izbrane listke?')
        if result:
            self.main.selected_box.delete_selected()
            self.ui_open_box(self.main.selected_box)

    def ui_edit_note(self):
        self.ui_select_notes()
        if len(self.main.selected_box.selected) == 1:
            enw.EditNoteWindow(self.root, self.main.selected_box, min(self.main.selected_box.selected), self.ui_open_box)
        else:
            tk.messagebox.showerror('Opozorilo', 'Izbrano neveljavno število listkov')

    def ui_move_notes(self):
        self.ui_select_notes()
        mnw.MoveNoteWindow(self.root, self.main.selected_box, self.main.boxes, self.ui_open_box)

    def what_does_this_do(self):
        pass
