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

    # Left Frame and Content
        self.left_frame = tk.Frame(self.root, height=LEFT_FRAME_HEIGHT, width=LEFT_FRAME_WIDTH)
        self.left_frame.grid(row=0, column=0, padx=OUTER_PADDING, pady=OUTER_PADDING, ipadx=INNER_PADDING, ipady=INNER_PADDING)
        self.left_frame.propagate(False)

        self.left_frame_title = tk.Label(self.left_frame, text='Škatle')
        self.left_frame_title.pack(side=tk.TOP)

        self.left_frame_listbox = tk.Listbox(self.left_frame, selectmode=tk.MULTIPLE)
        self.left_frame_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.left_frame_scrollbar = tk.Scrollbar(self.left_frame)
        self.left_frame_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        for box in self.mainframe.boxes:
            self.left_frame_listbox.insert(tk.END, box)

        self.left_frame_listbox.config(yscrollcommand=self.left_frame_scrollbar.set)
        self.left_frame_scrollbar.config(command=self.left_frame_listbox.yview)

    # Middle Frame and Content
        self.middle_frame = tk.Frame(self.root, height=MIDDLE_FRAME_HEIGHT, width=MIDDLE_FRAME_WIDTH)
        self.middle_frame.grid(row=0, column=1, padx=OUTER_PADDING, pady=OUTER_PADDING, ipadx=INNER_PADDING, ipady=INNER_PADDING)
        self.middle_frame.propagate(False)

        self.middle_frame_title = tk.Label(self.middle_frame, text='Listki')
        self.middle_frame_title.pack(side=tk.TOP)

        self.middle_frame_listbox = tk.Listbox(self.middle_frame, selectmode=tk.MULTIPLE)
        self.middle_frame_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.middle_frame_scrollbar = tk.Scrollbar(self.middle_frame)
        self.middle_frame_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        for i in range(100):
            self.middle_frame_listbox.insert(tk.END, i * str('AA'))

        self.middle_frame_listbox.config(yscrollcommand=self.middle_frame_scrollbar.set)
        self.middle_frame_scrollbar.config(command=self.middle_frame_listbox.yview)

    # Right Frame and Content
        self.right_frame = tk.Frame(self.root, height=RIGHT_FRAME_HEIGHT, width=RIGHT_FRAME_WIDTH)
        self.right_frame.grid(row=0, column=2, padx=OUTER_PADDING, pady=OUTER_PADDING, ipadx=INNER_PADDING, ipady=INNER_PADDING)
        self.right_frame.propagate(False)

        self.right_frame_text = tk.Text(self.right_frame)
        self.right_frame_text.pack(fill=tk.Y, expand=True)

        self.right_frame_lower_frame = tk.Frame(self.right_frame)
        self.right_frame_lower_frame.pack(fill=tk.X)

        self.tk_variable = tk.StringVar(self.root)
        self.right_frame_option_menu = tk.OptionMenu(self.right_frame_lower_frame, self.tk_variable, *self.mainframe.boxes)
        self.right_frame_option_menu.pack(fill=tk.X)

        self.root.mainloop()

    def refresh_boxes(self):
        pass

    def refresh_right_frame_option_menu(self):  # when all is combined in one refresh method, refresh mainframe boxes
        self.right_frame_option_menu.destroy()
        self.right_frame_option_menu = tk.OptionMenu(self.self.right_frame, self.tk_variable, *self.mainframe.boxes)
        self.right_frame_option_menu.pack(fill=tk.X)

    def refresh_left_frame_listbox_and_scrollbar(self):
        self.left_frame_listbox.destroy()
        self.left_frame_scrollbar.destroy()

        self.left_frame_listbox = tk.Listbox(self.left_frame, selectmode=tk.MULTIPLE)
        self.left_frame_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.left_frame_scrollbar = tk.Scrollbar(self.left_frame)
        self.left_frame_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        for box in self.mainframe.boxes:
            self.left_frame_listbox.insert(tk.END, box)

        self.left_frame_listbox.config(yscrollcommand=self.left_frame_scrollbar.set)
        self.left_frame_scrollbar.config(command=self.left_frame_listbox.yview)


App()
