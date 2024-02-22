from datetime import timedelta, datetime
from profile_editor import profileEditor

def lecturerPage(user, data,dataUpdater):
    def lecturer_menu_choice(user, data,dataUpdater):
        while True:
            options = input("1.Registe / Enroll students to modules\n"
                            "2.Update subject enrollment of a student\n"
                            "3.Approve the request from student\n"
                            "4.Delete students\n"
                            "5.Edit profile\n"
                            "6.Exit\n")
            if options == "1":
                menu = input("1.Register \n 2.Enroll")
                if menu == "1":
                    Register_students_to_modules()
                elif menu =="2":
                    Enroll_student(data,dataUpdater)
            elif options == "2":
                Update_subject_enrollment_of_a_student()
            elif options == "3":
                Approve_the_request_from_student()
            elif options == "4":
                Delete_students()
            elif options == "5":
                profileEditor(user, data, dataUpdater)
            elif options == "6":
                print("Exiting Lecturer menu..\n")
                break

    def Register_students_to_modules():
        name = input("Name: ")
        tp_number = "TP" + input("TP number: TP")
        level = input("Level: ")
        module = input("Module: ")
        date_of_enrollment = input("Date of enrollment (yyyy-mm-dd): ")
        module_fee = input("module fee:")

        module_id = f"{module[2]}{level[3]}{tp_number[-3]}{date_of_enrollment[-5]}"
        if name.isalpha and level.isalpha and module.isalpha:
            new_module = {"module_id": module_id,
                          "module_name": module,
                          "module_level":level,
                          "trainer_tp":tp_number,
                          "student_enrolled": [],
                          "module_starting_date":date_of_enrollment,
                          "module_fee":module_fee,}
        
        Register_Exit_Choice = input("Enter R to return to menu\n")
        if Register_Exit_Choice.upper() == 'R':
            break
        else:
            print("invalid choice!")
    def Enroll_student(data,dataUpdater):
        moduletempid = 1
        #show available modules#
        for module in data["modules_data"]:
            print(moduletempid, module["module_name"], module["module_level"])
            moduletempid+=1
        #prompt trainer for a specific module#
        pmodule=int(input("Enter a module id:")) -1
        #prompt trainer for student tp#
        ptp= input("Enter tp number:")
        #validate studenet tp (if already in module or if not registered)#
        #append student tp to modules data["studennts_enrolled"]#
        data["modules_data"][pmodule]["students_enrolled"].append(ptp)

        dataUpdater(data)
    def Update_subject_enrollment_of_a_student():
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
        else:
            print("Student got no modules!")

    def Approve_the_request_from_student():
        # For loop to view request #
        for pending_requests in data["enrollment_requests"][0]["pending_requests"]:
            print(f'''Request id: {pending_requests["request_id"]}
                  student tp: {pending_requests["student_tp"]}
                  trainer tp: { pending_requests["trainer_tp"]}
                 module id: {pending_requests["module_id"]}
                 request status: {pending_requests["request_status"]}
                 issue date: {pending_requests["issue_date"]}''')

        # Prompt lecturer for request id to approve #
            request_id =input("Enter id to approve:") 
            for request in data["enrollment_requests"][0]["pending_requests"]:
                 if request["request_id"] == request_id:
                    request["request_status"] = "Approved"
                    current_date = str(datetime.date.today())
                    request["processed_date"] = current_date
                    move_request = request
                    data["enrollment_requests"][0]["pending_requests"].remove(request)
                    data["enrollment_requests"][0]["approved_requests"].append(move_request)
                    dataUpdater(data)
                     
                 print(f"Request with ID {request_id} has been approved.")
                 return
            print(f"Request with ID {request_id} not found.")
            
    def Delete_students():
       # From data #############################
        # module starting date #
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
                while position >= 0:
                    del students[position]
                    position -= 1
                module["module_starting_date"] = "1999-01-01"
                dataUpdater(data)

    lecturer_menu_choice(user,data,dataUpdater)
# write your code inside the function
