# Generated by Django 3.0.7 on 2020-07-24 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_remove_album_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='description',
            field=models.TextField(default='No Description', max_length=300),
            preserve_default=False,
        ),
    ]
