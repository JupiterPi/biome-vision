import time
import tkinter as tk
import threading
import queue

import numpy as np
import tensorflow as tf
from tensorflow import keras

from PIL import ImageGrab

# class_names = ['badlands',
#                'birch_forest',
#                'cave',
#                'dark_forest',
#                'desert',
#                'flower_forest',
#                'forest',
#                'ice',
#                'jungle',
#                'mountain',
#                'mycelium',
#                'ocean',
#                'plains',
#                'river',
#                'savanna',
#                'snowy',
#                'swamp',
#                'taiga']
class_names = ['desert', 'forest', 'jungle', 'plains', 'river', 'taiga']

interval = 300
gui_invertal = 100


command_queue = queue.Queue()


def thread_main():
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.resizable(width=False, height=False)

    label = tk.Label(text="forest", width=30, height=5, font=("Arial", 15))
    label.pack()

    def timer_tick():
        try:
            item = command_queue.get_nowait()
        except queue.Empty:
            pass
        else:
            print("something in queue: " + item)
            label["text"] = item
        root.after(gui_invertal, timer_tick)

    timer_tick()
    root.mainloop()

    print("thread started")


threading.Thread(target=thread_main).start()

# iterations = 0
# while True:
# iterations = iterations + 1
# print("iterations: " + str(iterations))
# command_queue.put("iteration #" + str(iterations))
# time.sleep(1)


 #model = keras.models.load_model("C:\Private\BiomeVision\model1-2022-06-20-pre")
model = keras.models.load_model("C:\\Private\\BiomeVision\\model1-2022-07-06-lite-cache4")

while True:
    screenshot = ImageGrab.grab()
    # input_screenshot = np.asmatrix(screenshot)
    # print(screenshot.size)
    screenshot = screenshot.resize((128, 256))
    # print(screenshot.size)
    input_screenshot = keras.preprocessing.image.img_to_array(screenshot)
    # print(input_screenshot.shape)
    prediction = model.predict(np.expand_dims(input_screenshot, axis=0))

    predictions = {}
    i = 0
    for p in prediction[0]:
        predictions[class_names[i]] = p
        i = i + 1
    s_predictions = sorted(predictions.items(), key=lambda x: x[1])
    for p in s_predictions:
        print(p[0], p[1])

    first = s_predictions[len(s_predictions)-1]
    second = s_predictions[len(s_predictions)-2]
    result = first[0] + " (" + second[0] + "?)"
    print(result)
    command_queue.put(result)
    time.sleep(interval/1000)

# test_data = np.random.random((0, 256, 128, 3))
# print(test_data.shape())
# prediction = model.predict(test_data)
# print(prediction)
