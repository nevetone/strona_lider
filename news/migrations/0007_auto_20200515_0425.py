# Generated by Django 3.0.6 on 2020-05-15 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20200515_0424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='web_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
