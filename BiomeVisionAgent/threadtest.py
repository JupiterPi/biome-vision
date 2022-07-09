import time
import tkinter as tk
import threading
import queue

command_queue = queue.Queue()

command_queue.put("hi")

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
        root.after(500, timer_tick)

    timer_tick()
    root.mainloop()

    print("thread started")


threading.Thread(target=thread_main).start()



iterations = 0
while True:
    iterations = iterations + 1
    print("iterations: " + str(iterations))
    command_queue.put("iteration #" + str(iterations))
    time.sleep(1)
