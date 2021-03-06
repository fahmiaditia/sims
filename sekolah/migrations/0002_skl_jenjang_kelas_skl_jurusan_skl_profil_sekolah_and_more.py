# Generated by Django 4.0.2 on 2022-06-03 10:12

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('sekolah', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SKL_Jenjang_Kelas',
            fields=[
                ('skl_jenjang_uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('skl_jenjang_nama', models.CharField(blank=True, max_length=20, null=True, verbose_name='Jenjang Kelas')),
            ],
            options={
                'verbose_name_plural': 'KL | Jenjang Kelas',
            },
        ),
        migrations.CreateModel(
            name='SKL_Jurusan',
            fields=[
                ('skl_jurusan_uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('skl_jurusan_nama', models.CharField(blank=True, max_length=120, null=True, verbose_name='Nama Jurusan')),
            ],
            options={
                'verbose_name_plural': 'KL | Jurusan',
            },
        ),
        migrations.CreateModel(
            name='SKL_Profil_Sekolah',
            fields=[
                ('skl_profil_sekolah_uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('skl_nama_sekolah', models.CharField(blank=True, max_length=120, null=True, verbose_name='Nama Sekolah')),
                ('skl_alamat_sekolah', models.CharField(blank=True, max_length=120, null=True, verbose_name='Alamat')),
                ('skl_nomor_telepon_sekolah', models.CharField(blank=True, max_length=120, null=True, verbose_name='Nomor Telp')),
                ('skl_email_sekolah', models.CharField(blank=True, max_length=120, null=True, verbose_name='Email')),
                ('skl_npsn_sekolah', models.CharField(blank=True, max_length=120, null=True, verbose_name='NPSN')),
                ('skl_kepala_sekolah', models.CharField(blank=True, max_length=120, null=True, verbose_name='Kepala Sekolah')),
                ('skl_visi_sekolah', models.TextField(blank=True, null=True, verbose_name='Visi')),
                ('skl_misi_sekolah', models.TextField(blank=True, null=True, verbose_name='Misi')),
            ],
        ),
        migrations.CreateModel(
            name='SKL_Ruang_Kelas',
            fields=[
                ('skl_ruang_uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('skl_ruang_nama', models.CharField(blank=True, max_length=10, null=True, verbose_name='Ruang Kelas')),
            ],
            options={
                'verbose_name_plural': 'KL | Ruang Kelas',
            },
        ),
        migrations.AlterModelOptions(
            name='akun',
            options={'verbose_name_plural': 'Akun'},
        ),
        migrations.CreateModel(
            name='SKL_Kelas',
            fields=[
                ('skl_k_kelas_uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('skl_k_kelas_nama', models.CharField(blank=True, max_length=20, null=True, verbose_name='Kelas')),
                ('skl_k_jenjang', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sekolah.skl_jenjang_kelas', verbose_name='Jenjang')),
                ('skl_k_jurusan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sekolah.skl_jurusan', verbose_name='Jurusan')),
                ('skl_k_ruang', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sekolah.skl_ruang_kelas', verbose_name='Ruang')),
            ],
            options={
                'verbose_name_plural': 'KL | Kelas',
            },
        ),
    ]
