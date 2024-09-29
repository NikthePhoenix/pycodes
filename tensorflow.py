try:
  import tensorflow.compat.v2 as tf
  #preferred for numerical computation and large scale ML
  #open source, created by google brain team
except Exception:
  pass

import numpy as np
from tensorflow import keras
#open source software library that provides a python interface for ai neural network, acts as an tensorflow library, used to evaluate deep learing models

import tensorflow as tf
from keras import Sequential
#Sequential is a class in Keras which heklps in building model, constructor of sequential return final model; training and inference features on this model
from keras.layers import Dense #class in keras (dense)

# model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])

# #Dense implements the operation:
# #output = activation(dot(input,kernel)+bias)
model = tf.keras.Sequential([
    keras.Input(shape=[1]),  # Specify the input shape here
    Dense(units=1)           # Add Dense layer
])

# Compile the model
model.compile(optimizer='sgd', loss='mean_squared_error', metrics=['accuracy'])
# #optimizer finds the solution with lowest cost. fast execution, lowest memory, has different gradients
# #sgd = stochastic gradient descent
# #other optimizers = Adam RMSprop, etc.
# #loss function tells us by how much we are missing the mark

xs = np.array([-1.0,  0.0, 1.0, 2.0, 3.0, 4.0], dtype = float)
ys = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype = float)

history = model.fit(xs, ys, epochs=500)
#epochs is one entire iteration from forward to back for the model to get trained; assuming 500 is suficient for th machine to learn
#accuracy increasesif epochs increases and vice versa
prediction_value = np.array([[15.0]], dtype=float)  # Wrap input in an array with shape (1, 1)
print(model.predict(prediction_value))

import matplotlib.pyplot as plt

plt.plot(history.history['accuracy'], label='model accuracy', color='red')
plt.plot(history.history['loss'], label='model loss', color='blue')
plt.legend()
plt.show()