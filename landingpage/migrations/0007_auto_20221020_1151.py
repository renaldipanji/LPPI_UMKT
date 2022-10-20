# Generated by Django 3.2.5 on 2022-10-20 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0006_journalresearch'),
    ]

    operations = [
        migrations.RenameField(
            model_name='journalresearch',
            old_name='member_image',
            new_name='cover_jurnal',
        ),
        migrations.RenameField(
            model_name='journalresearch',
            old_name='overview',
            new_name='deskripsi',
        ),
        migrations.AddField(
            model_name='journalresearch',
            name='index',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='journalresearch',
            name='issn',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='journalresearch',
            name='judul_jurnal',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='journalresearch',
            name='link_current_issue',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='journalresearch',
            name='link_download_template',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='journalresearch',
            name='link_online_submission',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='journalresearch',
            name='link_view_jurnal',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='journalresearch',
            name='publication',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
