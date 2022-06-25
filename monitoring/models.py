from django.db import models
from role_guru.models import *
from role_murid.models import *
from sekolah.models import *
from crum import get_current_user
import uuid

def IsNewChecker(var):
	is_new = True
	if var is None:
		is_new = True
	else:
		is_new = False
	return is_new
# Create your models here.
urutan_penilaian = [
	('1','Satu'),
	('2','Dua'),
	('3','Tiga'),
]

des_nilai = [
	('Sangat Baik', 'Sangat Baik'),
	('Baik', 'Baik'),
	('Cukup', 'Cukup'),
	('Kurang', 'Kurang'),
]

juara = [
	('I', 'Satu'),
	('II', 'Dua'),
	('III', 'Tiga'),
	('IV', 'Harapan I'),
	('V', 'Harapan II'),
	('VI', 'Harapan III'),
]

tingkat_kejuaraan = [
	('Sekolah', 'Sekolah'),
	('Kota / Kabupaten', 'Kota / Kabupaten'),
	('Provinsi', 'Provinsi'),
	('Nasional', 'Nasional'),
	('Internasional', 'Internasional'),
]

status_ujian = [
	('Baru', 'Baru'),
	('Remedial', 'Remedial'),
]

ulangan_ke = [
	('1', '1'),
	('2', '2'),
	('3', '3'),
	('4', '4'),
	('5', '5'),
	('6', '6'),
	('7', '7'),
	('8', '8'),
	('9', '9'),
	('10', '10'),
	('11', '11'),
	('12', '12'),
	('13', '13'),
	('14', '14'),
	('15', '15'),
	('16', '16'),
	('17', '17'),
	('18', '18'),
	('19', '19'),
	('20', '20'),
	('21', '21'),
	('22', '22'),
	('23', '23'),
	('24', '24'),
	('25', '25'),
	('26', '26'),
	('27', '27'),
	('28', '28'),
	('29', '29'),
	('30', '30'),
	('31', '31'),
	('32', '32'),
	('33', '33'),
	('34', '34'),
	('35', '35'),
	('36', '36'),
	('37', '37'),
	('38', '38'),
	('39', '39'),
	('40', '40'),
	('41', '41'),
	('42', '42'),
	('43', '43'),
	('44', '44'),
	('45', '45'),
	('46', '46'),
	('47', '47'),
	('48', '48'),
	('49', '49'),
	('50', '50'),
	('51', '51'),
	('52', '52'),
	('53', '53'),
	('54', '54'),
	('55', '55'),
	('56', '56'),
	('57', '57'),
	('58', '58'),
	('59', '59'),
	('60', '60'),
	('61', '61'),
	('62', '62'),
	('63', '63'),
	('64', '64'),
	('65', '65'),
	('66', '66'),
	('67', '67'),
	('68', '68'),
	('69', '69'),
	('70', '70'),
	('71', '71'),
	('72', '72'),
	('73', '73'),
	('74', '74'),
	('75', '75'),
	('76', '76'),
	('77', '77'),
	('78', '78'),
	('79', '79'),
	('80', '80'),
	('81', '81'),
	('82', '82'),
	('83', '83'),
	('84', '84'),
	('85', '85'),
	('86', '86'),
	('87', '87'),
	('88', '88'),
	('89', '89'),
	('90', '90'),
	('91', '91'),
	('92', '92'),
	('93', '93'),
	('94', '94'),
	('95', '95'),
	('96', '96'),
	('97', '97'),
	('98', '98'),
	('99', '99'),
	('100', '100'),
]

ketuntasan = [
	('Tuntas', 'Tuntas'),
	('Belum Tuntas', 'Belum Tuntas'),
]

