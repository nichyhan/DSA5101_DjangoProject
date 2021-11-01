# Generated by Django 3.2.8 on 2021-11-01 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutus', '0002_movie_poster'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='movie',
            name='grade',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='movie',
            name='name',
            field=models.CharField(default='', max_length=256),
        ),
    ]