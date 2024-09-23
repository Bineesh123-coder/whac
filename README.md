Here's a sample `README.md` file for your Python bot project using PyAutoGUI and Pynput, along with instructions to include it in a Git repository:

---

# Whack-a-Mole Bot

This Python script automates clicking on a specified image on the screen (e.g., a target in the Whack-a-Mole game). The script continuously scans the screen for the target image and clicks on it when found. You can stop the bot by pressing the `q` key.

## Features

- Locates the target image on the screen using PyAutoGUI.
- Automatically clicks the image once it is found.
- Allows stopping the bot via the keyboard (`q` key).
- Designed to continue running even if the target image is not found.

## Requirements

To run this script, you'll need the following libraries:

- **pyautogui**: For locating and clicking on the screen.
- **pynput**: For detecting key presses.
- **time**: Standard Python library for time-related functions.

Install the required dependencies by running:

```bash
pip install pyautogui pynput
```

## How to Use

1. Clone the repository and navigate to the project directory:

```bash
git clone [https://github.com/Bineesh123-coder/whack-a-mole-game-bot-]
```

2. Place the image you want to detect (e.g., `nose.png`) in the correct directory.

3. Run the script:

```bash
python whackamolebot.py
```

4. The script will wait for 5 seconds, then start scanning the screen for the image. When the image is found, the bot will click on it.

5. Press `q` to stop the bot.

## Customization

- **Image Path**: You can change the image to be detected by updating the `image_path` in the script.
- **Confidence Level**: Adjust the `confidence=0.8` parameter to change how accurately the bot needs to detect the image.

## Known Issues

- Ensure that the image is visible on the screen, and that the resolution or scaling does not affect image recognition.



