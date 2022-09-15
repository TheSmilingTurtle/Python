from typing import List
import nltk
import gensim
import numpy as np

def norm_list(l: List):
    return [np.linalg.norm(x) for x in l]

#### Opening Word Embeddings ####
word2vec_sample =  str(nltk.data.find('models/word2vec_sample/pruned.word2vec.txt'))

#### defining nltk things ####
model = gensim.models.KeyedVectors.load_word2vec_format(word2vec_sample, binary=False)
tokenizer = nltk.data.load("nltk:tokenizers/punkt/english.pickle")
stopwords = nltk.corpus.stopwords.words("english")

#### Input methods ####
in_text = input("Enter Text: ")

#### Input sanitisation
sentence_tokenized = tokenizer.tokenize(in_text)
word_tokenized = [nltk.word_tokenize(sentence) for sentence in sentence_tokenized]
cleaned = [[word for word in sentence if word not in stopwords] for sentence in word_tokenized]

print(cleaned)

#### Vectorizing the data ####
vectorized = [[model[word] for word in sentence] for sentence in cleaned]

#### Computing Sentence averages ####
average = []

for sentence in vectorized:
    sum = 0
    for word in sentence: 
        sum += word
    
    average.append(sum/len(sentence))

print(norm_list(average))

#### Computing first order cognitive divergence ####
dist_array = []

for (index, sentence) in enumerate(average[:-1]):
    dist_array.append(sentence - average[index + 1])

print(norm_list(dist_array))

out = 0
for i in dist_array:
    out += np.linalg.norm(i)/2 # over 2, because embeddins are contained to a sphere with radius 1 (i think, maybe square with radius 1, but ill just assume sphere.). So the maximum distance between two points is 2 and i want to normalize it to 1.

print(out/len(dist_array))