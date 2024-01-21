# Import Profile Editor Function #
from profile_editor import profileEditor

import os, json, time, datetime

# Student #
def studentPage(user, data, dataUpdater):
    
    modulesData = data["modules_data"]
    
    studentCurrentModules = [module for module in modulesData for student in module["students_enrolled"] if student == user["user_tp"]]
    
    # Student Menu Loop #
    while True:
        # Student Menu Navigator #
        studentMenuChoice = input("1.Schedule\n2.Requests\n3.Payments\n4.Profile\n5.Log out\n")

        if studentMenuChoice == '1':
            studentScheduleViewer()

        elif studentMenuChoice == '2':
            studentRequestMenu()
            # choicer

        elif studentMenuChoice == '3':
            studentPaymentMenu(data, user, modulesData, dataUpdater)

        elif studentMenuChoice == '4':
            profileEditor(user,data, dataUpdater)
        
        elif studentMenuChoice == '5':
            print("Logging out...\n")
            break

        else:
            print("Invalid choice!")

# Student's Menu Functions #
                  
def studentScheduleViewer():
    while True:
        print("Schedule")

        studentScheduleExitChoice = input("Enter B to return to Student menu\n")
        if studentScheduleExitChoice.upper() == 'B':
            break
        else:
            print("invalid choice!")

def studentRequestMenu():
    print("request")
    # Create Request #
    # Cancel Request #
    # View Requests (pending - canceled - approved) #

def studentPaymentMenu(data, user, modulesData, dataUpdater):
                        
    # Access the unpaid invoices
    unpaidInvoices = data["invoices_data"][0]["unpaid_invoices"]
    paidInvoices = data["invoices_data"][0]["paid_invoices"]

    while True:

        paymentMenuChoice = input("1.Pay an invoice\n2.View paid invoices\n3.Return to menu\n")
        match paymentMenuChoice :
            case '1':

                # Filter invoices by student #
                studentUnpaidInvoices = [invoice for invoice in unpaidInvoices if invoice["student_tp"] == user["user_tp"]]

                if len(studentUnpaidInvoices) == 0:
                    print("No unpaid invoices :)\n")
                
                else:

                    # Print the filtered invoices #
                    for invoice in studentUnpaidInvoices:
                        # Grab module details for invoice using module id #
                        for module in modulesData:
                            if invoice["module_id"] == module["module_id"]:
                                moduleName = module["module_name"]
                                moduleLevel = module["module_level"]

                        print("Invoice ID:", invoice["invoice_id"])
                        print("Module:", f"{moduleName} ({moduleLevel})")
                        print("Payable:", invoice["payable"])
                        print("--------------------")

                # Fix invalid ID #
                paymentPayIDChoice = input("Please enter invoice ID to pay the invoice: ")

                for payingInvoice in studentUnpaidInvoices:
                    if paymentPayIDChoice == payingInvoice["invoice_id"]:
                        print("Transaction in process\nPlease wait")
                        time.sleep(4)

                        currentDate = datetime.date.today()

                        payingInvoice["invoice_status"] = "paid"
                        payingInvoice["payable"] = 0
                        payingInvoice["transaction_date"] = f"{currentDate}"

                        module["students_enrolled"].append(user["user_tp"])

                    for oldInvoice in data["invoices_data"][0]["unpaid_invoices"]:
                        if paymentPayIDChoice == oldInvoice["invoice_id"]:
                            data["invoices_data"][0]["unpaid_invoices"].remove(oldInvoice)
                                    
                    data["invoices_data"][0]["paid_invoices"].append(payingInvoice)

                    dataUpdater(data)

                    os.system('cls')
                    print("payment successfull!\n")
                    break

            case '2':
               print("paid")

            case '3':
                return

            case other:
                print("Invalid option!")

          