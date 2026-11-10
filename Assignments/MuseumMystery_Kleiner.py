"""
Name: Sarah Kleiner
Course: MCON 141
Assignment: Museum Mystery
Museum Breakout Challenges. The player solves three puzzles to find the code.
"""
# Creates the menu display
def show_menu(name, energy, clue_count):
    print()
    print("=================================")
    print("     THE GREAT MUSEUM MYSTERY")
    print("=================================")
    print()
    print(f"Welcome, {name}!")
    print(f"Energy: {energy}")
    print(f"Clues collected: {clue_count} of 3")
    print("1. Enter Gallery 1")
    print("2. Enter Gallery 2")
    print("3. Enter Gallery 3")
    print("4. View collected clues")
    print("5. Attempt to escape")
    print("6. Quit the museum")
    print()

# Creates a function that validates every integer input
def get_number(prompt, low, high):
    while True:
        text = input(prompt)
        try:
            number = int(text)

            if number < low or number > high:
                raise ValueError("Number out of range")
            return number
        except ValueError:
            print("Invalid input. Please enter a number in range.")
            print("No energy was lost.")

# Subtracts from total energy when user makes a mistake, and ensures that energy level is never negative
def reduce_energy(energy, cost):
    energy -= cost

    if energy < 0:
        energy = 0
    return energy

