import requests
import constants


class User:

    def __init__(self):
        self.username = "MuravevaTest"
        self.user_data = {
            "id": 1,
            "username": self.username,
            "firstName": "test",
            "lastName": "test",
            "email": "test@test.com",
            "password": "qwerty",
            "phone": "89990000000",
            "userStatus": 0
        }
        self.headers = {
            "accept": "application/json",
            "Content-Type": "application/json"
        }

    def create_user(self):

        r = requests.post(url=constants.BASE_USER_URL, headers=self.headers, json=self.user_data)
        if r.status_code == 200:
            print(constants.USER_CREATE_SUCCESS_MESSAGE)
            return 200
        process_status_code_err(r.status_code)
        return r.status_code

    def updatе_user(self, upd):
        r = requests.put(url=f'{constants.BASE_USER_URL}/{self.username}', headers=self.headers, json=upd)
        if r.status_code == 200:
            print(constants.USER_UPDATE_SUCCESS_MESSAGE)
            return 200
        process_status_code_err(r.status_code)
        return r.status_code

    def get_user_by_user_name(self):
        r = requests.get(url=f'{constants.BASE_USER_URL}/{self.username}', headers=self.headers)
        if r.status_code == 200:
            print(r.json())
            return 200
        process_status_code_err(r.status_code)
        return r.status_code

    def delete_user(self):
        r = requests.delete(url=f'{constants.BASE_USER_URL}/{self.username}', headers=self.headers)
        if r.status_code == 200:
            print(constants.USER_DELETE_SUCCESS_MESSAGE)
            return 200
        process_status_code_err(r.status_code)
        return r.status_code


def process_status_code_err(status_code):
    if status_code == 400:
        raise UserWarning(f'{constants.INCORRECT_USER_NAME_FAIL_MESSAGE}{status_code}')
    elif status_code == 404:
        raise UserWarning(f'{constants.INCORRECT_USER_NAME_FAIL_MESSAGE}{status_code}')
    else:
        raise UserWarning(f'{constants.UNKNOWN_ERROR_MESSAGE}{status_code}')
