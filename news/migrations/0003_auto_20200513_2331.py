# Generated by Django 3.0.6 on 2020-05-13 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20200513_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainnews',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
