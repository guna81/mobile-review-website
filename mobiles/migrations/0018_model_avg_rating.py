# Generated by Django 3.0.7 on 2020-07-06 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobiles', '0017_remove_model_avg_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='model',
            name='avg_rating',
            field=models.IntegerField(blank=True, default=5, null=True),
        ),
    ]
