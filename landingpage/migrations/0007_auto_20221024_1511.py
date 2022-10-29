# Generated by Django 3.2.5 on 2022-10-24 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0006_auto_20221020_1533'),
    ]

    operations = [
        migrations.RenameField(
            model_name='journalsmodel',
            old_name='nama',
            new_name='fakultas',
        ),
        migrations.RenameField(
            model_name='textbooksmodel',
            old_name='nama',
            new_name='fakultas',
        ),
        migrations.AddField(
            model_name='journalsmodel',
            name='nama_dosen',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='journalsmodel',
            name='nidn',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='journalsmodel',
            name='program_studi',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='textbooksmodel',
            name='nama_dosen',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='textbooksmodel',
            name='nidn',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
