import os, json, getpass
from pages.student import studentPage
from pages.admin import adminPage
from pages.lecturer import lecturerPage
from pages.trainer import trainerPage

# Importing os to Clear Terminal (lines , , ) #
# Importing getpass to Mask User Password Input #
# Importing json to Read Data from Text File (lines , ) #

# Read Data Text File with JSON #
db = open("data.txt", "r")
data = json.load(db)

def dataUpdater(data):
    # Formatting Data into JSON Format #
    data = json.dumps(data, indent=2)

    # Updating Data in Text File # 
    db = open("data.txt", "w")
    db.write(data)

    # Reloading Data #
    db = open("data.txt", "r")
    data = json.load(db)

# Functions to Help Search from data #
def grabModule(moduleGrabKey, moduleGrabValue):
    
    for moduleGrabbed in data["modules_data"]:
        if moduleGrabKey == moduleGrabbed[moduleGrabValue]:
            moduleName = moduleGrabbed["module_name"]
            moduleLevel = moduleGrabbed["module_level"]
            moduleFee = moduleGrabbed["module_fee"]
            moduleDate = moduleGrabbed["module_starting_date"]
    return moduleName, moduleLevel, moduleFee, moduleDate

def grabTrainerName(trainerGrabTP):

    for trainer in data["users_data"]:
        if trainer["user_tp"] == trainerGrabTP:
            trainerFullName = trainer["fullname"]
    return trainerFullName

# Log In Function #
def logIn(data):
    # Setting Variables #
    attempts = 3
    loggedIn = False

    # Loop to Compare Entered Credentials to Database #
    while (attempts + 1) > 0 and loggedIn == False :
            # User Input #
            print("Kindly Log In")

            enteredTP = input("TP number: TP")
            enteredPasskey = getpass.getpass(prompt="Password: ")

            for user in data["users_data"]:
                if user["user_tp"] == (f"TP{enteredTP}") and user["password"] == enteredPasskey:
                    os.system("cls")

                    print("successful log in!")
                    loggedIn = True

                    name = user["fullname"].split()[0]
                    print(f"Hello, {name}!")

                    # Redirect to Page Respective to User Role #
                    match user["role"]:
                        case "admin":
                            adminPage(user, data, dataUpdater)
                            break
                        case "trainer":
                            trainerPage(user, data, dataUpdater)
                            break
                        case "student":
                            studentPage(user, data, dataUpdater, grabModule, grabTrainerName)
                            break
                        case "lecturer":
                            lecturerPage(user, data,dataUpdater)
                            break
                        case other:
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

def homePage():
    # Home Page Navigator #
    while True:

        # Home Page Welcoming #
        print("Welcome to APU Café")

        homeMenuChoice = input("1. Log in \n2. Exit\n")

        match homeMenuChoice:
            case '1':
                logIn(data)
            case '2':
                print("Thanks for using APU Café!")
                break
            case other:
                print("Invalid choice!")

homePage()
