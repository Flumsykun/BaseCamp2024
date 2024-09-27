# There are numerous phrases that are palindromes when spacing is ignored.
# Examples include “go dog”, “flee to me remote elf” and “some men interpret nine memos”, among many others.
# Write a program that ignores spacing while determining whether or not a string is a palindrome

# Extra (additional challenge):
# Extend your solution so that is also ignores punctuation marks (like , . ? ! ;)
# Extend your solution so that it treats uppercase and lowercase letters as equivalent.
# Input example:
# Sentence: go dog
# Sentence: some men interpret nine memos
# Sentence: some random sentence
# Output example:
# "go dog" is a palindrome
# "some men interpret nine memos" is a palindrome
# "some random sentence" is not a palindrome

sentence = input("Sentence: ")

# Remove all non-alphanumeric characters from the input string
sentence = ''.join(e for e in sentence if e.isalnum())

# Convert the input string to lowercase
sentence = sentence.lower()

# Check if the input string is a palindrome

if sentence == '':
    print('Empty string is not a palindrome')
else:
    reversed_sentence = ''
    for char in sentence:
        reversed_sentence = char + reversed_sentence
    if sentence == reversed_sentence:
        print(f'"{sentence}" is a palindrome')
    else:
        print(f'"{sentence}" is not a palindrome')