class Mo_Penilaian_Pengetahuan(models.Model):
	class Meta:
		verbose_name_plural="Nilai Pengetahuan"
	mo_penilaian_pengetahuan_uuid = models.UUIDField(default=uuid.uuid4,verbose_name="UUID Penilaian Pengetahuan", primary_key=True)
	mo_siswa 				  = models.ForeignKey(Profil_Murid, verbose_name="Siswa", on_delete=models.CASCADE, null=True, blank=True)
	mo_kelas 				  = models.ForeignKey(SKL_Kelas, verbose_name="Kelas", on_delete=models.CASCADE, null=True, blank=True, help_text="Tidak perlu diisi")
	mo_tahun_ajaran 		  = models.ForeignKey(SKL_Tahun_Ajaran, verbose_name="Tahun Ajaran", on_delete=models.CASCADE, null=True, blank=True)
	mo_semester 			  = models.ForeignKey(SKL_Semester, verbose_name="Semester", on_delete=models.CASCADE, null=True, blank=True)
	mo_kompetensi_dasar 	  = models.ForeignKey(Gu_Data_Kompetensi_Dasar, verbose_name="Kompetensi Dasar", on_delete=models.CASCADE, null=True, blank=True)
	mo_mata_pelajaran_wajib   = models.ForeignKey(SKL_Mata_Pelajaran_Wajib, verbose_name="Mata Pelajaran Wajib", on_delete=models.CASCADE, null=True, blank=True)
	mo_mata_pelajaran_jurusan = models.ForeignKey(SKL_Mata_Pelajaran_Jurusan, verbose_name="Mata Pelajaran Jurusan", on_delete=models.CASCADE, null=True, blank=True)
	mo_penilaian_ke 		  = models.CharField(choices=urutan_penilaian, max_length=20, verbose_name="Penilaian Ke", null=True, blank=True)
	mo_nilai_P1_TGS 		  = models.FloatField(default=0, verbose_name="Nilai P1 TGS", null=True, blank=True)
	mo_nilai_P2_TLS 		  = models.FloatField(default=0, verbose_name="Nilai P2 TLS", null=True, blank=True)
	mo_nilai_P3_TLS 		  = models.FloatField(default=0, verbose_name="Nilai P3 TLS", null=True, blank=True)

class Mo_Penilaian_Keterampilan(models.Model):
	class Meta:
		verbose_name_plural="Nilai Keterampilan"
	mo_penilaian_keterampilan_uuid = models.UUIDField(default=uuid.uuid4,verbose_name="UUID Penilaian Keterampilan", primary_key=True)
	mo_siswa 				  = models.ForeignKey(Profil_Murid, verbose_name="Siswa",on_delete=models.CASCADE, null=True, blank=True)
	mo_kelas 				  = models.ForeignKey(SKL_Kelas, verbose_name="Kelas",on_delete=models.CASCADE, null=True, blank=True)
	mo_tahun_ajaran 		  = models.ForeignKey(SKL_Tahun_Ajaran, verbose_name="Tahun Ajaran",on_delete=models.CASCADE, null=True, blank=True)
	mo_semester 			  = models.ForeignKey(SKL_Semester, verbose_name="Semester",on_delete=models.CASCADE, null=True, blank=True)
	mo_kompetensi_dasar 	  = models.ForeignKey(Gu_Data_Kompetensi_Dasar, verbose_name="Kompetensi Dasar",on_delete=models.CASCADE, null=True, blank=True)
	mo_mata_pelajaran_wajib   = models.ForeignKey(SKL_Mata_Pelajaran_Wajib, verbose_name="Mata Pelajaran Wajib",on_delete=models.CASCADE, null=True, blank=True)
	mo_mata_pelajaran_jurusan = models.ForeignKey(SKL_Mata_Pelajaran_Jurusan, verbose_name="Mata Pelajaran Jurusan",on_delete=models.CASCADE, null=True, blank=True)
	mo_penilaian_ke 		  = models.CharField(choices=urutan_penilaian, max_length=20, verbose_name="Penilaian Ke", null=True, blank=True)
	mo_praktek 		  		  = models.FloatField(default=0, verbose_name="Praktek", null=True, blank=True)
	mo_produk 				  = models.FloatField(default=0, verbose_name="Produk", null=True, blank=True)
	mo_proyek 				  = models.FloatField(default=0, verbose_name="Proyek", null=True, blank=True)
	mo_portofolio 			  = models.FloatField(default=0, verbose_name="Portofolio", null=True, blank=True)

