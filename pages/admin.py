#PYP assign
#Admin home page
#welcome message#

def adminPage():
    print ("welcome admin")
    def admin_menu_choice():
        while True:
            #user input#
            choice = input("1. register or delete or assign trainer \n2. Monthly Income Report \n3. View Trainer Feedback \n4. exit \n")
            match choice:
                case "1":
                    reigster_delete_assign_trainer()
                case "2":
                    monthly_income_report()
                case "3":
                    view_trainer_feedback()
                case "4":
                    print("Exiting the admin system. Goodbye!")
                    break
                case other:
                    print("Invalid choice. Please enter a valid option.")
    #register delete assign code#
    def reigster_delete_assign_trainer():
        print(" reigster or delete trainer functionality goes here")
    
        register_delete_choice = input ("1.register new trainer \n2.delete trainer \n3.assign trainer to a level \n4.back to main menu \n")
        match register_delete_choice:
            case" 1":
                trainername1 = input ("enter trainer full name:    ")
            case "2":
                trainername = input ("enter trainer full name:    ")
            case "3":
                trainername = input ("enter trainer full name:    ")
                print ("1. beginner, \n2.intermeidate, \n3.advance, \n")
                trainerlevel = input ("choose a level for the trainer: ")
                if trainerlevel == 1 or trainerlevel == "beginner":
                    "add trainer name to the level"
                elif trainerlevel == 2 or trainerlevel == "intermeidate":
                    "add trainer name to the level"
                elif trainerlevel == 3 or trainerlevel == "advance":
                    "add trainer name to the level"
                else:
                    print ("invalid choice please choose again")
    #view icome monthly#                
    def monthly_income_report():
        print("Monthly Income Report functionality goes here.")
        print ("this is your monlthy income")
    # view trainer feedback#
    def view_trainer_feedback():
        print("View Trainer Feedback functionality goes here.")
