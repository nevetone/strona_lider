# Generated by Django 3.0.6 on 2020-05-25 22:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0034_remove_category_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 25, 22, 5, 31, 492373, tzinfo=utc)),
        ),
    ]
