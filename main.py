
from Corpus import Corpus
from word2vec import word2vec

w2v = word2vec()
corp = Corpus("text")
w2v.generate_training_data(corp)
