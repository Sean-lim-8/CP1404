PASSWORD_LENGTH = 8

password = str(input("Enter password: "))
while len(password) < PASSWORD_LENGTH:
    print("Password must be at least 8 characters long")
    password = str(input("Enter password: "))

print(len(password) * "*")