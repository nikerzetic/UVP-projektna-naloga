from os import remove


class Main:

    def __init__(self):
        self.boxes = []
        self.notes = []
        self.selected = set()
        self.selected_notes = set()
        self.main_file = 'boxes_main_file.txt'
        self.refresh_boxes()
        self.position = 0

    def refresh_boxes(self):
        try:
            dat = open(self.main_file, 'r', encoding='UTF-8')
            self.boxes = [Box(line.strip('\n')) for line in dat]
            dat.close()
        except IOError:
            dat = open(self.main_file, 'w', encoding='UTF-8')
            print('Praškatla', file=dat)
            self.boxes.append(Box('Praškatla'))
            dat.close()

    def new_box(self, name):
        box = Box(name)
        self.boxes.append(box)
        self.save_changes()
        box.refresh_notes()

    def delete_selected_boxes(self):
        for box in self.selected:
            try:
                remove(box.address)
            except FileNotFoundError:
                pass
            self.boxes.remove(box)
        self.selected = set()
        self.save_changes()
        self.position = 0

    def save_changes(self):
        dat = open(self.main_file, 'w', encoding='UTF-8')
        for box in self.boxes:
            print(box.name, file=dat)
        dat.close()

    def open_boxes(self):
        self.notes.clear()
        for box in self.selected:
            box.refresh_notes()
            self.notes.extend(box.content)

    # Tools for use trough console

    def add_box_to_selection(self):
        self.selected.add(self.boxes[self.position])

    def remove_box_from_selection(self):
        self.selected.remove(self.boxes[self.position])

    def deselect_all(self):
        self.position = 0
        while len(self.selected) > 0:
            self.remove_box_from_selection()

    def next_box(self):
        if self.position != len(self.boxes)-1:
            self.position += 1
        else:
            self.position = 0

    def previous_box(self):
        if self.position != 0:
            self.position -= 1
        else:
            self.position = len(self.boxes) - 1


class Box:

    def __init__(self, name):
        self.name = name
        self.address = self.name + '.txt'
        self.content = []
        self.selected = set()
        self.position = 0

    def __repr__(self):
        return 'Box("%s")' % self.name

    def __str__(self):
        return self.name

    def refresh_notes(self):
        try:
            dat = open(self.address, 'r', encoding='UTF-8')
            self.content = [line.strip('\n') for line in dat]
        except IOError:
            dat = open(self.address, 'w', encoding='UTF-8')
        dat.close()

    def add_note(self, note):
        self.refresh_notes()
        self.content.append(note)
        self.save_changes()

    def delete_selected(self):
        for note in self.selected:
            self.content.remove(note)
        self.selected = set()
        self.save_changes()

    def save_changes(self):
        dat = open(self.address, 'w', encoding='UTF-8')
        for note in self.content:
            print(note, file=dat)
        dat.close()

    def move_note(self, other):
        for note in self.selected:
            other.content.append(note)
            self.content.remove(note)
            self.selected.discard(note)
        self.save_changes()
        other.save_changes()

    def add_note_to_selection(self):
        self.selected.add(self.content[self.position])

    def remove_note_from_selection(self):
        self.selected.discard(self.content[self.position])

    def next_note(self):
        if self.position != len(self.content)-1:
            self.position += 1
        else:
            self.position = 0

    def previous_note(self):
        if self.position != 0:
            self.position -= 1
        else:
            self.position = len(self.content) - 1
