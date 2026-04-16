# Dictionary are allow to make key value pairs
# It was Mutable in Nature

# EX 1 :
bunch = {
    "name": "John",
    "age": 30,
    "address": "123 Main St",
    "isStudent": False,
    "courses": ["Math", "Science", "History"],
    "grades": {"Math": 90, "Science": 85, "History": 95},
}

print(bunch["name"])
print(bunch["age"])
print(bunch["address"])
print(bunch["isStudent"])
print(bunch["courses"])
print(bunch["grades"])

# # Accessing nested values
print(bunch["courses"][1])  # here 1 is index
print(bunch["grades"]["Science"])  # here "Science" is key

# Adding new key value pair
bunch["email"] = "[EMAIL_ADDRESS]"
print(bunch)

# Updating values

bunch["name"] = "Haneef"
print(bunch["name"])

# Delete a values

# del bunch["name"]  # --> it delete the value by del keyword
# print(bunch["name"])

# loop through the dictionary

for key, value in bunch.items():
    print(key, value)
    print(key)
    print(value)


for value in bunch["courses"]:
    print(value)

bunch["isStudent"] = True
print(bunch)

for value in bunch["grades"]:
    print(value)

for value in bunch["grades"].keys():
    print(value)

for value in bunch["grades"].values():
    print(value)
