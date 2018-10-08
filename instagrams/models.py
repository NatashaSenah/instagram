from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField






class Profile(models.Model):
    bio = models.TextField(max_length=500, blank=True)
    profile_photo= models.ImageField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, default=1)

    def __str__(self):
    
        return self.bio

    def save_profile(self):
        self.save()

    class Meta:
        ordering = ['bio']

    @classmethod
    def search_profile(cls, name):
        profile = cls.objects.filter(user__username__icontains=name)
        return profile

    @classmethod
    def get_by_id(cls, id):
        profile = cls.objects.get(user=id)
        return profile

    @classmethod
    def filter_by_id(cls, id):
        profile = cls.objects.filter(user=id).first()
        return profile

class Image(models.Model):
    image_image = models.ImageField(upload_to = 'image/')
    image_name = models.CharField(max_length =30)
    image_caption = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(Profile)
  
    # comment = models.TextField()
    @classmethod
    def home(cls,date):
        instagrams = cls.objects.all()
        return instagrams

    @classmethod
    def get_profile_images(cls, profile):
        images = Image.objects.filter(profile=profile)
        return images

    @classmethod
    def search_by_image_name(cls,search_term):
        album = cls.objects.filter(image_name__icontains=search_term)
        return album
    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()

# Create your models here.
class Comment(models.Model):
    post = models.ForeignKey(Image, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)
class InstagramsLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()
