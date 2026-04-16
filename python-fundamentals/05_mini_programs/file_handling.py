# write a file

with open("entry.txt", "w") as fs:
    fs.write("Hello\n")
    fs.write("Entries are Written Here\n")
    fs.write("Thank you\n")

# read a file

with open("entry.txt", "r") as fs:
    data = fs.read()
    print(data)

# read a file line by line

with open("entry.txt", "r") as fs:
    for line in fs:
        print(line.strip())

# read a file line by line using readlines

with open("entry.txt", "r") as fs:
    lines = fs.readlines()
    for line in lines:
        print(line.strip())

# append to a file

with open("entry.txt", "a") as fs:
    fs.write("Appended Line\n")

# store these data in files

users = [{"name": "John", "age": 25}, {"name": "Ram", "age": 30}]


def file_handling():
    try:
        with open("users.txt", "w") as fs:
            for user in users:
                fs.write(f"User name is {user['name']} , Age is {user['age']}\n")

        with open("users.txt", "r") as fs:
            for line in fs:
                print(line.strip().split(","))

    except FileNotFoundError:
        print("File are not Found")


file_handling()
