def search_key(dictionary, key):
    if key in dictionary:
        return True
    else:
        return False
# user input
my_dict = {'one': 1, 'two': 2, 'three': 3}
search_key_str = input("Enter a key to search for: ")
if search_key(my_dict, search_key_str):
    print("Key found in the dictionary.")
else:
    print("Key not found in the dictionary.")