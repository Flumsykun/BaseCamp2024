import random  # Importing the random module to generate random numbers

# Function to generate and handle arithmetic exercises


def arithmetic_operation(arithmetic_type):
    correct = 0  # Variable to count correct answers
    incorrect = 0  # Variable to count incorrect answers
    mistakes = []  # List to store mistakes (incorrect answers)

    # Loop to generate 10 arithmetic exercises
    for i in range(10):
        # Generate two random numbers between 1 and 100
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)

        # Check the type of arithmetic operation
        if arithmetic_type == "summation":
            result = num1 + num2  # Summation operation
            print(f"{num1} + {num2} = ")  # Display the problem to the user

        elif arithmetic_type == "multiplication":
            result = num1 * num2  # Multiplication operation
            print(f"{num1} * {num2} = ")  # Display the problem to the user

        elif arithmetic_type == "subtraction":
            result = num1 - num2  # Subtraction operation
            print(f"{num1} - {num2} = ")  # Display the problem to the user

        # Get the user's answer for the arithmetic problem
        user_result = int(input())  # Convert the input to an integer

        # Check if the user's answer is correct
        if user_result == result:
            correct += 1  # Increment correct counter if the answer is correct
        else:
            incorrect += 1  # Increment incorrect counter if the answer is wrong
            # Store the incorrect answer details in the mistakes list
            mistakes.append(
                f"{num1} {'+' if arithmetic_type == 'summation' else '*' if arithmetic_type == 'multiplication' else '-'} {num2} = {result}, but you answered {user_result}")

    # After the loop, print the total correct and incorrect answers
    print(
        f"You had {correct} correct and {incorrect} incorrect answers in '{arithmetic_type}'.")

    # If there are any mistakes, print them out
    if mistakes:
        print("\nHere are your mistakes:")
        for mistake in mistakes:
            print(mistake)


# Main entry point for the script
if __name__ == "__main__":
    # Ask the user for the type of arithmetic operation they want to practice
    arithmetic_type = input(
        "Arithmetic operation (summation, multiplication, subtraction): ").lower()

    # Call the function to generate and check the arithmetic exercises
    arithmetic_operation(arithmetic_type)
