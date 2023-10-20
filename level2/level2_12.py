correct_username = "your_username"
correct_password = "your_password"
login_attempts = 0

while login_attempts < 3:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username == correct_username and password == correct_password:
        print("Login successful!")
        break
    else:
        print("Incorrect username or password. Please try again.")
        login_attempts += 1
if login_attempts == 3:
    print("Maximum login attempts reached. Access denied.")
