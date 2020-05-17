# Generated by Django 3.0.5 on 2020-05-10 18:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oth', '0008_auto_20200510_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='image',
            field=models.ImageField(blank=True, default='images/level1.jpg', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='level',
            name='image',
            field=models.ImageField(default='images/level1.jpg', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='notif',
            name='date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2020, 5, 10, 18, 57, 5, 177686)),
        ),
    ]