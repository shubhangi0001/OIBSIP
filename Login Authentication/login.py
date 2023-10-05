# Define an empty dictionary to store user credentials (username and password)
user_credentials = {}

# Function to register a new user
def register():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    user_credentials[username] = password
    print("Registration successful!")

# Function to login a user
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in user_credentials and user_credentials[username] == password:
        print("Login successful!")
        access_secured_page()
    else:
        print("Login failed. Invalid username or password.")
# Define an empty dictionary to store user credentials (username and password)
user_credentials = {}

# Function to register a new user
def register():
    username = input("Enter a new username: ")
    if username in user_credentials:
        print("Username already exists. Please choose a different one.")
    else:
        password = input("Enter a password: ")
        user_credentials[username] = password
        print("Registration successful!")

# Function to login a user
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in user_credentials and user_credentials[username] == password:
        print("Login successful!")
        access_secured_page()
    else:
        print("Login failed. Invalid username or password.")

# Function to access a secured page
def access_secured_page():
    print("Welcome to the secured page!")
    # Add your secured page code here

# Main program loop
while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Select an option: ")

    if choice == '1':
        register()
    elif choice == '2':
        login()
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")

# Define an empty dictionary to store user credentials (username and password)
user_credentials = {}

# Function to register a new user
def register():
    username = input("Enter a new username: ")
    if username in user_credentials:
        print("Username already exists. Please choose a different one.")
    else:
        password = input("Enter a password: ")
        user_credentials[username] = password
        print("Registration successful!")

# Function to login a user
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in user_credentials:
        if user_credentials[username] == password:
            print("Login successful!")
            access_secured_page()
        else:
            print("Wrong password. Login failed.")
    else:
        print("Username not found. Please register.")

# Function to access a secured page
def access_secured_page():
    print("Welcome to the secured page!")
    # Add your secured page code here

# Main program loop
while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Select an option: ")

    if choice == '1':
        register()
    elif choice == '2':
        login()
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")

# Function to access a secured page
def access_secured_page():
    print("Welcome to the secured page!")
    # Add your secured page code here

# Main program loop
while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Select an option: ")

    if choice == '1':
        register()
    elif choice == '2':
        login()
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
