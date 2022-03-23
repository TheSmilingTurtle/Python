import NeuralNetwork4
import mnist_loader_Kopie as loader
import numpy as np
import random
import matplotlib.pyplot as plt

training_data, validation_data, test = loader.load_data_wrapper('mnist.pkl.gz')

net = NeuralNetwork4.NeuralNetwork([784,16,10])

net.SGD(training_data, 10, 10, 0.5, test_data=validation_data)

print("done")