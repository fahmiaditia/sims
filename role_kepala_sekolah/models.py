from django.db import models
from sims import settings
from sekolah.models import *
import uuid

# Create your models here.

class Profil_Kepsek(models.Model):
	class Meta:
		verbose_name_plural = "Profil Kepala Sekolah"
	kepsek_profil_uuid 	 		 	 = models.UUIDField(default=uuid.uuid4, primary_key=True)
	kepsek_user 			     	 = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="User", null=True, blank=True)
	kepsek_nama			 		 	 = models.CharField(max_length=120, verbose_name="Nama", null=True, blank=True)
	kepsek_nip			 		 	 = models.CharField(max_length=120, verbose_name="NIP", null=True, blank=True)
	kepsek_nuptk			 		 = models.CharField(max_length=120, verbose_name="NUPTK", null=True, blank=True)
	kepsek_tempat_tanggal_lahir	 	 = models.CharField(max_length=120, verbose_name="Tempat, Tanggal Lahir", null=True, blank=True)
	kepsek_jabatan				 	 = models.CharField(max_length=120, verbose_name="Jabatan", null=True, blank=True)
	kepsek_pangkat_golongan		 	 = models.CharField(max_length=120, verbose_name="Pangkat Golongan", null=True, blank=True)
	def __str__(self):
		return f"{self.kepsek_nama}"