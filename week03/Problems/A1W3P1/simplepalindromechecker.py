# Assignment description
# A string is a palindrome if it is identical forward and backward.
# For example “anna”, “civic”, “level” and “hannah” are all examples of palindromic words.
# Write a program that reads a string from the user and uses a loop to determines whether or not it is a palindrome.
# Display the result, including a meaningful output message.

# Extra (additional challenge):
# Extend your solution so that is also ignores punctuation marks (like , . ? ! ;)
# Extend your solution so that it treats uppercase and lowercase letters as equivalent.
# Input example:
# String: anna
# String: hannah
# String: lepels
# Output example:
# "anna" is a palindrome
# "hannah" is a palindrome
# "lepels" is not a palindrome

"""
ik mocht geen gebruik maken van string slicing shortcuts
en daar ben ik zoutig over
"""

#ask the user to enter 3 strings in a list
#empty string should not be a palindrome
#initialize the list
#strings = []

#ask the user to enter 3 strings
# for i in range(3):
#     strings.append(input("String: "))
string = input("String: ")
#check if the string is a palindrome
# for string in strings:
    #remove punctuation marks
string = ''.join(e for e in string if e.isalnum())
    #convert the string to lowercase
string = string.lower()
    #check if the string is a palindrome
if string == '':
        print('Empty string is not a palindrome')
else:
        #manually reverse the string
        reversed_string = ''
        for char in string:
            reversed_string = char + reversed_string
        if string == reversed_string:
            print(f'"{string}" is a palindrome')
        else:
            print(f'"{string}" is not a palindrome')
            
    # elif string == string[::-1]:
    #     print(f'"{string}" is a palindrome')
    # else:
    #     print(f'"{string}" is not a palindrome')
        
        #     else:
        # print(f'"{string}" is not a palindrome')
        # elif string == '':
        #     print('Empty string is not a palindrome')