import threading
import time

# Function that takes parameters
def background_task(name, delay):
    print(f"[{name}] Starting task with {delay}s delay")
    time.sleep(delay)
    print(f"[{name}] Task complete")

# Start the thread (non-blocking)
