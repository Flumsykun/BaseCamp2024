def fizzBuzz(n):


# Ask the user for a number
i = int(input("Enter a digit: "))

# Check if the number is divisible by both 3 and 5
if i % 3 == 0 and i % 5 == 0:
    print("FizzBuzz")
elif i % 3 == 0:
    print("Fizz")
elif i % 5 == 0:
    print("Buzz")
else:
    print(i)
if __name__ == '__main__':
