import tkinter as tk
import model_2
import constants as cst
import setup as stp
import listbox_and_scrollbar as las
import new_box_window as nbw
import new_note_window as nnw
import ctypes


class App:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Spominske škatle')
        self.root.configure(bg='gray')

        self.commands = [None, None, None, None, None, None, None]

        self.left_frame = stp.LeftFrame(self.root, cst.LEFT_FRAME_HEIGHT, cst.LEFT_FRAME_WIDTH, cst.OUTER_PADDING, cst.INNER_PADDING)
        self.middle_frame = stp.MiddleFrame(self.root, cst.MIDDLE_FRAME_HEIGHT, cst.MIDDLE_FRAME_WIDTH, cst.OUTER_PADDING, cst.INNER_PADDING)
        self.right_frame = stp.RightFrame(self.root, cst.RIGHT_FRAME_HEIGHT, cst.RIGHT_FRAME_WIDTH, cst.OUTER_PADDING, cst.INNER_PADDING, self.commands)

        self.root.mainloop()

    # Box methods

    def ui_select_box(self):
        pass

    def ui_new_box(self):
        pass

    def ui_open_box(self):
        pass

    def ui_rename_box(self):
        pass

    def ui_delete_box(self):
        pass

    # Note methods

    def ui_select_notes(self):
        pass

    def ui_new_note(self):
        pass

    def ui_edit_note(self):
        pass

    def ui_move_note(self):
        pass

    def ui_delete_notes(self):
        pass


App()
