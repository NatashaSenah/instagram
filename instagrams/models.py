from django.db import models

# Create your models here.
class Image(models.Model):
    image_image = models.ImageField(upload_to = 'image/')
    image_name = models.CharField(max_length =30)
    image_name = models.CharField(max_length =30)
    profile = models.ForeignKey(Profile)
    