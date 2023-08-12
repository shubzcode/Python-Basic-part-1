def fibonacci(n):
    #   Prints the Fibonacci sequence up to a given number.
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
        print(a)

# value define in code
fibonacci(10)  # Prints 0 1 1 2 3 5 8 13 21 34 55