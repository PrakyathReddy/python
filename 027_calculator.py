# Task: Create a Python file that stores two numbers in variables, performs basic math operations on them (addition, subtraction, multiplication, division), and prints out each result.

# get those 2 numbers from user
# perform operations on them
import sys

try:
    n1 = float(input("enter first number: "))
    n2 = float(input("enter second number: "))
except ValueError:
    print("Please enter valid numeric value")
    sys.exit(1)

add = n1 + n2
sub = n1 - n2
mul = n1 * n2
div = n1 / n2
mod = n1 % n2

print(add, sub, mul, div, mod, sep="\n")