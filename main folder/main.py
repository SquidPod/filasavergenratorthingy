#this project is a little python script for mr modeegger
#here is the goal that:
# get a random number from 1 to 13, store this number somewhere, for each iteration, this number cant be chosen, maybe
# signal if the iterattion is done, there should be an option to see all previous entrys, all entrys should be deleted if the iteration is done.

import random

max_chars = 13
chosen_chars = []

def view():
    k = chosen_chars
    print(sorted(k))

def make_char():
    a = random.randint(1, max_chars)
    if a in chosen_chars:
        make_char()
    else:
        chosen_chars.append(a)
        print("success!")

def print_to_file():
    with open("lol.txt", "w") as file:
        file.write(str(sorted(chosen_chars)))

# normal questioning
while True:
    cmd = input("select option: \n 1. 'view' for all entries \n 2. 'new' for new char \n 3. 'print' for printing onto txt\n")
    if cmd == "view" or cmd == "new" or cmd == "print":
        if cmd == "view":
            view()
        elif cmd == "new":
            make_char()
        else:
            print_to_file()
    else:
        print("pls check for correct spelling or enter a valid command!")