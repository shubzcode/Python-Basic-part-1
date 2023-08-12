#  using user input 
def check_substring(main_string, substring):
    if substring in main_string:
        return True
    else:
        return False

main_str = input("Enter the main string: ")
sub_str = input("Enter the substring to check: ")

if check_substring(main_str, sub_str):
    print("The main string contains the substring.")
else:
    print("The main string does not contain the substring.")
