import time
import os
import shutil

dirname = "dataset-03--09-04-2022---1-out-grouped-lite"

for category in os.listdir(dirname):
    print("category: " + category)
    i = 0
    for file in os.listdir(dirname + "/" + category):
        target_filename = category + "_" + str(i).zfill(5) + ".png"
        #if not file == target_filename:
        os.rename(dirname + "/" + category + "/" + file, dirname + "/" + category + "/" + target_filename)
        i = i + 1
