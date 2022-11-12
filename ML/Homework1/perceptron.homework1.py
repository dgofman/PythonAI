#!/usr/bin/env python
# coding: utf-8

# ## Code for homework #1
# 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Helper functions for plotting and drawing lines
def plot_points(X, y):
    admitted = X[np.argwhere(y==1)]
    rejected = X[np.argwhere(y==0)]
    plt.scatter([s[0][0] for s in rejected], [s[0][1] for s in rejected], s = 25, color = 'blue', edgecolor = 'k')
    plt.scatter([s[0][0] for s in admitted], [s[0][1] for s in admitted], s = 25, color = 'red', edgecolor = 'k')

def display(m, b, color='g--'):
    plt.xlim(-0.05,1.05)
    plt.ylim(-0.05,1.05)
    x = np.arange(-10, 10, 0.1)
    plt.plot(x, m*x+b, color)

# Read and plot data
data = pd.read_csv('data.csv', header=None)
X = np.array(data[[0,1]])
y = np.array(data[2])
#plot_points(X,y)
#plt.show()

# Setting the random seed, feel free to change it and see different solutions.
np.random.seed(42)

def stepFunction(t):
    if t >= 0:
        return 1
    return 0

def prediction(X, W, b):
    return stepFunction((np.matmul(X,W)+b)[0])


# Fill in the code below to implement the perceptron trick.<br> <br>
# The function should receive as inputs the data X, the labels y, the weights W (as an array), and the bias b.<br>
# Update the weights W and bias b, according to the perceptron algorithm, and return W and b.
def perceptronStep(X, y, W, b, learn_rate):
    for i in range(len(X)):
        y_hat = prediction(X[i],W,b)
        next_y_hat = y[i] - y_hat
        if next_y_hat != 0:
            x0 = X[i][0] * learn_rate
            x1 = X[i][1] * learn_rate
            if next_y_hat > 0:
                W[0] += x0
                W[1] += x1
            else:
                W[0] -= x0
                W[1] -= x1
    return W, b
    
# This function runs the perceptron algorithm repeatedly on the dataset,
# and returns a few of the boundary lines obtained in the iterations,
# for plotting purposes.
# Feel free to play with the learning rate and the num_epochs,
# and see your results plotted below.
def trainPerceptronAlgorithm(X, y, learn_rate = 0.01, num_epochs = 65):
    W = np.array(np.random.rand(2,1))
    b = np.random.rand(1)[0]
    # These are the solution lines that get plotted below.
    boundary_lines = []
    for i in range(num_epochs):
        # In each epoch, we apply the perceptron step.
        W, b = perceptronStep(X, y, W, b, learn_rate)
        boundary_lines.append((-W[0]/W[1], -b/W[1]))
        if i==0:
            display(-W[0]/W[1], -b/W[1], 'r--')
        else:
            display(-W[0]/W[1], -b/W[1])

    # Plotting the solution boundary
    plt.title("Solution boundary")
    display(-W[0]/W[1], -b/W[1], 'black')

    # Plotting the data
    plot_points(X, y)
    plt.show()
    return boundary_lines

trainPerceptronAlgorithm(X, y)