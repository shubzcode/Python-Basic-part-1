# Sorting a Dictionary by Value:
#  using weight

dictionary = {"apple": 10, "banana": 50, "cherry": 30}

sorted_dictionary = sorted(dictionary.items(), key=lambda x: x[1])

print(sorted_dictionary)  # Prints [(cherry, 30), (banana, 20), (apple, 10)]
