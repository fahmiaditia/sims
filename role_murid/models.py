from django.db import models
from sims import settings
from sekolah.models import *
import uuid

# Create your models here.
class Profil_Murid(models.Model):
	class Meta:
		verbose_name_plural = "Profil Murid"
	murid_profil_uuid  = models.UUIDField(default=uuid.uuid4, verbose_name="Profil Murid", primary_key=True)
	murid_user 		   = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="User", null=True, blank=True)
	murid_nama 		   = models.CharField(max_length=120, verbose_name="Nama", null=True, blank=True)
	murid_kelas 	   = models.ForeignKey(SKL_Kelas, on_delete=models.CASCADE, verbose_name="Kelas", null=True, blank=True)
	murid_nisn 		   = models.CharField(max_length=120, verbose_name="NISN", null=True, blank=True)
	murid_nss 		   = models.CharField(max_length=120, verbose_name="NSS", null=True, blank=True)
	murid_npsn 		   = models.CharField(max_length=120, verbose_name="NPSN", null=True, blank=True)
	murid_nomor_induk  = models.CharField(max_length=120, verbose_name="Nomor Induk", null=True, blank=True)
	murid_semester 	   = models.ForeignKey(SKL_Semester, on_delete=models.CASCADE, verbose_name="Semester", null=True, blank=True)
	murid_tahun_ajaran = models.ForeignKey(SKL_Tahun_Ajaran, on_delete=models.CASCADE, verbose_name="Tahun Ajaran", null=True, blank=True)
	murid_ekskul	   = models.ForeignKey(SKL_Ekskul, on_delete=models.SET_NULL, verbose_name="Ekstrakulikuler", null=True, blank=True, default=None)
	def __str__(self):
		return f"{self.murid_nama} - {self.murid_kelas}"
