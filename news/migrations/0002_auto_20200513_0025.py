# Generated by Django 3.0.6 on 2020-05-12 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='overview',
            field=models.CharField(max_length=400),
        ),
    ]
