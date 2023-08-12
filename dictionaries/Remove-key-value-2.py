# Another method 
def remove_from_dictionary(dictionary, key):
    if key in dictionary:
        del dictionary[key]
    return dictionary

my_dict = {'apple': 5, 'banana': 3, 'cherry': 8}
key_to_remove = input("Enter a key to remove: ")
updated_dict = remove_from_dictionary(my_dict, key_to_remove)
print("Updated dictionary:", updated_dict)
