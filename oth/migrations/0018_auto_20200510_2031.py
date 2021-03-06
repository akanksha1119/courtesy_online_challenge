# Generated by Django 3.0.5 on 2020-05-10 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oth', '0017_auto_20200510_2004'),
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module', models.ImageField(upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='answer',
            name='l_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='oth.Level'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='oth.Player'),
        ),
        migrations.AddField(
            model_name='level',
            name='module',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='oth.Module'),
            preserve_default=False,
        ),
    ]
