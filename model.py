class YetNameless:

    def __init__(self, main_file):
        self.boxes = []
        self.main_file = main_file
        self.refresh_boxes()

    def refresh_boxes(self):
        dat = open(self.main_file, 'r', encoding='UTF-8')
        self.boxes = [Box(line.strip('\n')) for line in dat]
        dat.close()

    def new_box(self):
        self.boxes.append(input('Škatla: ') + '.txt')
        self.save_changes()

    def delete_box(self):
        self.boxes.remove(input('Škatla: ') + '.txt')
        self.save_changes()

    def move_note(self, other):
        source = Box(input('Iz: ') + '.txt')
        source.delete_note(other)
        target = Box(input('V: ') + '.txt')
        target.add_note(other)

    def save_changes(self):
        dat = open(self.main_file, 'w', encoding='UTF-8')
        for box in self.boxes:
            print(box.name, file=dat)
        dat.close()


class Box:

    def __init__(self, name):
        self.name = name
        self.content = []
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


class Note:

    def __init__(self, text):
        self.text = text
