import threading
import time

# Shared variable
shared_data = {"value": 0}
# Lock to avoid race conditions
data_lock = threading.Lock()

# Background function that modifies the variable
def update_variable():
    while True:
        with data_lock:
            shared_data["value"] += 1
        time.sleep(1)

# Start background thread
thread = threading.Thread(target=update_variable, daemon=True)
thread.start()

# Access the variable in real-time
while True:
    with data_lock:
        current_value = shared_data["value"]
    print(f"Current value: {current_value}")
    time.sleep(0.5)