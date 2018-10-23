# Generated by Django 2.1.2 on 2018-10-19 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ai', '0009_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='applicant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=12)),
                ('experience', models.IntegerField()),
                ('company', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=200)),
                ('city', models.CharField(choices=[('Bgl', 'Bengaluru'), ('kgp', 'Kharagpur')], default='Kharagpur', max_length=3)),
                ('fee_status', models.CharField(choices=[('NP', 'Not paid'), ('PP', 'Partially Paid'), ('FP', 'Fully Paid')], default='NP', max_length=2)),
                ('amount_paid', models.IntegerField()),
                ('applicant_status', models.CharField(choices=[('NV', 'Not yet verified'), ('AV', 'Application verified'), ('CC', 'Course completed')], default='NV', max_length=2)),
            ],
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
