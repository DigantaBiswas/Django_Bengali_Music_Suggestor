# Generated by Django 2.0.6 on 2018-07-06 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music_data',
            name='release_date',
            field=models.DecimalField(decimal_places=0, max_digits=5),
        ),
    ]
