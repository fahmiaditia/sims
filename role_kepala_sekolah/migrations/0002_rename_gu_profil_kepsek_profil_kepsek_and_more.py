# Generated by Django 4.0.2 on 2022-06-12 14:49

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('role_kepala_sekolah', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Gu_Profil_Kepsek',
            new_name='Profil_Kepsek',
        ),
        migrations.AlterModelOptions(
            name='profil_kepsek',
            options={'verbose_name_plural': 'Profil Kepala Sekolah'},
        ),
    ]