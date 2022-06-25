# Generated by Django 4.0.2 on 2022-06-03 16:34

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('sekolah', '0004_skl_semester_skl_tahun_ajaran'),
        ('role_murid', '0001_initial'),
        ('role_guru', '0004_gu_data_teknik_penilaian_gu_data_kompetensi_dasar'),
        ('monitoring', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mo_Sikap_Spiritual',
            fields=[
                ('mo_penilaian_sikap_spiritual_uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='UUID Penilaian Sikap Spiritual')),
                ('mo_penilaian_ke', models.CharField(blank=True, choices=[('1', 'Satu'), ('2', 'Dua'), ('3', 'Tiga')], max_length=20, null=True, verbose_name='Penilaian Ke')),
                ('mo_nilai', models.CharField(blank=True, choices=[('Sangat Baik', 'Sangat Baik'), ('Baik', 'Baik'), ('Cukup', 'Cukup'), ('Kurang', 'Kurang')], max_length=20, null=True, verbose_name='Praktek')),
                ('mo_kelas', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sekolah.skl_kelas', verbose_name='Kelas')),
                ('mo_kompetensi_dasar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='role_guru.gu_data_kompetensi_dasar', verbose_name='Kompetensi Dasar')),
                ('mo_mata_pelajaran_jurusan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sekolah.skl_mata_pelajaran_jurusan', verbose_name='Mata Pelajaran Jurusan')),
                ('mo_mata_pelajaran_wajib', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sekolah.skl_mata_pelajaran_wajib', verbose_name='Mata Pelajaran Wajib')),
                ('mo_semester', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sekolah.skl_semester', verbose_name='Semester')),
                ('mo_siswa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='role_murid.profil_murid', verbose_name='Siswa')),
                ('mo_tahun_ajaran', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sekolah.skl_tahun_ajaran', verbose_name='Tahun Ajaran')),
            ],
            options={
                'verbose_name_plural': 'Nilai Sikap Sosial',
            },
        ),
        migrations.CreateModel(
            name='Mo_Sikap_Sosial',
            fields=[
                ('mo_penilaian_sikap_sosial_uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='UUID Penilaian Sikap Sosial')),
                ('mo_penilaian_ke', models.CharField(blank=True, choices=[('1', 'Satu'), ('2', 'Dua'), ('3', 'Tiga')], max_length=20, null=True, verbose_name='Penilaian Ke')),
                ('mo_nilai', models.CharField(blank=True, choices=[('Sangat Baik', 'Sangat Baik'), ('Baik', 'Baik'), ('Cukup', 'Cukup'), ('Kurang', 'Kurang')], max_length=20, null=True, verbose_name='Praktek')),
                ('mo_kelas', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sekolah.skl_kelas', verbose_name='Kelas')),
                ('mo_kompetensi_dasar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='role_guru.gu_data_kompetensi_dasar', verbose_name='Kompetensi Dasar')),
                ('mo_mata_pelajaran_jurusan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sekolah.skl_mata_pelajaran_jurusan', verbose_name='Mata Pelajaran Jurusan')),
                ('mo_mata_pelajaran_wajib', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sekolah.skl_mata_pelajaran_wajib', verbose_name='Mata Pelajaran Wajib')),
                ('mo_semester', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sekolah.skl_semester', verbose_name='Semester')),
                ('mo_siswa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='role_murid.profil_murid', verbose_name='Siswa')),
                ('mo_tahun_ajaran', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sekolah.skl_tahun_ajaran', verbose_name='Tahun Ajaran')),
            ],
            options={
                'verbose_name_plural': 'Nilai Sikap Sosial',
            },
        ),
    ]