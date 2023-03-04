# Generated by Django 3.2.5 on 2023-02-28 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0043_alter_validasiopl_link_matkul'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamTeachingModel',
            fields=[
                ('id', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('salt', models.CharField(max_length=64, null=True)),
                ('fakultas', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='landingpage.fakultasmodel')),
                ('matkul', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landingpage.validasiopl')),
                ('prodi', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='landingpage.prodimodel')),
                ('team_teaching', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landingpage.dosenmodel')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
