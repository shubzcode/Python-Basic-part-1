def division(a, b):
    if b == 0:
        return "Cannot divide by zero"
    result = a / b
    return result
# User input values
num1 = float(input("Enter the numerator: "))
num2 = float(input("Enter the denominator: "))
div_result = division(num1, num2)
print("The division result is:", div_result)
