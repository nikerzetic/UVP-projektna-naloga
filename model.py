class App:

    def __init__(self, main_file):
        self.boxes = []
        self.selected = set()
        self.main_file = main_file
        self.refresh_boxes()
        self.position = 0

    def refresh_boxes(self):
        dat = open(self.main_file, 'r', encoding='UTF-8')
        self.boxes = [Box(line.strip('\n')) for line in dat]
        dat.close()

    def new_box(self):
        self.boxes.append(input('Škatla: ') + '.txt')
        self.save_changes()

    def delete_box(self):
        for box in self.selected:
            self.boxes.remove(box)
            self.selected.discard(box)
        self.save_changes()

    def save_changes(self):
        dat = open(self.main_file, 'w', encoding='UTF-8')
        for box in self.boxes:
            print(box.name, file=dat)
        dat.close()

    def select_box(self):
        self.selected |= set(self.boxes[self.position])

    def next(self):
        self.position += 1

    def previous(self):
        self.position -= 1


class Box:

    def __init__(self, name):
        self.name = name
        self.content = []
        self.selected = set()
        self.position = 0
        self.refresh_notes()

    def __repr__(self):
        return 'Box(%s)' % self.name

    def __print__(self):
        return self.name.strip('.txt')

    def open_box(self):
        return self.content

    def refresh_notes(self):
        dat = open(self.name, 'r', encoding='UTF-8')
        self.content = [Note(line.strip('\n')) for line in dat]
        dat.close()

    def add_note(self, other):
        self.content.append(other.text)
        self.save_changes()

    def delete_note(self, other):
        self.content.remove(other.text)
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
        self.selected |= set(self.content[self.position])

    def remove_not_from_selection(self):
        self.selected.discard(self.content[self.position])

    def next(self):
        self.position += 1

    def previous(self):
        self.position -= 1


class Note:

    def __init__(self, text):
        self.text = text
