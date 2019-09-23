# Generated by Django 2.2.5 on 2019-09-23 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('title_en', models.CharField(max_length=20)),
                ('audience', models.IntegerField()),
                ('open_data', models.DateTimeField()),
                ('genre', models.CharField(max_length=20)),
                ('watch_grade', models.CharField(max_length=20)),
                ('score', models.FloatField()),
                ('poster_url', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
    ]
