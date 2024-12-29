# Generated by Django 5.1.3 on 2024-11-26 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_img',
            field=models.ImageField(default='/Users/dhruvbharara/djangoproject/socialmedia_app/media/blank_default_pp.webp', upload_to='profile_images'),
        ),
    ]
