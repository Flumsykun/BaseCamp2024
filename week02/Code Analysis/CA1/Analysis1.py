fourdigit_num = int(input("Input a four digit number: "))
# x  = fourdigit_num // 1000
# x1 = (fourdigit_num - x * 1000) // 100
# x2 = (fourdigit_num - x * 1000 - x1 * 100) // 10
# x3 = fourdigit_num - x * 1000 - x1 * 100 - x2 * 10
# print("Sum:",x+x1+x2+x3)

if len(fourdigit_num) != 4 or not fourdigit_num.isdigit():
    print("Please enter a valid four-digit number.")
else:
    x = int(fourdigit_num[0])
    x1 = int(fourdigit_num[1])
    x2 = int(fourdigit_num[2])
    x3 = int(fourdigit_num[3])
    
    total_sum = x + x1 + x2 + x3
    print(f"{x} + {x1} + {x2} + {x3} = {total_sum}")
