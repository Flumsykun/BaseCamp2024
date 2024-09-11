#An online retailer sells two products: widgets and gizmos.
#Write a program that reads the number of widgets and the number of gizmos in an order from the user.
#Then your program should compute and display the total weight of the order.

#Each widget weighs 75 grams.
#Each gizmo weighs 112 grams.

#Your program should display the total weight of the order in grams.

input_widgets = int(input("Enter the number of widgets: "))
input_gizmos = int(input("Enter the number of gizmos: "))

output = "The total weight of the order is: " + str((input_widgets * 75) + (input_gizmos * 112)) + " grams"
print(output)