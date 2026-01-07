# Implement the function divide_numbers(a: int, b: int) -> None. It should attempt to divide a by b and print the result. If an error occurs, print "An error occurred!".

def divide_numbers(a: int, b: int) -> None:
    try:
        print(a/b)
    except:
        print("An error occurred!")



# do not modify below this line
divide_numbers(10, 2)
divide_numbers(12, 3)
divide_numbers(2, 0)
