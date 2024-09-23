import pyautogui
import time
from pynput import keyboard

# Flag to control the running of the loop
running = True

# Function to execute on key press
def on_press(key):
    global running
    try:
        if key.char == 'q':
            print("Exiting...")
            running = False  # Stop the loop
            return False  # Stop listener
        print(f'Key {key.char} pressed')
    except AttributeError:
        print(f'Special key {key} pressed')

def find_and_click_image(image_path):
    time.sleep(5)  # Wait for 5 seconds before starting
    while running:  # Use the global 'running' flag to control the loop
        try:
            x, y = pyautogui.locateCenterOnScreen(image_path, confidence=0.8)
            if x and y:
                pyautogui.click(x, y)
                print(f"Clicked at: ({x}, {y})")
            else:
                print("Image not found!")
        except pyautogui.ImageNotFoundException:
            print("Image not found, continuing...")  # Continue if image is not found
          # Delay before the next search to avoid overwhelming the system

# Start the listener in a separate thread
listener = keyboard.Listener(on_press=on_press)
listener.start()

# Run the function to find and click the image
image_path = 'whachamolebot/nose.png'
find_and_click_image(image_path)

# Wait for the listener to complete (when 'q' is pressed)
listener.join()
