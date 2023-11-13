import json
from InquirerPy import inquirer


class file:
    def get_data(self):
        with open('data.json') as f:
            return json.load(f)
    def write_data(self,_new_data):
        with open('data.json', "w") as f:
            f.write(json.dumps(_new_data, indent=4))


def send_money ( user):
    amount = get_amount(user)
    receiver_phone = get_receiver()
    sender_phone = user["phone"]
    data = file().get_data()
    try :
        for i in data:
            if i["phone"] == sender_phone:
                i["balance"] =i["balance"] - amount
            elif i["phone"] == receiver_phone:
                i["balance"] = i["balance"] + amount
        file().write_data(data)
        return True        
    except Exception as error:
        print(error,"error")
        return False   

def get_receiver ():
    number = inquirer.text(message="Enter the receiver Phone number:").execute()
    data = file().get_data()
    for i in data:
        if i["phone"] == number :
            return number
    
    print("Receiver User not found. Please check the phone number")
    get_receiver()


def get_amount (user):
    amount = int(inquirer.text(message="Enter Amount").execute())
    if int(user["balance"]) > amount :
            return amount
    else:
        print("Insufficient Balance Check the input")
        get_amount(user)


def change_pass (user):
    old_password = inquirer.secret(message="Enter your old password:").execute()
    new_password = inquirer.secret(message="Enter your new password:").execute()
    confirm_password = inquirer.secret(message="Confirm your new password:").execute()
    data = file().get_data()
    if(old_password == user["password"] and new_password == confirm_password):
        for i in data:
            if i["phone"] == user["phone"]:
                    i["password"] = new_password
            file().write_data(data)
        return True
    else:
        print("check your old password and maybe your password and confirm password are not same")
        change_pass(user)
