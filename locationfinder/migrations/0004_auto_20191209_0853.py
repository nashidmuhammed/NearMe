# Generated by Django 2.2.5 on 2019-12-09 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locationfinder', '0003_add'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add',
            name='img',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
