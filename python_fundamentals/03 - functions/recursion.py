def factorial(n):

    if n < 0:
        return "The Given Number is Negative Number"

    if n in (0, 1):
        return 1

    return n * factorial(n - 1)


print("The factorial of 5 is : ", factorial(5))


def fibonacci(n):

    if n in (0, 1):
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


for i in range(10):
    print(fibonacci(i), end=" ")
