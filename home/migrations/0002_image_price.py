# Generated by Django 3.0.2 on 2022-07-11 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='price',
            field=models.CharField(default='', max_length=50),
        ),
    ]
