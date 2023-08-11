def exponentiation(a, b):
    result = a ** b
    return result
#  input from user 
base = float(input("Enter the base: "))
exponent = float(input("Enter the exponent: "))
exp_result = exponentiation(base, exponent)
print("The result of", base, "raised to the power of", exponent, "is:", exp_result)
