from json import loads, dumps
from auth_service import get_current_user


def purchase_product(product_id):
    with open('./users.txt', 'r+') as file:
        current_username = get_current_user()
        result = []
        for user_line in file:
            user_obj = loads(user_line.strip())
            if user_obj['username'] == current_username:
                user_obj['products'].append(product_id)
                result.append(dumps(user_obj) + '\n')
            else:
                result.append(user_line)

        file.seek(0)
        file.truncate()

        file.writelines(result)