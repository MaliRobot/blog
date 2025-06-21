# story/tests/test_forms.py
from django.test import TestCase
from story.forms import ReaderLoginForm, ReaderUserCreationForm
from story.models import ReaderUser


class ReaderLoginFormTest(TestCase):
    def test_valid_form(self):
        form = ReaderLoginForm(data={
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertTrue(form.is_valid())

    def test_empty_form(self):
        form = ReaderLoginForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)
        self.assertIn('password', form.errors)


class ReaderUserCreationFormTest(TestCase):
    def test_valid_form(self):
        form = ReaderUserCreationForm(data={
            'username': 'newuser',
            'email': 'new@example.com',
            'first_name': 'New',
            'last_name': 'User',
            'password1': 'testpassword123',
            'password2': 'testpassword123'
        })
        self.assertTrue(form.is_valid())

    def test_password_mismatch(self):
        form = ReaderUserCreationForm(data={
            'username': 'newuser',
            'email': 'new@example.com',
            'password1': 'testpassword123',
            'password2': 'differentpassword'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors)

    def test_duplicate_username(self):
        # Create existing user
        ReaderUser.objects.create(
            username='existinguser',
            email='existing@example.com'
        )

        form = ReaderUserCreationForm(data={
            'username': 'existinguser',
            'email': 'new@example.com',
            'password1': 'testpassword123',
            'password2': 'testpassword123'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)

    def test_duplicate_email(self):
        # Create existing user
        ReaderUser.objects.create(
            username='existinguser',
            email='existing@example.com'
        )

        form = ReaderUserCreationForm(data={
            'username': 'newuser',
            'email': 'existing@example.com',
            'password1': 'testpassword123',
            'password2': 'testpassword123'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_form_save(self):
        form = ReaderUserCreationForm(data={
            'username': 'newuser',
            'email': 'new@example.com',
            'first_name': 'New',
            'last_name': 'User',
            'password1': 'testpassword123',
            'password2': 'testpassword123'
        })

        self.assertTrue(form.is_valid())
        reader = form.save()

        self.assertEqual(reader.username, 'newuser')
        self.assertEqual(reader.email, 'new@example.com')
        self.assertTrue(reader.check_password('testpassword123'))
