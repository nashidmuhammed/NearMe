# Generated by Django 2.2.5 on 2019-12-09 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locationfinder', '0004_auto_20191209_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add',
            name='img',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
