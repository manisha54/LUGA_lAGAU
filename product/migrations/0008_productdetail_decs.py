# Generated by Django 3.0.2 on 2022-07-16 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_productdetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdetail',
            name='decs',
            field=models.TextField(default='', max_length=200),
        ),
    ]
