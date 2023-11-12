from InquirerPy import inquirer 
import bankingProcess
from cls import file


user_phone = inquirer.text(message="What's your phone:").execute()
user_pass = inquirer.secret(message="What's your password:").execute()
data = file().get_data()
for user in data:
    if user['phone'] == user_phone and user['password'] == user_pass:
        bankingProcess(user, data)
        break 
    else:
        print("login failed. Please check your phone number and password")



