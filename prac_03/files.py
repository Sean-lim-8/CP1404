"""
CP1404 - Practical
Program to create and edit files
"""

# Question 1
name = input("Enter name: ")
out_file = open(f"name.txt", "w")
out_file.write(name)
out_file.close()

# Question 2
in_file = open("name.txt", "r")
name = in_file.read()
in_file.close()
print(f"Hi {name}!")

# Question 3
with open("numbers.txt", "r") as in_file:
    number1 = int(in_file.readline())
    number2 = int(in_file.readline())
    result = number1 + number2

print(f"The sum of the numbers is: {result}.")



