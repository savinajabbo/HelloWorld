name = input("Enter your name: ")

while len(name) < 3:
    print("Your name must be at least 3 characters")
    name = input("Enter your name: ")

while len(name) > 50:
    print("Your name must have a maxium of 50 characters")
    name = input("Enter your name: ")
else:
    print("Name looks good!")