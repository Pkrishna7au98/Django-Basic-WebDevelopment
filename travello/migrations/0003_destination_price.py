# Generated by Django 4.0.1 on 2022-02-03 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0002_remove_destination_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
