import numpy as np
import nnfs
from nnfs.datasets import spiral_data
import matplotlib.pyplot as plt
from DenseLayer import Dense_Layer

nnfs.init()


X,y = spiral_data(samples=100, classes=3)

dense1 = Dense_Layer(n_inputs=2, n_neurons=3)

dense1.forward(X)

print(dense1.output)