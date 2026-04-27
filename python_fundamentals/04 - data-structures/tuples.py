# Tuples

fruits = ("apple", "banana", "cherry")

print(fruits)

for i in fruits:
    print(i)

# Example for tuples are immutable

# fruits[0] = "papaya"  # Error doesn't work as normal
# print(fruits[0])

values = ({"name": "John", "age": 30}, {"name": "Jane", "age": 25})

# all work normal as like list

print(values[0]["name"])  # we only access the value only by put it in square brackets

print(values[0]["age"])

print(values[1]["name"])

print(values[1]["age"])

for i in values:
    print(i)
    print("Name is ", i["name"])
    print("Age is ", i["age"])

for i in values:
    print("Name is : " + i["name"] + " and Age is : " + str(i["age"]))
