# Generated by Django 3.0.6 on 2020-05-20 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth_user', '0001_initial'),
        ('news', '0017_auto_20200519_0348'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='rank',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth_user.Rangs'),
        ),
        migrations.AddField(
            model_name='category',
            name='color',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='allfiles',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='news.Author'),
        ),
        migrations.AlterField(
            model_name='allwebs',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='news.Author'),
        ),
        migrations.AlterField(
            model_name='files',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='news.Author'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='news.Author'),
        ),
        migrations.AlterField(
            model_name='mainnews',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='news.Author'),
        ),
        migrations.AlterField(
            model_name='news',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='news.Author'),
        ),
        migrations.AlterField(
            model_name='pictures',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='news.Author'),
        ),
        migrations.AlterField(
            model_name='webs',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='news.Author'),
        ),
    ]