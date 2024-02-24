def trainerPage(user, data, dataUpdater):

#     #db = open("data.txt", "r")
#     #data = json.load(db)
#     #print("trainer")
    def admin_menu_choice(user, data, dataUpdater):
        
        state= True
        while state == True:
            choise= input("1.Add class info \n 2. Update and delete class info \n 3. View list of students\n 4.Send feedback \n 5. Exit")
            match choise:
                case "1":
                    Add_class_info(user, data, dataUpdater)  
                case "2":
                    Update_delete_class_info(data)
                case"3":
                    View_list_students()
                case "4":
                    Send_feedback()
                case "5":
                    state= False
                    break
                case other:
                    print("Invalid choise, please chose form the given choises")
                    return
                
# Adding coaching info code
    def Add_class_info(user, data, dataUpdater):
        module_name = None
        fee = None
        strtclass = None
        level = None
        
        print("Adding coaching class information")
        module_name = input("Enter programming module: ")
        fee = input("Enter the fee: RM")
        strtclass = input("Enter the starting date (yyyy-mm-dd): ")
        level = input("Enter level: ") # Beginner - Intermediate - Advanced #
                    
        newmodule_id=f"{module_name.lower()[:2]}{level[:3].lower()}{strtclass[5:7]}"
        
        new_class = {
        "module_id": newmodule_id,
        "module_name": module_name,
        "module_level": level,
        "trainer_tp": None,
        "students_enrolled": [],
        "module_starting_date": strtclass,
        "module_fee": fee
        }
        
        data["modules_data"].append(new_class)
        
        dataUpdater(data)
        print("class added successfully!")
                
                        

#    #adding cource info
        
#    #########showing the modules to the trainer
#         for modules in data["modules_data"] :
#                 print(f"""                  
#                           module name: {modules["module_name"]}
#                           module leve:{modules["module_level"]}
#                           module starting: {modules["module_starting_date"]}
#                           module fee: {modules["module_fee"]}\n""")


  ########updatin and deleting 
    def Update_delete_class_info(data):
        choise4= input('Enter the module ID of the module')
        for update in data["modules_data":]:
            if choise4==update["module_id"]:
                print("Updating and deleting coaching class info")
                state1= True
                while state1 == True:
                    choise2= input("1. Update \n 2.Delete")
                    match choise2:
                        case"1":
                            update_info(data, dataUpdater)
                        case "2":
                             deleting()
                        case "3":
                            state1= False
                        case other:
                            print("Invalid choise, please chose form the given choises, choose from the given number please")
            else:
                print("this TP dose not exixt try again")
                        

    # updating foncation   
    def update_info(data , dataUpdater):
        choise5= input('1.module name\n 2.module level3\n3.module starting data\n4.module fee')
        if choise5== "module name":
            update_moudle_name()
        elif  choise5== "module level":
            update_module_level()
    
        elif choise5== "module starting date":
            update_moudle_starting_date()
    
        elif  choise5== "module fee":
            update_module_fee()
        else:
            print("viled coice")
    #function for the udateing confunction                
    def update_moudle_name(dataUpdater , data):
        newmodulename= input("Enter the new name")
        newmoduleupdatedname={"module_name":newmodulename}
        data["module_data"]["module_name"].append(newmoduleupdatedname)
        dataUpdater(data)


    def update_module_level():
        newmodulelevel= input("Enter the new level")
        newmoduleupdatelevel={"module_level":newmodulelevel}
        data["module_data"]["module_level"].append(newmoduleupdatelevel)
        dataUpdater(data)
               
    def update_moudle_starting_date():
        newdate= input("Enter the new date")
        newupdatedate={"module_starting_date":newdate}
        data["module_data"]["module_starting_date"].apppend(newupdatedate)
        dataUpdater(data)

    def update_module_fee():
       newfee= input("Enter the new fee")
       newupdatefee={"module_fee":newfee}
       data["module_data"]["module_fee"].append(newupdatefee)
       dataUpdater(data)
                    
    #deleteing a module 
    def deleting():
       for deletedata in data["modules_data"]:
        if choise4 == deletedata["module_id"]:
           data["module_id"].remove(deletedata)
           dataUpdater(data)
    


    #viewlist of student
    def View_list_students():
        for students in data["modules_data"]:
            print(students["students_enrolled"])
            input("unter SHIFT to go to the menu")
        
    
    ##send feedback
    def Send_feedback():
        new_message= input("Enter a massage\n")
    
        ids=[]
        for feedback in data["trainer_feedback"]:
            ids.append(feedback["message_id"])
            
            new_id= int(max(ids))+1
            
            new_feedback= {"massage=id":new_id,
                        "author_tp": user["user_tp"],
                        "message":new_message}
                        
        data["trainer_feedback"].append(new_feedback)     
        
        dataUpdater(data)
    admin_menu_choice(user, data, dataUpdater)
    
    
# write your code inside the function