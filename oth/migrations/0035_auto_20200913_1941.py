# Generated by Django 2.2.16 on 2020-09-13 14:11

from django.db import migrations, models
import oth.models


class Migration(migrations.Migration):

    dependencies = [
        ('oth', '0034_auto_20200913_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='videofile',
            field=models.FileField(blank=True, null=True, upload_to=oth.models.get_upload_path),
        ),
    ]
