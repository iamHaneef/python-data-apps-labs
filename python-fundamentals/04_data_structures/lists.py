# Array working in Python

from array import array

# create an array of integers

num1 = array("i", [1, 2, 3, 4, 5])

num2 = array("i", [1, 2, 3, 4, 5])

for i in num1:
    print(i)

for j in num2:
    print(j)

# ---------------------------------------------------------------------

# Now it was replace by list in most cases

# EX 1
data = [10, "North Street", 10.5, True]

data[0] = 25  # its changed because it's a mutable data type

print(data)

for i in data:
    print(type(i))
    print(i)


# EX 2

values = [{"name": "John", "age": 30}, {"name": "Jane", "age": 25}]

print(values[0]["name"])  # we only access the value only by put it in square brackets

print(values[0]["age"])

print(values[1]["name"])

print(values[1]["age"])

for i in values:
    print(i["name"])

for i in values:
    print(i["age"])

for i in values:
    print(i["name"] + " " + str(i["age"]))
