# Implement the divide_numbers(a: str, b: str) -> None function. It accepts two strings as arguments. You should attempt to convert the strings into integers, and then divide the first number by the second number, and then print the result.

# If a ValueError occurs, print "Error: Invalid value!".
# If a ZeroDivisionError occurs, print "Error: Division by zero!".
# If any other error occurs, print "An error occurred:", followed by the error message.

def divide_numbers(a: str, b: str) -> None:
    try:
        print(int(a)/int(b))
    except ValueError:
        print("Error: Invalid value!")
    except ZeroDivisionError:
        print("Error: Division by zero!")
    except Exception as error:
        print(f"An error occurred: {error}")



# do not modify below this line
divide_numbers("10", "2")
divide_numbers("12", "0")
divide_numbers("2", "not a number")
