# Generated by Django 3.0.2 on 2022-07-16 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_productdetail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productdetail',
            name='decs',
        ),
    ]
