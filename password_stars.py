MIN_LENGTH = 8
password = input("Enter a password (at least 8 characters): ")

while len(password) < MIN_LENGTH:
    print("Password too short. Try again.")
    password = input("Enter a password (at least 8 characters): ")

print('*' * len(password))
