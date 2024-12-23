import random

max_chars = 13
chosen_chars = []

def view():
    print("Current entries:", sorted(chosen_chars) if chosen_chars else "No entries yet.")

def make_char():
    while True:
        new_char = random.randint(1, max_chars + 1)
        if new_char not in chosen_chars:
            chosen_chars.append(new_char)
            print(f"Generated character: {new_char}")
            break
        else:
            pass

# Command interface
while True:
    cmd = input("Select an option: \n 1. 'view' or 'v' to see all entries \n 2. 'new' or 'n' to generate a new character "
                "\n 3. 'reset' or 'r' to clear entries \n 4. 'exit' or 'x' or 'q' to quit\n").strip().lower()
    if cmd == "view" or cmd == "v":
        view()
    elif cmd == "new" or cmd == "n":
        make_char()
    elif cmd == "reset" or cmd == "r":
        chosen_chars = []
        print("All entries have been cleared.")
    elif cmd == "exit" or cmd == "x" or cmd == "q":
        print("Goodbye!")
        break
    else:
        print("Invalid command. Please try again.")
