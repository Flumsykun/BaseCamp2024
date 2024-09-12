# Code Analysis 1
# Inputs
a = int(input("enter value A: "))
b = int(input("enter value B: "))

# Processing
t = a
a = b
b = t

# Outputs
print("A =", a)
print("B =", b)

# By looking at the results it seems that when given a value the interpreter switches
# the values around  with a temporary variable t, t = a stores the value of a in t a = b
# assigns the value of b to a, b = t puts the value stored in t (which is also the
# original value of a) to b. resulting in swapped outputs so A = 3 and B = 2
