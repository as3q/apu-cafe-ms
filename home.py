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
data = json.load(db)

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
            print("Password does not match!")

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
    new_user = {"user_tp":f"TP{userTPNumber}", "password":userPassword, "fullname":userName, "role":userRole}

    # Adding the User to JSON # 
    data["users_data"].append(new_user) 

    # ? #
    json_data = json.dumps(data, indent=2)

    # Updating Data in Text File # FIX THIS PART
    db = open("data.txt", "w")
    db.write(json_data)

    # Message # 
    print(f"Account successfully created!")


# Log in # 
def logIn():
    # In Case No User is Assigned #
    if len(data["users_data"]) == 0:
        print("No users assigned! Please sign up.")
    else:
        # Setting Variables #
        attempts = 3
        loggedIn = False

        # Loop to Compare Entered Credentials to Database #
        while (attempts + 1) > 0 and loggedIn == False :
                
                # User Input #
                print("Kindly Log In")
                enteredTP = input("TP number: TP")
                enteredPasskey = input("Password: ")

                for user in data["users_data"]:


                    if user["user_tp"] == (f"TP{enteredTP}") and user["password"] == enteredPasskey:
                        print("successful log in!")
                    
                        name = user["fullname"]

                        # Redirect to Page Respective to User Role #
                        if user["role"] == "admin":
                            print(f"Hello, {name}!")
                            loggedIn = True
                            adminPage()
                            break
                        elif user["role"] == "trainer":
                            print(f"Hello, {name}!")
                            loggedIn = True
                            trainerPage()
                            break
                        elif user["role"] == "student":
                            print(f"Hello, {name}!")
                            loggedIn = True
                            studentPage(user, data)
                            break
                        elif user["role"] == "lecturer":
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
                        print(f"Invalid TP number or password! {attempts} attempts left")
                        attempts-=1
                                     

# Home Page Initiator #
homePage()
