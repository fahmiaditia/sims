# Generated by Django 4.0.2 on 2022-06-10 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sekolah', '0006_skl_ekskul'),
        ('role_murid', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profil_murid',
            name='murid_ekskul',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sekolah.skl_ekskul', verbose_name='Ekstrakulikuler'),
        ),
    ]
