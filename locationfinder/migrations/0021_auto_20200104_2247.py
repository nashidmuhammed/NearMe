# Generated by Django 2.2.5 on 2020-01-04 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locationfinder', '0020_auto_20200104_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fed',
            name='date',
            field=models.DateField(),
        ),
    ]
