#this project is a little python script for mr modeegger
#here is the goal that:
# get a random number from 1 to 13, store this number somewhere, for each iteration, this number cant be chosen, maybe
# signal if the iteration is done, there should be an option to see all previous entrys, all entrys should be deleted if the iteration is done.

import random
import os

max_chars = 13
file_name = "lol.txt"

# Initialize chosen_chars from file or create a new list
try:
    with open(file_name, "r") as file:
        chosen_chars = list(map(int, file.read().strip().split(',')))
except ValueError:
    print("File content is invalid. Resetting entries.")
    chosen_chars = []


def view():
    print("Current entries:", sorted(chosen_chars) if chosen_chars else "No entries yet.")

def make_char():
    while True:
        new_char = random.randint(1, max_chars)
        if new_char not in chosen_chars:
            chosen_chars.append(new_char)
            print(f"Generated character: {new_char}")
            print_to_file()
            break
        else:
            print(f"Character {new_char} already chosen. Retrying...")

def print_to_file():
    with open(file_name, "w") as file:
        file.write(','.join(map(str, sorted(chosen_chars))))

def reset_entries():
    global chosen_chars
    chosen_chars = []
    with open(file_name, "w") as file:
        file.write("")
    print("All entries have been cleared.")

# Command interface
while True:
    cmd = input("Select an option: \n 1. 'view' to see all entries \n 2. 'new' to generate a new character \n 3. 'reset' to clear entries \n 4. 'exit' to quit\n").strip().lower()
    if cmd == "view":
        view()
    elif cmd == "new":
        make_char()
    elif cmd == "reset":
        reset_entries()
    elif cmd == "exit":
        print("Goodbye!")
        break
    else:
        print("Invalid command. Please try again.")
