# Generated by Django 4.2.6 on 2023-10-16 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('director', models.CharField(max_length=100)),
                ('genre', models.CharField(choices=[('Select Genre', 'Select Genre'), ('Action', 'Action'), ('Comedy', 'Comedy'), ('Drama', 'Drama'), ('Romance', 'Romance'), ('Science Fiction', 'Science Fiction'), ('Horror', 'Horror')], default='Select Genre', max_length=100)),
            ],
        ),
    ]
