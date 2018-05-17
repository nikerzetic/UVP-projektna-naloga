class YetNameless:

    def __init__(self, main_file):
        self.boxes = []
        self.main_file = main_file

    def refresh_boxes(self):
        dat = open(self.main_file, 'r')
        for line in dat:
            self.boxes.append(line.strip('\n'))
        dat.close()

    def refresh_notes(self):
        pass

    def open_box(self):
        pass

    def new_box(self):
        pass

    def delete_box(self):
        pass

    def add_note(self):
        pass

    def delete_note(self):
        pass

    def move_note(self):
        pass

    def save_changes(self):
        pass
