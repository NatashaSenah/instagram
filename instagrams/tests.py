from django.test import TestCase
from .models import Image

# Create your tests here.
def test_save_method(self):
        self.image.save_image()
        image = Image.objects.all()
        self.assertTrue()