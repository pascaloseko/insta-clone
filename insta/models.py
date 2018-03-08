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
      user = models.ForeignKey(User,on_delete=models.CASCADE)
      profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
      likes = models.IntegerField(default=0)

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

class Comment(models.Model):
      comments = models.CharField(max_length=60,blank=True,null=True)
      comment_time = models.DateTimeField(auto_now_add=True)
      user = models.ForeignKey(User,on_delete=models.CASCADE, blank=True)
      pic = models.ForeignKey(Image,on_delete=models.CASCADE, related_name='comments',blank=True)

      def __str__(self):
            return self.comments

      class Meta:
            ordering = ['-comment_time']

      def save_comment(self):
            return self.save()

      def delete_comment(self):
            return self.delete()

      @classmethod
      def get_comments(cls):
            comment = Comment.objects.all()
            return comment