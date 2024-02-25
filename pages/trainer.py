def trainerPage(user, data, dataUpdater):

    def trainer_menu_choice(user, data, dataUpdater):
        while True:
            print("1. Add class info\n2. Update and delete class info\n3. View list of students\n4. Send feedback\n5. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                Add_class_info(user, data, dataUpdater)
            elif choice == "2":
                Update_delete_class_info(data, dataUpdater)
            elif choice == "3":
                View_list_students(data)
            elif choice == "4":
                Send_feedback(data, dataUpdater)
            elif choice == "5":
                break
            else:
                print("Invalid choice, please choose from the given options.")

    def Add_class_info(user, data, dataUpdater):
        module_name = input("Enter name of the module: ")
        fee = input("Enter the fee: ")
        strtclass = input("Enter the starting date (yyyy-mm-dd): ")
        while True:
            level = input("1.Beginner\n2.Intermediate\n3.Advanced")
            if level == "1":
                    level="Beginner"
                    break
            if level == "2":
                    level="Intermediate"
                    break
            if level == "2":
                    level="Advanced"
                    break
            else:
                print("valied choice")
            

        newmodule_id = f"{module_name.lower()[:2]}{level[:3].lower()}{strtclass[5:7]}"

        new_class = {
            "module_id": newmodule_id,
            "module_name": module_name,
            "module_level": level,
            "trainer_tp": user["user_tp"],
            "students_enrolled": [],
            "module_starting_date": strtclass,
            "module_fee": fee
        }

        data["modules_data"].append(new_class)

        dataUpdater(data)
        print("Class added successfully!")

    def Update_delete_class_info(data, dataUpdater):
        # Display Modules #
        for modules in data["modules_data"]:
            print(f"""
                    module ID  : {modules["module_id"]}                  
                    module name: {modules["module_name"]}
                    module level: {modules["module_level"]}
                    module starting: {modules["module_starting_date"]}
                    module fee: {modules["module_fee"]}\n""")

        # Prompt for module #
        while True:
            choice4 = input('Enter the module ID of the module: ')

            module_found = next((update for update in data["modules_data"] if choice4 == update["module_id"]), None)
            if module_found:
                # Module ID exists, you can break the loop
                break
            else:
                print("This module ID does not exist. Please try again.")
            continue
                   
       

                

            # Choose Delete/Update #
        while True:
            print("1. Update\n2. Delete\n3. Exit")
            choice2 = input("Enter your choice: ")

            if choice2 == "1":
                update_info(choice4, data, dataUpdater)
            elif choice2 == "2":
                confirm_delete = input("Are you sure you want to delete this module? (y/n): ").lower()
                if confirm_delete == "y":
                    deleting(choice4, data, dataUpdater)
                    break
                elif confirm_delete == "n":
                    print("Deletion canceled.")
                    break
                else:
                    print("Invalid choice. Please enter 'y' or 'n'.")
            elif choice2 == "3":
                return
            else:
                print("Invalid choice, please choose from the given options.")

    def update_info(choice4, data, dataUpdater):
        while True:
            print("1. Module starting date\n2. Module fee\n3. Exit")
            choice5 = input("Enter your choice: ")

            if choice5 == "1":
                update_module_starting_date(choice4, data, dataUpdater)
            elif choice5 == "2":
                update_module_fee(choice4, data, dataUpdater)
            elif choice5 == "3":
                return
            else:
                print("Invalid choice")

    def update_module_starting_date(choice4, data, dataUpdater):
        newdate = input("Enter the new date: ")
        for update_module in data["modules_data"]:
            if choice4 == update_module["module_id"]:
                update_module["module_starting_date"] = newdate
                update_module_id(update_module)
                break

        dataUpdater(data)

    def update_module_fee(choice4, data, dataUpdater):
        newfee = input("Enter the new fee: ")
        for update_module in data["modules_data"]:
            if choice4 == update_module["module_id"]:
                update_module["module_fee"] = newfee
                update_module_id(update_module)
                break

        dataUpdater(data)

    def update_module_id(module):
        module["module_id"] = f"{module['module_name'].lower()[:2]}{module['module_level'][:3].lower()}{module['module_starting_date'][5:7]}"

    def deleting(choice4, data, dataUpdater):
        for delete_module in data["modules_data"]:
            if choice4 == delete_module["module_id"]:
                data["modules_data"].remove(delete_module)
                dataUpdater(data)
                break

    def View_list_students(data):
         while True:
            for students in data["modules_data"]:
                for studentdata in students["students_enrolled"]:
                    print(f"student TP:{studentdata["student_tp"]}\nStudent enrolled date:{studentdata["enrollment_date"]}")
            
            gettingout=input("Enter B to go back: ").lower()
            if gettingout =="b":
                break
            
            
        

    def Send_feedback(data, dataUpdater):
        new_message = input("Enter a message:\n")

        ids = [feedback["message_id"] for feedback in data["trainer_feedback"]]
        new_id = str(int(max(ids)) + 1)

        new_feedback = {
            "message_id": new_id,
            "author_tp": user["user_tp"],
            "message": new_message
        }

        data["trainer_feedback"].append(new_feedback)
        dataUpdater(data)

    trainer_menu_choice(user, data, dataUpdater)

# Call the function
# trainerPage(user_data, your_data, your_data_updater_function)
