# Generated by Django 3.1 on 2020-08-23 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0004_auto_20200823_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='phone_number',
            field=models.IntegerField(default=0),
        ),
    ]
