import tkinter as tk
import model_2
import constants as cst
import frames as frs
import listbox_and_scrollbar as las
import new_box_window as nbw
import new_note_window as nnw
import ctypes


class App:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Spominske škatle')
        self.root.configure(bg='gray')

        self.main = model_2.Main()

        self.notes = []
        self.commands = [None, self.ui_delete_box, None, None, None, None, None]

        self.left_frame = frs.LeftFrame(self.root, cst.LEFT_FRAME_HEIGHT, cst.LEFT_FRAME_WIDTH, cst.OUTER_PADDING, cst.INNER_PADDING, self.main.boxes)
        self.middle_frame = frs.MiddleFrame(self.root, cst.MIDDLE_FRAME_HEIGHT, cst.MIDDLE_FRAME_WIDTH, cst.OUTER_PADDING, cst.INNER_PADDING, self.notes)
        self.right_frame = frs.RightFrame(self.root, cst.RIGHT_FRAME_HEIGHT, cst.RIGHT_FRAME_WIDTH, cst.OUTER_PADDING, cst.INNER_PADDING, self.commands)

        self.selected_box = None
        self.selected_notes = set()

        self.root.mainloop()

    # Box methods

    def ui_select_box(self):
        self.selected_box = next(iter(self.left_frame.listbox_and_scrollbar.select()))

    def ui_new_box(self):
        pass

    def ui_open_box(self):
        pass

    def ui_rename_box(self):
        pass

    def ui_delete_box(self):
        self.ui_select_box()
        self.main.delete_box(self.selected_box)
        self.left_frame.listbox_and_scrollbar.refresh_listbox()

    # Note methods

    def ui_select_notes(self):
        self.selected_notes = self.middle_frame.frame_listbox_and_scrollbar.select()

    def ui_new_note(self):
        pass

    def ui_edit_note(self):
        pass

    def ui_move_note(self):
        pass

    def ui_delete_notes(self):
        pass


App()
