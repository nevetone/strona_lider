# Generated by Django 3.0.6 on 2020-05-25 22:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0035_auto_20200526_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 25, 22, 7, 36, 563567, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 25, 22, 7, 36, 559569, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='mainnews',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 25, 22, 7, 36, 557569, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='news',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 25, 22, 7, 36, 556570, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='pictures',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 25, 22, 7, 36, 560568, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='webcategory',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 25, 22, 7, 36, 562568, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='webs',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 25, 22, 7, 36, 561568, tzinfo=utc)),
        ),
    ]
