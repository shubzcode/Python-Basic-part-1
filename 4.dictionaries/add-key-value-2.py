def add_to_dictionary(dictionary, key, value):
    dictionary[key] = value
    return dictionary

my_dict = {'a': 1, 'b': 2, 'c': 3}
new_key = input("Enter a new key: ")
new_value = input("Enter a corresponding value: ")
updated_dict = add_to_dictionary(my_dict, new_key, new_value)
print("Updated dictionary:", updated_dict)