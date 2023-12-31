# Change Users' Data Function #
def profileEditor(user):
    print("Edit")
    print(f"Hey, {user[0]}")
    profileEditorChoice = input(f"1.Change password\n2.Return to previous page\n")
    if profileEditorChoice == '1':
        while True :
            changedPassword = input("Enter new password: ")
            changedPasswordConfirm = input("Confirm new password: ")
            
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
