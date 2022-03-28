import numpy as np
import matplotlib.pyplot as plt
import random
import math

# current version
# ToDo: mnake a brute force attempt for nnn
# 100 objects with (initially randomized) weights
# they get a score according to their performance
# the worse half gets killed and replaced by slight mutations of the best performing ones
# stonks
# some matplotlib learning data to vizualize learning success

class NeuralNetwork_B(object):
    def __init__(self, sizes, name=None, weights=None, biases=None):
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.name = name
        # genes
        self.mutation_strength = 10.0
        ##
        if not (weights and biases):
            self.default_weight_initiator()
        else:
            self.biases = biases
            self.weights = weights
            self.mutate()

    def default_weight_initiator(self):
        self.biases = [np.random.randn(y, 1) for y in self.sizes[1:]]
        self.weights = [np.random.randn(y, x)/np.sqrt(x)
                        for x, y in zip(self.sizes[:-1], self.sizes[1:])]

    def feedforward(self, a):
        for b, w in zip(self.biases, self.weights):
            a = sigmoid(np.dot(w, a)+b)
        return a

    def mutate(self):
        delta_b = [np.random.randn(y, 1)/(self.mutation_strength)
                   for y in self.sizes[1:]]
        delta_w = [np.random.randn(y, x)/(np.sqrt(x)*self.mutation_strength)
                   for x, y in zip(self.sizes[:-1], self.sizes[1:])]
        self.biases = [b+db for b, db in zip(self.biases, delta_b)]
        self.weights = [w+dw for w, dw in zip(self.weights, delta_w)]
        self.mutation_strength = self.mutation_strength + \
            ((random.random()-0.499)/(abs(self.mutation_strength)**(1/2)))

    def predict(self, input_thingy):
        out = self.feedforward(input_thingy)
        return out


def score(output_layer):

    sum_outputs = sum(output_layer)

    val = 200-abs(200-sum_outputs)**2

    np.argmax(val)

    return val


def sort_better(list, args):
    # nice
    new_list = [i for i in list]
    for i in range(len(args)):
        new_list[i] = list[args[i]]
    return new_list


def sigmoid(x):
    return 1.0/(1.0+np.exp(-x))

    ################
    ################
    ################


def mean(list):
    return sum(list)/len(list)


def mutationRadio(creature):
    creature.mutate()
    return creature


all_scores = []
all_mutation_strengths = []


def training(shape,  score_function ,LIVING_THINGS=100,iterations=100):
    snap = math.floor(LIVING_THINGS/2)  # constant, half of test subjects
    creatures = [NeuralNetwork_B(shape, "creature"+str(i))
                 for i in range(LIVING_THINGS)]  # test subjects

    # an arbitrary input, probablay to be changed in later versions
    input = np.array([2, 1])

    for it in range(iterations):
        # the scores evaluated for the test subjects
        scores = np.array([score_function(i.predict(input)) for i in creatures])

        # sorted indicies, for sorting the test subjects' scores
        scoresS = list(np.argsort(scores, 0))
        for i in range(len(scoresS)):
            # converting the sorted indicies from a list of lists to a list of ints
            scoresS[i] = int(scoresS[i])
        # sorting test subjects according to their scores
        creatures = sort_better(creatures, scoresS)

        # scores = np.array([score(i.predict(input)) for i in creatures])    # scores again ?
        if it % 50 == 0:
            print("{} at it {}".format(max(scores), 2*it))
        creatures = creatures[-snap:]

        #new_creatures=[mutationRadio(i) for i in creatures]
        new_creatures = []
        for ij in creatures:
            new_creatures.append(NeuralNetwork_B(
                shape, ij.name, ij.weights, ij.biases))
        for i in new_creatures:
            creatures.append(i)
        all_scores.append(score_function(creatures[snap].predict(input)))
        all_mutation_strengths.append(creatures[snap].mutation_strength)
    
    return (creatures[snap].weights, creatures[snap].biases)


# hidden layer cannot be bigger than 1, plz fix
training([2, 1, 500], score, 1000, 500)

print("\n\n/////////////////\n\n") 

plt.plot(list(range(len(all_mutation_strengths))), all_mutation_strengths)
plt.plot(list(range(len(all_scores))), all_scores)

plt.show()