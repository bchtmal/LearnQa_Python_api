import allure
import pytest
from lib.assertions import Assertions
from lib.base_case import BaseCase
from lib.my_requests import MyRequests

@allure.epic("Register cases")
class TestUserRegister(BaseCase):
    exclude_params = [
        'password',
        'username',
        'firstName',
        'lastName',
        'email'
    ]

    @allure.description("This test created user successfully")
    def test_user_create_successfully(self):
        data = self.prepare_registration_data()

        response = MyRequests.post("/user", data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, 'id')

    @allure.description("This test try to create user with existing email")
    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registration_data(email)

        response = MyRequests.post("/user", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            'utf-8') == f"Users with email '{email}' already exists", f"Unexpected response content :{response.content}"

    @allure.description("This test try to create user with existing email")
    def test_create_user_with_incorrect_email(self):
        email = 'emailexample.com'
        data = self.prepare_registration_data(email)

        response = MyRequests.post("/user", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            'utf-8') == "Invalid email format"

    @allure.description("This test try to create user without one of required values")
    @pytest.mark.parametrize('condition', exclude_params)
    def test_create_user_without_one_of_required_values(self, condition):
        data = self.prepare_registration_data()
        del data[condition]
        response = MyRequests.post("/user", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            'utf-8') == f"The following required params are missed: {condition}"

    @allure.description("This test try to create user with too short username")
    def test_create_user_with_too_short_username(self):
        data = self.prepare_registration_data()
        data['username'] = 'a'

        response = MyRequests.post("/user", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            'utf-8') == "The value of 'username' field is too short"

    @allure.description("This test try to create user with too long username")
    def test_create_user_with_too_long_username(self):
        data = self.prepare_registration_data()
        data['username'] = 'a' * 250

        response = MyRequests.post("/user", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            'utf-8') == "The value of 'username' field is too long"
