# Generated by Django 3.2.8 on 2021-11-17 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudmovies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='duration',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(),
        ),
    ]
