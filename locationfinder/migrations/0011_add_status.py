# Generated by Django 2.2.5 on 2020-01-02 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locationfinder', '0010_auto_20191231_0905'),
    ]

    operations = [
        migrations.AddField(
            model_name='add',
            name='status',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
