# Generated by Django 4.0.6 on 2022-08-02 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profileimg',
            field=models.ImageField(default='blankpicture.jpg', upload_to='profile-images'),
        ),
    ]
