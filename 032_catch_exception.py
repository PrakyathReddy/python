# Implement the function divide_numbers(a: str, b: str) -> None. It accepts two strings as arguments. You should attempt to convert the strings into integers, and then divide the first number by the second number. And then print the result.

# If an error occurs, print "An error occurred:", followed by the error message.

def divide_numbers(a: str, b: str) -> None:
    try:
        div = int(a)/int(b)
        print(div)
    except Exception as error:
        print(f"An error occurred: {error}")

# do not modify below this line
divide_numbers("10", "2")
divide_numbers("12", "0")
divide_numbers("2", "not a number")