class Mo_Sikap_Sosial(models.Model):
	class Meta:
		verbose_name_plural="Nilai Sikap Sosial"
	mo_penilaian_sikap_sosial_uuid = models.UUIDField(default=uuid.uuid4,verbose_name="UUID Penilaian Sikap Sosial", primary_key=True)
	mo_siswa 				  = models.ForeignKey(Profil_Murid, verbose_name="Siswa",on_delete=models.CASCADE, null=True, blank=True)
	mo_kelas 				  = models.ForeignKey(SKL_Kelas, verbose_name="Kelas",on_delete=models.CASCADE, null=True, blank=True)
	mo_tahun_ajaran 		  = models.ForeignKey(SKL_Tahun_Ajaran, verbose_name="Tahun Ajaran",on_delete=models.CASCADE, null=True, blank=True)
	mo_semester 			  = models.ForeignKey(SKL_Semester, verbose_name="Semester",on_delete=models.CASCADE, null=True, blank=True)
	mo_kompetensi_dasar 	  = models.ForeignKey(Gu_Data_Kompetensi_Dasar, verbose_name="Kompetensi Dasar",on_delete=models.CASCADE, null=True, blank=True)
	mo_mata_pelajaran_wajib   = models.ForeignKey(SKL_Mata_Pelajaran_Wajib, verbose_name="Mata Pelajaran Wajib",on_delete=models.CASCADE, null=True, blank=True)
	mo_mata_pelajaran_jurusan = models.ForeignKey(SKL_Mata_Pelajaran_Jurusan, verbose_name="Mata Pelajaran Jurusan",on_delete=models.CASCADE, null=True, blank=True)
	mo_penilaian_ke 		  = models.CharField(choices=urutan_penilaian, max_length=20, verbose_name="Penilaian Ke", null=True, blank=True)
	mo_nilai  		  		  = models.CharField(choices=des_nilai, max_length=20, verbose_name="Nilai", null=True, blank=True)
	mo_proyeksi_nilai		  = models.FloatField(default=None, verbose_name="Proyeksi Nilai ke Angka", null=True, blank=True)

	def save(self, *args, **kwargs):
		if self.mo_nilai == "Sangat Baik":
			self.mo_proyeksi_nilai = 100
		elif self.mo_nilai == "Baik":
			self.mo_proyeksi_nilai = 75
		elif self.mo_nilai == "Cukup":
			self.mo_proyeksi_nilai = 50
		elif self.mo_nilai == "Kurang":
			self.mo_proyeksi_nilai = 25
		super(Mo_Sikap_Sosial, self).save(*args, **kwargs)

