# Generated by Django 3.1.2 on 2020-10-21 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0002_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='posts/'),
        ),
    ]
