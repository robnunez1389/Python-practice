password = "random"
correct = False
while not correct:
    user_pword = input("Please enter your password:")
    if user_pword==password:
        print("Welcome back user!")
        correct = True
    else:
        print("Invalid password, try again...") 
print("Access Granted")

