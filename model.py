class YetNameless:

    def __init__(self, main_file):
        self.boxes = []
        self.main_file = main_file

    def refresh_boxes(self):
        dat = open(self.main_file, 'r')
        for line in dat:
            self.boxes.append(line.strip('\n'))
        dat.close()
