# Generated by Django 4.0.5 on 2022-06-26 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cover',
            field=models.ImageField(upload_to='featured_images/%Y/%m/%d/'),
        ),
    ]
