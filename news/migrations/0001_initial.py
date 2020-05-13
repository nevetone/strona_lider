# Generated by Django 3.0.6 on 2020-05-13 20:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=50, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallery_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pictures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture_title', models.CharField(max_length=50)),
                ('picture', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('overview', models.CharField(max_length=400)),
                ('content', tinymce.models.HTMLField(blank=True, null=True)),
                ('timestamp', models.TimeField(auto_now=True)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='')),
                ('has_own_web', models.BooleanField(default=False)),
                ('web_name', models.CharField(blank=True, max_length=50)),
                ('has_gallery', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.Author')),
                ('category', models.ManyToManyField(to='news.Category')),
                ('gallery', models.ManyToManyField(blank=True, to='news.Gallery')),
            ],
        ),
        migrations.CreateModel(
            name='MainNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('overview', models.CharField(max_length=1000)),
                ('content', tinymce.models.HTMLField(blank=True, null=True)),
                ('timestamp', models.DateField(auto_now=True)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='')),
                ('has_own_web', models.BooleanField(default=False)),
                ('web_name', models.CharField(blank=True, max_length=50)),
                ('featured', models.BooleanField(default=True)),
                ('has_gallery', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.Author')),
                ('category', models.ManyToManyField(to='news.Category')),
                ('gallery', models.ManyToManyField(blank=True, to='news.Gallery')),
            ],
        ),
        migrations.AddField(
            model_name='gallery',
            name='pictures',
            field=models.ManyToManyField(blank=True, to='news.Pictures'),
        ),
    ]
