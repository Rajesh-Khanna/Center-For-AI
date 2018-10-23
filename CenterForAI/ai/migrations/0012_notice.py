# Generated by Django 2.1.2 on 2018-10-21 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ai', '0011_auto_20181019_1131'),
    ]

    operations = [
        migrations.CreateModel(
            name='notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(blank=True, max_length=20, null=True)),
                ('message', models.TextField()),
                ('link', models.URLField(blank=True, null=True)),
                ('notice_end_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
