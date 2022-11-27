from django.test import TestCase
from django.urls import reverse


class SignUpViewTests(TestCase):
    VALID_DATA = {
        'username': 'testtest',
        'email': 'test33@test.bg',
        'password1': '123.my4567@Q',
        'password2': '123.my4567@Q',
    }

    def test_SignUpView__when_valid_data__assert_login_and_redirect(self):
        response = self.client.post(reverse('register'), data=self.VALID_DATA, )

        self.assertEqual(response.status_code, 302)