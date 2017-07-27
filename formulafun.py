# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# Example
# Let us assume the following comma separated input sequence is given to the program:
# 100,150,180
# The output of the program should be:
# 18,22,24

## DOES NOT WORK ####

def form_fun():
    import math
    x = input("Please enter a list of integer values seperated by commas: ")
    c = 50
    h = 30
    x = list(x)
    a = len(x)
    y = []
    for i in range(a):
        y.append(str(int(round(math.sqrt(2 * c * float(x[i]) / h)))))
    i = i + 1
    return y

form_fun()
