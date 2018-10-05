from django.db import models
class Profile(models.Model):
    bio = models.TextField(max_length=500, blank=True)
    profile_photo = models.ProfileField(upload_to = 'image/')
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
# Create your models here.
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments')
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



class Image(models.Model):
    image_image = models.ImageField(upload_to = 'image/')
    image_name = models.CharField(max_length =30)
    image_name = models.CharField(max_length =30)
    pub_date = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(Profile)
    comment = models.ForeignKey(Comment)
