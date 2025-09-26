import sys

def add(num1, num2):
    add = num1 + num2
    return add

def sub(num1, num2):
    sub = num2 - num1
    return sub

num1=int(sys.argv[1])
num2=int(sys.argv[3])
operation=sys.argv[2]

if operation == "add":
    output=add(num1,num2)
    print(output)
elif operation == "sub":
    output=sub(num1,num2)
    print(output)