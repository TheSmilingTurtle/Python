import numpy as np
import time
import pandas as pd
import re
import nltk
import networkx as nx
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from sklearn.metrics.pairwise import cosine_similarity

word_embeddings = {} 
f = open('PyPrograms/glove.6B/Word_embeddings.txt', encoding='utf-8') # Extract word vectors
for line in f: 
  values = line.split()
  word = values[0]
  coefs = np.asarray(values[1:], dtype='float32')
  word_embeddings[word] = coefs
  print("Extracting word vectors: ", len(word_embeddings)/4000,"%")
f.close()

stop_words = stopwords.words('english')   #Get stopwords
mode = input("Select mode: ")
df = "He laughs until he cries and then he dies, then he dies."#pd.read_csv("tennis_articles_v4.csv") #Fetch data
sum_num = int(input("Number of outputs:"))

def cleanup():
  """Make clean frags for the evaluation"""
  # remove punctuations, numbers and special characters
  clean_frags = pd.Series(frags).str.replace("[^a-zA-Z]", " ")

  # make alphabets lowercase
  clean_frags = [s.lower() for s in clean_frags]

  # function to remove stopwords
  def remove_stopwords(sen):
      sen_new = " ".join([i for i in sen if i not in stop_words])
      return sen_new

  # remove stopwords from the frags
  clean_frags = [remove_stopwords(r.split()) for r in clean_frags]

  return clean_frags

def vectorize():
  """Vectorize the fragments"""
  frag_vectors = []
  for i in clean_frags:     #assign word vectors
    if len(i) != 0:
      v = sum([word_embeddings.get(w, np.zeros((100,))) for w in i.split()])/(len(i.split())+0.001)
    else:
      v = np.zeros((100,))
    frag_vectors.append(v)
  
  return frag_vectors

if mode == "sent":
  frags = sent_tokenize(df)
elif mode == "word":
  frags = word_tokenize(df.lower())

clean_frags = cleanup()
frag_vectors = vectorize()


sim_mat = np.zeros([len(frags), len(frags)]) # similarity matrix

for i in range(len(frags)):       #determine similarity
  for j in range(len(frags)):
    if i != j:
      sim_mat[i][j] = cosine_similarity(frag_vectors[i].reshape(1,100), frag_vectors[j].reshape(1,100))[0,0]

nx_graph = nx.from_numpy_array(sim_mat)
scores = nx.pagerank(nx_graph)

ranked_frags = list(dict.fromkeys(sorted(((scores[i],s) for i,s in enumerate(frags)), reverse=True)))    

for i in range(sum_num):        # Extract top frags
  print(ranked_frags[i][1])

print(ranked_frags)