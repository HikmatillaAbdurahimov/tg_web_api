# Generated by Django 5.1 on 2024-08-10 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='albom',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='artist',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='songs',
            options={'ordering': ['id']},
        ),
        migrations.RenameField(
            model_name='songsalbom',
            old_name='albom',
            new_name='artist',
        ),
        migrations.AlterField(
            model_name='albom',
            name='image',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='artist',
            name='image',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='songs',
            name='image',
            field=models.URLField(),
        ),
    ]
