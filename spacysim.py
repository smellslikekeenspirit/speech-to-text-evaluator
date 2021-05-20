import spacy as sp
import re

# Load vectors directly from the file

nlp = sp.load('en_core_web_lg')


def read(filename):
    with open(filename, encoding='utf-8') as f1, open("parsed", 'w', encoding='utf-8') as f2:
        scores = dict()
        line = f1.readline()
        while line:
            line.replace('–', '-')
            print(line)
            words = line.lower().split('-')
            f2.write(line.strip() + " : " + str(nlp(words[0].strip()).similarity(nlp(words[1].strip()))) + "\n")
            line = f1.readline()



if __name__ == '__main__':
    read("car20pc.txt")
