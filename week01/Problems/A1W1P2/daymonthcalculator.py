#convert years to months and days
#input: years
#output: months and days
years = int(input("Enter a number of years: "))
months = years * 12 #convert years to months
days = years * 365 #convert years to days
output = "Months: " + str(months)+"," + " Days: " + str(days)
print(output)
