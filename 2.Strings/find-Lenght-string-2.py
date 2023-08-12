#  input from user 
def string_length(input_string):
    length = len(input_string)
    return length

user_input = input("Enter a string: ")
length_result = string_length(user_input)
print("The length of the string is:", length_result)
