# Generated by Django 3.0.7 on 2020-07-03 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mobiles', '0008_spec_model'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spec',
            name='varient',
        ),
    ]
