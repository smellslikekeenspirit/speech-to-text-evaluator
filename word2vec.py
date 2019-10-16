from collections import defaultdict

from settings import settings
import Corpus

from Corpus import Corpus


class word2vec:

    def __init__(self):
        self.n = settings['n']
        self.lr = settings['learning_rate']
        self.epochs = settings['epochs']
        self.window = settings['window_size']

    def generate_training_data(self, corpus):
        word_count = defaultdict(int)
        corp = Corpus("text")
        print(corp.words)
        for line in corp.words:
            for word in line:
                word_count[word] += 1
        self.vocabulary_count = len(word_count.keys())
        self.unique_word_list = list(word_count.keys())
        # dict indexed by word
        self.word_index = dict((word, i) for i, word in enumerate(self.unique_word_list))
        # dict indexed by i
        self.index_word = dict((i, word) for i, word in enumerate(self.unique_word_list))
        training_data = []
        for line in corp.words:
            length_of_line = len(line)  # length of list containing words, representative of a line from text
            for i, word in enumerate(line):
                w_target = self.word2onehot(line[i])
                w_context = list()
                for j in range(i - self.window, i + self.window + 1):
                    if j != i and 0 <= j < length_of_line:
                        w_context += [self.word2onehot(line[j])]

            training_data += [w_target, w_context]
        return training_data


    def word2onehot(self, word):
        # word_vec - initialise a blank vector
        word_vec = [0 for i in range(0, self.vocabulary_count)]  # Alternative - np.zeros(self.v_count)
        # Get ID of word from word_index
        word_index = self.word_index[word]
        # Change value from 0 to 1 according to ID of the word
        word_vec[word_index] = 1
        return word_vec
