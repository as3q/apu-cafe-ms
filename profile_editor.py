# Change User's Data Function #
def profileEditor(user):
    print(f"Hey, {user[0]}")
    
    profileEditorChoice = input(f"1.Change password\n2.Return to previous page\n")
    if profileEditorChoice == '1':
        while True :
            # Prompt User for New Password #
            changedPassword = input("Enter new password: ")
            changedPasswordConfirm = input("Confirm new password: ")
            
            # Password Requirements Checker #
            if changedPassword == changedPasswordConfirm:
                if len(changedPassword) < 8:
                    print("Password too short!")
                else:
                    user[1] = changedPassword
                    break
            else:
                print("Password must match!")
    else:
        print("Invalid choice!")
