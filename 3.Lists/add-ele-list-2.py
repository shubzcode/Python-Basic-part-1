# Adding elements to a list user input
def add_element(list, element):
    list.append(element)
    return list
# list alredy defins 
my_list = [1, 2, 3, 4, 5] #givn list
new_element = int(input("Enter an element to add to the list: "))
updated_list = add_element(my_list, new_element)
print("Updated list:", updated_list)
