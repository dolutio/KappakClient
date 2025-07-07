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
    
user_data = load_user_data()
user: User

if user_data is not None:
    user = User(*user_data)

else:
    user = User()


messages_show_place_widget = KappakNullable()
message_input_box = KappakNullable()
message_send_button = KappakNullable()

chats_data = KappakNullable()
current_chat_name = KappakNullable()

with open('chats.json', 'r') as chats_file:
    chats_data = json.load(chats_file)

def save_user_data():
    if user.signed_up:
        with open('user_data.json', 'w') as file:
            json.dump(user.get_user_data(), file, indent=4)


def save_chats_data():
    with open('chats.json', 'w') as file:
        json.dump(chats_data, file, indent=4)