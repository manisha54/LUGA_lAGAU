# Generated by Django 3.0.2 on 2022-07-11 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='caption2',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='image',
            name='decs',
            field=models.TextField(default='', max_length=200),
        ),
    ]
