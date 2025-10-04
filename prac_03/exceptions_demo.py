"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    # Added validation to ensure that denominator cannot be 0
    if denominator  <= 0:
        print("The denominator must not be 0.")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# Q1. When will a ValueError occur?
# When the user input is not a number.

# Q2. When will a ZeroDivisionError occur?
# When the user inputs 0 as a denominator.

# Q3. Could you change the code to avoid the possibility of a ZeroDivisionError?
# We can validate the user's input before calculating the inputs.