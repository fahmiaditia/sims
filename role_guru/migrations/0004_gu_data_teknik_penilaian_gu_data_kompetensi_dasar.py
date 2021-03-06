# Generated by Django 4.0.2 on 2022-06-03 14:13

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('sekolah', '0004_skl_semester_skl_tahun_ajaran'),
        ('role_guru', '0003_rename_profil_guru_gu_profil_guru'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gu_Data_Teknik_Penilaian',
            fields=[
                ('guru_teknik_penilaian_uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('guru_teknik_penilaian', models.CharField(max_length=120, verbose_name='Teknik Penilaian')),
            ],
            options={
                'verbose_name_plural': 'Data Teknik Penilaian',
            },
        ),
        migrations.CreateModel(
            name='Gu_Data_Kompetensi_Dasar',
            fields=[
                ('guru_kompetensi_dasar_uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('guru_nomor_kd', models.CharField(blank=True, max_length=20, null=True, verbose_name='Nomor KD')),
                ('guru_kompetensi_dasar', models.TextField(blank=True, null=True, verbose_name='Kompetensi Dasar')),
                ('guru_kompetensi_dasar_kelas', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sekolah.skl_jenjang_kelas', verbose_name='Kelas')),
                ('guru_kompetensi_dasar_mata_pelajaran_jurusan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sekolah.skl_mata_pelajaran_jurusan', verbose_name='Mata Pelajaran Jurusan')),
                ('guru_kompetensi_dasar_mata_pelajaran_wajib', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sekolah.skl_mata_pelajaran_wajib', verbose_name='Mata Pelajaran Wajib')),
                ('guru_kompetensi_dasar_semester', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sekolah.skl_semester', verbose_name='Semester')),
            ],
            options={
                'verbose_name_plural': 'Data Kompetensi Dasar',
            },
        ),
    ]
