# Generated by Django 4.0.5 on 2022-06-29 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='default_m06lmc.jpg', upload_to='profile_images'),
        ),
    ]
