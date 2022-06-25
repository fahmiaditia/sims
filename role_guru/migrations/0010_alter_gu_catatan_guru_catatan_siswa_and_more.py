# Generated by Django 4.0.2 on 2022-06-15 13:13

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('role_murid', '0002_profil_murid_murid_ekskul'),
        ('role_guru', '0009_rename_guru_catatan_dasar_mata_pelajaran_jurusan_gu_catatan_guru_catatan_mata_pelajaran_jurusan_and_'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gu_catatan',
            name='guru_catatan_siswa',
            field=models.ForeignKey(blank=True, help_text='Tidak perlu diisi ketika catatan berstatus pengumuman', null=True, on_delete=django.db.models.deletion.CASCADE, to='role_murid.profil_murid', verbose_name='Siswa'),
        ),
        migrations.AlterField(
            model_name='gu_catatan',
            name='guru_catatan_uuid',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='UUID'),
        ),
    ]
