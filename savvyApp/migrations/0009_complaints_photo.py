# Generated by Django 5.0.2 on 2024-04-03 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('savvyApp', '0008_remove_complaints_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaints',
            name='photo',
            field=models.ImageField(default='', upload_to='complaint_photos/images'),
        ),
    ]
