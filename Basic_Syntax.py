# Python Syntax for all Fundamentals

# print Statement

# print("Welcome to Python Learning")
# print("TECH BOY")

# multi line print

# print("""
# Shall we try
# one more
# Time !!
# """)

# -------------------------------------------------------------------------------------

# Get input from User

# String Input

# name = input("What is Your Full Name ? ")
# print("The Full Name is : ", name)

# # Integer Input
# age = int(input("What is your Age ? "))
# print("The Age is : ", age)

# # Float Input
# salary = float(input("What is your Salary ? "))
# print("The salary amount is : ", salary)

# # String Input
# Initial = input("What is Your Initial ? ")[0]
# print("The Name Initial is : ", Initial)


# -------------------------------------------------------------------------------------

# Variable Declaration and Basic Arithmetic Opeartions

# a = 10
# b = 20

# Author_name = "BatMan"
# power = "Being Rich"

# print(f"Addition of {a} and {b} is", a + b)
# print(f"Substraction of {a} and {b} is", a - b)
# print(f"Multiplication of {a} and {b} is", a * b)
# print(f"Division of {a} and {b} is", a / b)
# print(f"Modulus of {a} and {b} is", a % b)

# -------------------------------------------------------------------------------------

# If condition

# purchase_amount = float(input("Enter the Purchase Amount this month :"))

# if purchase_amount < 2000:
#     print("5% Discount is ", purchase_amount * 0.05)
#     print(
#         "Total Amount include 5 % Discount is ",
#         purchase_amount - (purchase_amount * 0.05),
#     )

# elif purchase_amount >= 2000 and purchase_amount < 6000:
#     print("20 % Discount is ", purchase_amount * 0.20)
#     print(
#         "Total Amount include 20 % Discount is ",
#         purchase_amount - (purchase_amount * 0.20),
#     )

# else:
#     print(
#         "Total Amount include 50 % Discount is ",
#         purchase_amount - (purchase_amount * 0.50),
#     )


# -------------------------------------------------------------------------------------


# Looping Statement

# for loop

# arr1 = [2, 4, 6, 8, 10]

# for i in range(len(arr1)):
#     print(arr1[i])

# # while loop

# i = 0
# while i < len(arr1):
#     print(arr1[i])
#     i += 1

# # Ternary Operator

# value = 100

# answer = True if value >= 100 else 200
# print(answer)

# -------------------------------------------------------------------------------------

# Function -> Most Important Topics


def factorial(n):

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


print("The factorial of 5 is : ", factorial(5))

unsorted = [23, 1, 56, 33, 99, 10]


def AscSort(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    print("The Ascending Sorted Array is : ", arr)


def DescSort(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] < arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    print("The Descending Sorted Array is : ", arr)


AscSort(unsorted)
DescSort(unsorted)
