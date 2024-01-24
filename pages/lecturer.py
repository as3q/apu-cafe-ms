def lecturerPage():
    def lecturer_menu_choice():
        while True:
            options = input("1.Register/enroll student to modules\n"
                            "2.Update subject enrollment of a student\n"
                            "3.Approve the request from student\n"
                            "4.Delete students\n"
                            "5.exit")
            if options == "1":
                Register_enroll_students_to_modules()
            elif options == "2":
                Update_subject_enrollment_of_a_student()
            elif options == "3":
                Approve_the_request_from_student()
            elif options == "4":
                Delete_students()
            elif options == "5":
                print("Exiting Lecturer menu..\n")

    def Register_enroll_students_to_modules():
        name = input("Name: ")
        tp_number = input("TP number: ")
        email = input("Email: ")
        contact_number = input("Contact number: ")
        address = input("Address: ")
        level = input("Level: ")
        modules = input("Modules: ")
        month_of_enrollment = input("Month of enrollment: ")


    def Update_subject_enrollment_of_a_student():
        print("A")


    def Approve_the_request_from_student():
        print("N")

    def Delete_students():
        print("I")

    lecturer_menu_choice()
# write your code inside the function
