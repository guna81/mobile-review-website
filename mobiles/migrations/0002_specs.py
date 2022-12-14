# Generated by Django 3.0.7 on 2020-07-02 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Specs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_size', models.DecimalField(decimal_places=2, max_digits=2)),
                ('front_camera', models.CharField(max_length=60)),
                ('rear_camera', models.CharField(max_length=60)),
                ('processor', models.CharField(max_length=60)),
                ('ram', models.IntegerField()),
                ('storage', models.IntegerField()),
                ('battery', models.IntegerField()),
            ],
        ),
    ]
