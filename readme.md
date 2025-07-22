# twoslash-alternative 
## Python Keyboard-Driven GenAI Assistant

A CLI and keyboard-triggered assistant for quickly generating code snippets or rich formatted text using Google Gemini GenAI, inspired by twoslash. Use live keyboard triggers to submit requests and get answers, pasted automatically wherever you are working.

## Features

- **Keyboard global capture**: Monitors for patterns like `>>{your_prompt}<<` and triggers a completion.
- **Generates plain code or structured text**: Distinguishes if your request is code-related or general text and returns clean output.
- **Auto pastes into active text fields**: Uses clipboard and keyboard simulation to insert results.
- **Environment-safe authentication**: Loads your API key from a `.env` file – keeping secrets secure.
- **Cross-platform**: Works on Windows, macOS, Linux (where `pynput` and clipboard are supported).


## Prerequisites

- Python 3.8 or above
- [pip](https://pip.pypa.io/) for package installation
- Google GenAI account \& API key (see [Google GenAI documentation](https://ai.google.dev/))


## Setup Instructions

### 1. Clone the Repository

```sh
git clone https://github.com/adityabhalsod/twoslash-alternative.git
cd twoslash-alternative
```


### 2. Create a Python Virtual Environment

This keeps dependencies isolated from your system Python.

```sh
# On Linux/macOS
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```


### 3. Install Dependencies

```sh
pip install -r requirements.txt
```

### 4. Set Up Your `.env` File

Add your Google GenAI API key in a `.env` file in your project root:

```
GOOGLE_API_KEY=your-google-genai-api-key-here
```

> **Never share or commit your `.env` file.**

### 5. Run the Assistant

```sh
python twoslash_alternative.py
```

*(Assuming you've saved the script as `twoslash_alternative.py`.)*

## Usage

- **To trigger a response:** Type anywhere `>>your prompt<<` and press Enter.
    - For code/computation: `>>Write a Python function for Fibonacci<<`
    - For structured text: `>>Summarize the theory of relativity<<`
- **Automatic clipboard:** The result is copied to your clipboard and pasted into the current active input field.
- **Exit:** Type `>>exit<<` and press Enter or press `Esc`.
- **Supports OS copy/paste:** Uses simulated keyboard, so works in editors, browsers, terminals, etc.


## Tips

- **VirtualEnv Reminder:** Always activate your virtual environment before running the assistant.
- **API Key Safety:** Store only in `.env`; never hardcode.
- **Keyboard Permissions:** On MacOS or Linux, you may need to grant accessibility/input monitoring permissions for global key listening/pasting.
- **Stopping the Script:** Use `Esc` or type `>>exit<<`.


## Troubleshooting

- **Clipboard or paste does not work:** Ensure you have permission and required clipboard packages (`pyperclip`) installed.
- **Listener not operating globally:** Check for OS restrictions on keyboard hooks, especially on macOS (System Preferences > Security \& Privacy > Accessibility).
- **Python errors for missing packages:** Double check your virtual environment is activated before installing or running.


## Example .env

```
GOOGLE_API_KEY=AIza...
```


## Acknowledgments

- Inspired by [twoslash](https://twoslash.dev/) and the idea of tight-loop developer workflows.
- Uses [Google Gemini GenAI API].

: https://ai.google.dev/

