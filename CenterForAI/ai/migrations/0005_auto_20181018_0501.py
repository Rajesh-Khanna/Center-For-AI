# Generated by Django 2.1.2 on 2018-10-18 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ai', '0004_auto_20181018_0334'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='profil_images'),
        ),
        migrations.AddField(
            model_name='student',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='profil_images'),
        ),
    ]
