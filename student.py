# Import Profile Editor Function #
from profile_editor import profileEditor

# Student #
def studentPage(user, data):
    while True:
        # Student Menu Navigator #
        studentMenuChoice = input("1.Schedule\n2.Requests\n3.Payments\n4.Profile\n5.Return to menu\n")

        if studentMenuChoice == '1':
            print("schedule here")
            while True:
             studentSubMenuChoice = input("Enter B to return to Student menu\n")
             if studentSubMenuChoice.upper() == 'B':
                    studentPage(user)
                    break
             else:
                 print("invalid choice!")

        elif studentMenuChoice == '2':
            studentRequestMenu()
            # choicer

        elif studentMenuChoice == '3':
            studentPaymentMenu()
            # choicer

        elif studentMenuChoice == '4':
            profileEditor(user, data)
            break
            # choicer
        
        elif studentMenuChoice == '5':
            break

        else:
            print("Invalid choice!")
        
def studentRequestMenu():
    print("request")
    # Create Request #
    # Cancel Request #
    # View Requests (pending - canceled - approved) #

def studentPaymentMenu():
    print("payment")
    # Pay an Invoice "infoFromTrainer" #
    # View Paid Invoices #     

