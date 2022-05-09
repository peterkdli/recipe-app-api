from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating new user with successful email"""
        email = 'test.test@email.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalised(self):
        """test email is normalised"""
        email = "test@aSDADSSD.COM"
        user = get_user_model().objects.create_user(email, 'testpassword')

        self.assertEqual(user.email, email.lower())