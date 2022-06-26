from json import dumps, loads

USERS_DB_PATH_FILE = './users.txt'


def register(username, password):
    with open(USERS_DB_PATH_FILE, 'r') as users_db:
        for line in users_db:
            user = loads(line.strip())
            if user['username'] == username:
                return False

    with open(USERS_DB_PATH_FILE, 'a') as users_db:
        user = {
            'username': username,
            'password': password,
            'products': [],
        }
        user_json = dumps(user)
        users_db.write(user_json + '\n')
        return True


def login(username, password):
    with open(USERS_DB_PATH_FILE, 'r') as users_db, open('./current_user.txt', 'w') as current_user_file:
        for line in users_db:
            user = loads(line.strip())
            if user['username'] == username and user['password'] == password:
                current_user_file.write(username)
                return True
        return False


def get_current_user():
    with open('./current_user.txt', 'r') as file:
        return file.read().strip()