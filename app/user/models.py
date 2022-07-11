from ast import arg
from email.mime import image
from django.contrib.auth.models import User
from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage as storage    


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #https://res.cloudinary.com/javier-jaramillo/image/upload/v1656468320/media/default_m06lmc.jpg
    avatar = models.ImageField(default= 'default_m06lmc.jpg', upload_to='profile_images')
    bio = models.TextField()
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username

    # resizing images
    def save(self, *args, **kwargs):
        super().save()
        #super(User, self).save(*args, **kwargs)
        image_read = storage.open(self.avatar.name, "r")
        image = Image.open(image_read)
        if image.height > 100 or image.width > 100:
            size = (100, 100)
            
            imageBuffer = BytesIO()
            
            image.thumbnail(size, Image.ANTIALIAS)
            
            # Check whether it is resized
            image.show()
            # Save the modified image
            user = User.objects.get(pk=self.pk)
            user.profile_image.save(self.avatar.name, ContentFile(imageBuffer.getvalue()))
            image_read = storage.open(user.avatar.name, "r")
            image = Image.open(image_read)
            image.show()
        image_read.close()
                
        #super().save()
        #
        #img = Image.open(self.avatar.name)
        ##img = Image.open(self.avatar.path)
        #
        #if img.height > 100 or img.width > 100:
            #new_img = (100, 100)
            #img.thumbnail(new_img)
            #img.save(self.avatar.name)
            ##img.save(self.avatar.path)