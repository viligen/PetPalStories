from django.test import TestCase
from django.urls import reverse


class SignUpViewTests(TestCase):
    VALID_DATA = {
        'username': 'testtest',
        'email': 'test33@test.bg',
        'password1': '123.my4567@Q',
        'password2': '123.my4567@Q',
    }

    def test_SignUpView__when_valid_data__assert_success_login_id_1(self):
        response = self.client.post(reverse('register'), data=self.VALID_DATA, )

        self.assertEqual('1', self.client.session['_auth_user_id'])

    def test_SignUpView__when_valid_data__assert_successful_redirect_302(self):
        response = self.client.post(reverse('register'), data=self.VALID_DATA, )

        self.assertEqual(302, response.status_code)