# Generated by Django 3.0.6 on 2020-05-15 02:21

import builtins
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20200514_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='web_name',
            field=models.CharField(blank=True, default=builtins.id, max_length=50),
        ),
    ]
