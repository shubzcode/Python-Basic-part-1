def contains_substring(string, substring):
    # Checks if a string contains a certain substring.
    return substring in string


print(contains_substring("Hello, world!", "world"))  # True
print(contains_substring("Hello, world!", "hello"))  # False
