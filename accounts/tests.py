from django.test import TestCase
from django.shortcuts import reverse
from .forms import UserLoginForm, UserRegistrationForm


# Create your tests here.
class Test_Pages(TestCase):
    def test_login_page(self):
        '''
        Checks if the login page loads the login template
        correctly
        '''
        page = self.client.get("/accounts/login/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")

    def test_logout_page(self):
        '''
        Checks if the logout page loads and then redirects
        to the index page correctly
        '''
        page = self.client.get("/accounts/logout/")
        self.assertEqual(page.status_code, 302)
        self.client.post(reverse('index'))

    def test_registration_page(self):
        '''
        Checks if the register page loads the register template
        correctly
        '''
        page = self.client.get("/accounts/register/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "registration.html")

    def test_profile_page(self):
        '''
        Checks if the profile page loads the login profile page
        correctly
        '''
        page = self.client.get("/accounts/profile/")
        self.assertEqual(page.status_code, 302)
        self.client.post(reverse('profile'))


class Test_Forms(TestCase):
    def test_valid_login_form(self):
        '''
        Makes sure the login form works if its valid
        '''
        form = UserLoginForm({"username": "User", "password": "Password"})
        self.assertTrue(form.is_valid())

    def test_invalid_login_form(self):
        '''
        Makes sure the login form shows error messages if its invalid
        '''
        form = UserLoginForm({"username": ""})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["username"],
                         [u"This field is required."])

    def test_valid_egister_form(self):
        '''
        Makes sure the register form works when valid
        '''
        form = UserRegistrationForm({
            "username": "User",
            "email": "user@testing.com",
            "password1": "Password123",
            "password2": "Password123"
        })
        self.assertTrue(form.is_valid())

    def test_invalid_register_form(self):
        '''
        Makes sure the register form shows error messages if its invalid
        '''
        form = UserRegistrationForm({"username": ""})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["username"],
                         [u"This field is required."])

    def test_valid_register_form_passwords(self):
        '''
        Makes sure the register form shows error messages
        if its invalid for the passwords
        '''
        form = UserRegistrationForm({
            "password1": "Password1",
            "password2": "Password2"
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["password2"],
                         [u"Passwords must match"])
