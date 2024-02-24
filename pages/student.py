# Importing Libraries #
import os, datetime, time
from profile_editor import profileEditor 

# Importing os to Clear Terminal (lines , , ) #
# Importing json to Read Data from Text File (lines , ) #
# Importing datetime to Display Current Time (line ) #
# Importing time to Simulate Paying Transaction (line ) #

# Get Current Date #
currentDate = datetime.date.today()

# A Function to Refresh Lists after Updating the Text File #
def refreshLists(data):
    global pendingRequests, approvedRequests, canceledRequests, deniedRequests, allModules, allRequests, unpaidInvoices, paidInvoices

    # Updating Requests Lists #
    pendingRequests = [request for request in data["enrollment_requests"][0]["pending_requests"]]
    approvedRequests = [request for request in data["enrollment_requests"][0]["approved_requests"]]
    canceledRequests = [request for request in data["enrollment_requests"][0]["canceled_requests"]]
    deniedRequests = [request for request in data["enrollment_requests"][0]["denied_requests"]]

    allModules = [module for module in data["modules_data"]]
    allRequests = [pendingRequests + approvedRequests + canceledRequests + deniedRequests]

    # Grab/Update and Sort Invoices #
    unpaidInvoices = data["invoices_data"][0]["unpaid_invoices"]
    paidInvoices = data["invoices_data"][0]["paid_invoices"]

# Student #
def studentPage(user, data, dataUpdater, grabModule, grabTrainerName):
    # Modules into list #
    allModules = [module for module in data["modules_data"]]

    studentCurrentModules = [scmodule for scmodule in allModules for student in scmodule["students_enrolled"]
                             if student["student_tp"] == user["user_tp"]]

    # A Boolean to Log the Student out if They Change Password (True) #
    profileChanged = False

    # Student Menu Loop #
    while True:
        # Student Menu Navigator #
        studentMenuChoice = input("1.Schedule\n2.Requests\n3.Payments\n4.Profile\n5.Log out\n")

        match studentMenuChoice:
            case '1':
                studentScheduleViewer(data, studentCurrentModules, grabTrainerName)

            case '2':
                studentRequestMenu(user, data, dataUpdater, grabTrainerName, grabModule)

            case '3':
                studentPaymentMenu(user, data, dataUpdater)

            case '4':
                profileChanged = profileEditor(user, data, profileChanged, dataUpdater)
                if profileChanged == True:
                    break

            case '5':
                print("Logging out...")
                break

            case other:
                print("Invalid choice!")

# Student Functions #
def studentScheduleViewer(data, studentCurrentModules, grabTrainerName):
    while True:

        refreshLists(data)

        # Read Schedule Made by Trainer #
        print("Schedule:")

        if len(studentCurrentModules) == 0:
            print("No scheduled modules :)")

        for module in studentCurrentModules:
            moduleTimetable = module["module_timetable"]

            trainerName = grabTrainerName(module["trainer_tp"])

            print(f'Module: {module["module_name"]} ({module["module_level"]})')
            print(f"Trainer: {trainerName} \n---------")
            print(f'Monday: {moduleTimetable[0]["Monday"]}')
            print(f'Tuesday: {moduleTimetable[1]["Tuesday"]}')
            print(f'Wednesday: {moduleTimetable[2]["Wednesday"]}')
            print(f'Thursday: {moduleTimetable[3]["Thursday"]}')
            print(f'Friday: {moduleTimetable[4]["Friday"]}')
            print("--------------------")

        studentExitChoice = input("Enter R to return to menu\n")
        if studentExitChoice.upper() == 'R':
            break
        else:
            print("invalid choice!")

