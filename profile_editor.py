import json

# Change User's Data Function #
def profileEditor(user, data):
    tp = user["user_tp"]
    print(f"Hey, {tp}")
    
    profileEditorChoice = input(f"1.Change password\n2.Return to previous page\n")
    if profileEditorChoice == '1':
        while True :
            # Prompt User for New Password #
            changedPassword = input("Enter new password: ")
            changedPasswordConfirm = input("Confirm new password: ")
            
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

                        # Updating JSON Database #
                        json_data = json.dumps(data, indent=4)

                        # Updating Database in Text File #
                        db = open("data.txt", "w")
                        db.write(json_data)
                        db.close

                        print("Password successfully changed!")
                        break
                    
            else:
                print("Password must match!")
    else:
        print("Invalid choice!")
