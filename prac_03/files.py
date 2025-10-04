"""
CP1404 - Practical
Program to create and edit files
"""

name = input("Enter name: ")
out_file = open(f"name.txt", "w")
out_file.write(name)
out_file.close()

in_file = open("name.txt", "r")
name = in_file.read()
in_file.close()
print(f"Hi {name}!")