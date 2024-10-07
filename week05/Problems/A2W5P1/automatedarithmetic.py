import random

# Function to generate arithmetic exercises


def arithmetic_operation(arithmetic_type):
    correct = 0
    incorrect = 0
    mistakes = []  # To store incorrect answers

    for i in range(10):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)

        if arithmetic_type == "summation":
            result = num1 + num2
            print(f"{num1} + {num2} = ")

        elif arithmetic_type == "multiplication":
            result = num1 * num2
            print(f"{num1} * {num2} = ")

        elif arithmetic_type == "subtraction":
            result = num1 - num2
            print(f"{num1} - {num2} = ")

        # Get user input and check the result
        user_result = int(input())

        if user_result == result:
            correct += 1
        else:
            incorrect += 1
            mistakes.append(
                f"{num1} {'+' if arithmetic_type == 'summation' else '*' if arithmetic_type == 'multiplication' else '-'} {num2} = {result}, but you answered {user_result}")

    # Print final result
    print(
        f"You had {correct} correct and {incorrect} incorrect answers in '{arithmetic_type}'.")

    if mistakes:
        print("\nHere are your mistakes:")
        for mistake in mistakes:
            print(mistake)


# Ask the user for the type of arithmetic operation
arithmetic_type = input(
    "Arithmetic operation (summation, multiplication, subtraction): ").lower()

# Run the arithmetic operation function
arithmetic_operation(arithmetic_type)
