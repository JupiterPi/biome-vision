import time
import os
import shutil

groups = {}
image = open("biomes.csv", "r").read()
for line in image.split("\n"):
    if not line == "":
        (biome, group) = line.split(",")
        groups[biome] = group
print(groups)

dirname = "testdata_out_1649507049.541665"
out_dirname = "grouped_out_" + str(time.time())
os.mkdir(out_dirname)
for category in os.listdir(dirname):
    print("category: " + category)
    biome_group = groups[category]
    if not os.path.isdir(out_dirname + "/" + biome_group):
        os.mkdir(out_dirname + "/" + biome_group)
    for image in os.listdir(dirname + "/" + category):
        filename = biome_group + "_" + image[-8:]
        print("file: " + image + " (" + biome_group + ") -> " + filename)
        shutil.copyfile(dirname + "/" + category + "/" + image, out_dirname + "/" + biome_group + "/" + filename)
