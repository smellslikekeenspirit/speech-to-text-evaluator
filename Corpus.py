import re


class Corpus:

    def __init__(self, filename):
        self.lines = []
        r = r"(?<!\d)[.?,;:](?!\d)"
        with open(filename, encoding='utf-8') as f1, open("parsed", 'w', encoding='utf-8') as f2:
            line = f1.readline()
            i = 1
            while line:
                line = re.sub(r'\n+', '', re.sub(r"\$", "", re.sub("_", "", re.sub("-", "", re.sub(r, "", line)))))
                if line != "":
                    print(line.lower(), " (spk1_%i)" % i)
                    i += 1
                self.lines += line
                line = f1.readline()


if __name__ == '__main__':
    c = Corpus("new7.txt")
    print(c)
