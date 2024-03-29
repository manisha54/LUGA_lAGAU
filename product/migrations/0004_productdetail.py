# Generated by Django 3.0.2 on 2022-07-16 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20220711_1100'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=50)),
                ('caption2', models.CharField(default='', max_length=50)),
                ('decs', models.TextField(default='', max_length=200)),
                ('image', models.FileField(default='defult.jpg', upload_to='static/image/background')),
            ],
            options={
                'db_table': 'ProductDetail',
            },
        ),
    ]
