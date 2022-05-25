import math
import time
from PIL import Image
import colorsys

image = Image.open("picture.png")

colors = {}

start_time = time.time()

for x in range(730):
    for y in range(487):
        rgb = image.getpixel((x, y))
        (hue, saturation, value) = colorsys.rgb_to_hsv(rgb[0] / 256, rgb[1] / 256, rgb[2] / 256)

        hue *= 360
        hue = math.floor(hue / (360/5)) * (360/5)
        hue /= 360

        saturation *= 100
        saturation = math.floor(saturation / (100/5)) * (100/5)
        saturation /= 100

        value *= 100
        value = math.floor(value / (100/3)) * (100/3)
        value /= 100

        #color = (hue, saturation, value)
        color = colorsys.hsv_to_rgb(round(hue, 2), round(saturation, 2), round(value, 2))
        #color = rgb
        if color in colors.keys():
            colors[color] += 1
        else:
            colors[color] = 1

print(time.time() - start_time)

sorted_colors = sorted(colors.items(), key=lambda item: item[1], reverse=True)
print("colors length: " + str(len(sorted_colors)))
for color in sorted_colors[:10]:
    print(color)
