import tensorflow as tf
from tensorflow import keras
from keras import datasets, layers, models
import numpy
import matplotlib.pyplot as plt

print(tf.__version__)

(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data(path="mnist.npz")
train_images = train_images / 255.0
test_images = test_images / 255.0
train_images = numpy.expand_dims(train_images, -1)
test_images = numpy.expand_dims(test_images, -1)

model = models.Sequential()
model.add(layers.Conv2D(6, (5, 5), activation='relu'))  # 5,5
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(16, (5, 5), activation='relu'))  # 5,20
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Dropout(0.25))
model.add(layers.Flatten())
model.add(layers.Dense(120, activation='relu'))
model.add(layers.Dense(100, activation='relu'))
model.add(layers.Dropout(0.5))
model.add(layers.Dense(10, activation='softmax'))

model.compile(optimizer='adam',metrics=['accuracy'], loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True))
history = model.fit(train_images, train_labels, epochs=15, validation_data=(test_images, test_labels))
predictions = model.predict(test_images)
