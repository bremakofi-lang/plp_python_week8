from utils import todo_list_manager, number_guessing_game, simple_calculator

#==========================================================================================
# TOOL 1: SIMPLE CALCULATOR
# performs basic arithmetic operations (addition, subtraction, multiplication, division).
# Uses: Conditionals (if/elif/else), f-strings, user input handling.
# =========================================================================================


        #==========================================================================================
        # MAIN MENU LOOP
        #Controls program execution, routing choice, and handling invalid input.
        #===========================================================================================
while True:
    print("/n---MAIN MENU---")
    print("1. Simple Calculator")
    print("2. Interactive To-Do List")
    print("3. Number Guessing Game")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ").strip()

    if choice == "1":
        simple_calculator()
    elif choice == "2":
        todo_list_manager()
    elif choice == "3":
        number_guessing_game()
    elif choice == "4":
        print("Thank you for using the Personal Mini-Toolkit. Goodbye!")
        break
    else:
        print(f"Invalid choice: {choice}. is not a valid option. Please choose (1-4).")
