# Generated by Django 3.2.5 on 2022-10-19 11:20

from django.db import migrations, models
import landingpage.models


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0003_auto_20221018_1737'),
    ]

    operations = [
        migrations.CreateModel(
            name='articletranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_image', models.FileField(blank=True, null=True, upload_to=landingpage.models.filepath_article_translation)),
                ('overview', models.TextField(blank=True)),
            ],
        ),
    ]
