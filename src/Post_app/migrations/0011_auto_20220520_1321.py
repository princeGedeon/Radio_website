# Generated by Django 3.2.13 on 2022-05-20 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post_app', '0010_auto_20220520_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='audio',
            name='type',
            field=models.CharField(choices=[('Reportage', 'Reportage'), ('Divertissement', 'Divertissement'), ('Science', 'Science')], default=('Science', 'Science'), max_length=20),
        ),
        migrations.AddField(
            model_name='document',
            name='type',
            field=models.CharField(choices=[('Reportage', 'Reportage'), ('Divertissement', 'Divertissement'), ('Science', 'Science')], default=('Science', 'Science'), max_length=20),
        ),
        migrations.AddField(
            model_name='video',
            name='type',
            field=models.CharField(choices=[('Reportage', 'Reportage'), ('Divertissement', 'Divertissement'), ('Science', 'Science')], default=('Science', 'Science'), max_length=20),
        ),
        migrations.AddField(
            model_name='visuel',
            name='type',
            field=models.CharField(choices=[('Reportage', 'Reportage'), ('Divertissement', 'Divertissement'), ('Science', 'Science')], default=('Science', 'Science'), max_length=20),
        ),
    ]
