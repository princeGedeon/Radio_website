# Generated by Django 3.2.13 on 2022-05-14 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(default=0, upload_to='Student/profile'),
        ),
        migrations.AlterField(
            model_name='user',
            name='image_couverture',
            field=models.ImageField(default=0, upload_to='Student/couverture'),
        ),
    ]
