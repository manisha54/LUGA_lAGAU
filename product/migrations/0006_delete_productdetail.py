# Generated by Django 3.0.2 on 2022-07-16 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_remove_productdetail_decs'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProductDetail',
        ),
    ]