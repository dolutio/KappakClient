import json
from kappak_user import User

class KappakNullable: # for objects still non defined
    def __init__(self):
        return None

    def __getattribute__(self, name):
        print(f"KappakNullable object have not {name} attribute")
        
        return self

    def __call__(self, *args, **kwds):
        print(f"KappakNullable object is not callable, arguments: {args=}, {kwds=}")

        return self
    
    def __bool__(self):
        return False

def load_user_data():
    try:
        with open('user_data.json', 'r') as file:
            data = json.load(file)

            return data['username'], data['age'], data["the_last_sended_message_id"], data["need_to_filter_censoreship"]
    
    except FileNotFoundError:
        return None

def load_chats_data():
    try:
        with open('chats.json', 'r') as chats_file:
            data = json.load(chats_file)

    except FileNotFoundError:
        data = dict()
    
    return data
    
user_data = load_user_data()
user: User

chats_data = load_chats_data();print("ChData:", chats_data)

if user_data is not None:
    user = User(*user_data)

else:
    user = User()


messages_show_place_widget = KappakNullable()
message_input_box = KappakNullable()
message_send_button = KappakNullable()

current_chat_name = KappakNullable()



def save_user_data():
    if user.signed_up:
        with open('user_data.json', 'w') as file:
            json.dump(user.get_user_data(), file, indent=4)


def save_chats_data():
    with open('chats.json', 'w') as file:
        if chats_data:
            json.dump(chats_data, file, indent=4)
