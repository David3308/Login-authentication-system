USERNAME = "admin"
PASSWORD = "1234"

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == USERNAME and password == PASSWORD:
        print("Login successful")
    else:
        print("Invalid login details")

def main():
    while True:
        print("1. Login")
        print("2. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            login()
        elif choice == "2":
            break
        else:
            print("Invalid option")

main()
