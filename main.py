
from corpus import Corpus
from word2vec import word2vec

w2v = word2vec()
corp = Corpus("text1.txt")
w2v.train(w2v.generate_training_data(corp))
w2v.word_sim("built", 5)
