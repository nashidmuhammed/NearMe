# Generated by Django 2.2.5 on 2019-12-09 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locationfinder', '0005_auto_20191209_0903'),
    ]

    operations = [
        migrations.RenameField(
            model_name='add',
            old_name='name',
            new_name='locname',
        ),
    ]
