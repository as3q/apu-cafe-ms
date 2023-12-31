from student import studentPage
from lecturer import lecturerPage
from admin import adminPage
from trainer import trainerPage
import os

# Home #
def homePage():

    # Home Page Welcoming #
    print("Welcome to APU Café")

    # Home Page Navigator #
    while True:
        homeMenuChoice = input("1. Log in \n2. Sign up\n3. Exit\n")

        if homeMenuChoice == '1' :
            logIn()
        elif homeMenuChoice == '2' :
            signUp()
            break
        elif homeMenuChoice == '3' :
            print("Thanks for using APU Café!")
            break
        else:
            print("Invalid choice!")          

# Sign up (name - password - role) #
def signUp():
    print("Creating an account")

    while True:
     try:
         userTPNumber = str(input("Enter your TP number: TP"))
     except: 
         ValueError
         continue
     else:
        if not userTPNumber.isnumeric or len(str(userTPNumber)) < 6:
            print("Invalid TP Number!")
        else:
            break

    while True:
      userFirstName = input("Enter your First name: ")
      userLastName = input("Enter your Last name: ")

      if userFirstName.isalpha() and userLastName.isalpha():
          break
      else:
          print("Name includes unallowed characters!")
      
    userName = (f"{userFirstName} {userLastName}")

    while True:
        userPassword = input("Enter your Password: ")
        userPasswordConfirm = input("Confirm your Password: ")

        if userPassword == userPasswordConfirm:
            if len(userPassword) < 8:
                print("Password too short!")
            else:
                break
        else:
            print("Password must match!")
        
    while True:
        userRoleChoice = input("1. Admin \n2.Lecturer \n3.Trainer \n4.Student\n")

        userRole = "unassigned"

        if userRoleChoice == '1' :
            userEmailDomain = "@admin.apu.cafe"
            userRole = "admin"
            break
        elif userRoleChoice == '2' :
            userEmailDomain = "@lecturer.apu.cafe"
            userRole = "lecturer"
            break
        elif userRoleChoice == '3' :
            userEmailDomain = "@trainer.apu.cafe"
            userRole = "trainer"
            break
        elif userRoleChoice == '4' :
            userEmailDomain = "@stu.apu.cafe"
            userRole = "student"
            break
        else:
            print("Invalid choice!")
        
    userEmail = str(f"TP{userTPNumber}{userEmailDomain}")
    print(f"Account successfully created! \n{userEmail}")

# Export Added User to Text #
    db = open("users_data.txt", "a")
    db.write(f"\n{userEmail.upper()}, {userPassword}, {userName.upper()}, {userRole}")
    db.close

users = []

# Import Users from Text Temporarily #
db = open("users_data.txt", "r")
tempUsers = db.readlines()

# Store Users to "users" List # 
for line in tempUsers:
    line = line.split(', ')
    user = [line[0], line[1], line[2], line[3]]
    users.append(user)

# Log in # 
def logIn():
    if len(users) == 0:
        print("No users assigned! Please sign up.")
    else:
        attempts = 3
        loggedIn = False

        while (attempts + 1) > 0 and loggedIn == False :
            for user in users:
                print("Kindly Log In")
                enteredEmail = input("Email: ")
                enteredPasskey = input("Password: ")
                if user[0] == enteredEmail.upper() and user[1] == enteredPasskey:
                    print("successful log in!")
                    if user[3] == "admin\n":
                        print(f"Hello, {user[2]}!")
                        loggedIn = True
                        adminPage()
                        break
                    elif user[3] == "trainer\n":
                        print(f"Hello, {user[2]}!")
                        loggedIn = True
                        trainerPage()
                        break
                    elif user[3] == "student\n":
                        print(f"Hello, {user[2]}!")
                        loggedIn = True
                        studentPage(user)
                        break
                    elif user[3] == "lecturer\n":
                        print(f"Hello, {user[2]}!")
                        loggedIn = True
                        lecturerPage ()
                        break
                    else:
                        print("Role unassigned! Please contact an APU Café admin.")
                
                else:
                    if attempts == 0 :
                        print("Too much attempts, try again later.")
                        break
                    else:
                        os.system('cls')
                        print(f"Invalid Email or password! {attempts} attempts left")
                        attempts-=1
                        break                       

# Home Page Initiator #
homePage()




