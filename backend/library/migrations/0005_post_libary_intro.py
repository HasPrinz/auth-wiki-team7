# Generated by Django 3.2.3 on 2022-07-25 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_rename_library_cotent_post_library_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='libary_intro',
            field=models.TextField(default='Library Introduction'),
        ),
    ]
