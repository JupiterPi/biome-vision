import time
from PIL import ImageGrab

while True:
    print("screenshotted")
    time.sleep(1)

im = ImageGrab.grab()
im.save("screenshot.png")
