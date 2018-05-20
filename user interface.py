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
        root = tk.Tk()
        root.title('Spominske škatle')
        root.configure(bg='gray')

        # Left Frame and Content
        left_frame = tk.Frame(root, height=LEFT_FRAME_HEIGHT, width=LEFT_FRAME_WIDTH)
        left_frame.grid(row=0, column=0, padx=OUTER_PADDING, pady=OUTER_PADDING, ipadx=INNER_PADDING, ipady=INNER_PADDING)
        left_frame.propagate(False)

        left_frame_listbox = tk.Listbox(left_frame)
        left_frame_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        left_frame_scrollbar = tk.Scrollbar(left_frame)
        left_frame_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        for i in range(100):
            left_frame_listbox.insert(tk.END, i)

        left_frame_listbox.config(yscrollcommand=left_frame_scrollbar.set)
        left_frame_scrollbar.config(command=left_frame_listbox.yview)

        # Middle Frame and Content
        middle_frame = tk.Frame(root, height=MIDDLE_FRAME_HEIGHT, width=MIDDLE_FRAME_WIDTH)
        middle_frame.grid(row=0, column=1, padx=OUTER_PADDING, pady=OUTER_PADDING, ipadx=INNER_PADDING, ipady=INNER_PADDING)
        middle_frame.propagate(False)

        middle_frame_listbox = tk.Listbox(middle_frame)
        middle_frame_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        middle_frame_scrollbar = tk.Scrollbar(middle_frame)
        middle_frame_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Right Frame and Content
        right_frame = tk.Frame(root, height=RIGHT_FRAME_HEIGHT, width=RIGHT_FRAME_WIDTH)
        right_frame.grid(row=0, column=2, padx=OUTER_PADDING, pady=OUTER_PADDING, ipadx=INNER_PADDING, ipady=INNER_PADDING)

        root.mainloop()

    def refresh_boxes(self):
        pass

App()
