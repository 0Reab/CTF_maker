# CTF_maker

CTF_maker is a Python project designed to help you create interactive challenges, and provide a framework for Capture the Flag events.
This project includes various utils to help you create engaging CTF challenges.

# Features
- Interactive Questioning
- Slow Print
- Base64 Encoding/Decoding
- Image Display
- Browser Automation
- Command Execution (cmd)
- Alert Messages

# Dependencies
This project requires the following Python libraries:

pyautogui: For displaying alert boxes.
PIL: For working with images (from the Pillow package).
You can install the necessary dependencies using pip:

`pip install pyautogui pillow`
# How to Use
Clone the repository and navigate to the project directory.

Activate your virtual environment (if you have one) and run the project:

`.\.venv\scripts\activate.bat`
`python main.py`

The main() function demonstrates the capabilities of the project, including:

Prompting the user for input and checking the correctness of the answers.
Printing messages with a delay between each character.
Running a shell command that opens a new command prompt window.
Opening a web browser to a specified URL.
Displaying an image.

# Customization
You can customize this project by adding your own questions, adjusting the delay for the slow_print() function, or extending the existing functionality with additional features.

# Contributing
Feel free to fork this repository, submit issues, or make pull requests if you have ideas for improvements or new features.

# License
This project is licensed under the MIT License. See the LICENSE file for details.
