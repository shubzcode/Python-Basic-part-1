# Removing elements from a list:
def remove_element(lst, element):
    if element in lst:
        lst.remove(element)
    return lst

my_list = [10, 20, 30, 40, 50]
element_to_remove = int(input("Enter an element to remove from the list: "))
updated_list = remove_element(my_list, element_to_remove)
print("Updated list:", updated_list)
