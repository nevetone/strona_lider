# Generated by Django 3.0.6 on 2020-05-22 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0030_auto_20200522_2209'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('web_cat_name', models.CharField(max_length=25, unique=True)),
                ('webs', models.ManyToManyField(to='news.Webs')),
            ],
        ),
    ]
