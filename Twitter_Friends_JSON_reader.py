import json
import requests
from requests_oauthlib import OAuth1
import private

def input_data():
    screen_name = input("Enter user nickname: ")
    url = "https://api.twitter.com/1.1/friends/list.json?screen_name=" + \
          screen_name
    # auth = OAuth1(API_KEY, API_SECRET, TOKEN_KEY, TOKEN_SECRET)
    auth = OAuth1(private.api_key, private.api_key_secret,
                  private.token, private.token_secret)

    req = requests.get(url, auth=auth)

    users_python = json.loads(req.text)
    users_json = json.dumps(users_python, indent=4)

    f = open("subs.json", "w")
    f.write(users_json)
    f.close()
    return users_json


def json_operator(json_users):
    python_users = json.loads(json_users)

    current_dict = "python_users"
    old_dict = current_dict
    current_level_str = "> "
    old_level_str = current_level_str

    while True:
        print(current_level_str)

        if isinstance(eval(current_dict), list):
            for el in range(len(eval(current_dict))):
                print("Object #" + str(el))
            command = input("\nEnter object number to check, 'back' to return"
                            " one level back or 'exit' to exit: ")

        elif isinstance(eval(current_dict), dict):
            for key, value in eval(current_dict + ".items()"):
                if (isinstance(value, list) and value) or isinstance(value, dict):
                    print("[+]", key)
                else:
                    print(key, ":", value)
            command = input("\nEnter a key to check, 'back' to return one"
                            " level back or 'exit' to exit: ")

        if command == "exit" or ' ' in command:
            return
        elif command == "back":
            current_dict = old_dict
            current_level_str = old_level_str
        elif (isinstance(eval(current_dict), list) and
              int(command) not in range(len(eval(current_dict)))) or\
                (isinstance(eval(current_dict), dict) and
                 command not in eval(current_dict + ".keys()")):
            print("\nPlease, type correct level name or number!", '\n')
            continue
        else:
            old_dict = current_dict
            old_level_str = current_level_str

            if isinstance(eval(current_dict), list):
                current_dict += "[" + command + "]"
            elif isinstance(eval(current_dict), dict):
                current_dict += "['" + command + "']"
            current_level_str += command + " > "
        print('\n')


if __name__ == "__main__":
    users = input_data()
    json_operator(users)
