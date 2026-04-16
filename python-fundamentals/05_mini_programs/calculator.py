def calculator():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    op = input("Enter the Operator (+, -, *, /):  ")

    if op == "+":
        return num1 + num2

    elif op == "-":
        return num1 - num2

    elif op == "*":
        return num1 * num2

    elif op == "/":
        return num1 / num2 if num2 != 0 else "Cannot divide this denominator is zero"

    return "Invalid Input from User"


print(calculator())
