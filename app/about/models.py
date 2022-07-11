from django.db import models

class About(models.Model):
    team1 = models.TextField()
    team2 = models.TextField()

class Members(models.Model):
    name = models.CharField(max_length=50, default='/')
    github = models.CharField(max_length=250, default='www.github.com')
    profession = models.CharField(max_length=250, default='/')
    img = models.ImageField(upload_to='teams')
    