# Student #
def studentPage():
    while True:
        studentMenuChoice = input("1.Schedule\n2.Requests\n3.Payments\n4.Profile\n5.Return to menu\n")
        if studentMenuChoice == '1':
            print("schedule here")
            break        
        elif studentMenuChoice == '2':
            studentRequestMenu()
            break
        elif studentMenuChoice == '3':
            studentPaymentMenu()
            break
        elif studentMenuChoice == '4':
            # profileEditor()
            break
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

# # Initiator #
# studentPage()