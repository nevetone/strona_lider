# Generated by Django 3.0.6 on 2020-05-22 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0024_auto_20200522_0250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='file',
            field=models.FileField(upload_to=''),
        ),
    ]
