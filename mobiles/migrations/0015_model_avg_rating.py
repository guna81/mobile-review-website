# Generated by Django 3.0.7 on 2020-07-06 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobiles', '0014_delete_recentsearch'),
    ]

    operations = [
        migrations.AddField(
            model_name='model',
            name='avg_rating',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
