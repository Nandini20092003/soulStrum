# Generated by Django 5.0.3 on 2024-03-22 07:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('bio', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='artist_images')),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('release_date', models.DateField()),
                ('cover_image', models.ImageField(blank=True, upload_to='album_covers')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music_catalog.artist')),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('duration', models.DurationField()),
                ('audio_file', models.FileField(upload_to='audio_files')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music_catalog.album')),
            ],
        ),
    ]
