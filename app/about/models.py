from django.db import models
from parler.models import TranslatableModel, TranslatedFields

class About(TranslatableModel):
    translations = TranslatedFields(
        page_header = models.CharField(max_length=200),
        page_subheader = models.CharField(max_length=200),
        team1 = models.TextField(),
        team2 = models.TextField(),
    )
    
    def __str__(self) -> str:
        return self.team1

class Members(TranslatableModel):
    name = models.CharField(max_length=50, default='/'),
    github = models.CharField(max_length=250, default='www.github.com')
    img = models.ImageField(upload_to='teams')
    translations = TranslatedFields(
        profession = models.CharField(max_length=250, default='/'),
        
    )
    
    def __str__(self):
        return self.name