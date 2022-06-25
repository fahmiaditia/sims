from django.db import models
from sims import settings
from sekolah.models import *
from role_murid.models import *
import uuid

# Create your models here.
status_catatan = [
	('Peringatan', 'Peringatan'),
	('Himbauan', 'Himbauan'),
	('Pengumuman', 'Pengumuman'),
]

class Profil_BK(models.Model):
	class Meta:
		verbose_name_plural = "Profil Bimbingan Konseling"
	bk_profil_uuid 	 		 	 = models.UUIDField(default=uuid.uuid4, primary_key=True)
	bk_user 			     	 = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="User", null=True, blank=True)
	bk_nama			 		 	 = models.CharField(max_length=120, verbose_name="Nama", null=True, blank=True)
	bk_nip			 		 	 = models.CharField(max_length=120, verbose_name="NIP", null=True, blank=True)
	bk_nuptk			 		 = models.CharField(max_length=120, verbose_name="NUPTK", null=True, blank=True)
	bk_tempat_tanggal_lahir	 	 = models.CharField(max_length=120, verbose_name="Tempat, Tanggal Lahir", null=True, blank=True)
	bk_jabatan				 	 = models.CharField(max_length=120, verbose_name="Jabatan", null=True, blank=True)
	bk_pangkat_golongan		 	 = models.CharField(max_length=120, verbose_name="Pangkat Golongan", null=True, blank=True)
	def __str__(self):
		return f"{self.bk_nama}"

class BK_Catatan(models.Model):
	class Meta:
		verbose_name_plural="Catatan"
	bk_catatan_uuid   						 = models.UUIDField(default=uuid.uuid4, primary_key=True, verbose_name="UUID")
	bk_catatan_status 						 = models.CharField(max_length=30, choices=status_catatan, verbose_name="Status", null=True, blank=True)
	bk_catatan_siswa  						 = models.ForeignKey(Profil_Murid, on_delete=models.CASCADE, verbose_name="Siswa" ,null=True, blank=True, help_text="Tidak perlu diisi ketika catatan berstatus pengumuman")
	bk_catatan 	    					     = models.TextField(max_length=300, verbose_name="Catatan")
	def __str__(self):
		return f"{self.bk_catatan_siswa} - {self.bk_catatan_status}"