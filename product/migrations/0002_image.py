# Generated by Django 3.0.2 on 2022-07-11 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=50)),
                ('image', models.FileField(default='defult.jpg', upload_to='static/image/background')),
            ],
        ),
    ]
