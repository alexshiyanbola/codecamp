# Generated by Django 4.0.6 on 2022-08-10 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.CharField(default='a', max_length=50),
        ),
    ]
