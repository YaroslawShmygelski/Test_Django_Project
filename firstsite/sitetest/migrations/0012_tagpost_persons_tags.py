# Generated by Django 4.2.7 on 2023-12-17 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitetest', '0011_alter_persons_cat'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='persons',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tags', to='sitetest.tagpost'),
        ),
    ]
