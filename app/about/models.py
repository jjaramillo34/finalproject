from django.db import models
from parler.models import TranslatableModel, TranslatedFields

class About(TranslatableModel):
    translations = TranslatedFields(
        team1 = models.TextField(),
        team2 = models.TextField(),
    )
    
    def __str__(self) -> str:
        return self.team1

class Members(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=50, default='/'),
        github = models.CharField(max_length=250, default='www.github.com'),
        profession = models.CharField(max_length=250, default='/'),
        img = models.ImageField(upload_to='teams'),
    )
    
    def __str__(self):
        return self.name