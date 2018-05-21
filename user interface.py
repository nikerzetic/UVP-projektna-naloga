import tkinter as tk
import model

# Window constants
WINDOW_HEIGHT = 720
WINDOW_WIDTH = 1280

# Padding constants
OUTER_PADDING = 10
INNER_PADDING = 5

# Right frame constants
LEFT_FRAME_HEIGHT = WINDOW_HEIGHT - 2 * OUTER_PADDING
LEFT_FRAME_WIDTH = 0.30 * (WINDOW_WIDTH - 6 * OUTER_PADDING)

# Middle frame constants
MIDDLE_FRAME_HEIGHT = WINDOW_HEIGHT - 2 * OUTER_PADDING
MIDDLE_FRAME_WIDTH = 0.60 * (WINDOW_WIDTH - 6 * OUTER_PADDING)

# Right frame constants
RIGHT_FRAME_HEIGHT = WINDOW_HEIGHT - 2 * OUTER_PADDING
RIGHT_FRAME_WIDTH = 0.30 * (WINDOW_WIDTH - 6 * OUTER_PADDING)


class App:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Spominske škatle')
        self.root.configure(bg='gray')

        self.mainframe = model.Mainframe()

    # Menu

        main_menu = tk.Menu(self.root)
        self.root.config(menu=main_menu)

        menu_boxes = tk.Menu(main_menu)
        main_menu.add_cascade(label='Škatle', menu=menu_boxes)
        menu_notes = tk.Menu(main_menu)
        main_menu.add_cascade(label='Listki', menu=menu_notes)
        menu_test = tk.Menu(main_menu)
        main_menu.add_cascade(label='Test', menu=menu_test)

        menu_boxes.add_command(label='Nova škatla', command=self.ui_new_box)  # refresh boxes - better define new commands that do both
        menu_boxes.add_command(label='Izbriši škatle', command=self.ui_delete_box)  # add confirmation before deleting boxes

        menu_test.add_command(label='What does this do', command=self.what_does_this_do)

    # Left Frame and Content
        self.left_frame = tk.Frame(self.root, height=LEFT_FRAME_HEIGHT, width=LEFT_FRAME_WIDTH)
        self.left_frame.grid(row=0, column=0, padx=OUTER_PADDING, pady=OUTER_PADDING, ipadx=INNER_PADDING, ipady=INNER_PADDING)
        self.left_frame.propagate(False)

        self.left_frame_title = tk.Label(self.left_frame, text='Škatle')
        self.left_frame_title.pack(side=tk.TOP)

        self.ui_pack_left_frame_listbox_and_scrollbar()

    # Middle Frame and Content
        self.middle_frame = tk.Frame(self.root, height=MIDDLE_FRAME_HEIGHT, width=MIDDLE_FRAME_WIDTH)
        self.middle_frame.grid(row=0, column=1, padx=OUTER_PADDING, pady=OUTER_PADDING, ipadx=INNER_PADDING, ipady=INNER_PADDING)
        self.middle_frame.propagate(False)

        self.middle_frame_title = tk.Label(self.middle_frame, text='Listki')
        self.middle_frame_title.pack(side=tk.TOP)

        self.ui_pack_middle_frame_listbox_and_scrollbar()

    # Right Frame and Content
        self.right_frame = tk.Frame(self.root, height=RIGHT_FRAME_HEIGHT, width=RIGHT_FRAME_WIDTH)
        self.right_frame.grid(row=0, column=2, padx=OUTER_PADDING, pady=OUTER_PADDING, ipadx=INNER_PADDING, ipady=INNER_PADDING)
        self.right_frame.propagate(False)

        self.right_frame_text = tk.Text(self.right_frame)
        self.right_frame_text.pack(fill=tk.Y, expand=True)

        self.right_frame_lower_frame = tk.Frame(self.right_frame)
        self.right_frame_lower_frame.pack(fill=tk.X)

        self.tk_variable = tk.StringVar(self.root)
        self.ui_pack_right_frame_option_menu()

        self.root.mainloop()

    def ui_pack_left_frame_listbox_and_scrollbar(self):
        self.left_frame_listbox = tk.Listbox(self.left_frame, selectmode=tk.MULTIPLE)  # worth sacrificing this offense for cleaner code?
        self.left_frame_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.left_frame_scrollbar = tk.Scrollbar(self.left_frame)
        self.left_frame_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        for box in self.mainframe.boxes:
            self.left_frame_listbox.insert(tk.END, box)

        self.left_frame_listbox.config(yscrollcommand=self.left_frame_scrollbar.set)
        self.left_frame_scrollbar.config(command=self.left_frame_listbox.yview)

    def ui_pack_middle_frame_listbox_and_scrollbar(self):
        self.middle_frame_listbox = tk.Listbox(self.middle_frame, selectmode=tk.MULTIPLE)
        self.middle_frame_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.middle_frame_scrollbar = tk.Scrollbar(self.middle_frame)
        self.middle_frame_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        for i in range(100):
            self.middle_frame_listbox.insert(tk.END, i * str('AA'))

        self.middle_frame_listbox.config(yscrollcommand=self.middle_frame_scrollbar.set)
        self.middle_frame_scrollbar.config(command=self.middle_frame_listbox.yview)

    def ui_pack_right_frame_option_menu(self):
        self.right_frame_option_menu = tk.OptionMenu(self.right_frame, self.tk_variable, *self.mainframe.boxes)
        self.right_frame_option_menu.pack(fill=tk.X)

    def ui_refresh(self):
        self.ui_refresh_left_frame_listbox_and_scrollbar()
        self.ui_refresh_right_frame_option_menu()

    def ui_refresh_right_frame_option_menu(self):  # when all is combined in one ui_refresh method, ui_refresh mainframe boxes
        self.right_frame_option_menu.destroy()
        self.ui_pack_right_frame_option_menu()

    def ui_refresh_left_frame_listbox_and_scrollbar(self):
        self.left_frame_listbox.destroy()
        self.left_frame_scrollbar.destroy()
        self.ui_pack_left_frame_listbox_and_scrollbar()

    def ui_new_box(self):  # ask for name in separate window and change model.py
        self.mainframe.new_box()
        self.ui_refresh()

    def ui_select_box(self):
        for i in self.left_frame_listbox.curselection():
            self.mainframe.selected.add(model.Box(self.left_frame_listbox.get(i) + '.txt'))

    def ui_delete_box(self):
        self.ui_select_box()
        self.mainframe.delete_selected_boxes()
        self.ui_refresh()

    def what_does_this_do(self):
        print(self.left_frame_listbox.curselection())
        for i in self.left_frame_listbox.curselection():
            print(self.left_frame_listbox.get(i))

App()
