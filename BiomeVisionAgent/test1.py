import time
import tkinter as tk

root = tk.Tk()
root.attributes("-topmost", True)
root.resizable(width=False, height=False)

label = tk.Label(text="forest", width=30, height=5, font=("Arial", 15))
label.pack()

root.mainloop()
#label["text"] = "hi"

print("hi")


#iterations = 0
#while True:
#    iterations = iterations + 1
#    label["text"] = str(iterations)
 #   time.sleep(1)