# The first puzzle
def gallery_one():
    print()
    print("--- GALLERY 1: THE ANCIENT NUMBERS ROOM ---")
    print("A stone tablet with a golden scarab guards a lock.")
    print("The curator's note reads:")
    print()
    print("  'The lock needs a THREE-DIGIT code.'")
    print("  'The three digits add up to 12.'")
    print("  'The code can be divided evenly by 5.'")
    print("  'The first digit is twice the second digit.'")
    print("  'No digit is repeated.'")
    print()

    answer = get_number("Enter the three-digit code: ", 100, 999)

    first = answer // 100
    second = (answer // 10) % 10
    third = answer % 10

    digits_add_to_12 = (first + second + third == 12)
    divisible_by_5 = (answer % 5 == 0)
    first_is_double = (first == second * 2)
    all_different = (first != second and first != third and second != third)

    if digits_add_to_12 and divisible_by_5 and first_is_double and all_different:
        print("The scarab's eyes glow. The lock clicks open!")
        return True
    else:
        print("The tablet rumbles. That code is incorrect.")
        return False

# The second puzzle
def gallery_two():
    print()
    print("--- GALLERY 2: THE CLOCKWORK CODE ---")
    print("A giant clock ticks loudly. It's gears show these numbers:")
    print()

    sequence = []
    number = 3

    for i in range(6):
        sequence.append(number)
        number *= 2

    shown = ""

    for i in range(4):
        shown += f"{sequence[i]} "

    print(f"   {shown}...")
    print()
    print("The curator's note reads:")
    print("  'Find the pattern. What is the TOTAL of the first")
    print("   SIX numbers in this sequence?'")
    print()

    total = 0
    for value in sequence:
        total += value

    answer = get_number("Enter the total: ", 0, 100000)

    if answer == total:
        print("The gears spin and a small drawer slides open!")
        return True
    else:
        print("The clock chimes angrily. That total is not right.")
        return False

# The third puzzle
def gallery_three():
    print()
    print("--- GALLERY 3: THE LOGIC CHAMBER ---")
    print("Three levers, A, B, and C, stick out of the wall.")
    print("A brass owl holds the curator's rule:")
    print()
    print("  'The passage opens if (A is UP and B is NOT up)")
    print("   or if C is UP.'")
    print()
    print("1. A UP,   B UP,   C DOWN")
    print("2. A DOWN, B DOWN, C DOWN")
    print("3. A UP,   B DOWN, C DOWN")
    print()

    choice = get_number("Which option opens the passage? (1-3): ", 1, 3)

    a_up = (choice == 1 or choice == 3)
    b_up = (choice == 1)
    c_up = False

    if (a_up and not b_up) or c_up:
        print("The wall slides away, revealing a secret passage!")
        return True
    else:
        print("Nothing happens. The owl stares at you.")
        return False

# Makes sure that each clue is only given once, and adds the clue to the list of clues
def award_clue(clues, clue):
    if clue in clues:
        print("You already have this clue.")

    else:
        clues.append(clue)
        print(f"You have found a clue! {clue}")

# Shows the clues to the user
def show_clues(clues):
    print()
    print("--- YOUR CLUES ---")

    if len(clues) == 0:
        print("You have not received any clues yet. Try again!")

    else:
        number = 1
        for clue in clues:
            print(f"{number}. {clue}")
            number += 1

        print()
        print("Hint: The security code uses the clue digits")
        print("in gallery order (Gallery 1, then 2, then 3).")

# Allows the user to enter their code and try to escape
def attempt_escape(clues, all_clues, energy, secret_code):
    print()
    print("--- THE SECURITY EXIT ---")

    if len(clues) < 3:
        print("The security panel is dark. You are missing these clues:")

        for clue in all_clues:
            if clue not in clues:
                print(f"  - {clue}")
        return "Locked"

    if energy < 1:
        print("You are too tired to escape.")
        return "Locked"

    print("The panel lights up and asks for a 3-digit security code.")
    code = get_number("Enter the security code: ", 0, 999)

    if code == secret_code:
        return "win"

    else:
        print("The alarm buzzes.")
        return "wrong"

# The winning message
def show_win_ending(name, energy):
    print()
    print("==================================")
    print("       YOU ESCAPED!")
    print("==================================")
    print()
    print(f"Congratulations, {name}!")
    print()
    print("You collected all three clues,")
    print("disabled the museum security system,")
    print(f"and escaped with {energy} energy points!")
    print()
    print("The curator would be proud.")
    print("==================================")

# The losing message
def show_lose_ending(name, clue_count):
    print()
    print("==================================")
    print("       GAME OVER")
    print("==================================")
    print()
    print(f"Sorry, {name}. You ran out of energy.")
    print(f"You collected {clue_count} of 3 clues.")
    print("You curl up on a bench and wait for the")
    print("morning guard to unlock the doors...")
    print("==================================")

# The mutation that shows that appending to a list mutates but rebinding doesn't change original, only local
def mutation_demo(items):
    items.append("NEW ITEM")
    print(f"Inside function after append: {items}")
    items = ["A", "COMPLETELY", "NEW", "LIST"]
    print(f"Inside function after rebinding: {items}")

# Runs the demo
def run_demo():
    print("===== MUTATION vs REBINDING DEMO =====")
    demo_list = ["OLD ITEM"]
    print(f"Before function: {demo_list}")
    mutation_demo(demo_list)
    print(f"After function: {demo_list}")
    print("======================================")
    print()

# The intro to the game, all the options that the user could choose, lets them play in whatever order, gives the code, shows the energy, clues, etc.
def main():
    all_clues = ["GOLDEN SCARAB (Gallery 1) - digit 4",
                 "BRASS GEAR (Gallery 2) - digit 7",
                 "SILVER OWL (Gallery 3) - digit 2"]
    secret_code = 472

    energy = 10
    clues = []
    solved = [False, False, False]

    print("It's 5:59 PM. The museum is closing...")
    print("The alarms switch on and the exit doors lock behind you!")
    print("The curator left puzzles behind. Solve them to escape.")
    print()
    name = input("What is your name? ")
    if name == "":
        name = "Explorer"

    playing = True
    while playing:
        show_menu(name, energy, len(clues))
        choice = get_number("Choose an option: ", 1, 6)

        if choice == 1 or choice == 2 or choice == 3:
            gallery_index = choice - 1

            if solved[gallery_index]:
                print()
                print(f"You already solved Gallery {choice}.")
                print("Nothing new here. (No energy was lost.)")
            else:
                if choice == 1:
                    result = gallery_one()
                elif choice == 2:
                    result = gallery_two()
                else:
                    result = gallery_three()

                if result:
                    solved[gallery_index] = True
                    award_clue(clues, all_clues[gallery_index])
                else:
                    energy = reduce_energy(energy, 1)
                    print(f"You lost 1 energy point. Energy left: {energy}")
                    if energy > 0:
                        print("You may try this gallery again from the menu.")

        elif choice == 4:
            show_clues(clues)

        elif choice == 5:
            outcome = attempt_escape(clues, all_clues, energy, secret_code)
            if outcome == "win":
                show_win_ending(name, energy)
                playing = False
            elif outcome == "wrong":
                energy = reduce_energy(energy, 1)
                print(f"You lost 1 energy point. Energy left: {energy}")

        else:
            print()
            print(f"You give up and wait for morning. Goodbye, {name}!")
            playing = False

        if playing and energy == 0:
            show_lose_ending(name, len(clues))
            playing = False
run_demo()
main()

# 1. Gallery three, because it was hard to figure out how to show the user the options.
# 2. If the user entered the correct secret code, I used return win, and it displayed the winning message.
# 3. Appending mutates the list but rebinding doesn't, it only changes locally.
# 4. When I created the return for the winning or losing message, I capitalized the first letter, but in main, when it was called, it was in lowercase.
