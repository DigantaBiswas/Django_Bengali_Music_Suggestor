# Generated by Django 2.0.6 on 2018-07-06 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0003_auto_20180706_0600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music_data',
            name='release_date',
            field=models.IntegerField(),
        ),
    ]
