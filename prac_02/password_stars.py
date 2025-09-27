"""
CP1404 - Practical 2
Program that gets password and prints the password length in stars
"""
PASSWORD_LENGTH = 8

def main():
    password = get_password()
    print_stars(password)


def print_stars(password):
    """function to print stars"""
    print(len(password) * "*")


def get_password():
    """function to get and validate password"""
    password = str(input("Enter password: "))
    while len(password) < PASSWORD_LENGTH:
        print("Password must be at least 8 characters long")
        password = str(input("Enter password: "))
    return password


main()