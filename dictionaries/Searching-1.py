dictionary = {"name": "ganpat rav apte", "age": 30, "occupation": "hotel manager"}

key = "name"

if key in dictionary:
    value = dictionary[key]
    print(value)  # Prints ganpat rav apte
else:
    print("The key does not exist in the dictionary.")
