"""
CP1404 Practical 5
Emails
Estimate: 30 minutes
Actual: 32 minutes
"""
email_to_name = {}

email = input("Enter email: ")
while email != "":

    username = email.split("@")[0]
    name_parts = username.replace('.', ' ').replace('_', ' ').split()
    name = ' '.join(name_parts).title()

    confirmation = input(f"Is your name {name}? (Y/n): ").strip().lower()
    if confirmation != "" and confirmation != "y":
        name = input("Name: ")

    email_to_name[email] = name
    email = input("Enter email: ")

print()
for email, name in email_to_name.items():
    print(f"{name} {email}")