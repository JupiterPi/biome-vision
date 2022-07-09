import math
import time
import numpy as np
import tensorflow as tf
from PIL import Image
import colorsys

image = Image.open("red.png")
image = image.resize((256, 128))

img_mat = tf.keras.preprocessing.image.img_to_array(image)
inputs = tf.convert_to_tensor(np.expand_dims(img_mat, axis=0))


def color_layer(inputs):
    colors = {}
    factor = 1

    row_i = 0
    for row in inputs[0]:
        row_i = row_i + 1
        print("row " + str(row_i))

        for pixel in row:
            # print(pixel)

            (hue, saturation, value) = colorsys.rgb_to_hsv(pixel[0], pixel[1], pixel[2])

            hue = math.floor(hue * 5) / 5
            saturation = math.floor(saturation * 5) / 5
            value = math.floor(value * 3) / 3

            color = colorsys.hsv_to_rgb(hue, saturation, value)
            if color in colors.keys():
                colors[color] += 1
            else:
                colors[color] = 1

    print([list(colors.values())])
    print(colors.values())
    return tf.convert_to_tensor([list(colors.values())])


print("started")
result = color_layer(inputs)
print(result)
