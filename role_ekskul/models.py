from django.db import models
from sekolah.models import *
from sims import settings


# Create your models here.
class Profil_Pembimbing(models.Model):
	class Meta:
		verbose_name_plural = "Profil Pembimbing"
	ekskul_profil_uuid  			= models.UUIDField(default=uuid.uuid4, verbose_name="UUID", primary_key=True)
	ekskul_user 		    		= models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="User", null=True, blank=True)
	ekskul_nama						= models.CharField(max_length=120, verbose_name="Nama Lengkap", null=True, blank=True)
	ekskul_tempat_tanggal_lahir		= models.CharField(max_length=120, verbose_name="Tempat, Tanggal Lahir", null=True, blank=True)
	ekskul_alamat					= models.CharField(max_length=200, verbose_name="Alamat", null=True, blank=True)
	ekskul_telp 					= models.CharField(max_length=200, verbose_name="No Telp / Whatsapp", null=True, blank=True)
	ekskul_mata_ekskul				= models.ForeignKey(SKL_Ekskul, on_delete=models.SET_NULL, null=True, blank=True)
	def __str__(self):
		return f"{self.ekskul_nama} - {self.ekskul_mata_ekskul}"