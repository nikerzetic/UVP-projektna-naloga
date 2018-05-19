import tkinter as tk
import model

# Constants
WINDOW_HEIGHT = 800
WINDOW_WIDTH = 1400

OUTER_PADDING = 10
INNER_PADDING = 5

LEFT_FRAME_HEIGHT = WINDOW_HEIGHT - 2 * OUTER_PADDING
LEFT_FRAME_WIDTH = 0.30 * (WINDOW_WIDTH - 6 * OUTER_PADDING)

MIDDLE_FRAME_HEIGHT = WINDOW_HEIGHT - 2 * OUTER_PADDING
MIDDLE_FRAME_WIDTH = 0.60 * (WINDOW_WIDTH - 6 * OUTER_PADDING)

RIGHT_FRAME_HEIGHT = WINDOW_HEIGHT - 2 * OUTER_PADDING
RIGHT_FRAME_WIDTH = 0.30 * (WINDOW_WIDTH - 6 * OUTER_PADDING)


class App:

    def __init__(self):
        root = tk.Tk()
        root.title('Spominske škatle')
        root.configure(bg='gray')

        # Left Frame and Content
        left_frame = tk.Frame(root, width=LEFT_FRAME_WIDTH, height=LEFT_FRAME_HEIGHT)
        left_frame.grid(row=0, column=0, padx=OUTER_PADDING, pady=OUTER_PADDING, ipadx=INNER_PADDING, ipady=INNER_PADDING)

        left_frame_scrollbar = tk.Scrollbar(left_frame, bg='gray')
        # left_frame_scrollbar.pack()

        # Middle Frame and Content
        middle_frame = tk.Frame(root, width=MIDDLE_FRAME_WIDTH, height=MIDDLE_FRAME_HEIGHT)
        middle_frame.grid(row=0, column=1, padx=OUTER_PADDING, pady=OUTER_PADDING, ipadx=INNER_PADDING, ipady=INNER_PADDING)

        middle_frame_scrollbar = tk.Scrollbar(middle_frame)
        # middle_frame_scrollbar.pack()

        # Right Frame and Content
        right_frame = tk.Frame(root, width=RIGHT_FRAME_WIDTH, height=RIGHT_FRAME_HEIGHT)
        right_frame.grid(row=0, column=2, padx=OUTER_PADDING, pady=OUTER_PADDING, ipadx=INNER_PADDING, ipady=INNER_PADDING)

        root.mainloop()


App()
