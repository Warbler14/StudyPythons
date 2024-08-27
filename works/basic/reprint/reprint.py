import time
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


message = "Hello World"

print(message)

time.sleep(1)

os.system('clear')

message = "Goodbye World"

print(message)
