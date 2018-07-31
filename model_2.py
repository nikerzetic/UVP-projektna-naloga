from os import remove

class Main:

    def __init__(self):
        self.boxes = []
        self.main_file = 'boxes_main_file.txt'
        self.refresh_boxes()

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

    def save_changes(self):
        dat = open(self.main_file, 'w', encoding='UTF-8')
        for box in self.boxes:
            print(box.name, file=dat)
        dat.close()

    def add_box(self, box):
        self.boxes.append(box)
        self.save_changes()
        box.refresh_notes()

    def delete_box(self, box):
        try:
            remove(box.address)
        except FileNotFoundError:
            pass
        self.boxes.remove(box)
        self.save_changes()
        box.refresh_notes()


class Box:

    def __init__(self, name):
        self.name = name
        self.address = self.name + '.txt'
        self.opened = False
        self.content = None

    def __repr__(self):
        return 'Box("%s")' % self.name

    def __str__(self):
        return self.name

    def refresh_notes(self):
        self.opened = True
        self.content = []
        try:
            dat = open(self.address, 'r', encoding='UTF-8')
            self.content = [line.strip('\n') for line in dat]
        except IOError:
            dat = open(self.address, 'w', encoding='UTF-8')
        dat.close()

    def save_changes(self):
        dat = open(self.address, 'w', encoding='UTF-8')
        for note in self.content:
            print(note, file=dat)
        dat.close()

    def open(self):
        self.refresh_notes()
        return self.content

    def close(self):
        if self.opened:
            self.opened = False
            self.save_changes()
            self.content = None

    def add_note(self, note):
        self.refresh_notes()
        self.content.append(note)
        self.save_changes()

    def delete_notes(self, selected):
        for note in selected:
            self.content.remove(note)
        self.save_changes()


def move_note(box1, box2, selected):
    box1.refresh_notes()
    box2.refresh_notes()
    for note in selected:
        box1.content.remove(note)
        box2.content.append(note)
    box1.close()
    box2.close()
