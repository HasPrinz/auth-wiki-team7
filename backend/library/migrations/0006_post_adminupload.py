# Generated by Django 4.0.6 on 2022-07-27 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_post_libary_intro'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='adminupload',
            field=models.FileField(default='DEFAULT VALUE', upload_to='media'),
        ),
    ]
