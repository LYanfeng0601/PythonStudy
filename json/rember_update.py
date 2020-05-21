import json


def get_store_name():
    file_name = 'usernames.json'
    try:
        with open(file_name) as f_obj:
            username = json.load(f_obj)
            return username
    except FileNotFoundError as e:
        return None


def get_new_username():
    username = input("please input your name")
    file_name = 'usernames.json'
    with open(file_name,'w') as f_obj:
    	json.dump(username,f_obj)
    return username


def greet_user():
    username = get_store_name()
    if username:
        print("welcome you back" + username)
    else:
        username = get_new_username()
        print("welcome you back" + username)

if __name__ == '__main__':
    greet_user()
