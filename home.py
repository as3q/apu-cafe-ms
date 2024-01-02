# Import All Pages #
from student import studentPage
from lecturer import lecturerPage
from admin import adminPage
from trainer import trainerPage

# Import OS to Clear Terminal (line 172) #
import os

# Import JSON to Read Data from Text File #
import json

# Read Data Text File with JSON #
db = open("data.txt", "r")
json_data = json.load(db)

# Seperating Data # ??
# users_data = json_data["users_data"]
# modules_data = json_data["modules_data"]

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

# Sign Up #
def signUp():
    print("Creating an account")

    # TP Number #
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
    
    # Name #
    while True:
      userFirstName = input("Enter your First name: ")
      userLastName = input("Enter your Last name: ")

      if userFirstName.isalpha() and userLastName.isalpha():
          break
      else:
          print("Name includes unallowed characters!")
      
    userName = (f"{userFirstName.capitalize()} {userLastName.capitalize()}")
    
    # Password #
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

    # User Role Assigner #      
    while True:
        userRoleChoice = input("1. Admin \n2.Lecturer \n3.Trainer \n4.Student\n")

        userRole = "unassigned"

        if userRoleChoice == '1' :
            userRole = "admin"
            break
        elif userRoleChoice == '2' :
            userRole = "lecturer"
            break
        elif userRoleChoice == '3' :
            userRole = "trainer"
            break
        elif userRoleChoice == '4' :
            userRole = "student"
            break
        else:
            print("Invalid choice!")

    # New User Formatting #
    new_user = ',\n{' + f'"user":"{userTPNumber}", "password":"{userPassword}", "fullname":"{userName}", "role":"{userRole}"' + '}'

    # Adding the User to JSON #
    json_data["users_data"].load(new_user)

    # Updating Data in Text File #
    db = open("data.txt", "w")
    db.write(json_data)
    db.close

    # Message # 
    print(f"Account successfully created!")


# Log in # 
def logIn():
    # In Case No User is Assigned #
    if len(json_data["users_data"]) == 0:
        print("No users assigned! Please sign up.")
    else:
        # Setting Variables #
        attempts = 3
        loggedIn = False

        # Loop to Compare Entered Credentials to Database #
        while (attempts + 1) > 0 and loggedIn == False :
            for user in json_data["users_data"]:

                # User Input #
                print("Kindly Log In")
                enteredTP = input("TP number: TP")
                enteredPasskey = input("Password: ")

                if user["user"] == (f"TP{enteredTP()}") and user["password"] == enteredPasskey:
                    print("successful log in!")
                    
                    name = user["fullname"]

                    # Redirect to Page Respective to User Role #
                    if user[3] == "admin\n":
                        print(f"Hello, {name}!")
                        loggedIn = True
                        adminPage()
                        break
                    elif user[3] == "trainer\n":
                        print(f"Hello, {name}!")
                        loggedIn = True
                        trainerPage()
                        break
                    elif user[3] == "student\n":
                        print(f"Hello, {name}!")
                        loggedIn = True
                        studentPage(user, json_data)
                        break
                    elif user[3] == "lecturer\n":
                        print(f"Hello, {name}!")
                        loggedIn = True
                        lecturerPage ()
                        break
                    else:
                        print("Role unassigned! Please contact an APU Café admin.")
                
                # Attempts Counter #
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
