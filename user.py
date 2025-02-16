for i in range(3):
    username=input("Enter username")
    password=input("Enter Password")
    if username=='testuser' and password=='Password@123':
        print("login Successfull")
    elif i<3:
        print("You have next chance")
    else:
        print("no.of attempts are completed")
 