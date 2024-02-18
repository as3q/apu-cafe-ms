#PYP assign
#Admin home page
#welcome message#
from profile_editor import profileEditor
import getpass


def adminPage(user, data, dataUpdater):
    print ("welcome admin")
    def admin_menu_choice(user, data):
        while True:
            #user input#
            choice = input("1. register or delete or assign trainer\n"
                           "2.Monthly Income Report\n" 
                           "3. View Trainer Feedback\n" 
                           "4.Update profile\n"
                           "5. Log out\n")
            match choice:
                case "1":
                    reigster_delete_assign_trainer(user, data, dataUpdater)
                case "2":
                    monthly_income_report(data)
                case "3":
                    view_trainer_feedback( data)
                case "4":
                    profileEditor(user, data, dataUpdater)
                    print("Update")
                case "5":
                    print("Exiting the admin system. Goodbye!")
                    break
                case other:
                    print("Invalid choice. Please enter a valid option.")
    #register delete assign code#
    def reigster_delete_assign_trainer(user , data , dataUpdater):
       
    
        register_delete_choice = input ("1.register new trainer\n" 
                                        "2.delete trainer\n"
                                        "3.assign trainer to a module \n" 
                                        "4.back to main menu \n")
        match register_delete_choice:
            case"1":
                    
                def registerUser(data):
                    # TP Number #
                    userValid = False

                    while userValid == False:
                    
                        userTPNumber = str(input("Enter your TP number: TP"))
                        
                        if not userTPNumber.isnumeric or not len(str(userTPNumber)) == 6:
                            print("Invalid TP Number!")
                        else:
                            for user in data["users_data"]:
                                if f"TP{userTPNumber}" == user["user_tp"]:
                                    print("TP number is already existing!")
                                    return
                            else:
                                userValid = True                        
                    
                    # Name #
                    while True:
                        userFirstName = input("Enter your First name: ")
                        userLastName = input("Enter your Last name: ")

                        if userFirstName.isalpha() and userLastName.isalpha():
                            userName = (f"{userFirstName.capitalize()} {userLastName.capitalize()}")
                            break
                        else:
                            print("Name includes unallowed characters!")
                        
                        
                    # Password #
                    userPassword = f'{userFirstName}{userLastName[0]}@{userTPNumber}'
                    
                    userRole = "trainer"
    
                    # New User Formatting #
                    newUser = {
                                "user_tp":f"TP{userTPNumber}",
                                "password":userPassword,
                                "fullname":userName,
                                "role":userRole,
                                }

                    # Adding the User to Database # 
                    data["users_data"].append(newUser)

                    dataUpdater(data)

                registerUser(data)

            case "2":
                while True:
                    delete_trainer = "TP" + input("Enter trainer Tp number: Tp")
                    for trainer in data["users_data"]:
                        if trainer["user_tp"] == delete_trainer:
                            if trainer["role"] == "trainer":
                                sure = input(f"Are you sure you want to delete {trainer['fullname']}? "
                                            "If yes, press 'y'; if no, press 'n': ")
                                if sure.upper() == "Y":
                                    index = data["users_data"].index(trainer)

                                    del data["users_data"][index]
                                    print("Trainer deleted successfully")
                                    dataUpdater(data)
                                    return
                                elif sure.upper() == "N":
                                    break

  
            case "3":
                while True:
                    modules_without_trainers = []
                    for module_data in data["modules_data"]:
                        if module_data["trainer_tp"] == "None" or "none":
                            modules_without_trainers.append(module_data["module_id"])

                            if modules_without_trainers:
                                print("Modules without trainers:")
                                for module_id in modules_without_trainers:
                                    print(module_id)
                            else:
                                print("All modules have trainers.")

                            select_module_id = input("Enter the module ID you want to assign a trainer to: ")

                            trainer_tp_number = input("Enter the trainer TP number: ")

                            for module_data in data["modules_data"]:
                                if module_data["module_id"] == select_module_id:
                                    module_data["trainer_tp"] = trainer_tp_number
                                    print("Trainer TP number assigned successfully.")
                                    break
                            else:
                                print("Module ID not found.")
                        else:
                            print("All modules have trainers or no modules found.")


            case "4":
                while True:
                    trainer_module_tp = int(input ("enter trainer TP number: Tp"))
                    for trainer_module_tp1 in data["modules_data"]:
                        
                            if trainer_module_tp1 == trainer_module_tp:
                                while True:
                                    choose1 = input("type a module you want to add: ")
                                    trainer_module_tp1["module_name"].append(choose1)
                                    adding_1_module = input("do you want to add more modules?" 
                                                            "if yes press Y if no press N:\n")
                                    if adding_1_module.upper == "Y":
                                        choose2 = input("type a module you want to add: ")
                                        trainer_module_tp1["module_namae"].append(choose2)
                                    elif adding_1_module.upper == "N":
                                        print ("trainers have been assigned")
                                        break
                                    adding_2_module = input("do you want to add more modules?" 
                                                            "if yes press Y if no press N:\n")
                                    if adding_2_module.upper == "Y":
                                        choose3 = input("type a module you want to add: ")
                                        trainer_module_tp1["module_namae"].append(choose3)
                                    elif adding_2_module.upper == "N":
                                        print ("trainers have been assigned")
                                        dataUpdater(data)
                                    break
                                    
            case other:
                print("invalid")

                 

    #view icome monthly#                
    def monthly_income_report(data):
        while True:
            trainer_income = 0
            trainer_income_tp = input("enter trainer TPnumber (or R to return): TP")
            if trainer_income_tp.upper() == "R":
                break
            else:
                for income_data in data["modules_data"]:
                    if f'TP{trainer_income_tp}' == income_data["trainer_tp"]:
                        student_count = len(income_data["students_enrolled"])
                        income_per_student = int(income_data["module_fee"])
                        trainer_income = student_count * income_per_student
                    if int(trainer_income) > 0:
                                    
                        print(f"The income for the trainer is: {trainer_income}")
                    else:
                        print(f"No data found for trainer {trainer_income_tp}.")

    # view trainer feedback#
    def view_trainer_feedback( data):
        while True:  
            for feedback in data["trainer_feedback"]:
                author_tp = feedback["author_tp"]
                text_message = feedback["message"]

                for user_filter in data["users_data"]:
                    if author_tp == user_filter["user_tp"]:
                        author_name = user_filter["fullname"]
                        
                print(f"From {author_name}")
                print(f"Message: {text_message}")
                print("----------------")
            return_to_menu = input("If you want to go back to the main menu, press 'y': ")
            if return_to_menu.upper() == "Y":
             break

    admin_menu_choice(user,data)
