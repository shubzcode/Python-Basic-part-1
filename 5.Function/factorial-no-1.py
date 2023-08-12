def factorial(n):
    # Calculates the factorial of a number.
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

#  already defines number
print(factorial(4))  # Prints 120
