# Generated by Django 4.2.7 on 2023-12-14 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitetest', '0005_persons_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persons',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]
