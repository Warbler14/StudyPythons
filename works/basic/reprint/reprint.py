import time
import os

# ! enable Emulate terminal in output console option for this run configuration

def clear_screen():
    if os.name == 'nt':
        os.system('cls')  # For Windows
    else:
        os.environ['TERM'] = 'xterm'  # Set TERM to 'xterm' for other platforms like macOS and Linux
        os.system('clear')


message = "Hello World"
print(message)

time.sleep(1)
clear_screen()

message = "Goodbye World"
print(message)
