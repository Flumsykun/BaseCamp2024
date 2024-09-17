# Write a program that reads an integer from the user. Then your program should display a message indicating whether the integer is even or odd.

# Input examples:
# Number: 1
# Number: 4
# Output examples:
# Odd
# Even

even_or_odd = int(input("Number:"))

if even_or_odd % 2 == 0:
    print("Even")
else:
    print("Odd")
    
output = "Even" if even_or_odd % 2 == 0 else "Odd"
print(output)