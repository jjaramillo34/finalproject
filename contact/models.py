from django.db import models

# Create your models here.
class Contact(models.Model):
    title_header = models.CharField(max_length=50, default='Contact Us')
    title_subheader = models.CharField(max_length=50, default='Send us an email')
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=200)