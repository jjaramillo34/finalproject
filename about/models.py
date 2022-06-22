from django.db import models

# Create your models here.
class About(models.Model):
    title_header = models.CharField(max_length=50, default='About Our Team')
    title_subheader = models.CharField(max_length=50, default='This is what we do')
    team1 = models.TextField()
    team2 = models.TextField()