def studentRequestMenu(user, data, dataUpdater, grabTrainerName, grabModule):
    studentRequestMenu = True

    while studentRequestMenu == True:

        refreshLists(data)

        studentPendingRequests = [requestpending for requestpending in pendingRequests if
                                  requestpending["student_tp"] == user["user_tp"]]
        studentApprovedRequests = [requestapproved for requestapproved in approvedRequests if
                                   requestapproved["student_tp"] == user["user_tp"]]

        # Request Menu Loop #
        requestMenuChoice = input("1.Create a request\n"
                                  "2.Cancel a request\n"
                                  "3.View requests\n"
                                  "4.Return to Student menu\n")
        match requestMenuChoice:
            case '1':
                ## Create Request ##

                # Temporary ID for Module #
                tempModuleID = 1

                # Only Show Modules the student is not enrolled in #
                availableModules = [module for module in allModules if user["user_tp"] not in
                                    [student["student_tp"] for student in module["students_enrolled"]]]

                if len(availableModules) == 0:
                    print("No available modules at the moment!")

                moduleIDs = []

                # Display Available-to-Request Modules #
                for moduleDisplaying in availableModules:
                    if moduleDisplaying["module_id"] not in [pending["module_id"] for pending in studentPendingRequests]:
                        if moduleDisplaying["module_id"] not in [approved["module_id"] for approved in
                                                                 studentApprovedRequests]:
                            moduleIDs.append(moduleDisplaying["module_id"])

                            trainerNamer = grabTrainerName(moduleDisplaying["trainer_tp"])

                            moduleName = moduleDisplaying["module_name"]
                            moduleLevel = moduleDisplaying["module_level"]
                            moduleFee = moduleDisplaying["module_fee"]
                            moduleDate = moduleDisplaying["module_starting_date"]

                            print(f"Module ID: {tempModuleID}")
                            print(f"Module: {moduleName} {(moduleLevel)}")
                            print(f"Trainer: {trainerNamer}")
                            print(f"Module Fee: {moduleFee}RM")
                            print(f"Starting at {moduleDate}")
                            print("--------------------")

                            tempModuleID += 1

                # Request ID Counter #
                newRequestID = len(allRequests[0]) + 1

                while True:
                    moduleIDChoice = input("Enter module ID that you want to join (or Enter R to return back to Request menu): ")

                    if moduleIDChoice.isnumeric() and 0 < int(moduleIDChoice) <= len(moduleIDs):
                        for moduleRequesting in availableModules:

                            moduleIDNumber = int(moduleIDChoice)
                            moduleID = moduleIDs[moduleIDNumber]

                            if moduleID == moduleRequesting["module_id"]:

                                # New Request Formatting #
                                newRequest = {
                                    "request_id": f"{newRequestID}",
                                    "student_tp": user["user_tp"],
                                    "trainer_tp": moduleRequesting["trainer_tp"],
                                    "module_id": moduleRequesting["module_id"],
                                    "request_status": "Pending",
                                    "issue_date": f'{currentDate}',
                                    "processed_date": "None"
                                }

                                # Adding the Request to Database #
                                data["enrollment_requests"][0]["pending_requests"].append(newRequest)

                                dataUpdater(data)

                                print("Request sent successfully!")
                                continue
                        break

                    elif moduleIDChoice.upper() == "R":
                        break

                    else:
                        print("Invalid Option!")

            case '2':
                ## Cancel Request ##

                if len(studentPendingRequests) == 0:
                    print("No Pending requests :(")
                # Viewing Student's Pending Requests #
                for request in studentPendingRequests:
                    trainerName = grabTrainerName(request["trainer_tp"])

                    moduleName, moduleLevel, moduleFee, moduleDate = grabModule(request["trainer_tp"], "trainer_tp")

                    print(f'Request ID: {request["request_id"]}\n'
                          f"Module: {moduleName} ({moduleLevel})\n"
                          f"Trainer: {trainerName}\n"
                          f"Module Fee: {moduleFee}\n"
                          f'requested on {request["issue_date"]}\n'
                          f'Status: {request["request_status"]}')
                    print("--------------------")

                # Cancel by Request ID #
                while True:

                    moduleIDChoiceCancel = input("Enter module ID that you want to cancel (Enter R to return back): ")

                    if moduleIDChoiceCancel.isnumeric():
                        for requestCanceling in pendingRequests:
                            if moduleIDChoiceCancel == requestCanceling["request_id"]:

                                # Remove the Request from Pending Status List #
                                data["enrollment_requests"][0]["pending_requests"].remove(requestCanceling)

                                # New Status and Cancelation Date #
                                requestCanceling["request_status"] = "Canceled"
                                requestCanceling["processed_date"] = currentDate

                                # Add the Request to Canceled Status List #
                                data["enrollment_requests"][0]["canceled_requests"].append(requestCanceling)

                                dataUpdater(data)

                                print("Request deleted successfully!")
                                continue

                            else:
                                print("ID not found!")

                    elif moduleIDChoiceCancel.upper() == "R":
                        break

                    else:
                        print("Invalid Options!")

            case '3':
                # View Requests (pending - canceled - approved - rejected) #

                while True:
                    # Grabbing Student's Requests Only #
                    studentRequests = []
                    for stuRequest in allRequests[0]:
                        if stuRequest["student_tp"] == user["user_tp"]:
                            studentRequests.append(stuRequest)

                    if len(studentRequests) == 0:
                        print("You don't have any requests.")

                    else:
                        for viewStuRequest in studentRequests:
                            if viewStuRequest["request_status"] == "Pending":
                                requestState = "Still Pending"
                            else:
                                requestState = f'{viewStuRequest["request_status"]} on {viewStuRequest["processed_date"]}'

                            # Requests Viewer Format #
                            print(f"Request ID: {viewStuRequest['request_id']}")
                            print(f"Module ID: {viewStuRequest['module_id']}")
                            print(f"Trainer TP: {viewStuRequest['trainer_tp']}")
                            print(f"Issue Date: {viewStuRequest['issue_date']}")
                            print(f"Status: {requestState}")
                            print("--------------------")

                    requestViewerChoice = input("Enter R to return back\n")
                    if requestViewerChoice.upper() == "R":
                        break
                    else:
                        print("Invalid option!")

            case '4':
                studentRequestMenu = False
                break

            case other:
                print("Invalid Option!")