class Mo_Sikap_Spiritual(models.Model):
	class Meta:
		verbose_name_plural="Nilai Sikap Spiritual"
	mo_penilaian_sikap_spiritual_uuid = models.UUIDField(default=uuid.uuid4,verbose_name="UUID Penilaian Sikap Spiritual", primary_key=True)
	mo_siswa 				  = models.ForeignKey(Profil_Murid, verbose_name="Siswa",on_delete=models.CASCADE, null=True, blank=True)
	mo_kelas 				  = models.ForeignKey(SKL_Kelas, verbose_name="Kelas",on_delete=models.CASCADE, null=True, blank=True)
	mo_tahun_ajaran 		  = models.ForeignKey(SKL_Tahun_Ajaran, verbose_name="Tahun Ajaran",on_delete=models.CASCADE, null=True, blank=True)
	mo_semester 			  = models.ForeignKey(SKL_Semester, verbose_name="Semester",on_delete=models.CASCADE, null=True, blank=True)
	mo_kompetensi_dasar 	  = models.ForeignKey(Gu_Data_Kompetensi_Dasar, verbose_name="Kompetensi Dasar",on_delete=models.CASCADE, null=True, blank=True)
	mo_mata_pelajaran_wajib   = models.ForeignKey(SKL_Mata_Pelajaran_Wajib, verbose_name="Mata Pelajaran Wajib",on_delete=models.CASCADE, null=True, blank=True)
	mo_mata_pelajaran_jurusan = models.ForeignKey(SKL_Mata_Pelajaran_Jurusan, verbose_name="Mata Pelajaran Jurusan",on_delete=models.CASCADE, null=True, blank=True)
	mo_penilaian_ke 		  = models.CharField(choices=urutan_penilaian, max_length=20, verbose_name="Penilaian Ke", null=True, blank=True)
	mo_nilai  		  		  = models.CharField(choices=des_nilai, max_length=20, verbose_name="Nilai", null=True, blank=True)
	mo_proyeksi_nilai		  = models.FloatField(default=None, verbose_name="Proyeksi Nilai ke Angka", null=True, blank=True)

	def save(self, *args, **kwargs):
		if self.mo_nilai == "Sangat Baik":
			self.mo_proyeksi_nilai = 100
		elif self.mo_nilai == "Baik":
			self.mo_proyeksi_nilai = 75
		elif self.mo_nilai == "Cukup":
			self.mo_proyeksi_nilai = 50
		elif self.mo_nilai == "Kurang":
			self.mo_proyeksi_nilai = 25
		super(Mo_Sikap_Spiritual, self).save(*args, **kwargs)


class Mo_Penilaian_Ulangan_KKM(models.Model):
	class Meta:
		verbose_name_plural="KKM"
	mo_penilaian_kkm_uuid 	  = models.UUIDField(default=uuid.uuid4, verbose_name='UUID KKM', primary_key=True)
	mo_mata_pelajaran_wajib   = models.ForeignKey(SKL_Mata_Pelajaran_Wajib, verbose_name="Mata Pelajaran Wajib",on_delete=models.CASCADE, null=True, blank=True)
	mo_mata_pelajaran_jurusan = models.ForeignKey(SKL_Mata_Pelajaran_Jurusan, verbose_name="Mata Pelajaran Jurusan",on_delete=models.CASCADE, null=True, blank=True)
	mo_jenjang_kelas 		  = models.ForeignKey(SKL_Jenjang_Kelas, verbose_name="Jenjang Kelas", on_delete=models.SET_NULL, null=True, blank=True)
	mo_kkm        		  	  = models.FloatField(default=0, verbose_name="KKM", null=True, blank=True)
	def __str__(self):
		return f"{self.mo_kkm} - {self.mo_mata_pelajaran_wajib} / {self.mo_mata_pelajaran_jurusan}"


