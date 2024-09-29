import numpy as np

#Step 1: define the actication function
def sigmoid(x):
    return 1/(1 + np.exp(-x))

#Step 2: For the purpose of weight adjustment, we perform back propogation
def sigmoid_derivative(x):
    return x * (1 - x)

#Step 3: Training data (xs: inputs, ys: expected output)
xs = np.array([[0,0],
               [0,1],
               [1,0],
               [1,1]])

ys = np.array([[0],
               [1],
               [1],
               [0]])

#Step 4: Initialize random weight with seed value
np.random.seed(1)
weights = np.random.random((2,1))

#Step 5: Initialize learning rate and number of epochs
learning_rate = 0.1
epochs = 10

for epoch in range(epochs):
  #Forward propogation aka feed forward
  input_layer = xs
  outputs = sigmoid(np.dot(input_layer, weights))

  #Calculate the error as a difference between observed and expected
  error = ys - outputs

  #Perform back propogation to adjust the errors
  adjustments = error * sigmoid_derivative(outputs)
  weights += np.dot(input_layer.T, adjustments) #.T is for transposing the 1d array into 2d array

  #Backpropogation
  error = ys - outputs
  adjustments = error * sigmoid_derivative(outputs)
  weights += np.dot(input_layer.T, adjustments)*learning_rate

#Step 6: Output after the traing, modified weights
print(np.size(adjustments))

print("Weights after training: ",weights)

print("Output after training: ",outputs)

import matplotlib.pyplot as plt

plt.plot(outputs)
plt.xlabel('Output')
plt.ylabel('Epochs')
plt.show()