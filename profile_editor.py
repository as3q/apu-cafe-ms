# Change User's Data Function #
def profileEditor(user, json_data):
    email = user[0]
    print(f"Hey, {email}")
    
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
                    if changedPassword == user[1] :
                        print("Password similar to the old one!")
                    else:
                        user["password"] = changedPassword

                    # Updating JSON Database #
                    json_data["users_data"].update(user["password"])

                    # Updating Database in Text File #
                    db = open("data.txt", "w")
                    db.write(json_data)
                    db.close
                    
                    break
            else:
                print("Password must match!")
    else:
        print("Invalid choice!")
