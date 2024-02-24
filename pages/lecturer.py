from datetime import timedelta, datetime
from profile_editor import profileEditor

def lecturerPage(user, data,dataUpdater):
    def lecturer_menu_choice(user, data,dataUpdater):
        while True:
            options = input("1.Register students \n"
                            "2.enroll students \n"
                            "3.Update subject enrollment \n"
                            "4.Approve the requests \n"
                            "5.Delete students\n"
                            "6.Edit profile\n"
                            "7.Exit\n")
            if options == "1":
                Register_students_to_modules()
            elif options =="2":
                Enroll_student(data,dataUpdater)
            elif options == "3":
                Update_subject_enrollment_of_a_student()
            elif options == "4":
                Approve_the_request_from_student()
            elif options == "5":
                Delete_students()
            elif options == "6":
                profileEditor(user, data, dataUpdater)
            elif options == "7":
                print("Exiting Lecturer menu..\n")
                break
            else: 
                print("Invalid option\n")

    def Register_students_to_modules():
        choice = input("Press R to register students or B to go back to the main menu: ")
        if choice.upper() == "R":
                
            def registerUser(data):
                # TP Number #
                userValid = False

                while userValid == False:
                
                    student_tp_number = str(input("Enter your TP number: TP"))
                    
                    if not student_tp_number.isnumeric or not len(str(student_tp_number)) == 6:
                        print("Invalid TP Number!\n")
                    else:
                        for user in data["users_data"]:
                            if f"TP{student_tp_number}" == user["user_tp"]:
                                print("TP number is already existing.\n")
                                return
                        else:
                            userValid = True                        
                
                # Name #
                while True:
                    student_first_name = input("Enter your First name: ")
                    student_last_name = input("Enter your Last name: ")

                    if student_first_name.isalpha() and student_last_name.isalpha():
                        student_name = (f"{student_first_name.capitalize()} {student_last_name.capitalize()}")
                        break
                    else:
                        print("Name includes unallowed characters!")
                    
                    
                # Password #
                student_Password = f'{student_first_name}{student_last_name[0]}@{student_tp_number}'
                
                userRole = "student"

                # New User Formatting #
                new_student = {
                            "user_tp":f"TP{student_tp_number}",
                            "password":student_Password,
                            "fullname":student_name,
                            "role":userRole,
                            }

                # Adding the User to Database # 
                data["users_data"].append(new_student)

                dataUpdater(data)
        elif choice.upper() == "B":
            return
        else:
            print("Invalid choice\n")

        registerUser(data)


    def Enroll_student(data, dataUpdater):
        choice = input("Press E to enroll students or B to go back to the main menu: ")
        if choice.upper() == "E":
            moduletempid = 1
            # Show available modules
            for module in data["modules_data"]:
                print(moduletempid, module["module_name"], module["module_level"])
                moduletempid += 1
            
            while True:
                # Prompt trainer for a specific module
                pmodule = int(input("Enter a module number:")) - 1
                if 0 <= pmodule < moduletempid - 1:
                    
                    # Prompt trainer for student TP
                    ptp =  "TP" + input("Enter tp number: TP") 
                    
                    # Validate student TP (check if already enrolled)
                    enrolled_students = [student["student_tp"] for student in data["modules_data"][pmodule].get("students_enrolled", [])]
                    if ptp in enrolled_students:
                        print("Student already enrolled in this module.")
                    else:
                        # Append student TP to modules data["students_enrolled"]
                        if "students_enrolled" not in data["modules_data"][pmodule]:
                            data["modules_data"][pmodule]["students_enrolled"] = []
                        data["modules_data"][pmodule]["students_enrolled"].append({"student_tp": ptp, "enrollment_date": "yyyy-mm-dd"})
                        print("Student enrolled successfully.\n")

                    # Update JSON data
                    dataUpdater(data)
                    break
                else: 
                    print("Invalid module number\n")

    def Update_subject_enrollment_of_a_student():
        choice = input("Press U to update subject enrollment or B to go back to the main menu: ")
        if choice.upper() == "U":
                # Ask lecturer for student tp #
                # View the student's modules #
                # Ask lecturer for a specific module to delete #
                Update_subject = "TP" + input("Enter the tp number: TP")
                modules_enrolled = []
                for module in data["modules_data"]:
                    for student in module ["students_enrolled"]:
                        if Update_subject == student["student_tp"]:
                            print(f'''module id: {module["module_id"]}
                                module name: {module["module_name"]}
                                    module level:{module["module_level"]}
                                    trainer tp: {module["trainer_tp"]} ''')
                            modules_enrolled.append(module)

                if len(modules_enrolled) != 0:
                    Delete_student = input("Enter module id to delete:")
                    for student_in_module in data["modules_data"]:
                        if student_in_module["module_id"] == Delete_student:
                            for student1 in student_in_module["students_enrolled"]:
                                if student1["student_tp"] == Update_subject:
                                    student_in_module["students_enrolled"].remove(student1)
                                    dataUpdater(data)
                    pass        
                else:
                    print("Student got no modules!\n")
        elif choice.upper() == "B":
            return
        else:
             print("Invalid choice\n")

    def Approve_the_request_from_student():
        
    # For loop to view request #
            for pending_requests in data["enrollment_requests"][0]["pending_requests"]:
                print(f'''\tRequest id: {pending_requests["request_id"]}
                    student tp: {pending_requests["student_tp"]}
                    trainer tp: { pending_requests["trainer_tp"]}
                    module id: {pending_requests["module_id"]}
                    request status: {pending_requests["request_status"]}
                    issue date: {pending_requests["issue_date"]}''')
            choice = input("Press A to approve requests or B to go back to the main menu: ")
            if choice.upper() == "A":
            # Prompt lecturer for request id to approve #
                request_id =input("Enter id to approve:") 
                for request in data["enrollment_requests"][0]["pending_requests"]:
                    if request["request_id"] == request_id:
                        request["request_status"] = "Approved"
                        current_date = datetime.today().strftime('%Y-%m-%d')
                        request["processed_date"] = current_date
                        move_request = request
                        data["enrollment_requests"][0]["pending_requests"].remove(request)
                        data["enrollment_requests"][0]["approved_requests"].append(move_request)
                        dataUpdater(data)
                        
                    print(f"Request with ID {request_id} has been approved.")
                    return
                print(f"Request with ID {request_id} not found.")        

            elif choice.upper() == "B":
             return
            else:
                print("Invalid choice")
            
    def Delete_students():
       # From data #############################
        # module starting date #
        
        choice = input("Press D to delete students or B to go back to the main menu: ")
        if choice.upper() == "D":
            
            for module in data["modules_data"]:
                    module_start = module["module_starting_date"]

                    # current date #
                    current_date = str(datetime.today())
                    # Convert string to datetime object
                    module_start_convert = datetime.strptime(module_start, "%Y-%m-%d")
                     # Add 3 months
                    module_end = module_start_convert + timedelta(days=90)
                    # Convert back to string
                    module_ending_date = module_end.strftime("%Y-%m-%d")

                    if current_date >= module_ending_date: #######################
                    # remove students from module (for loop) #
                    # change module_starting_date to "None" #
                        students = module["students_enrolled"]
                        position = len(students) - 1
                        deleted_students_number = 0
                        while position >= 0:
                            del students[position]
                            position -= 1
                            deleted_students_number += 1
                        module["module_starting_date"] = "1999-01-01"
                        dataUpdater(data)
                        print(f"{deleted_students_number} students has been deleted from {module["module_id"]}")
        elif choice.upper() == "B":
            return
        else:
         print("Invalid choice\n")    
       
    lecturer_menu_choice(user,data,dataUpdater)
        
# write your code inside the function