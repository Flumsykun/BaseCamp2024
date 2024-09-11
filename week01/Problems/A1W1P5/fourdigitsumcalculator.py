#Develop a program that reads a four-digit integer from the user and displays the sum of the digits in the number.
#For example, if the user enters 3141 then your program should display 3+1+4+1=9.

#input
four_digit_number = int(input("Enter a four-digit number:"))

#calculate the sum of the digits
#define thousands, hundreds, tens, and ones into the four-digit number
thousands = four_digit_number // 1000
hundreds = (four_digit_number % 1000) // 100
tens = (four_digit_number % 100) // 10
ones = four_digit_number % 10

#add the digits together
sum_of_digits = thousands + hundreds + tens + ones

#output the sum of the digits with the thousands, hundreds, tens, and ones in the four-digit number
output = "The sum of the digits is: " + str(thousands) + "+" + str(hundreds) + "+" + str(tens) + "+" + str(ones) + "=" + str(sum_of_digits)

#print the output
print(output)
