# Generated by Django 4.2.5 on 2023-10-06 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='rating',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='post',
            name='rating',
            field=models.FloatField(),
        ),
    ]
