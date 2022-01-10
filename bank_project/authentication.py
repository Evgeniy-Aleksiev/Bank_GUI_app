import json
import os


DB_FOLDER_NAME = 'db'
USER_FILE_NAME = 'users.txt'
SESSION_FILE_NAME = 'sessions.txt'


def register(username, password, first_name, last_name):
    with open(os.path.join(DB_FOLDER_NAME, USER_FILE_NAME), 'r+') as file:

        for user_line in file:
            user = json.loads(user_line.strip())
            if user['username'] == username:
                return 'The username has been already registered!'

            if user['password'] == password:
                return 'The password is already taken.'

        user_obj = {
            'username': username,
            'password': password,
            'firstName': first_name,
            'lastName': last_name
        }

        file.write(json.dumps(user_obj))
        file.write('\n')
        return True


def login(username, password):
    with open(os.path.join(DB_FOLDER_NAME, USER_FILE_NAME), 'r+') as user, \
            open(os.path.join(DB_FOLDER_NAME, SESSION_FILE_NAME), 'w') as session:
        for user_line in user:
            user = json.loads(user_line.strip())
            if user['username'] == username and user['password'] == password:
                session.write(user_line)
                return True
        return False


def forgotten_password(username):
    with open(os.path.join(DB_FOLDER_NAME, USER_FILE_NAME), 'r+') as user:

        for user_line in user:
            user = json.loads(user_line.strip())
            if user['username'] == username:
                return True
        return False


def changing_password(username, password):
    with open(os.path.join(DB_FOLDER_NAME, USER_FILE_NAME), 'r+') as file:
        users = file.readlines()
        file.seek(0)
        for user in users:
            user_as_dict = json.loads(user)
            if user_as_dict.get('username') == username:
                user_as_dict['password'] = password
            file.write(json.dumps(user_as_dict))
            file.write('\n')
            return True
        return False

