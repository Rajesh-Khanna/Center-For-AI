# Generated by Django 2.1.2 on 2018-10-18 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ai', '0005_auto_20181018_0501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='designation',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='position',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
