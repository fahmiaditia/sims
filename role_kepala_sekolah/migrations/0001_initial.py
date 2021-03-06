# Generated by Django 4.0.2 on 2022-06-12 14:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gu_Profil_Kepsek',
            fields=[
                ('kepsek_profil_uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('kepsek_nama', models.CharField(blank=True, max_length=120, null=True, verbose_name='Nama')),
                ('kepsek_nip', models.CharField(blank=True, max_length=120, null=True, verbose_name='NIP')),
                ('kepsek_nuptk', models.CharField(blank=True, max_length=120, null=True, verbose_name='NUPTK')),
                ('kepsek_tempat_tanggal_lahir', models.CharField(blank=True, max_length=120, null=True, verbose_name='Tempat, Tanggal Lahir')),
                ('kepsek_jabatan', models.CharField(blank=True, max_length=120, null=True, verbose_name='Jabatan')),
                ('kepsek_pangkat_golongan', models.CharField(blank=True, max_length=120, null=True, verbose_name='Pangkat Golongan')),
                ('kepsek_user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name_plural': 'Profil kepsek',
            },
        ),
    ]
