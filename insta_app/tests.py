from django.test import TestCase, Client
from django.urls import reverse
import random
from django.contrib.auth.models import User
from .models import Image, Profile, Comment
from .forms import UploadForm, EditProfile, CommentForm, SignUpForm

# Create your tests here.

class TestViews(TestCase):
    def create_user_with_id(self, username, password, user_id):
        # Check if a user with the provided ID exists
        user_exists = User.objects.filter(id=user_id).exists()

        # If the user exists, generate a random ID until we find one that's not in use
        while user_exists:
            user_id = random.randint(1, 10000)
            user_exists = User.objects.filter(id=user_id).exists()

        # Create the user with the generated or provided ID
        user = User.objects.create_user(id=user_id, username=username, password=password)
        return user
    
    def setUp(self):
        self.client = Client()
        self.test_user = self.create_user_with_id('testuser', '12345', 1)
        self.profile = Profile.objects.get(user=self.test_user)
        self.image = Image.objects.create(
            image_name='Test Image',
            image_caption='This is a test caption',
            user=self.test_user,
            profile=self.profile,
        )

    def test_register_GET(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/registration_form.html')

    def test_index_authenticated(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_profile_authenticated(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('profile', args=[self.test_user.id]))
        self.assertEqual(response.status_code, 302)

    def test_like_image_authenticated(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('like_image', args=[self.image.id]))
        self.assertEqual(response.status_code, 302)  # Expecting a redirect status code
