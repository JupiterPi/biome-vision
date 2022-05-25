import time

from PIL import Image
import os

# image = Image.open("testdata\\flower_forest\\flower_forest_1649450732771_292.0-15.0.png")
# image.thumbnail((256, 128))
# image.show()

out_dirname = "testdata_out_" + str(time.time())
os.mkdir(out_dirname)

for folder in os.listdir("testdata"):
    print("writing category: " + folder)

    category_dirname = out_dirname + "/" + folder
    os.mkdir(category_dirname)

    files = os.listdir("testdata/" + folder)
    length = len(files)
    i = 0
    for file in files:
        if i % 100 == 0:
            print("writing " + folder + " / " + str(i))

        image = Image.open("testdata/" + folder + "/" + file)
        image.thumbnail((256, 128))
        index = str(i).zfill(4)
        image.save(category_dirname + "/" + folder + "_" + index + ".png", "PNG")
        i = i + 1
