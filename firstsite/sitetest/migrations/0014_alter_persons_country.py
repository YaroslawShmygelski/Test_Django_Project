# Generated by Django 4.2.7 on 2023-12-19 21:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sitetest', '0013_country_persons_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persons',
            name='country',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='countri', to='sitetest.country'),
        ),
    ]
