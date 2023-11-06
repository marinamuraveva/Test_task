from api_functions import User
import allure


user = User()

@allure.step("Создаем пользователя")
def test_create_user():
    assert user.create_user() == 200


@allure.step("Обновляем пользователя")
def test_update_user():
    assert user.updatе_user(upd={"email": "test@test.com"}) == 200


@allure.step("Находим пользователя по имени")
def test_get_user_by_user_name():
    assert user.get_user_by_user_name() == 200


@allure.step("Удаляем пользователя")
def test_delete_user():
    assert user.delete_user() == 200









