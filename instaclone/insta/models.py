from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
      profile_photo = models.ImageField(upload_to='profile/',null=True,blank=True)
      bio = models.TextField(max_length=140)
      user = models.ForeignKey(User)

      def __str__(self):
            return self.bio

      def save_profile(self):
            self.save()

      def delete_profile(self):
            self.delete()

      @classmethod
      def search_profile(cls, search_term):
            profile = cls.objects.filter(user__username__icontains=search_term)
            return profile

      @classmethod
      def get_profile(cls):
            profile = Profile.objects.all()
            return profile

      @classmethod
      def find_profile(cls,search_term):
            prof = cls.objects.filter(user__username__icontains=search_term)
            return prof

class Image(models.Model):
      image = models.ImageField(upload_to='image/',null=True,blank=True)
      image_name = models.CharField(max_length=60)
      image_caption = models.CharField(max_length=70)
      profile = models.ForeignKey(Profile)
      likes = models.IntegerField(default=0)
      comments = models.CharField(max_length=120) 

      def __str__(self):
            return self.image_name

      def save_image(self):
            self.save()

      def delete_image(self):
            self.delete()

      @classmethod
      def update_caption(cls,id,caption):
        captions = Image.objects.filter(id=id).update(caption = caption)
        return captions

      @classmethod
      def get_image_by_id(cls,id): 
            image = Image.objects.filter(id = Image.id)
            return image

      @classmethod
      def get_images(cls):
            image = Image.objects.all()
            return image