# Generated by Django 3.0.7 on 2020-07-26 21:16

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0012_auto_20200726_2108'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='country',
            field=django_countries.fields.CountryField(default='NZ', max_length=2),
            preserve_default=False,
        ),
    ]
