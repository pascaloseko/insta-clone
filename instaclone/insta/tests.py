from django.test import TestCase
from .models import Image,Profile
from django.contrib.auth.models import User

# Create your tests here.

class ImageTestClass(TestCase):
      # set up the user class
      def setUp(self):
            self.new_user = User(username='pascal',email='pasco@gmail.com')
            self.new_user.save()

            # set up for the profile class
            self.new_profile = Profile(bio="living my life",user=self.new_user)
            self.new_profile.save()

            # set up for the image class
            self.lion = Image(image_caption='King Of The Jungle',likes=1000,profile=self.new_profile)
            self.lion.save()

      def tearDown(self):
            Profile.objects.all().delete()
            Image.objects.all().delete()

      def test_instance(self):
            self.assertTrue(isinstance(self.lion,Image))

      def test_save_image(self):
            images = Image.objects.all()
            self.assertTrue(len(images)>0)

      def test_get_images(self):
            self.lion.save_image()
            images = Image.get_images()
            self.assertEqual(len(images), 1)

      def test_delete_image(self):
        self.lion.save_image()
        self.lion.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images)<1)

class ProfileTestClass(TestCase):
      # set up the user class
      def setUp(self):
            self.new_user = User(username='pascal',email='pasco@gmail.com')
            self.new_user.save()

            # set up for the profile class
            self.my_profile = Profile(bio="living my life",user=self.new_user)
            self.my_profile.save()

      def tearDown(self):
            User.objects.all().delete()
            Profile.objects.all().delete()

      # test instance
      def test_instance(self):
            self.assertTrue(isinstance(self.my_profile, Profile))

      def test_save_profile(self):
            profiles = Profile.objects.all()
            self.assertTrue(len(profiles)>0)

      def test_delete_profile(self):
            self.my_profile.save_profile()
            self.my_profile.delete_profile()
            profiles = Profile.objects.all()
            self.assertTrue(len(profiles)<1)

      def test_get_profile(self):
            self.my_profile.save_profile()
            profile = Profile.get_profile()
            self.assertEqual(len(profile),1)

      def test_find_profile(self):
            self.my_profile.save_profile()
            pasco = Profile.objects.all()
            profiles = Profile.find_profile('pascal')
            self.assertEqual(profiles,profiles)