class Mo_Penilaian_Ulangan(models.Model):
	class Meta:
		verbose_name_plural="Nilai Ulangan"
	mo_penilaian_ulangan_uuid = models.UUIDField(default=uuid.uuid4,verbose_name="UUID Penilaian Ulangan", primary_key=True)
	mo_status 				  = models.CharField(choices=status_ujian, max_length=20, verbose_name="Status Ulangan", null=True, blank=True)
	mo_siswa 				  = models.ForeignKey(Profil_Murid, verbose_name="Siswa",on_delete=models.CASCADE, null=True, blank=True)
	mo_kelas 				  = models.ForeignKey(SKL_Kelas, verbose_name="Kelas",on_delete=models.CASCADE, null=True, blank=True)
	mo_tahun_ajaran 		  = models.ForeignKey(SKL_Tahun_Ajaran, verbose_name="Tahun Ajaran",on_delete=models.CASCADE, null=True, blank=True)
	mo_semester 			  = models.ForeignKey(SKL_Semester, verbose_name="Semester",on_delete=models.CASCADE, null=True, blank=True)
	mo_kompetensi_dasar 	  = models.ForeignKey(Gu_Data_Kompetensi_Dasar, verbose_name="Kompetensi Dasar",on_delete=models.CASCADE, null=True, blank=True)
	mo_mata_pelajaran_wajib   = models.ForeignKey(SKL_Mata_Pelajaran_Wajib, verbose_name="Mata Pelajaran Wajib",on_delete=models.CASCADE, null=True, blank=True)
	mo_mata_pelajaran_jurusan = models.ForeignKey(SKL_Mata_Pelajaran_Jurusan, verbose_name="Mata Pelajaran Jurusan",on_delete=models.CASCADE, null=True, blank=True)
	mo_ulangan_ke	 		  = models.CharField(choices=ulangan_ke, max_length=20, verbose_name="Ulangan Ke", null=True, blank=True)
	mo_kkm 					  = models.ForeignKey(Mo_Penilaian_Ulangan_KKM, verbose_name="KKM", on_delete=models.SET_NULL, null=True, blank=True)
	mo_nilai        		  = models.FloatField(default=0, verbose_name="Nilai", null=True, blank=True)
	mo_ketuntasan	 		  = models.CharField(choices=ketuntasan, max_length=20, verbose_name="Status Ketuntasan", null=True, blank=True)


class Mo_Penilaian_UTS(models.Model):
	class Meta:
		verbose_name_plural="Nilai Ulangan Tengah Semester"
	mo_penilaian_uts_uuid 	  = models.UUIDField(default=uuid.uuid4,verbose_name="UUID Penilaian UTS", primary_key=True)
	mo_status 				  = models.CharField(choices=status_ujian, max_length=20, verbose_name="Status Ulangan", null=True, blank=True)
	mo_siswa 				  = models.ForeignKey(Profil_Murid, verbose_name="Siswa",on_delete=models.CASCADE, null=True, blank=True)
	mo_kelas 				  = models.ForeignKey(SKL_Kelas, verbose_name="Kelas",on_delete=models.CASCADE, null=True, blank=True)
	mo_tahun_ajaran 		  = models.ForeignKey(SKL_Tahun_Ajaran, verbose_name="Tahun Ajaran",on_delete=models.CASCADE, null=True, blank=True)
	mo_semester 			  = models.ForeignKey(SKL_Semester, verbose_name="Semester",on_delete=models.CASCADE, null=True, blank=True)
	mo_mata_pelajaran_wajib   = models.ForeignKey(SKL_Mata_Pelajaran_Wajib, verbose_name="Mata Pelajaran Wajib",on_delete=models.CASCADE, null=True, blank=True)
	mo_mata_pelajaran_jurusan = models.ForeignKey(SKL_Mata_Pelajaran_Jurusan, verbose_name="Mata Pelajaran Jurusan",on_delete=models.CASCADE, null=True, blank=True)
	mo_kkm 					  = models.ForeignKey(Mo_Penilaian_Ulangan_KKM, verbose_name="KKM", on_delete=models.SET_NULL, null=True, blank=True)
	mo_nilai        		  = models.FloatField(default=0, verbose_name="Nilai", null=True, blank=True)
	mo_ketuntasan	 		  = models.CharField(choices=ketuntasan, max_length=20, verbose_name="Status Ketuntasan", null=True, blank=True)


