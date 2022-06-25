from django.db import models
from sims import settings
from sekolah.models import *
from role_murid.models import *
import uuid
# Create your models here.
def IsNewChecker(var):
	is_new = True
	if var is None:
		is_new = True
	else:
		is_new = False
	return is_new

status_catatan = [
	('Peringatan', 'Peringatan'),
	('Himbauan', 'Himbauan'),
	('Pengumuman', 'Pengumuman'),
]

class Gu_Profil_Guru(models.Model):
	class Meta:
		verbose_name_plural = "Profil Guru"
	guru_profil_uuid 	 		 = models.UUIDField(default=uuid.uuid4, primary_key=True)
	guru_user 			 		 = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="User", null=True, blank=True)
	guru_nama			 		 = models.CharField(max_length=120, verbose_name="Nama", null=True, blank=True)
	guru_nip			 		 = models.CharField(max_length=120, verbose_name="NIP", null=True, blank=True)
	guru_nuptk			 		 = models.CharField(max_length=120, verbose_name="NUPTK", null=True, blank=True)
	guru_tempat_tanggal_lahir	 = models.CharField(max_length=120, verbose_name="Tempat, Tanggal Lahir", null=True, blank=True)
	guru_jabatan				 = models.CharField(max_length=120, verbose_name="Jabatan", null=True, blank=True)
	guru_pangkat_golongan		 = models.CharField(max_length=120, verbose_name="Pangkat Golongan", null=True, blank=True)
	guru_mata_pelajaran_wajib	 = models.ForeignKey(SKL_Mata_Pelajaran_Wajib, on_delete=models.SET_NULL, verbose_name="Pengampu Mata Pelajaran Wajib", null=True, blank=True)
	guru_mata_pelajaran_jurusan	 = models.ForeignKey(SKL_Mata_Pelajaran_Jurusan, on_delete=models.SET_NULL, verbose_name="Pengampu Mata Pelajaran Jurusan", null=True, blank=True)
	guru_wali_kelas				 = models.ForeignKey(SKL_Kelas, on_delete=models.SET_NULL, verbose_name="Wali Kelas", null=True, blank=True, default=None)
	def __str__(self):
		return f"{self.guru_nama}"
class Gu_Data_Kompetensi_Dasar(models.Model):
	class Meta:
		verbose_name_plural = "Data Kompetensi Dasar"
	guru_kompetensi_dasar_uuid 					 = models.UUIDField(default=uuid.uuid4, primary_key=True)
	guru_nomor_kd 								 = models.CharField(max_length=20, verbose_name="Nomor KD", null=True, blank=True)
	guru_kompetensi_dasar 						 = models.TextField(verbose_name="Kompetensi Dasar", null=True, blank=True)
	guru_kompetensi_dasar_kelas 				 = models.ForeignKey(SKL_Jenjang_Kelas, on_delete=models.SET_NULL, verbose_name="Kelas", null=True, blank=True)
	guru_kompetensi_dasar_semester 				 = models.ForeignKey(SKL_Semester, on_delete=models.SET_NULL, verbose_name="Semester", null=True, blank=True)
	guru_kompetensi_dasar_mata_pelajaran_wajib 	 = models.ForeignKey(SKL_Mata_Pelajaran_Wajib, on_delete=models.SET_NULL, verbose_name="Mata Pelajaran Wajib", null=True, blank=True)
	guru_kompetensi_dasar_mata_pelajaran_jurusan = models.ForeignKey(SKL_Mata_Pelajaran_Jurusan, on_delete=models.SET_NULL, verbose_name="Mata Pelajaran Jurusan", null=True, blank=True)
	def __str__(self):
		return f"{self.guru_nomor_kd} - {self.guru_kompetensi_dasar}"

class Gu_Data_Teknik_Penilaian(models.Model):
	class Meta:
		verbose_name_plural="Data Teknik Penilaian"
	guru_teknik_penilaian_uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
	guru_teknik_penilaian 	   = models.CharField(max_length=120, verbose_name="Teknik Penilaian")
	def __str__(self):
		return f"{self.guru_teknik_penilaian}"

class Gu_Catatan(models.Model):
	class Meta:
		verbose_name_plural="Catatan"
	guru_catatan_uuid   						 = models.UUIDField(default=uuid.uuid4, primary_key=True, verbose_name="UUID")
	guru_catatan_status 						 = models.CharField(max_length=30, choices=status_catatan, verbose_name="Status", null=True, blank=True)
	guru_catatan_siswa  						 = models.ForeignKey(Profil_Murid, on_delete=models.CASCADE, verbose_name="Siswa" ,null=True, blank=True, help_text="Tidak perlu diisi ketika catatan berstatus pengumuman")
	guru_catatan_mata_pelajaran_wajib 	 		 = models.ForeignKey(SKL_Mata_Pelajaran_Wajib, on_delete=models.SET_NULL, verbose_name="Mata Pelajaran Wajib", null=True, blank=True)
	guru_catatan_mata_pelajaran_jurusan 		 = models.ForeignKey(SKL_Mata_Pelajaran_Jurusan, on_delete=models.SET_NULL, verbose_name="Mata Pelajaran Jurusan", null=True, blank=True)
	guru_catatan 	    					     = models.TextField(max_length=300, verbose_name="Catatan")
	def __str__(self):
		return f"{self.guru_catatan_siswa} - {self.guru_catatan_status}"