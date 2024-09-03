import base64
import subprocess as sb
import time as t
import sys
import webbrowser as wb
import pyautogui as py
from PIL import Image


def main():
    # call functions here

    print("Hello, thanks for using this project") # basic print
    sleep(1)
    slow_print('This prints slowly', 0.04)
    print('Opening new cmd window')
    sleep(1)
    run('start cmd.exe /c "echo There it is lol & pause"')
    sleep(2)
    check_answer('What is your name?: ', 'jeff', 'ur nem jeff', 'ur not jeff', True)
    sleep(0.5)
    alert('I shall open gugel')
    sleep(2)
    browser('https://google.com')
    sleep(3)
    print('I shall open a image')
    sleep(1)
    image('kali.png')
    check_answer('Press q to exit: ', 'q', 'bye!', 'press q plz...', True)

# helper function
def response(result: bool, correct_return, incorrect_return) -> str: # returns bool
    return correct_return if result else incorrect_return


def check_answer(question: str, correct: str, correct_return: str, incorrect_return: str, until=False):
    # usage: check_answer('question', 'wanted_answer', 'response_if_correct', 'response_if_incorrect', 'ask_until_correct')

    correct_answer = input(question) == correct # check if question was answered correctly
    print(response(correct_answer, correct_return, incorrect_return)) # respond based on correct/incorrect answer

    while until and not correct_answer: # repeat
        correct_answer = input(question) == correct
        print(response(correct_answer, correct_return, incorrect_return))


def slow_print(data: str, delay: float):
    # pass
    for char in data:
        sys.stdout.write(char)
        sys.stdout.flush()
        t.sleep(delay)
    print()


def encode_base64(data: str) -> str:
    # return base64 encoded string
    sample_string_bytes = data.encode("ascii")

    encoded_bytes = base64.b64encode(sample_string_bytes)
    final = encoded_bytes.decode("ascii")

    # usage: decode_base64('my_string')
    return final


def decode_base64(data: str) -> str:
    # return base64 decoded string
    base64_bytes = data.encode("ascii")

    decoded_bytes = base64.b64decode(base64_bytes)
    final = decoded_bytes.decode("ascii")

    # usage: decode_base64('my_string')
    return final


def image(name: str):
    with Image.open(name) as im:
        #im.rotate(45).show()
        im.show()


run = lambda string: sb.Popen(string, shell=True) # Run string as command in cmd; run('start cmd.exe /c echo Hello World & timeout /t 5 & pause')
sleep = lambda sec: t.sleep(sec)   # sleep function; sleep(1)
browser = lambda url: wb.open(url)    # open link in browser; browser('url')
alert = lambda msg: py.alert(msg)     # show alert box: alert('message')

if __name__ == "__main__":
    main()