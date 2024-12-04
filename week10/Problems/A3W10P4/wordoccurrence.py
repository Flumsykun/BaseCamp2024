# Step-by-Step Guide to Solve the Word Occurrences Problem in CodeGrade
# Understand the Problem:

# You need to read a file provided by the user.
# Count how often each word appears in the file.
# Display the word(s) that appear most and least frequently.
# Handle various forms of the same word as identical (e.g., apple, Apple! are the same).
# Handle errors if the file cannot be opened.

# Steps to Solve
# 1. Read the File Name
# Prompt the user to enter the name of the file.
# Handle file opening. If the file doesn't exist or can't be opened, display an error message.
file = input("Enter the name of the file: ")
try:
    with open(file, 'r') as f:
        content = f.read()
except FileNotFoundError:
    print("File not found.")



# 2. Read the File Content Line by Line
# For each line in the file, split the line into words by spaces.
# Ensure you read all lines of the file.



# 3. Normalize the Words
# For each word:
# Convert it to lowercase.
# Remove any leading or trailing punctuation (like .,!?;).
# Treat words like apple,, Apple!, apple as the same.
convert_words = []  # Initialize empty list
for line in content.split('\n'):
    words = line.split()
    for word in words:
        word = word.lower().strip('.,!?;')  # Normalize the word
        convert_words.append(word)  # Append normalized word to the list

# 4. Count Word Occurrences
# Use a data structure to count how often each word appears (e.g., a dictionary).
# Store each word as a key and its occurrence count as the value.
count_word = {}
for word in convert_words:
    if word in count_word:
        count_word[word] += 1
    else:
        count_word[word] = 1

# 5. Identify Most and Least Frequent Words
# Find the highest and lowest counts from the dictionary.
# Identify the words that match these counts (multiple words might share the same frequency).
most_frequent_words = []
least_frequent_words = []

for word, count in count_word.items():
    if count == max(count_word.values()):
        most_frequent_words.append(word)
    if count == min(count_word.values()):
        least_frequent_words.append(word)



# 6. Display the Results
# Print the most frequent word(s).
# Print the least frequent word(s).
# If there is a tie for most or least frequent, display all tied words as a list.
if __name__ == "__main__":
    display_results = []
    if len(most_frequent_words) > 1:
        display_results.append(f"Most frequent word(s): {most_frequent_words}")
    else:
        display_results.append(f"Most frequent word(s): {most_frequent_words[0]}")

    if len(least_frequent_words) > 1:
        display_results.append(f"Least frequent word(s): {least_frequent_words}")
    else:
        display_results.append(f"Least frequent word(s): {least_frequent_words[0]}")

    for result in display_results:
        print(result)


# 7. Handle Errors
# If the file cannot be opened (e.g., it doesn't exist), display an error message like:
# javascript
# Copy code
# Error reading file: "filename"
# Example Flow:
# User Input:
#
# Enter file name: randomtext.txt
# File Processing:
#
# Normalize words: Apple! -> apple
# Count word occurrences.
# Output:
#
# Most frequent word(s): ['so']
# Least frequent word(s): ['remarkably', 'solicitude', 'mean']
# Error Handling:
#
# If the file is missing: Error reading file: "blanc"
# By following these steps, you should be able to solve this assignment independently without relying on direct code.