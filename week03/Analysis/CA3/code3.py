# Code 3
sentence = "I just came to say hello!"
count = 0
for letter in sentence:
   if letter == " ":
       count = count + 1
   elif letter == "a":
       count = count - 1
print(count)

# •	Expected Output:
# o	Each space increments count.
# o	Each letter 'a' decrements count.
# o	The sentence has 5 spaces and 2 'a' letters, so count becomes 5 - 2 = 3.
# o	Output: 3.
