CTF_maker
CTF_maker is a Python project designed to help you create interactive challenges, automate tasks, and provide a framework for Capture the Flag (CTF) events. This project includes various utility functions that you can use to create engaging and automated CTF challenges.

Features
Interactive Questioning: Ask users questions and provide feedback based on their answers.
Slow Print: Print text with a delay between each character for a dramatic effect.
Base64 Encoding/Decoding: Easily encode and decode strings using Base64.
Image Display: Display images using the Python Imaging Library (PIL).
Browser Automation: Open URLs in the default web browser.
Command Execution: Execute shell commands from within the Python script.
Alert Messages: Display alert boxes using PyAutoGUI.
Dependencies
This project requires the following Python libraries:

base64: For encoding and decoding strings in Base64.
subprocess: For executing shell commands.
time: For handling delays and pauses.
sys: For interacting with the Python interpreter.
webbrowser: For opening URLs in a web browser.
pyautogui: For displaying alert boxes.
PIL: For working with images (from the Pillow package).
You can install the necessary dependencies using pip:

bash
Copy code
pip install pyautogui pillow
How to Use
Clone the repository and navigate to the project directory.

Activate your virtual environment (if you have one) and run the project:

bash
Copy code
.\.venv\scripts\activate.bat  # On Windows
python main.py
Follow the prompts to interact with the script.

The main() function demonstrates the capabilities of the project, including:

Prompting the user for input and checking the correctness of the answers.
Printing messages with a delay between each character.
Running a shell command that opens a new command prompt window.
Opening a web browser to a specified URL.
Displaying an image using the Pillow library.
Example Usage
Here is an example of what you might see when running the project:

plaintext
Copy code
Hello, thanks for using this project
This prints slowly
Opening new cmd window
What is your name?: 
ur nem jeff
I shall open gugel
I shall open an image
Press q to exit: 
bye!
Customization
You can customize this project by adding your own questions, adjusting the delay for the slow_print() function, or extending the existing functionality with additional features.

Contributing
Feel free to fork this repository, submit issues, or make pull requests if you have ideas for improvements or new features.

License
This project is licensed under the MIT License. See the LICENSE file for details.
