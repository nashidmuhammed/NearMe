# Generated by Django 2.2.5 on 2019-12-31 03:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('locationfinder', '0008_fed'),
    ]

    operations = [
        migrations.AddField(
            model_name='add',
            name='img_1',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='add',
            name='img_2',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='add',
            name='img_3',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='add',
            name='indro',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
