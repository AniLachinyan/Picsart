reserved_names = ['admin', 'root']

username = input("Enter username: ")
email = input("Enter email: ")
phone = input("Enter phone number: ")
password = input("Enter password: ")
password_repeat = input("Repeat password: ")

if len(username) < 5 or len(username) > 20:
    print("Username is not valid")
elif not username.isalnum():
    print("Username isnot valid")
elif username.lower() in reserved_names:
    print("Username should not be reserved")
else:
    print("Username is valid.")

if "@" not in email or "." not in email.split("@")[-1]:
    print("Email is not valid")
else:
    print("Email is valid.")

if (phone.startswith("+374") and phone[4:].isdigit() and len(phone) == 12) or (phone.startswith("0") and phone.isdigit() and len(phone) == 9):
    print("Phone number is valid.")
else:
    print("Phone number is not valid")

if len(password) < 8:
    print("Password should be at least 8 characters long.")
elif not any(char.isupper() for char in password):
    print("Password must contain at least one uppercase letter.")
elif not any(char.islower() for char in password):
    print("Password must contain at least one lowercase letter.")
elif not any(char.isdigit() for char in password):
    print("Password must contain at least one digit.")
elif not any(char in '!@#$%^&*()_+' for char in password):
    print("Password must contain at least one character")
elif password != password_repeat:
    print("Password repeat does not match with password.")
else:
    print("Password is valid ")

