#sorting method 2 
#sorted by value 
def sort_dict_by_value(dictionary):
    sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[1]))
    return sorted_dict

my_dict = {'apple': 5, 'banana': 3, 'cherry': 8}
sorted_by_value = sort_dict_by_value(my_dict)
print("Dictionary sorted by value:", sorted_by_value)
