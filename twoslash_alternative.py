import os
import sys
import re
import time
import threading

import pyperclip      # For clipboard operations
from pynput import keyboard
from dotenv import load_dotenv

# Import the required Google GenAI library
from google import genai

# Load .env file for environment variables
load_dotenv()

# Get the API key from environment variables
API_KEY = os.getenv("GOOGLE_API_KEY")

# Define the pattern for extracting text
# Variable to store the captured text
captured_text = ""

# Define the pattern you're looking for
PATTERN_START = ">>"
PATTERN_END = "<<"
# Controller for simulating key presses
keyboard_controller = keyboard.Controller()

def delayed_response(response):
    """Simulate a delayed response."""
    cleaned_text = "\n".join(
        line for line in str(response).splitlines() if "```" not in line
    )
    # Copy the response to the clipboard
    pyperclip.copy(cleaned_text)

    # Simulate pasting the clipboard content
    keyboard_controller.press(keyboard.Key.enter)
    keyboard_controller.release(keyboard.Key.enter)
    time.sleep(1)

    # Paste the clipboard content
    keyboard_controller.press(keyboard.Key.ctrl_l)  # Press Ctrl
    keyboard_controller.press("v")  # Press V to paste
    keyboard_controller.release("v")
    keyboard_controller.release(keyboard.Key.ctrl_l)  # Release Ctrl

def on_press(key):
    global captured_text

    try:
        # Check if the key has a character attribute (i.e., it's a normal key)
        if hasattr(key, "char"):
            captured_text += key.char
        elif key == keyboard.Key.space:
            captured_text += " "
        elif key == keyboard.Key.backspace:
            captured_text = captured_text[:-1]  # Remove the last character
        elif key == keyboard.Key.enter:
            captured_text += "\n"  # Add a newline for Enter key
        elif key == keyboard.Key.tab:
            captured_text += "\t"  # Add a tab for Tab key
        elif key == keyboard.Key.esc:
            print("Exiting...")
            return False

        # Check if the captured text matches the desired pattern
        if PATTERN_START in captured_text and captured_text.endswith(PATTERN_END):
            # Print the captured text
            print(f"Captured Text: {captured_text}")
            # Remove start and end markers
            matches = re.findall(r">>(.*?)<<", captured_text, re.DOTALL)
            extracted_text = "".join(matches)
            print(f"Extracted Pattern: {extracted_text}")

            # Reset the buffer after extracting
            captured_text = ""

            if extracted_text == "exit":
                print("Exiting...")
                sys.exit(0)  # Exit the program

            if len(extracted_text) > 0:
                try:
                    # Initialize the GenAI client with a valid API key
                    client = genai.Client(api_key=API_KEY)

                    if any(
                        [
                            check in extracted_text.lower()
                            for check in (
                                "code",
                                "python",
                                "javascript",
                                "java",
                                "c++",
                                "c#",
                                "html",
                                "css",
                                "program",
                                "script",
                                "function",
                                "class",
                                "method",
                                "variable",
                                "object",
                            )
                            if check in extracted_text.lower()
                        ]
                    ):
                        # Generate content using the GenAI model for programming code
                        response = client.models.generate_content(
                            model="gemini-2.0-flash",
                            contents=[
                                f"Only return raw code without any markdown formatting (no triple backticks, no language tags). Do not include explanations, greetings, or any other text outside the code. If needed, include brief explanations only as comments inside the code. Output must be clean, plain code. ```{extracted_text}```"
                            ],
                        )
                    else:
                        # Generate content using the GenAI model for structured text
                        response = client.models.generate_content(
                            model="gemini-2.0-flash",
                            contents=[
                                f"Do not return any programming code. Only return well-formatted, clean, and structured text using headings, bullet points, or numbered lists where appropriate. Make the content easy to read and understand. Avoid using code blocks.  Do not include any explanation, greetings, or extra text. If any clarification or explanation is needed ```{extracted_text}```"
                            ],
                        )

                    # Start a new thread for the delayed response
                    threading.Thread(
                        target=delayed_response, args=(response.text,)
                    ).start()
                except Exception as e:
                    print(f"Error in API call or response handling: {e}")
                    captured_text = ""  # Reset the buffer on error

    except AttributeError:
        # Handle special keys that don't have a 'char' attribute
        pass


# Set up the listener
with keyboard.Listener(on_press=on_press) as listener:
    print("Listening for global keyboard events...")
    listener.join()
