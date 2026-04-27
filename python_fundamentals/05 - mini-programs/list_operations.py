list = [10, 20, 40, 90, 50]

print(list)

list.append(99)  # append 99 at the end
print(list)

list.remove(20)  # remove 20 from the list
print(list)

list.insert(1, 20)  # insert 20 at index 1
print(list)

list.insert(2, 30)
print(list)

list.pop()  # pop last element
print(list)

list.insert(1, 20)
print(list)

list.sort()
print(list)

list.reverse()
print(list)

print(list.index(50))  # it will return the index of the value

print(list.count(20))  # it will return the count of the value

print(list.copy())  # it will return the copy of the list

# ------------------------------------------

# users = [
#     {"name": "John", "age": 25},
#     {"name": "Ram", "age": 30},
#     {"name": "Aisha", "age": 22},
# ]

# # print only names which are greater than 22
# for user in users:
#     if user["age"] > 22:
#         print(user["name"])

# # print only names
# for user in users:
#     print(user["name"])
