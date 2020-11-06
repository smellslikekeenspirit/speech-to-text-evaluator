from collections import defaultdict

import numpy as np

from settings import settings
import corpus

from corpus import Corpus


class word2vec:

    def __init__(self):
        self.n = settings['n']
        self.lr = settings['learning_rate']
        self.epochs = settings['epochs']
        self.window = settings['window_size']

    def generate_training_data(self, corpus):
        word_count = defaultdict(int)
        corp = corpus("text1.txt")
        print(corp.lines)
        for line in corp.lines:
            for word in line:
                word_count[word] += 1
        self.vocabulary_count = len(word_count.keys())
        self.unique_word_list = list(word_count.keys())
        # dict indexed by word
        self.word_index = dict((word, i) for i, word in enumerate(self.unique_word_list))
        # dict indexed by i
        self.index_word = dict((i, word) for i, word in enumerate(self.unique_word_list))
        training_data = []
        for line in corp.lines:
            length_of_line = len(line)  # length of list containing words, representative of a line from text1.txt
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

        # SOFTMAX ACTIVATION FUNCTION
        def softmax(self, x):
            e_x = np.exp(x - np.max(x))
            return e_x / e_x.sum(axis=0)

        # CONVERT WORD TO ONE HOT ENCODING
        def word2onehot(self, word):
            word_vec = [0 for i in range(0, self.v_count)]
            word_index = self.word_index[word]
            word_vec[word_index] = 1
            return word_vec

        # FORWARD PASS
        def forward_pass(self, x):
            h = np.dot(self.w1.T, x)
            u = np.dot(self.w2.T, h)
            y_c = self.softmax(u)
            return y_c, h, u

        # BACKPROPAGATION
        def backprop(self, e, h, x):
            dl_dw2 = np.outer(h, e)
            dl_dw1 = np.outer(x, np.dot(self.w2, e.T))

            # UPDATE WEIGHTS
            self.w1 = self.w1 - (self.eta * dl_dw1)
            self.w2 = self.w2 - (self.eta * dl_dw2)
            pass

    # SOFTMAX ACTIVATION FUNCTION
    def softmax(self, x):
        e_x = np.exp(x - np.max(x))
        return e_x / e_x.sum(axis=0)

    # CONVERT WORD TO ONE HOT ENCODING
    def word2onehot(self, word):
        word_vec = [0 for i in range(0, self.vocabulary_count)]
        word_index = self.word_index[word]
        word_vec[word_index] = 1
        return word_vec

    # FORWARD PASS
    def forward_pass(self, x):
        h = np.dot(self.w1.T, x)
        u = np.dot(self.w2.T, h)
        y_c = self.softmax(u)
        return y_c, h, u

    # BACKPROPAGATION
    def backprop(self, e, h, x):
        dl_dw2 = np.outer(h, e)
        dl_dw1 = np.outer(x, np.dot(self.w2, e.T))

        # UPDATE WEIGHTS
        self.w1 = self.w1 - (self.eta * dl_dw1)
        self.w2 = self.w2 - (self.eta * dl_dw2)
        pass

    def train(self, training_data):

        # INITIALIZE WEIGHT MATRICES
        self.w1 = np.random.uniform(-0.8, 0.8, (self.vocabulary_count, self.n))  # embedding matrix
        self.w2 = np.random.uniform(-0.8, 0.8, (self.n, self.vocabulary_count))  # context matrix

        # CYCLE THROUGH EACH EPOCH
        for i in range(0, self.epochs):

            self.loss = 0

            # CYCLE THROUGH EACH TRAINING SAMPLE
            for w_t, w_c in training_data:
                # FORWARD PASS
                y_pred, h, u = self.forward_pass(w_t)

                # CALCULATE ERROR
                EI = np.sum([np.subtract(y_pred, word) for word in w_c], axis=0)

                # BACKPROPAGATION
                self.backprop(EI, h, w_t)

                # CALCULATE LOSS
                self.loss += -np.sum([u[word.index(1)] for word in w_c]) + len(w_c) * np.log(np.sum(np.exp(u)))

            print('EPOCH:', i, 'LOSS:', self.loss)
        pass

    # input a word, returns a vector (if available)
    def word_vec(self, word):
        w_index = self.word_index[word]
        v_w = self.w1[w_index]
        return v_w


    # input word, returns top [n] most similar words
    def word_sim(self, word, top_n):

        v_w1 = self.word_vec(word)
        word_sim = {}

        for i in range(self.vocabulary_count):
            # Find the similary score for each word in vocab
            v_w2 = self.w1[i]
            theta_sum = np.dot(v_w1, v_w2)
            theta_den = np.linalg.norm(v_w1) * np.linalg.norm(v_w2)
            theta = theta_sum / theta_den

            word = self.index_word[i]
            word_sim[word] = theta

        words_sorted = sorted(word_sim.items(), key=lambda kv: kv[1], reverse=True)

        for word, sim in words_sorted[:top_n]:
            print(word, sim)

