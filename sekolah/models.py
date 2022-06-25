from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.

class Akun(AbstractUser):
	class Meta:
		verbose_name_plural = "Akun"
	uuid_akun = models.UUIDField(default=uuid.uuid4, primary_key=True)
	is_murid  = models.BooleanField(default=False, verbose_name="Role Murid", null=True, blank=True)
	is_guru   = models.BooleanField(default=False, verbose_name="Role Guru", null=True, blank=True)
	is_pembimbing_ekskul = models.BooleanField(default=False, verbose_name="Role Pelatih Ekskul", null=True, blank=True)
	is_kepsek = models.BooleanField(default=False, verbose_name="Role Kepala Sekolah", null=True, blank=True)
	is_bk = models.BooleanField(default=False, verbose_name="Role BK", null=True, blank=True)
	def __str__(self):
		return f"{self.first_name}"


# BAGIAN SEKOLAH
class SKL_Jurusan(models.Model):
	class Meta:
		verbose_name_plural = "KL | Jurusan"
	skl_jurusan_uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
	skl_jurusan_nama = models.CharField(max_length=120, verbose_name="Nama Jurusan", null=True, blank=True)
	def __str__(self):
		return f"{self.skl_jurusan_nama}"

class SKL_Jenjang_Kelas(models.Model):
	class Meta:
		verbose_name_plural = "KL | Jenjang Kelas"
	skl_jenjang_uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
	skl_jenjang_nama = models.CharField(max_length=20, verbose_name="Jenjang Kelas", null=True, blank=True)
	def __str__(self):
		return f"{self.skl_jenjang_nama}"

class SKL_Ruang_Kelas(models.Model):
	class Meta:
		verbose_name_plural = "KL | Ruang Kelas"
	skl_ruang_uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
	skl_ruang_nama = models.CharField(max_length=10, verbose_name="Ruang Kelas",null=True, blank=True)
	def __str__(self):
		return f"{self.skl_ruang_nama}"

class SKL_Kelas(models.Model):
	class Meta:
		verbose_name_plural = "KL | Kelas"
	skl_k_kelas_uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
	skl_k_jenjang    = models.ForeignKey(SKL_Jenjang_Kelas, verbose_name="Jenjang", null=True, blank=True, on_delete=models.SET_NULL)
	skl_k_jurusan    = models.ForeignKey(SKL_Jurusan, verbose_name="Jurusan", null=True, blank=True, on_delete=models.SET_NULL)
	skl_k_ruang 	 = models.ForeignKey(SKL_Ruang_Kelas, verbose_name="Ruang", null=True, blank=True, on_delete=models.SET_NULL)
	skl_k_kelas_nama = models.CharField(max_length=20, verbose_name="Kelas", null=True, blank=True)
	def save(self, *args, **kwargs):
		self.skl_k_kelas_nama = f"{self.skl_k_jenjang} {self.skl_k_jurusan} {self.skl_k_ruang}"
		super(SKL_Kelas, self).save(*args, **kwargs)
	def __str__(self):
		return f"{self.skl_k_kelas_nama}"

class SKL_Profil_Sekolah(models.Model):
	class Meta:
		verbose_name_plural = "Profil Sekolah"
	skl_profil_sekolah_uuid   = models.UUIDField(default=uuid.uuid4, primary_key=True)
	skl_nama_sekolah 		  = models.CharField(max_length=120, verbose_name="Nama Sekolah", null=True, blank=True)
	skl_alamat_sekolah 		  = models.CharField(max_length=120, verbose_name="Alamat", null=True, blank=True)
	skl_nomor_telepon_sekolah = models.CharField(max_length=120, verbose_name="Nomor Telp", null=True, blank=True)
	skl_email_sekolah 		  = models.CharField(max_length=120, verbose_name="Email", null=True, blank=True)
	skl_npsn_sekolah  		  = models.CharField(max_length=120, verbose_name="NPSN", null=True, blank=True)
	skl_kepala_sekolah 		  = models.CharField(max_length=120, verbose_name="Kepala Sekolah", null=True, blank=True)
	skl_visi_sekolah 		  = models.TextField(verbose_name="Visi", null=True, blank=True)
	skl_misi_sekolah 		  = models.TextField(verbose_name="Misi", null=True, blank=True)
	def __str__(self):
		return f"{self.skl_nama_sekolah}"

# END BAGIAN SEKOLAH



# BAGIAN PELAJARAN
class SKL_Mata_Pelajaran_Wajib(models.Model):
	class Meta:
		verbose_name_plural = "PL | Data Mata Pelajaran Wajib"
	mapel_wajib_pelajaran_uuid = models.UUIDField(default=uuid.uuid4, verbose_name="UUID Mata Pelajaran", primary_key=True)
	mapel_wajib_pelajaran 	   = models.CharField(max_length=120, verbose_name="Mata Pelajaran", null=True, blank=True)
	def __str__(self):
		return f"{self.mapel_wajib_pelajaran}"

class SKL_Mata_Pelajaran_Jurusan(models.Model):
	class Meta:
		verbose_name_plural = "PL | Data Mata Pelajaran Jurusan"
	mapel_jurusan_pelajaran_uuid = models.UUIDField(default=uuid.uuid4, verbose_name="UUID Mata Pelajaran", primary_key=True)
	mapel_jurusan_pelajaran  	 = models.CharField(max_length=120, verbose_name="Mata Pelajaran", null=True, blank=True)
	mapel_jurusan_jurusan 		 = models.ForeignKey(SKL_Jurusan, on_delete=models.CASCADE, verbose_name="Jurusan", null=True, blank=True)
	def __str__(self):
		return f"{self.mapel_jurusan_pelajaran}"

class SKL_Semester(models.Model):
	class Meta:
		verbose_name_plural = "PL | Semester"
	skl_s_semester_uuid = models.UUIDField(default=uuid.uuid4, verbose_name="UUID Semester", primary_key=True)
	skl_s_semester = models.IntegerField(verbose_name="Semester",null=True, blank=True)
	def __str__(self):
		return f"{self.skl_s_semester}"

class SKL_Tahun_Ajaran(models.Model):
	class Meta:
		verbose_name_plural = "PL | Tahun Ajaran"
	skl_t_tahun_ajaran_uuid = models.UUIDField(default=uuid.uuid4, verbose_name="Tahun Ajaran", primary_key=True)
	skl_t_tahun_ajaran = models.CharField(max_length=120, verbose_name="Tahun Ajaran", null=True, blank=True)
	def __str__(self):
		return f"{self.skl_t_tahun_ajaran}"
# END BAGIAN PELAJARAN


# BAGIAN EKSKUL
class SKL_Ekskul(models.Model):
	class Meta:
		verbose_name_plural = "Ektrakulikuler"
	skl_ekskul_uuid = models.UUIDField(default=uuid.uuid4, verbose_name="UUID Ektrakulikuler", primary_key=True)
	skl_ekskul = models.CharField(max_length=120, null=True, blank=True)
	def __str__(self):
		return f"{self.skl_ekskul}"