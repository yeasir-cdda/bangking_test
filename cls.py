import json


class file:
    def get_data(self):
        with open('data.json') as f:
            return json.load(f)
    def write_data(self,_new_data):
        with open('data.json', "w") as f:
            f.write(json.dumps(_new_data, indent=4))


def send_money (receiver_phone, sender_phone,amount):
    try :
        print("Sss")

    except e as e:
        print("Ss")   