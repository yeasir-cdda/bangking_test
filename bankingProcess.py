import sys
from InquirerPy import inquirer
from cls import file

def bankingProcess (user,data):
    print("Welcome to the banking system", user["name"])
    operation = inquirer.select(
            message="What you want to do?",
            choices=["Check Balance", "Change Password", "send Money","Exit"],
        ).execute()
    confirm = inquirer.confirm(message="Confirm?").execute()
    if(confirm):
        if(operation == "check Balance"):
            print("Your Balance is", user["balance"])
            previous_operation = inquirer.confirm(message="Do you want to back previous menu?").execute()
            if(previous_operation):
                bankingProcess(user)
            else:
                sys.exit()
        elif(operation == "Change Password"):
            old_password = inquirer.secret(message="Enter your old password:").execute()
            new_password = inquirer.secret(message="Enter your new password:").execute()
            confirm_password = inquirer.secret(message="Confirm your new password:").execute()
            if(old_password == user["password"] and new_password == confirm_password):
                
                user["password"] = new_password
                for i in data:
                    if i["phone"] == user["phone"]:
                         i["password"] = new_password
                    file().write_data(data)
                print("Password changed successfully")
                previous_operation = inquirer.confirm(message="Do you want to back previous menu?").execute()
                if(previous_operation):
                    bankingProcess(user,data)
                else:
                    sys.exit()
            else:
                print("check your old password and maybe your password and confirm password are not same")
        elif(operation == "send Money"):
            receiver_phone = inquirer.text(message="Enter the receiver Phone number:").execute()
            amount = inquirer.text(message="Enter Amount").execute()
            if(amount > user["balance"]):
                print("Insufficient Balance")
                confirm= inquirer.confirm(message="Do you want to try again?").execute()
                if confirm:
                   amount = inquirer.text(message="Enter Amount").execute()
            for i in data:
                if i["phone"] != receiver_phone:
                    print("Receiver User not found. Please check the phone number")
                    receiver_phone = inquirer.text(message="Enter the receiver Phone number again:").execute()
            
            
                    



sys.modules[__name__] = bankingProcess    