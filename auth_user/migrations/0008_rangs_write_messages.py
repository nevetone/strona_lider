# Generated by Django 3.0.6 on 2020-06-04 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_user', '0007_messages'),
    ]

    operations = [
        migrations.AddField(
            model_name='rangs',
            name='write_messages',
            field=models.BooleanField(default=False),
        ),
    ]
