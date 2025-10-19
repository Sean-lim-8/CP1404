"""
CP1404 Practical 5
Emails
Estimate: 30 minutes
Actual:
"""

email = input("Enter email: ")
while email != "":

    username = email.split("@")[0]
    name_parts = username.replace('.', ' ').replace('_', ' ').split()
    name = ' '.join(name_parts).title()

