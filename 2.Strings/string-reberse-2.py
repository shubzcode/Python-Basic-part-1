# User input using
def reverse_string(input_string):
    reversed_str = input_string[::-1]
    return reversed_str

user_input = input("Enter a string: ")
reversed_result = reverse_string(user_input)
print("The reversed string is:", reversed_result)
