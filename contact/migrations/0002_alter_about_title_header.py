# Generated by Django 4.0.5 on 2022-06-09 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='title_header',
            field=models.CharField(default='About Our Team', max_length=50),
        ),
    ]