# Generated by Django 3.2.5 on 2022-10-20 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0005_textbooks'),
    ]

    operations = [
        migrations.CreateModel(
            name='JournalsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50, null=True)),
                ('judul_artikel', models.CharField(max_length=100, null=True)),
                ('tahun', models.CharField(max_length=4, null=True)),
                ('link', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TextBooksModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program_studi', models.CharField(max_length=50, null=True)),
                ('nama', models.CharField(max_length=50, null=True)),
                ('judul_buku', models.CharField(max_length=100, null=True)),
                ('tahap_luaran_10', models.BooleanField(default=False)),
                ('tahap_luaran_40', models.BooleanField(default=False)),
                ('tahap_luaran_80', models.BooleanField(default=False)),
                ('reviewer', models.CharField(max_length=100, null=True)),
                ('tahun', models.CharField(max_length=100, null=True)),
                ('link', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Visimisi',
            new_name='VisiMisiModel',
        ),
        migrations.RenameModel(
            old_name='Workprogramme',
            new_name='WorkProgrammeModel',
        ),
        migrations.DeleteModel(
            name='Journals',
        ),
        migrations.DeleteModel(
            name='TextBooks',
        ),
    ]
