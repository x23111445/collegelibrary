# Generated by Django 2.1.15 on 2023-12-07 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=30)),
                ('publication_date', models.DateTimeField(verbose_name='publication date')),
                ('genre', models.CharField(max_length=200)),
                ('pages', models.IntegerField()),
            ],
        ),
    ]
