# Generated by Django 2.2.12 on 2020-05-17 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oth', '0030_auto_20200517_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='player_emotion',
            field=models.CharField(blank=True, default='neutral', max_length=50, null=True),
        ),
    ]
