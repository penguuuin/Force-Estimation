# -*- coding: utf-8 -*-
"""baseline.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rQayJkKvK08zISvomzoctGN5fJyywAJo
"""

import tensorflow as tf

from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt

# import training and testing video as array of images
(train_video, train_labels), (test_video, test_labels) = datasets.load_data()

# Normalize pixel values to be between 0 and 1
train_video, test_video = train_video / 255.0, test_video / 255.0

# preview input
plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_video[i])
    plt.xlabel(class_names[train_labels[i][0]])
plt.show()

model = models.Sequential()
# CNN part
model.add(layers.TimeDistributed(Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3))))
model.add(layers.TimeDistributed(MaxPooling2D((2, 2))))
model.add(layers.TimeDistributed(Conv2D(64, (3, 3), activation='relu')))
model.add(layers.TimeDistributed(MaxPooling2D((2, 2))))
model.add(layers.TimeDistributed(Conv2D(64, (3, 3), activation='relu')))

# Flatten CNN output
model.add(layers.TimeDistributed(Flatten()))

#TODO: integrate data from sensors

# RNN part
model.add(layers.Embedding(input_dim=1000, output_dim=64))

# Add a LSTM layer with 128 internal units.
model.add(layers.LSTM(128))

# final dense layers for output
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(1))

model = keras.Sequential()
# Add an Embedding layer expecting input vocab of size 1000, and
# output embedding dimension of size 64.
model.add(layers.Embedding(input_dim=1000, output_dim=64))

# Add a LSTM layer with 128 internal units.
model.add(layers.LSTM(128))

# Add a Dense layer with 10 units.
model.add(layers.Dense(10))

model.summary()



model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

history = model.fit(train_video, train_labels, epochs=10, 
                    validation_data=(test_video, test_labels))