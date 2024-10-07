# A primary school teacher needs to automate basic arithmetic (summation, multiplication table, subtraction) exercises for her students. You are asked to implement a program that asks what type of the arithmetic the user needs to practice. Then, the program will generate exercises and the user should give the result.

# Criteria:
# For each arithmetic operation keep the total number of the exercises 10
# The program must be interactive (generate random numbers for each operation, use random module)
# Your program must be implemented with a function arithmetic_operation(arithmetic_type)
# The artihmetic_type can be (summation, multiplication, subtraction)
# Numbers for summation, subtractions and multiplications will be between 1 and 100
# Collect all the mistakes from the user and print them at the end

# Input example:
# Arethmetic operation: summation
# 1 + 4 = 4
# 3 + 3 = 6
# 6 + 2 = 8
# 5 + 1 = 7
# 3 + 8 = 8
# 5 + 4 = 9
# 8 + 3 = 10
# 1 + 6 = 7
# 3 + 9 = 11
# Output example:
# You had 4 correct and 6 incorrect answers in "summation"

import random
# ask user for the type of arithmetic operation
arithmetic_type = input("Arethmetic operation: ")

# function to generate random numbers

def arithmetic_operation(arithmetic_type):
    correct = 0
    incorrect = 0
    for i in range(10):
        if arithmetic_type == "summation":
            num1 = random.randint(1, 100)
            num2 = random.randint(1, 100)
            result = num1 + num2
            print(f"{num1} + {num2} = ")
            user_result = int(input())
            if user_result == result:
                correct += 1
            else:
                incorrect += 1
        elif arithmetic_type == "multiplication":
            num1 = random.randint(1, 100)
            num2 = random.randint(1, 100)
            result = num1 * num2
            print(f"{num1} * {num2} = ")
            user_result = int(input())
            if user_result == result:
                correct += 1
            else:
                incorrect += 1
        elif arithmetic_type == "subtraction":
            num1 = random.randint(1, 100)
            num2 = random.randint(1, 100)
            result = num1 - num2
            print(f"{num1} - {num2} = ")
            user_result = int(input())
            if user_result == result:
                correct += 1
            else:
                incorrect += 1
    print(
        f"You had {correct} correct and {incorrect} incorrect answers in {arithmetic_type}")
