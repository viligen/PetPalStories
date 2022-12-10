from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

UserModel = get_user_model()


class SignUpViewTests(TestCase):
    VALID_DATA = {
        'username': 'testtest',
        'email': 'test33@test.bg',
        'password1': '123.my4567@Q',
        'password2': '123.my4567@Q',
    }

    def test_SignUpView__when_valid_data__assert_success__id_exists(self):
        self.client.post(reverse('register'), data=self.VALID_DATA, )

        self.assertEqual(int(self.client.session['_auth_user_id']), UserModel.objects
                         .filter(pk=self.client.session['_auth_user_id']).get().pk)

    def test_SignUpView__when_valid_data__assert_success__users_count__expect_1(self):
        self.client.post(reverse('register'), data=self.VALID_DATA, )
        self.assertEqual(1, UserModel.objects.count())

    def test_SignUpView__when_valid_data__assert_successful_redirect_302(self):
        response = self.client.post(reverse('register'), data=self.VALID_DATA, )

        self.assertEqual(302, response.status_code)