#PYP assign
#Admin home page
#welcome message#
# from ..profile_editor import profileEditor


def adminPage(user, data, dataUpdater):
    print ("welcome admin")
    def admin_menu_choice(user, data):
        while True:
            #user input#
            choice = input("1. register or delete or assign trainer\n"
                           "2.Monthly Income Report\n" 
                           "3. View Trainer Feedback\n" 
                           "4.Update profile\n"
                           "5. exit\n")
            match choice:
                case "1":
                    reigster_delete_assign_trainer(user, data, dataUpdater)
                case "2":
                    monthly_income_report()
                case "3":
                    view_trainer_feedback(user, data)
                case "4":
                    # profileEditor(user, data)
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
                                        "3.assign trainer to a level\n" 
                                        "4.assign trainer to a module \n" 
                                        "5.back to main menu \n")
        match register_delete_choice:
            case"1":
                register_trainer_name = input ("enter trainer full name: ")
                trainer_tpnumber = int(input("enter trainer's TPnumber: TP"))
                for trainer in ["users_data"]:
                    if trainer["fullname"] == register_trainer_name and trainer["user_tp"] == trainer_tpnumber:
                        if trainer["role"] == "trainer":
                         print("Trainer already registered.")
                    else:
            
                        trainer["role"] = "trainer"
                        print("Trainer role updated.")
                    break
                else:
                    new_trainer = {
                    "fullname": register_trainer_name,
                    "user_tp": trainer_tpnumber,
                    "role": "trainer"
                }
                data["users_data"].append(new_trainer)
                print("Trainer registered successfully.")
                
                dataUpdater(data)
                
                

            case "2":
                delete_trainer = int(input ("enter trainer Tp number: Tp    "))
                for trainer in data["users_data"]:
                    if trainer["user_tp"] == delete_trainer:
                        
                        if trainer ["role"] == "trainer":
                                 sure = input(f"are you sure you want to delete {trainer["fullname"]}?" 
                                     "if yes press y, if no press n")
                        if sure.upper == "Y" :
                            data["users_data"].remove(trainer)
                            print ("trainer deleted successfully")
                        elif  sure.upper =="N":
                            break

                        dataUpdater(data)


                        
            case "3":
                trainer_level_tp = int(input ("enter trainer TP number: Tp"))
                print ("1. beginner, \n2.intermeidate, \n3.advanced, \n")
                trainerlevel = input ("choose a level for the trainer: ")
                if trainerlevel == 1 or trainerlevel == "beginner":

                    for trainer_level_tp in data["modules_data"]:
                        if trainer_level_tp == trainer_level_tp["trainer_tp"]:
                            trainer_level_tp["module_level"] = "beginner"
                            print ("trainer level updated")
                            dataUpdater(data)
                            
                                
                        

                elif trainerlevel == 2 or trainerlevel == "intermeidate":
                    "add trainer name to the level"
                    for trainer_level_tp in data["modules_data"]:
                        if trainer_level_tp == data["trainer_tp"]:
                            trainer_level_tp["module_level"] = "intermeidate"
                            print ("trainer level updated")
                            dataUpdater(data)

                elif trainerlevel == 3 or trainerlevel == "advanced":
                    "add trainer name to the level"
                    for trainer_level_tp in data["modules_data"]:
                        if trainer_level_tp == data["trainer_tp"]:
                            trainer_level_tp["module_level"] = "advanced"
                            print ("trainer level updated")
                            dataUpdater(data)
                else:
                    print ("invalid choice please choose again")
            case "4":
                "add trainer to a module"
                trainer_module_tp = int(input ("enter trainer TP number: Tp"))
                for trainer_module_tp1 in data["modules_data"]:
                    if trainer_module_tp1 == trainer_module_tp:
                        choose1 = input("type a module you want to add: ")
                        trainer_module_tp1["module_namae"].append(choose1)
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
                            break
                        dataUpdater(data)
            case other:
                print("invalid")

                 

    #view icome monthly#                
    def monthly_income_report():
        print("Monthly Income Report functionality goes here.")
        print ("this is your monlthy income")
    # view trainer feedback#
    def view_trainer_feedback(user, data):
        print("View Trainer Feedback functionality goes here.")
    
        for feedback in data["trainer_feedback"]:
            author_tp = feedback["author_tp"]
            text_message = feedback["message"]

            for user_filter in data["users_data"]:
                if author_tp == user_filter["user_tp"]:
                    author_name = user_filter["fullname"]
                    
            print(f"From {author_name}")
            print(f"Message: {text_message}")
            print("----------------")
    return_to_menu = input("if you want to go back to main menu press y ")
    if return_to_menu.upper == "y":
        break
    
       

   

    admin_menu_choice(user,data)