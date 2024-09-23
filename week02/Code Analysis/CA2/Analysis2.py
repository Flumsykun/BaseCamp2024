numstr = input("enter a 4 digit number")
# sum = 0
# text = ""
# for i in range(len(numstr)):
#    sum += int(numstr[i])
#    text = text + numstr[i]
# print(text)

if len(numstr) != 4 or not numstr.isdigit():
    print("Please enter a valid four-digit number.")
else:
    sum_result = 0
    text = ""

    # Constructing the text with '+' and calculating the sum
    for i in range(len(numstr)):
        sum_result += int(numstr[i])
        if i < len(numstr) - 1:
            text += numstr[i] + "+"
        else:
            text += numstr[i]

    print(f"{text} = {sum_result}")
