# Generated by Django 2.2.5 on 2019-12-10 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locationfinder', '0006_auto_20191209_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='add',
            name='userid',
            field=models.CharField(default='nashi', max_length=100),
            preserve_default=False,
        ),
    ]