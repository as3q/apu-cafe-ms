import getpass

def profileEditor(user, data, profileChanged, syncData):
    name = user["fullname"].split(" ")
    print(f"Hey, {name[0]}")

    while True:
        if profileChanged:
            return False

        profileEditorChoice = input("1. Change password\n2. Return to menu\n")
        match profileEditorChoice:
            case '1':
                while True:
                    # Prompt User for New Password #
                    oldPasswordConfirm = getpass.getpass(prompt="Enter old password: ")
                    changedPassword = getpass.getpass(prompt="Enter new password: ")
                    changedPasswordConfirm = getpass.getpass(prompt="Confirm new password: ")

                    # Confirm Entered Old Password #
                    if oldPasswordConfirm != user["password"]:
                        print("Old password is wrong!")
                        break

                    # New Password Should Not be Same as the Old One #
                    if changedPassword == user["password"]:
                        print("Password similar to the old one!")
                        break

                    # Password Should be at least Eight Letters/Digits #
                    if len(changedPassword) < 8:
                        print("Password too short!")
                        break

                    # Check New Password Confirmation #
                    if changedPassword != changedPasswordConfirm:
                        print("Password must match!")
                        break

                    # Assigning New Password #
                    user["password"] = changedPassword
                    syncData(data)
                    print("Password successfully changed!")
                    return True

            case '2':
                break

            case other:
                print("Invalid choice!")
