
def reverse_string(string):
    # Reverses a string metrhod 1
    reversed_string = ""
    for i in range(len(string) - 1, -1, -1):
        reversed_string += string[i]

    return reversed_string


print(reverse_string("Hello, world!"))  # Prints !dlrow ,olleH
