# Generated by Django 4.0.2 on 2022-06-10 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sekolah', '0008_alter_akun_is_pembimbing_ekskul'),
        ('role_ekskul', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profil_pembimbing',
            name='ekskul_mata_ekskul',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sekolah.skl_ekskul'),
        ),
    ]
