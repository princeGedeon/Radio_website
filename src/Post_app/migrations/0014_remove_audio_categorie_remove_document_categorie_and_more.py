# Generated by Django 4.0.3 on 2022-07-06 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Post_app', '0013_audio_visible_document_visible_video_visible_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='audio',
            name='categorie',
        ),
        migrations.RemoveField(
            model_name='document',
            name='categorie',
        ),
        migrations.RemoveField(
            model_name='video',
            name='categorie',
        ),
        migrations.RemoveField(
            model_name='visuel',
            name='categorie',
        ),
    ]
