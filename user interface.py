import tkinter as tk
import model
import listbox_and_scrollbar as las
import new_box_window as nbw
import new_note_window as nnw

# Window constants
WINDOW_HEIGHT = 720
WINDOW_WIDTH = 1280

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

        self.mainframe = model.Mainframe()
        self.notes = []

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
        menu_boxes.add_command(label='Izbriši škatle', command=self.ui_delete_box)  # add confirmation before deleting boxes

        menu_notes.add_command(label='Nov listek')
        menu_notes.add_command(label='Izbriši listek')
        menu_notes.add_command(label='Premesti listek')

        menu_test.add_command(label='What does this do', command=self.what_does_this_do)

    # Left Frame and Content
        self.left_frame = tk.Frame(self.root, height=LEFT_FRAME_HEIGHT, width=LEFT_FRAME_WIDTH)
        self.left_frame.grid(row=0, column=0, padx=OUTER_PADDING, pady=OUTER_PADDING, ipadx=INNER_PADDING, ipady=INNER_PADDING)
        self.left_frame.propagate(False)

        self.left_frame_title = tk.Label(self.left_frame, text='Škatle')
        self.left_frame_title.pack(side=tk.TOP)

        self.left_frame_listbox_and_scrollbar = las.ListboxAndScrollbar(self.left_frame, self.mainframe.boxes)

    # Middle Frame and Content
        self.middle_frame = tk.Frame(self.root, height=MIDDLE_FRAME_HEIGHT, width=MIDDLE_FRAME_WIDTH)
        self.middle_frame.grid(row=0, column=1, padx=OUTER_PADDING, pady=OUTER_PADDING, ipadx=INNER_PADDING, ipady=INNER_PADDING)
        self.middle_frame.propagate(False)

        self.middle_frame_title = tk.Label(self.middle_frame, text='Listki')
        self.middle_frame_title.pack(side=tk.TOP)

        self.middle_frame_listbox_and_scrollbar = las.ListboxAndScrollbar(self.middle_frame, self.notes)

    # Right Frame and Content
        self.right_frame = tk.Frame(self.root, height=RIGHT_FRAME_HEIGHT, width=RIGHT_FRAME_WIDTH)
        self.right_frame.grid(row=0, column=2, padx=OUTER_PADDING, pady=OUTER_PADDING, ipadx=INNER_PADDING, ipady=INNER_PADDING)
        self.right_frame.propagate(False)

        self.button_box_label = tk.Label(self.right_frame, text='Škatle', bg='silver')
        self.button_box_label.pack(fill=tk.X)

        self.button_new_box = tk.Button(self.right_frame, text='Nova škatla', command=self.ui_new_box)
        self.button_new_box.pack(fill=tk.X)

        self.button_delete_box = tk.Button(self.right_frame, text='Izbriši škatle', command=self.ui_delete_box)
        self.button_delete_box.pack(fill=tk.X)

        self.button_open_box = tk.Button(self.right_frame, text='Odpri škatle')
        self.button_open_box.pack(fill=tk.X)

        self.button_box_label = tk.Label(self.right_frame, text='Listki', bg='silver')
        self.button_box_label.pack(fill=tk.X)

        self.button_new_note = tk.Button(self.right_frame, text='Nov listek', command=self.ui_new_note)
        self.button_new_note.pack(fill=tk.X)

        self.button_delete_note = tk.Button(self.right_frame, text='Izbriši listek')
        self.button_delete_note.pack(fill=tk.X)

        self.button_move_note = tk.Button(self.right_frame, text='Premakni listek')
        self.button_move_note.pack(fill=tk.X)

        # self.right_frame_text = tk.Text(self.right_frame)
        # self.right_frame_text.pack(fill=tk.Y, expand=True)

        #  self.right_frame_lower_frame = tk.Frame(self.right_frame)
        # self.right_frame_lower_frame.pack(fill=tk.X)

        #  self.tk_variable = tk.StringVar(self.root)
        #  self.ui_pack_right_frame_option_menu()

        self.root.mainloop()

    #  def ui_pack_right_frame_option_menu(self):
        #  self.right_frame_option_menu = tk.OptionMenu(self.right_frame, self.tk_variable, *self.mainframe.boxes)
        #  self.right_frame_option_menu.pack(fill=tk.X)

    #  def ui_refresh_right_frame_option_menu(self):  # when all is combined in one ui_refresh method, ui_refresh mainframe boxes
        #  self.right_frame_option_menu.destroy()
        #  self.ui_pack_right_frame_option_menu()

    def ui_new_box(self):  # find out why the listbox isn't refreshed when this method is called
        nbw.NewBoxWindow(self.root, self.mainframe.new_box)
        self.left_frame_listbox_and_scrollbar.refresh_listbox()

    def ui_select_boxes(self):
        self.mainframe.selected |= self.left_frame_listbox_and_scrollbar.select()

    def ui_delete_box(self):
        self.ui_select_boxes()
        self.mainframe.delete_selected_boxes()
        self.left_frame_listbox_and_scrollbar.refresh_listbox()

    def ui_open_box(self):
        for note in self.mainframe.selected:
            self.notes.append(note.text)
        self.middle_frame_listbox_and_scrollbar.refresh_listbox()

    def ui_new_note(self):
        nnw.NewNoteWindow(self.root, self.mainframe.boxes, model.box_add_note)
        self.middle_frame_listbox_and_scrollbar.refresh_listbox()

    def what_does_this_do(self):
        self.left_frame_listbox_and_scrollbar.refresh_listbox()


App()
