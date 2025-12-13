x = "awesome"

def my_func():
    x="fantastic"
    print("python is",x)

my_func()
print("python is",x)

def global_func():
    global x
    x="super"
    print("python is",x)

my_func()
global_func()
print("python is",x)