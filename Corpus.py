
class Corpus:

    def __init__(self, filename):
        self.lines = []
        with open(filename) as f:
            line = f.readline()
            while line:
                self.words += [[y.lower() for y in line.split()]]
                line = f.readline()

