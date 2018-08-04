import tkinter as tk
import model
import listbox_and_scrollbar as las
import new_box_window as nbw
import new_note_window as nnw
import move_note_window as mnw
import confirm_window as cw
import ctypes

# Window constants
user32 = ctypes.windll.user32
WINDOW_HEIGHT = user32.GetSystemMetrics(1) - 200
WINDOW_WIDTH = user32.GetSystemMetrics(0) - 100
WINDOW_X = 20
WINDOW_Y = 20

# Padding constants
OUTER_PADDING = 10
INNER_PADDING = 5


# Right frame constants
LEFT_FRAME_HEIGHT = WINDOW_HEIGHT - 2 * OUTER_PADDING
LEFT_FRAME_WIDTH = 0.20 * (WINDOW_WIDTH - 6 * OUTER_PADDING)

# Middle frame constants
MIDDLE_FRAME_HEIGHT = WINDOW_HEIGHT - 2 * OUTER_PADDING
MIDDLE_FRAME_WIDTH = 0.70 * (WINDOW_WIDTH - 6 * OUTER_PADDING)

# Right frame constants
RIGHT_FRAME_HEIGHT = WINDOW_HEIGHT - 2 * OUTER_PADDING
RIGHT_FRAME_WIDTH = 0.10 * (WINDOW_WIDTH - 6 * OUTER_PADDING)


class App:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Spominske škatle')
        self.root.configure(bg='gray')
        self.root.geometry('%dx%d+%d+%d' % (WINDOW_WIDTH + 3 * OUTER_PADDING, WINDOW_HEIGHT + OUTER_PADDING, WINDOW_X, WINDOW_Y))

        self.main = model.Main()

    # Menu

        main_menu = tk.Menu(self.root)
        self.root.config(menu=main_menu)

        menu_boxes = tk.Menu(main_menu)
        main_menu.add_cascade(label='Škatle', menu=menu_boxes)
        menu_notes = tk.Menu(main_menu)
        main_menu.add_cascade(label='Listki', menu=menu_notes)
        menu_test = tk.Menu(main_menu)
        main_menu.add_cascade(label='Test', menu=menu_test)

        menu_boxes.add_command(label='Nova škatla', command=self.ui_new_box)
        menu_boxes.add_command(label='Izbriši škatlo', command=self.ui_delete_box)  # add confirmation before deleting boxes

        menu_notes.add_command(label='Nov listek')
        menu_notes.add_command(label='Izbriši listke')
        menu_notes.add_command(label='Premakni listke')

        menu_test.add_command(label='What does this do', command=self.what_does_this_do)

    # Left Frame and Content
        self.left_frame = tk.Frame(self.root, height=LEFT_FRAME_HEIGHT, width=LEFT_FRAME_WIDTH)
        self.left_frame.grid(row=0, column=0, padx=OUTER_PADDING, pady=OUTER_PADDING, ipadx=INNER_PADDING, ipady=INNER_PADDING)
        self.left_frame.propagate(False)

        self.left_frame_title = tk.Label(self.left_frame, text='Škatle')
        self.left_frame_title.pack(side=tk.TOP)

        self.left_frame_listbox_and_scrollbar = las.ListboxAndScrollbar(self.left_frame, self.main.boxes, tk.SINGLE)

    # Middle Frame and Content
        self.middle_frame = tk.Frame(self.root, height=MIDDLE_FRAME_HEIGHT, width=MIDDLE_FRAME_WIDTH)
        self.middle_frame.grid(row=0, column=1, padx=OUTER_PADDING, pady=OUTER_PADDING, ipadx=INNER_PADDING, ipady=INNER_PADDING)
        self.middle_frame.propagate(False)

        self.middle_frame_title = tk.Label(self.middle_frame, text='Listki')
        self.middle_frame_title.pack(side=tk.TOP)

        self.middle_frame_listbox_and_scrollbar = las.ListboxAndScrollbar(self.middle_frame, self.main.notes)

    # Right Frame and Content
        self.right_frame = tk.Frame(self.root, height=RIGHT_FRAME_HEIGHT, width=RIGHT_FRAME_WIDTH)
        self.right_frame.grid(row=0, column=2, padx=OUTER_PADDING, pady=OUTER_PADDING, ipadx=INNER_PADDING, ipady=INNER_PADDING)
        self.right_frame.propagate(False)

        self.button_box_label = tk.Label(self.right_frame, text='Škatle', bg='silver')
        self.button_box_label.pack(fill=tk.X)

        self.button_new_box = tk.Button(self.right_frame, text='Nova škatla', command=self.ui_new_box)
        self.button_new_box.pack(fill=tk.X)

        self.button_delete_box = tk.Button(self.right_frame, text='Izbriši škatlo', command=self.ui_delete_box)
        self.button_delete_box.pack(fill=tk.X)

        self.button_open_box = tk.Button(self.right_frame, text='Odpri škatlo', command=self.ui_open_box)
        self.button_open_box.pack(fill=tk.X)

        self.button_box_label = tk.Label(self.right_frame, text='Listki', bg='silver')
        self.button_box_label.pack(fill=tk.X)

        self.button_new_note = tk.Button(self.right_frame, text='Nov listek', command=self.ui_new_note)
        self.button_new_note.pack(fill=tk.X)

        self.button_edit_note = tk.Button(self.right_frame, text='Uredi listek', command=self.ui_edit_note)
        self.button_edit_note.pack(fill=tk.X)

        self.button_delete_note = tk.Button(self.right_frame, text='Izbriši listke', command=self.ui_delete_notes)
        self.button_delete_note.pack(fill=tk.X)

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
        cw.ConfirmationWindow(self.root, 'Želite izbrisati izbrano škatlo?', self.main.delete_selected_box, self.left_frame_listbox_and_scrollbar.refresh_listbox)

    def ui_open_box(self, selected_box=None):
        if selected_box:
            self.main.selected = selected_box
        else:
            self.ui_select_box()
        self.main.open_box()
        self.left_frame_listbox_and_scrollbar.refresh_listbox()
        self.middle_frame_listbox_and_scrollbar.refresh_listbox()

    def ui_rename_box(self):
        pass

    # Note commands

    def ui_new_note(self):
        nnw.NewNoteWindow(self.root, self.main.boxes)

    def ui_select_notes(self):
        self.main.selected_box.refresh_notes()
        self.main.selected_box.selected = set(self.middle_frame_listbox_and_scrollbar.select())

    def ui_delete_notes(self):
        self.ui_select_notes()
        cw.ConfirmationWindow(self.root, 'Želite izbrisati izbrane listke?', self.main.selected_box.delete_selected, lambda x=self.main.selected_box: self.ui_open_box(x))
    
    def ui_edit_note(self):
        pass

    def ui_move_notes(self):
        self.ui_select_notes()
        mnw.MoveNoteWindow(self.root, self.main.selected_box, self.main.boxes, self.ui_open_box)

    def what_does_this_do(self):
        self.ui_select_notes()


App()
