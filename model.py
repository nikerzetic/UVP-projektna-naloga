from os import remove


class Mainframe:

    def __init__(self):
        self.boxes = []
        self.selected = set()
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
            print('Praškatla.txt', file=dat)
            self.boxes.append(Box('Praškatla.txt'))
            dat.close()

    def new_box(self, name):
        box = Box(name + '.txt')
        self.boxes.append(box)
        self.save_changes()
        box.refresh_notes()

    def delete_selected_boxes(self):
        for box in self.selected:
            try:
                remove(box.name)
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

    def add_box_to_selection(self):
        self.selected.add(self.boxes[self.position])

    def remove_box_from_selection(self):
        self.selected.remove(self.boxes[self.position])

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

    def open_current_box(self):
        self.boxes[self.position].open_box()


class Box:

    def __init__(self, name):
        self.name = name
        self.content = []
        self.selected = set()
        self.position = 0

    def __repr__(self):
        return 'Box("%s")' % self.name

    def __str__(self):
        return self.name.strip('.txt')

    def open_box(self):
        self.refresh_notes()
        return self.content

    def refresh_notes(self):
        try:
            dat = open(self.name, 'r', encoding='UTF-8')
            self.content = [Note(line.strip('\n')) for line in dat]
        except IOError:
            dat = open(self.name, 'w', encoding='UTF-8')
        dat.close()

    def add_note(self):
        note = Note(input('Zapisek: '))
        self.content.append(note)
        self.save_changes()

    def delete_selected(self):
        for note in self.selected:
            self.content.remove(note)
        self.selected = set()
        self.save_changes()

    def save_changes(self):
        dat = open(self.name, 'w', encoding='UTF-8')
        for note in self.content:
            print(note.text, file=dat)
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

    def remove_not_from_selection(self):
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


class Note:

    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return 'Note("%s")' % self.text

    def __str__(self):
        return self.text
