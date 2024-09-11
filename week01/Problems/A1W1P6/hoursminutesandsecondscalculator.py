#Implement a program that a user enters number of days as input,
#and the program prints number of hours,
#minutes and seconds separately as output.

#example
#input
#Enter number of days: 3

#output
#Hours: 72 Minutes: 4320 Seconds: 259200

number_of_days = int(input("Enter number of days: "))
#multiply the number of days by 24 to get the number of hours
hours = number_of_days * 24
#multiply the number of hours by 60 to get the number of minutes
minutes = hours * 60
#multiply the number of minutes by 60 to get the number of seconds
seconds = minutes * 60

#combine the hours, minutes, and seconds into a string
output = "Hours: " + str(hours) + "," + " Minutes: " + str(minutes) + "," + " Seconds: " + str(seconds)

#print the output
print(output)