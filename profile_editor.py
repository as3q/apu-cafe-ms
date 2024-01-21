import json, getpass, os
# from .pages.student import studentPage 

# Change User's Data Function #
def profileEditor(user, data, dataUpdater):
    tp = user["user_tp"]
    print(f"Hey, {tp}")

    while True:   
        profileEditorChoice = input(f"1.Change password\n2.Return to previous page\n")
        match profileEditorChoice:
            case '1':
                while True :
                    # Prompt User for New Password #
                    oldPasswordConfirm = getpass.getpass(prompt="Enter old password: ")
                    changedPassword = getpass.getpass(prompt="Enter new password: ")
                    changedPasswordConfirm = getpass.getpass(prompt="Confirm new password: ")
                    
                    if oldPasswordConfirm == user["password"] :
                        # Password Requirements Checker #
                            # to Confirm Password #
                        if changedPassword == changedPasswordConfirm:
                            if len(changedPassword) < 8:
                                print("Password too short!")
                            else:
                                # Password Should NOT Be Same as the Old Password #
                                if changedPassword == user["password"] :
                                    print("Password similar to the old one!")
                                    continue
                                else:
                                    # Assigning New Password #
                                    user["password"] = changedPassword

                                    dataUpdater(data)

                                    os.system('cls')
                                    print("Password successfully changed!")
                                    break
                                
                        else:
                
                            print("Password must match!")
                    else:
                        print("Old password is wrong!")

            case '2':
                return

            case other:
                print("Invalid choice!")