class Mo_Penilaian_UAS(models.Model):
	class Meta:
		verbose_name_plural="Nilai Ulangan Akhir Semester"
	mo_penilaian_uas_uuid 	  = models.UUIDField(default=uuid.uuid4,verbose_name="UUID Penilaian UAS", primary_key=True)
	mo_status 				  = models.CharField(choices=status_ujian, max_length=20, verbose_name="Status Ulangan", null=True, blank=True)
	mo_siswa 				  = models.ForeignKey(Profil_Murid, verbose_name="Siswa",on_delete=models.CASCADE, null=True, blank=True)
	mo_kelas 				  = models.ForeignKey(SKL_Kelas, verbose_name="Kelas",on_delete=models.CASCADE, null=True, blank=True)
	mo_tahun_ajaran 		  = models.ForeignKey(SKL_Tahun_Ajaran, verbose_name="Tahun Ajaran",on_delete=models.CASCADE, null=True, blank=True)
	mo_semester 			  = models.ForeignKey(SKL_Semester, verbose_name="Semester",on_delete=models.CASCADE, null=True, blank=True)
	mo_mata_pelajaran_wajib   = models.ForeignKey(SKL_Mata_Pelajaran_Wajib, verbose_name="Mata Pelajaran Wajib",on_delete=models.CASCADE, null=True, blank=True)
	mo_mata_pelajaran_jurusan = models.ForeignKey(SKL_Mata_Pelajaran_Jurusan, verbose_name="Mata Pelajaran Jurusan",on_delete=models.CASCADE, null=True, blank=True)
	mo_kkm 					  = models.ForeignKey(Mo_Penilaian_Ulangan_KKM, verbose_name="KKM", on_delete=models.SET_NULL, null=True, blank=True)
	mo_nilai        		  = models.FloatField(default=0, verbose_name="Nilai", null=True, blank=True)
	mo_ketuntasan	 		  = models.CharField(choices=ketuntasan, max_length=20, verbose_name="Status Ketuntasan", null=True, blank=True)


class Mo_Penilaian_Ekskul(models.Model):
	class Meta:
		verbose_name_plural = "Nilai Ekstrakulikuler"
	mo_penilaian_ekskul_uuid = models.UUIDField(default=uuid.uuid4,verbose_name="UUID Penilaian Penilaian Ekstrakulikuler", primary_key=True)
	mo_siswa 				  = models.ForeignKey(Profil_Murid, verbose_name="Siswa",on_delete=models.CASCADE, null=True, blank=True)
	mo_kelas 				  = models.ForeignKey(SKL_Kelas, verbose_name="Kelas",on_delete=models.CASCADE, null=True, blank=True)
	mo_tahun_ajaran 		  = models.ForeignKey(SKL_Tahun_Ajaran, verbose_name="Tahun Ajaran",on_delete=models.CASCADE, null=True, blank=True)
	mo_semester 			  = models.ForeignKey(SKL_Semester, verbose_name="Semester",on_delete=models.CASCADE, null=True, blank=True)
	mo_ekskul 				  = models.ForeignKey(SKL_Ekskul, verbose_name="Ekstrakulikuler",on_delete=models.CASCADE, null=True, blank=True)
	mo_nilai 				  = models.FloatField(default=0, verbose_name="Nilai", null=True, blank=True)

class Mo_Juara_Ekskul(models.Model):
	class Meta:
		verbose_name_plural = "Kejuaraan Ekstrakulikuler"
	mo_juara_ekskul_uuid = models.UUIDField(default=uuid.uuid4, verbose_name="UUID Juara Ekstrakulikuler", primary_key=True)
	mo_siswa 				  = models.ForeignKey(Profil_Murid, verbose_name="Siswa",on_delete=models.CASCADE, null=True, blank=True)
	mo_ekskul 				  = models.ForeignKey(SKL_Ekskul, verbose_name="Ekstrakulikuler",on_delete=models.CASCADE, null=True, blank=True)
	mo_tahun 				  = models.CharField(max_length=120, verbose_name="Tahun Kejuaraan", null=True, blank=True)
	mo_tingkatan			  = models.CharField(choices=tingkat_kejuaraan, max_length=120, verbose_name="Tingkat Kejuaraan", null=True, blank=True)
	mo_pelaksana			  = models.CharField(max_length=120, verbose_name="Dilaksanakan Oleh", null=True, blank=True)
	mo_kejuaraan			  = models.TextField(max_length=300, verbose_name="Kejuaraan", null=True, blank=True)
	mo_juara 				  = models.CharField(choices=juara, max_length=120, verbose_name="Juara", null=True, blank=True)