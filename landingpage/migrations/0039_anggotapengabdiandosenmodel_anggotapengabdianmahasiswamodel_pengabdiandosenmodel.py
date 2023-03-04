# Generated by Django 3.2.5 on 2023-02-25 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0038_auto_20230225_1459'),
    ]

    operations = [
        migrations.CreateModel(
            name='PengabdianDosenModel',
            fields=[
                ('id', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('salt', models.CharField(max_length=64, null=True)),
                ('judul', models.TextField(blank=True, max_length=150)),
                ('tahun', models.TextField(blank=True, max_length=4)),
                ('asal_pendanaan', models.TextField(blank=True, max_length=100)),
                ('total_pendanaan', models.IntegerField(blank=True)),
                ('link_laporan', models.TextField(blank=True, max_length=200)),
                ('fakultas', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='landingpage.fakultasmodel')),
                ('ketua_peneliti', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landingpage.dosenmodel')),
                ('prodi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landingpage.prodimodel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AnggotaPengabdianMahasiswaModel',
            fields=[
                ('id', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('salt', models.CharField(max_length=64, null=True)),
                ('anggota_mahasiswa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landingpage.mahasiswamodel')),
                ('fakultas', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='landingpage.fakultasmodel')),
                ('penelitian', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landingpage.pengabdiandosenmodel')),
                ('prodi', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='landingpage.prodimodel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AnggotaPengabdianDosenModel',
            fields=[
                ('id', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('salt', models.CharField(max_length=64, null=True)),
                ('anggota_dosen', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='landingpage.dosenmodel')),
                ('fakultas', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='landingpage.fakultasmodel')),
                ('penelitian', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='landingpage.pengabdiandosenmodel')),
                ('prodi', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='landingpage.prodimodel')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
