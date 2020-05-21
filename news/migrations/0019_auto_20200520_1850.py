# Generated by Django 3.0.6 on 2020-05-20 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0018_auto_20200520_1741'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mainnews',
            name='gallery',
        ),
        migrations.AddField(
            model_name='mainnews',
            name='gallery',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='news.Gallery'),
        ),
        migrations.RemoveField(
            model_name='news',
            name='gallery',
        ),
        migrations.AddField(
            model_name='news',
            name='gallery',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='news.Gallery'),
        ),
    ]
