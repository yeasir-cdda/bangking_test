import sys
from InquirerPy import inquirer
from cls import send_money,change_pass

def bankingProcess (user,data):
    print("Welcome to the banking system", user["name"])
    operation = inquirer.select(
            message="What you want to do?",
            choices=["Check Balance", "Change Password", "send Money","Exit"],
        ).execute()
    confirm = inquirer.confirm(message="Confirm?").execute()
    if(confirm):
        if(operation == "Check Balance"):
            print("Your Balance is", user["balance"])
            previous_operation = inquirer.confirm(message="Do you want to back previous menu?").execute()
            if(previous_operation):
                bankingProcess(user,data)
            else:
                sys.exit()
        elif(operation == "Change Password"):
            if change_pass(user):
                previous_operation = inquirer.confirm(message="Do you want to back previous menu?").execute()
                if(previous_operation):
                    bankingProcess(user,data)
                else:
                    sys.exit()
            
        elif(operation == "send Money"):
            if send_money(user):
                print("Sending Money is Successful")
            else:
                print("Something went wrong")
                confirm = inquirer.confirm(message="Do you want to try again?").execute()
                if(confirm):
                    send_money(user)
                else:
                    sys.exit()
        elif(operation == "Exit"):
            sys.exit()
            
            
                    



sys.modules[__name__] = bankingProcess    