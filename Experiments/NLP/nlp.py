import nltk
import gensim
import matplotlib.pyplot as plt
import numpy as np
import math

BAR_NUM = 10

def norm_list(l):
    return [np.linalg.norm(x)/2 for x in l]

#### defining nltk things ####
model = gensim.models.KeyedVectors.load_word2vec_format(nltk.data.find('models/word2vec_sample/pruned.word2vec.txt'), binary=False)
tokenizer = nltk.data.load("nltk:tokenizers/punkt/english.pickle")
stopwords = nltk.corpus.stopwords.words("english")

#### Input methods ####
in_text = input("Enter Text: ")

#### Input sanitisation
sentence_tokenized = tokenizer.tokenize(in_text)
word_tokenized = [nltk.word_tokenize(sentence) for sentence in sentence_tokenized]
cleaned = [[word for word in sentence if word not in stopwords and word in model] for sentence in word_tokenized]
cleaned = [x for x in cleaned if x != []]

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

#### Computing first order cognitive divergence ####
dist_array = []

for (index, sentence) in enumerate(average[:-1]):
    dist_array.append(sentence - average[index + 1])

print(norm_list(dist_array))

#out = 0
#for i in dist_array:
#    out += np.linalg.norm(i) # over 2, because embeddins are contained to a sphere with radius 1 (i think, maybe square with radius 1, but ill just assume sphere.). So the maximum distance between two points is 2 and i want to normalize it to 1.

#print(out/len(dist_array))

#### Graphing ####
l = [0] * BAR_NUM
for i in norm_list(dist_array):
    l[math.floor(i * BAR_NUM)] += 1

#plt.bar([str(round(x, 2)) for x in np.arange(0, 1, 1/BAR_NUM)], l)
plt.plot(range(len(dist_array)), norm_list(dist_array))
plt.show()