def studentPaymentMenu(user, data, dataUpdater):
    studentPaymentMenu = True
    while studentPaymentMenu == True:

        refreshLists(data)

        paymentMenuChoice = input("1.Pay an invoice\n2.View paid invoices\n3.Return to menu\n")
        match paymentMenuChoice:
            case '1':

                # Filter invoices by student #
                studentUnpaidInvoices = [uninvoice for uninvoice in unpaidInvoices if uninvoice["student_tp"] == user["user_tp"]]

                if len(studentUnpaidInvoices) == 0:
                    print("No invoices to pay :D")

                else:
                    # Print the filtered invoices #
                    for duninvoice in studentUnpaidInvoices:
                        # Grab module details for invoice using module id #
                        for modulePay in allModules:
                            if duninvoice["module_id"] == modulePay["module_id"]:
                                modulePayName = modulePay["module_name"]
                                modulePayLevel = modulePay["module_level"]

                        print("Invoice ID:", duninvoice["invoice_id"])
                        print("Module:", f"{modulePayName} ({modulePayLevel})")
                        print("Payable:", duninvoice["payable"])
                        print("--------------------")

                while True:
                    # Payment by ID #
                    paymentPayIDChoice = input(
                        "Please enter invoice ID to pay the invoice (or press R to return back): ")

                    if paymentPayIDChoice.isnumeric():
                        for payingInvoice in studentUnpaidInvoices:
                            if paymentPayIDChoice == payingInvoice["invoice_id"]:
                                print("Transaction in process\nPlease wait")
                                time.sleep(2)

                                payingInvoice["invoice_status"] = "paid"
                                payingInvoice["payable"] = 0
                                payingInvoice["transaction_date"] = f'{currentDate}'

                                newEnrollee = {"student_tp": user["user_tp"], "enrollment_date": f'{currentDate}'}

                                for moduleEnroll in allModules:
                                    students = moduleEnroll["students_enrolled"]

                                    if moduleEnroll["module_id"] == payingInvoice["module_id"]:
                                        # Update the students_enrolled list of the module
                                        students.append(newEnrollee)

                                for oldInvoice in data["invoices_data"][0]["unpaid_invoices"]:
                                    if paymentPayIDChoice == oldInvoice["invoice_id"]:
                                        data["invoices_data"][0]["unpaid_invoices"].remove(oldInvoice)

                                data["invoices_data"][0]["paid_invoices"].append(payingInvoice)

                                dataUpdater(data)

                                os.system('cls')
                                print("payment successfull!")
                                break
                            else:
                                print("Invalid ID!")

                    elif paymentPayIDChoice.upper() == 'R':
                        break

            case '2':
                while True:
                    # Filter invoices by student #
                    studentPaidInvoices = [pinvoice for pinvoice in paidInvoices if pinvoice["student_tp"] == user["user_tp"]]

                    if len(studentPaidInvoices) == 0:
                        print("You have no paid invoices yet :(")

                    else:

                        # Print the filtered invoices #
                        for dpinvoice in studentPaidInvoices:
                            # Grab module details for invoice using module id #
                            for module in allModules:
                                if dpinvoice["module_id"] == module["module_id"]:
                                    moduleName = module["module_name"]
                                    moduleLevel = module["module_level"]

                            print("Invoice ID:", dpinvoice["invoice_id"])
                            print("Module:", f"{moduleName} ({moduleLevel})")
                            print(f"Paid {module['module_fee']}RM on", dpinvoice["transaction_date"])
                            print("--------------------")

                    studentExitChoice = input("Enter R to return back\n")
                    if studentExitChoice.upper() == 'R':
                        break
                    else:
                        print("invalid choice!")

            case '3':
                studentPaymentMenu = False
                return

            case other:
                print("Invalid option!")
