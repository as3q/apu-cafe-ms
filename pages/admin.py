#PYP assign
#Admin home page
#welcome message#

def adminPage(user, data, dataUpdater):
    print ("welcome admin")
    #main menu
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
    def reigster_delete_assign_trainer():
        print(" reigster or delete trainer functionality goes here")
    
        register_delete_choice = input ("1.register new trainer \n2.delete trainer \n3.assign trainer to a level \n4.back to main menu \n")
        match register_delete_choice:
            case"1":
                # register new trainer
                    
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
                #delete trainer
                while True:
                    delete_trainer = "TP" + input("Enter trainer Tp number: Tp")
                    for trainer in data["users_data"]:
                        if trainer["user_tp"] == delete_trainer:
                            if trainer["role"] == "trainer":
                                sure = input(f"Are you sure you want to delete {trainer['fullname']}? "
                                            "If yes, press 'y'; if no, press 'n': ")
                                if sure.upper() == "Y":
                                    index = data["users_data"].index(trainer)
                                    #deleteing trainer
                                    del data["users_data"][index]
                                    print("Trainer deleted successfully")
                                    dataUpdater(data)
                                    return
                                elif sure.upper() == "N":
                                    break

  
            case "3":
                #assign trainer to a module
                while True:
                    modules_without_trainers = []
                    for module_data in data["modules_data"]:
                        if module_data["trainer_tp"] == "None":
                            modules_without_trainers.append(module_data["module_id"])

                    if len(modules_without_trainers) == 0:
                        print("All modules have trainers.")
                        break

                    else:
                        print("Modules without trainers:")
                        for module_id in modules_without_trainers:
                            print(module_id)
                        

                    select_module_id = input("Enter the module ID you want to assign a trainer to: ")

                    # Verify if the entered module ID exists
                    module_exists = False
                    for module_data in data["modules_data"]:
                        if module_data["module_id"] == select_module_id:
                            module_exists = True
                            break

                    if not module_exists:
                        print("Module ID does not exist!")
                        continue  # Restart the loop to prompt the user again


                    trainer_tp_number = "TP" + str(input("Enter the trainer TP number: TP"))
                    #verify that the user tp is found
                    trainer_found = False
                    for user_data in data["users_data"]:
                        if user_data["user_tp"] == trainer_tp_number:
                            if user_data["role"] == "trainer":
                                trainer_found = True
                                break

                    if trainer_found:
                        for module_data in data["modules_data"]:
                            if module_data["module_id"] == select_module_id:
                                module_data["trainer_tp"] = trainer_tp_number
                                dataUpdater(data)
                                print("Trainer assigned successfully!")
                                break
                    else:
                        print("Trainer TP number not found or user is not a trainer!")
            case"4":
                return
          
                        
    def monthly_income_report(data):
        #monthly income
        while True:
            trainer_income = 0
            trainer_income_tp = "TP" + input("Enter trainer TP number (or 'R' to return): TP ")
            if trainer_income_tp.upper() == 'TPR':
                break
                #verify if the trainer tp exists
            trainer_found = False
            for user_data in data["users_data"]:
                if trainer_income_tp == user_data["user_tp"]:
                    trainer_found = True
                    break

            if not trainer_found:
                print("Trainer TP number not found.")
                continue  # Restart the loop to prompt the user again
                #calculate the monthly income
            for module_data in data["modules_data"]:
                if module_data["trainer_tp"] == trainer_income_tp:
                    if module_data["students_enrolled"]:
                        student_count = len(module_data["students_enrolled"])
                        income_per_student = int(module_data["module_fee"])
                        trainer_income += student_count * income_per_student
                        print(f"The income for module {module_data['module_id']} is: {trainer_income}")

            if trainer_income == 0:
                print(f"No income data found for trainer TP {trainer_income_tp}.")

        
                        
                            

    # view trainer feedback#
    def view_trainer_feedback():
        print("View Trainer Feedback functionality goes here.")
    
    admin_menu_choice()