from django import forms
from role_guru.models import *
from monitoring.models import *
from sekolah.models import *
from crum import get_current_user

class page_guru_profil_forms(forms.ModelForm):
	class Meta:
		model = Gu_Profil_Guru
		fields = [
			"guru_nama",
			"guru_nip",
			"guru_nuptk",
			"guru_tempat_tanggal_lahir",
			"guru_jabatan",
			"guru_pangkat_golongan",
			"guru_mata_pelajaran_wajib",
			"guru_mata_pelajaran_jurusan",
		]
		exclude = ('guru_profil_uuid',)
		widgets = {
			"guru_nama": forms.TextInput(attrs={'class':'form-control'}),
			"guru_nip": forms.TextInput(attrs={'class':'form-control'}),
			"guru_nuptk": forms.TextInput(attrs={'class':'form-control'}),
			"guru_tempat_tanggal_lahir": forms.TextInput(attrs={'class':'form-control'}),
			"guru_jabatan": forms.TextInput(attrs={'class':'form-control'}),
			"guru_pangkat_golongan": forms.TextInput(attrs={'class':'form-control'}),
			"guru_mata_pelajaran_wajib": forms.Select(attrs={'class':'form-control'}),
			"guru_mata_pelajaran_jurusan": forms.Select(attrs={'class':'form-control'}),
		}



# FORM PENGETAHUAN
class page_guru_kompetensi_dasar_forms(forms.ModelForm):
	class Meta:
		model = Gu_Data_Kompetensi_Dasar
		fields = [
			"guru_nomor_kd",
			"guru_kompetensi_dasar",
			"guru_kompetensi_dasar_kelas",
			"guru_kompetensi_dasar_semester",

		]
		# exclude = ("mo_penilaian_pengetahuan_uuid")
		widgets = {
			"guru_nomor_kd": forms.TextInput(attrs={'class':'form-control'}),
			"guru_kompetensi_dasar": forms.TextInput(attrs={'class':'form-control'}),
			"guru_kompetensi_dasar_kelas": forms.Select(attrs={'class':'form-control'}),
			"guru_kompetensi_dasar_semester": forms.Select(attrs={'class':'form-control'}),
		}
class page_guru_input_kompetensi_dasar_wajib_forms(forms.ModelForm):
	class Meta:
		model = Gu_Data_Kompetensi_Dasar
		fields = [
			"guru_nomor_kd",
			"guru_kompetensi_dasar",
			"guru_kompetensi_dasar_kelas",
			"guru_kompetensi_dasar_semester",
			"guru_kompetensi_dasar_mata_pelajaran_wajib",
			"guru_kompetensi_dasar_mata_pelajaran_jurusan",

		]
		# exclude = ("mo_penilaian_pengetahuan_uuid")
		widgets = {
			"guru_nomor_kd": forms.TextInput(attrs={'class':'form-control'}),
			"guru_kompetensi_dasar": forms.TextInput(attrs={'class':'form-control'}),
			"guru_kompetensi_dasar_kelas": forms.Select(attrs={'class':'form-control'}),
			"guru_kompetensi_dasar_semester": forms.Select(attrs={'class':'form-control'}),
			"guru_kompetensi_dasar_mata_pelajaran_wajib": forms.Select(attrs={'class':'form-control'}),
			"guru_kompetensi_dasar_mata_pelajaran_jurusan": forms.Select(attrs={'class':'form-control'}),
		}
		def __init__(self, *args, **kwargs):
			super(page_guru_input_kompetensi_dasar_wajib_forms, self).__init__(*args, **kwargs)
			# murid = Akun.objects.filter(is_murid=True)
			guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
class page_guru_input_kompetensi_dasar_jurusan_forms(forms.ModelForm):
	class Meta:
		model = Gu_Data_Kompetensi_Dasar
		fields = [
			"guru_nomor_kd",
			"guru_kompetensi_dasar",
			"guru_kompetensi_dasar_kelas",
			"guru_kompetensi_dasar_semester",
			"guru_kompetensi_dasar_mata_pelajaran_wajib",
			"guru_kompetensi_dasar_mata_pelajaran_jurusan",

		]
		# exclude = ("mo_penilaian_pengetahuan_uuid")
		widgets = {
			"guru_nomor_kd": forms.TextInput(attrs={'class':'form-control'}),
			"guru_kompetensi_dasar": forms.TextInput(attrs={'class':'form-control'}),
			"guru_kompetensi_dasar_kelas": forms.Select(attrs={'class':'form-control'}),
			"guru_kompetensi_dasar_semester": forms.Select(attrs={'class':'form-control'}),
			"guru_kompetensi_dasar_mata_pelajaran_wajib": forms.Select(attrs={'class':'form-control'}),
			"guru_kompetensi_dasar_mata_pelajaran_jurusan": forms.Select(attrs={'class':'form-control'}),
		}
		def __init__(self, *args, **kwargs):
			super(page_guru_input_kompetensi_dasar_jurusan_forms, self).__init__(*args, **kwargs)
			# murid = Akun.objects.filter(is_murid=True)
			guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())



# FORM PENGETAHUAN
class page_guru_nilai_pengetahuan_forms(forms.ModelForm):
	class Meta:
		model = Mo_Penilaian_Pengetahuan
		fields = [
			"mo_siswa",
			"mo_kelas",
			"mo_tahun_ajaran",
			"mo_semester",
			"mo_kompetensi_dasar",
			"mo_penilaian_ke",
			"mo_nilai_P1_TGS",
			"mo_nilai_P2_TLS",
			"mo_nilai_P3_TLS",
		]
		# exclude = ("mo_penilaian_pengetahuan_uuid")
		widgets = {
			"mo_siswa": forms.Select(attrs={'class':'form-control'}),
			"mo_kelas": forms.Select(attrs={'class':'form-control'}),
			"mo_tahun_ajaran": forms.Select(attrs={'class':'form-control'}),
			"mo_semester": forms.Select(attrs={'class':'form-control'}),
			"mo_kompetensi_dasar": forms.Select(attrs={'class':'form-control'}),
			"mo_penilaian_ke": forms.Select(attrs={'class':'form-control'}),
			"mo_nilai_P1_TGS": forms.NumberInput(attrs={'class':'form-control'}),
			"mo_nilai_P2_TLS": forms.NumberInput(attrs={'class':'form-control'}),
			"mo_nilai_P3_TLS": forms.NumberInput(attrs={'class':'form-control'}),
		}
class page_guru_input_nilai_pengetahuan_wajib_forms(forms.ModelForm):
	class Meta:
		model = Mo_Penilaian_Pengetahuan
		fields = [
			"mo_siswa",
			"mo_kelas",
			"mo_tahun_ajaran",
			"mo_semester",
			"mo_kompetensi_dasar",
			"mo_mata_pelajaran_wajib",
			"mo_mata_pelajaran_jurusan",
			"mo_penilaian_ke",
			"mo_nilai_P1_TGS",
			"mo_nilai_P2_TLS",
			"mo_nilai_P3_TLS",
		]
		# exclude = ("mo_penilaian_pengetahuan_uuid")
		widgets = {
			"mo_siswa": forms.Select(attrs={'class':'form-control'}),
			"mo_kelas": forms.Select(attrs={'class':'form-control'}),
			"mo_tahun_ajaran": forms.Select(attrs={'class':'form-control'}),
			"mo_semester": forms.Select(attrs={'class':'form-control'}),
			"mo_kompetensi_dasar": forms.Select(attrs={'class':'form-control'}),
			"mo_mata_pelajaran_wajib": forms.Select(attrs={'class':'form-control'}),
			"mo_mata_pelajaran_jurusan": forms.Select(attrs={'class':'form-control'}),
			"mo_penilaian_ke": forms.Select(attrs={'class':'form-control'}),
			"mo_nilai_P1_TGS": forms.NumberInput(attrs={'class':'form-control'}),
			"mo_nilai_P2_TLS": forms.NumberInput(attrs={'class':'form-control'}),
			"mo_nilai_P3_TLS": forms.NumberInput(attrs={'class':'form-control'}),
		}
	def __init__(self, *args, **kwargs):
		super(page_guru_input_nilai_pengetahuan_wajib_forms, self).__init__(*args, **kwargs)
		# murid = Akun.objects.filter(is_murid=True)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		self.fields['mo_kompetensi_dasar'].queryset = Gu_Data_Kompetensi_Dasar.objects.filter(guru_kompetensi_dasar_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib)
class page_guru_input_nilai_pengetahuan_jurusan_forms(forms.ModelForm):
	class Meta:
		model = Mo_Penilaian_Pengetahuan
		fields = [
			"mo_siswa",
			"mo_kelas",
			"mo_tahun_ajaran",
			"mo_semester",
			"mo_kompetensi_dasar",
			"mo_mata_pelajaran_wajib",
			"mo_mata_pelajaran_jurusan",
			"mo_penilaian_ke",
			"mo_nilai_P1_TGS",
			"mo_nilai_P2_TLS",
			"mo_nilai_P3_TLS",
		]
		# exclude = ("mo_penilaian_pengetahuan_uuid")
		widgets = {
			"mo_siswa": forms.Select(attrs={'class':'form-control'}),
			"mo_kelas": forms.Select(attrs={'class':'form-control'}),
			"mo_tahun_ajaran": forms.Select(attrs={'class':'form-control'}),
			"mo_semester": forms.Select(attrs={'class':'form-control'}),
			"mo_kompetensi_dasar": forms.Select(attrs={'class':'form-control'}),
			"mo_mata_pelajaran_wajib": forms.Select(attrs={'class':'form-control'}),
			"mo_mata_pelajaran_jurusan": forms.Select(attrs={'class':'form-control'}),
			"mo_penilaian_ke": forms.Select(attrs={'class':'form-control'}),
			"mo_nilai_P1_TGS": forms.NumberInput(attrs={'class':'form-control'}),
			"mo_nilai_P2_TLS": forms.NumberInput(attrs={'class':'form-control'}),
			"mo_nilai_P3_TLS": forms.NumberInput(attrs={'class':'form-control'}),
		}
	def __init__(self, *args, **kwargs):
		super(page_guru_input_nilai_pengetahuan_jurusan_forms, self).__init__(*args, **kwargs)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		self.fields['mo_kompetensi_dasar'].queryset = Gu_Data_Kompetensi_Dasar.objects.filter(guru_kompetensi_dasar_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan)


# FORM KETERAMPILAN
class page_guru_nilai_keterampilan_forms(forms.ModelForm):
	class Meta:
		model = Mo_Penilaian_Keterampilan
		fields = [
			"mo_siswa",
			"mo_kelas",
			"mo_tahun_ajaran",
			"mo_semester",
			"mo_kompetensi_dasar",
			"mo_penilaian_ke",
			"mo_praktek",
			"mo_produk",
			"mo_proyek",
			"mo_portofolio",
		]
		# exclude = ("mo_penilaian_pengetahuan_uuid")
		widgets = {
			"mo_siswa": forms.Select(attrs={'class':'form-control'}),
			"mo_kelas": forms.Select(attrs={'class':'form-control'}),
			"mo_tahun_ajaran": forms.Select(attrs={'class':'form-control'}),
			"mo_semester": forms.Select(attrs={'class':'form-control'}),
			"mo_kompetensi_dasar": forms.Select(attrs={'class':'form-control'}),
			"mo_penilaian_ke": forms.Select(attrs={'class':'form-control'}),
			"mo_praktek": forms.NumberInput(attrs={'class':'form-control'}),
			"mo_produk": forms.NumberInput(attrs={'class':'form-control'}),
			"mo_proyek": forms.NumberInput(attrs={'class':'form-control'}),
			"mo_portofolio": forms.NumberInput(attrs={'class':'form-control'}),
		}
class page_guru_input_nilai_keterampilan_wajib_forms(forms.ModelForm):
	class Meta:
		model = Mo_Penilaian_Keterampilan
		fields = [
			"mo_siswa",
			"mo_kelas",
			"mo_tahun_ajaran",
			"mo_semester",
			"mo_kompetensi_dasar",
			"mo_mata_pelajaran_wajib",
			"mo_mata_pelajaran_jurusan",
			"mo_penilaian_ke",
			"mo_praktek",
			"mo_produk",
			"mo_proyek",
			"mo_portofolio",
		]
		# exclude = ("mo_penilaian_pengetahuan_uuid")
		widgets = {
			"mo_siswa": forms.Select(attrs={'class':'form-control'}),
			"mo_kelas": forms.Select(attrs={'class':'form-control'}),
			"mo_tahun_ajaran": forms.Select(attrs={'class':'form-control'}),
			"mo_semester": forms.Select(attrs={'class':'form-control'}),
			"mo_kompetensi_dasar": forms.Select(attrs={'class':'form-control'}),
			"mo_mata_pelajaran_wajib": forms.Select(attrs={'class':'form-control'}),
			"mo_mata_pelajaran_jurusan": forms.Select(attrs={'class':'form-control'}),
			"mo_penilaian_ke": forms.Select(attrs={'class':'form-control'}),
			"mo_praktek": forms.NumberInput(attrs={'class':'form-control'}),
			"mo_produk": forms.NumberInput(attrs={'class':'form-control'}),
			"mo_proyek": forms.NumberInput(attrs={'class':'form-control'}),
			"mo_portofolio": forms.NumberInput(attrs={'class':'form-control'}),
		}
	def __init__(self, *args, **kwargs):
		super(page_guru_input_nilai_keterampilan_wajib_forms, self).__init__(*args, **kwargs)
		# murid = Akun.objects.filter(is_murid=True)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		self.fields['mo_kompetensi_dasar'].queryset = Gu_Data_Kompetensi_Dasar.objects.filter(guru_kompetensi_dasar_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib)
class page_guru_input_nilai_keterampilan_jurusan_forms(forms.ModelForm):
	class Meta:
		model = Mo_Penilaian_Keterampilan
		fields = [
			"mo_siswa",
			"mo_kelas",
			"mo_tahun_ajaran",
			"mo_semester",
			"mo_kompetensi_dasar",
			"mo_mata_pelajaran_wajib",
			"mo_mata_pelajaran_jurusan",
			"mo_penilaian_ke",
			"mo_praktek",
			"mo_produk",
			"mo_proyek",
			"mo_portofolio",
		]
		# exclude = ("mo_penilaian_pengetahuan_uuid")
		widgets = {
			"mo_siswa": forms.Select(attrs={'class':'form-control'}),
			"mo_kelas": forms.Select(attrs={'class':'form-control'}),
			"mo_tahun_ajaran": forms.Select(attrs={'class':'form-control'}),
			"mo_semester": forms.Select(attrs={'class':'form-control'}),
			"mo_kompetensi_dasar": forms.Select(attrs={'class':'form-control'}),
			"mo_mata_pelajaran_wajib": forms.Select(attrs={'class':'form-control'}),
			"mo_mata_pelajaran_jurusan": forms.Select(attrs={'class':'form-control'}),
			"mo_penilaian_ke": forms.Select(attrs={'class':'form-control'}),
			"mo_praktek": forms.NumberInput(attrs={'class':'form-control'}),
			"mo_produk": forms.NumberInput(attrs={'class':'form-control'}),
			"mo_proyek": forms.NumberInput(attrs={'class':'form-control'}),
			"mo_portofolio": forms.NumberInput(attrs={'class':'form-control'}),
		}
	def __init__(self, *args, **kwargs):
		super(page_guru_input_nilai_keterampilan_jurusan_forms, self).__init__(*args, **kwargs)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		self.fields['mo_kompetensi_dasar'].queryset = Gu_Data_Kompetensi_Dasar.objects.filter(guru_kompetensi_dasar_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan)


# FORM SIKAP SOSIAL
class page_guru_nilai_sikap_sosial_forms(forms.ModelForm):
	class Meta:
		model = Mo_Sikap_Sosial
		fields = [
			"mo_siswa",
			"mo_kelas",
			"mo_tahun_ajaran",
			"mo_semester",
			"mo_kompetensi_dasar",
			"mo_penilaian_ke",
			"mo_nilai",
		]
		# exclude = ("mo_penilaian_pengetahuan_uuid")
		widgets = {
			"mo_siswa": forms.Select(attrs={'class':'form-control'}),
			"mo_kelas": forms.Select(attrs={'class':'form-control'}),
			"mo_tahun_ajaran": forms.Select(attrs={'class':'form-control'}),
			"mo_semester": forms.Select(attrs={'class':'form-control'}),
			"mo_kompetensi_dasar": forms.Select(attrs={'class':'form-control'}),
			"mo_penilaian_ke": forms.Select(attrs={'class':'form-control'}),
			"mo_nilai": forms.Select(attrs={'class':'form-control'}),
		}
class page_guru_input_nilai_sikap_sosial_wajib_forms(forms.ModelForm):
	class Meta:
		model = Mo_Sikap_Sosial
		fields = [
			"mo_siswa",
			"mo_kelas",
			"mo_tahun_ajaran",
			"mo_semester",
			"mo_kompetensi_dasar",
			"mo_mata_pelajaran_wajib",
			"mo_mata_pelajaran_jurusan",
			"mo_penilaian_ke",
			"mo_nilai",
		]
		# exclude = ("mo_penilaian_pengetahuan_uuid")
		widgets = {
			"mo_siswa": forms.Select(attrs={'class':'form-control'}),
			"mo_kelas": forms.Select(attrs={'class':'form-control'}),
			"mo_tahun_ajaran": forms.Select(attrs={'class':'form-control'}),
			"mo_semester": forms.Select(attrs={'class':'form-control'}),
			"mo_kompetensi_dasar": forms.Select(attrs={'class':'form-control'}),
			"mo_mata_pelajaran_wajib": forms.Select(attrs={'class':'form-control'}),
			"mo_mata_pelajaran_jurusan": forms.Select(attrs={'class':'form-control'}),
			"mo_penilaian_ke": forms.Select(attrs={'class':'form-control'}),
			"mo_nilai": forms.Select(attrs={'class':'form-control'}),
		}
	def __init__(self, *args, **kwargs):
		super(page_guru_input_nilai_sikap_sosial_wajib_forms, self).__init__(*args, **kwargs)
		# murid = Akun.objects.filter(is_murid=True)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		self.fields['mo_kompetensi_dasar'].queryset = Gu_Data_Kompetensi_Dasar.objects.filter(guru_kompetensi_dasar_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib)
class page_guru_input_nilai_sikap_sosial_jurusan_forms(forms.ModelForm):
	class Meta:
		model = Mo_Sikap_Sosial
		fields = [
			"mo_siswa",
			"mo_kelas",
			"mo_tahun_ajaran",
			"mo_semester",
			"mo_kompetensi_dasar",
			"mo_mata_pelajaran_wajib",
			"mo_mata_pelajaran_jurusan",
			"mo_penilaian_ke",
			"mo_nilai",
		]
		# exclude = ("mo_penilaian_pengetahuan_uuid")
		widgets = {
			"mo_siswa": forms.Select(attrs={'class':'form-control'}),
			"mo_kelas": forms.Select(attrs={'class':'form-control'}),
			"mo_tahun_ajaran": forms.Select(attrs={'class':'form-control'}),
			"mo_semester": forms.Select(attrs={'class':'form-control'}),
			"mo_kompetensi_dasar": forms.Select(attrs={'class':'form-control'}),
			"mo_mata_pelajaran_wajib": forms.Select(attrs={'class':'form-control'}),
			"mo_mata_pelajaran_jurusan": forms.Select(attrs={'class':'form-control'}),
			"mo_penilaian_ke": forms.Select(attrs={'class':'form-control'}),
			"mo_nilai": forms.Select(attrs={'class':'form-control'}),
		}
	def __init__(self, *args, **kwargs):
		super(page_guru_input_nilai_sikap_sosial_jurusan_forms, self).__init__(*args, **kwargs)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		self.fields['mo_kompetensi_dasar'].queryset = Gu_Data_Kompetensi_Dasar.objects.filter(guru_kompetensi_dasar_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan)


# FORM SIKAP SOSIAL
class page_guru_nilai_sikap_spiritual_forms(forms.ModelForm):
	class Meta:
		model = Mo_Sikap_Sosial
		fields = [
			"mo_siswa",
			"mo_kelas",
			"mo_tahun_ajaran",
			"mo_semester",
			"mo_kompetensi_dasar",
			"mo_penilaian_ke",
			"mo_nilai",
		]
		# exclude = ("mo_penilaian_pengetahuan_uuid")
		widgets = {
			"mo_siswa": forms.Select(attrs={'class':'form-control'}),
			"mo_kelas": forms.Select(attrs={'class':'form-control'}),
			"mo_tahun_ajaran": forms.Select(attrs={'class':'form-control'}),
			"mo_semester": forms.Select(attrs={'class':'form-control'}),
			"mo_kompetensi_dasar": forms.Select(attrs={'class':'form-control'}),
			"mo_penilaian_ke": forms.Select(attrs={'class':'form-control'}),
			"mo_nilai": forms.Select(attrs={'class':'form-control'}),
		}
class page_guru_input_nilai_sikap_spiritual_wajib_forms(forms.ModelForm):
	class Meta:
		model = Mo_Sikap_Sosial
		fields = [
			"mo_siswa",
			"mo_kelas",
			"mo_tahun_ajaran",
			"mo_semester",
			"mo_kompetensi_dasar",
			"mo_mata_pelajaran_wajib",
			"mo_mata_pelajaran_jurusan",
			"mo_penilaian_ke",
			"mo_nilai",
		]
		# exclude = ("mo_penilaian_pengetahuan_uuid")
		widgets = {
			"mo_siswa": forms.Select(attrs={'class':'form-control'}),
			"mo_kelas": forms.Select(attrs={'class':'form-control'}),
			"mo_tahun_ajaran": forms.Select(attrs={'class':'form-control'}),
			"mo_semester": forms.Select(attrs={'class':'form-control'}),
			"mo_kompetensi_dasar": forms.Select(attrs={'class':'form-control'}),
			"mo_mata_pelajaran_wajib": forms.Select(attrs={'class':'form-control'}),
			"mo_mata_pelajaran_jurusan": forms.Select(attrs={'class':'form-control'}),
			"mo_penilaian_ke": forms.Select(attrs={'class':'form-control'}),
			"mo_nilai": forms.Select(attrs={'class':'form-control'}),
		}
	def __init__(self, *args, **kwargs):
		super(page_guru_input_nilai_sikap_spiritual_wajib_forms, self).__init__(*args, **kwargs)
		# murid = Akun.objects.filter(is_murid=True)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		self.fields['mo_kompetensi_dasar'].queryset = Gu_Data_Kompetensi_Dasar.objects.filter(guru_kompetensi_dasar_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib)
class page_guru_input_nilai_sikap_spiritual_jurusan_forms(forms.ModelForm):
	class Meta:
		model = Mo_Sikap_Sosial
		fields = [
			"mo_siswa",
			"mo_kelas",
			"mo_tahun_ajaran",
			"mo_semester",
			"mo_kompetensi_dasar",
			"mo_mata_pelajaran_wajib",
			"mo_mata_pelajaran_jurusan",
			"mo_penilaian_ke",
			"mo_nilai",
		]
		# exclude = ("mo_penilaian_pengetahuan_uuid")
		widgets = {
			"mo_siswa": forms.Select(attrs={'class':'form-control'}),
			"mo_kelas": forms.Select(attrs={'class':'form-control'}),
			"mo_tahun_ajaran": forms.Select(attrs={'class':'form-control'}),
			"mo_semester": forms.Select(attrs={'class':'form-control'}),
			"mo_kompetensi_dasar": forms.Select(attrs={'class':'form-control'}),
			"mo_mata_pelajaran_wajib": forms.Select(attrs={'class':'form-control'}),
			"mo_mata_pelajaran_jurusan": forms.Select(attrs={'class':'form-control'}),
			"mo_penilaian_ke": forms.Select(attrs={'class':'form-control'}),
			"mo_nilai": forms.Select(attrs={'class':'form-control'}),
		}
	def __init__(self, *args, **kwargs):
		super(page_guru_input_nilai_sikap_spiritual_jurusan_forms, self).__init__(*args, **kwargs)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		self.fields['mo_kompetensi_dasar'].queryset = Gu_Data_Kompetensi_Dasar.objects.filter(guru_kompetensi_dasar_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan)

class page_guru_kkm_forms(forms.ModelForm):
	class Meta: 
		model = Mo_Penilaian_Ulangan_KKM
		fields = [
			"mo_jenjang_kelas",
			"mo_kkm",
		]
		att = {
			'class': 'form-control',
		}
		widgets = {
			'mo_jenjang_kelas': forms.Select(attrs=att),
			'mo_kkm': forms.NumberInput(attrs=att),
		}
	def __init__(self, *args, **kwargs):
		super(page_guru_kkm_forms, self).__init__(*args, **kwargs)

class page_guru_kkm_create_forms(forms.ModelForm):
	class Meta: 
		model = Mo_Penilaian_Ulangan_KKM
		fields = [
			"mo_mata_pelajaran_wajib",
			"mo_mata_pelajaran_jurusan",
			"mo_jenjang_kelas",
			"mo_kkm",
		]
		att = {
			'class': 'form-control',
		}
		widgets = {
			'mo_jenjang_mata_pelajaran_wajib': forms.Select(attrs=att),
			'mo_jenjang_mata_pelajaran_jurusan': forms.Select(attrs=att),
			'mo_jenjang_kelas': forms.Select(attrs=att),
			'mo_kkm': forms.NumberInput(attrs=att),
		}
	def __init__(self, *args, **kwargs):
		super(page_guru_kkm_create_forms, self).__init__(*args, **kwargs)



class page_guru_catatan_forms(forms.ModelForm):
	class Meta: 
		model = Gu_Catatan
		fields = [
			"guru_catatan_status",
			"guru_catatan_siswa",
			"guru_catatan",
		]
		att = {
			'class': 'form-control',
		}
		widgets = {
			"guru_catatan_status": forms.Select(attrs=att),
			"guru_catatan_siswa": forms.Select(attrs=att),
			"guru_catatan": forms.Textarea(attrs=att),
		}
	def __init__(self, *args, **kwargs):
		super(page_guru_catatan_forms, self).__init__(*args, **kwargs)

class page_guru_catatan_create_forms(forms.ModelForm):
	class Meta: 
		model = Gu_Catatan
		fields = [
			"guru_catatan_status",
			"guru_catatan_siswa",
			"guru_catatan_mata_pelajaran_wajib",
			"guru_catatan_mata_pelajaran_jurusan",
			"guru_catatan",
		]
		att = {
			'class': 'form-control',
		}
		widgets = {
			"guru_catatan_status": forms.Select(attrs=att),
			"guru_catatan_siswa": forms.Select(attrs=att),
			'guru_catatan_mata_pelajaran_wajib': forms.Select(attrs=att),
			'guru_catatan_mata_pelajaran_jurusan': forms.Select(attrs=att),
			'guru_catatan': forms.Textarea(attrs=att),
		}
	def __init__(self, *args, **kwargs):
		super(page_guru_catatan_create_forms, self).__init__(*args, **kwargs)





# ULANGAN
class page_guru_nilai_ulangan_wajib_forms(forms.ModelForm):
	class Meta:
		model = Mo_Penilaian_Ulangan
		fields = [
			"mo_status",
			"mo_siswa",
			"mo_kelas",
			"mo_tahun_ajaran",
			"mo_semester",
			"mo_kompetensi_dasar",
			"mo_ulangan_ke",
			"mo_kkm",
			"mo_nilai",
			"mo_ketuntasan",
		]
		# exclude = ("mo_penilaian_ulangan_uuid")
		widgets = {
			"mo_status": forms.Select(attrs={'class': 'form-control'}),
			"mo_siswa": forms.Select(attrs={'class':'form-control'}),
			"mo_kelas": forms.Select(attrs={'class':'form-control'}),
			"mo_tahun_ajaran": forms.Select(attrs={'class':'form-control'}),
			"mo_semester": forms.Select(attrs={'class':'form-control'}),
			"mo_kompetensi_dasar": forms.Select(attrs={'class':'form-control'}),
			"mo_ulangan_ke": forms.Select(attrs={'class':'form-control'}),
			"mo_kkm": forms.Select(attrs={'class':'form-control'}),
			"mo_nilai": forms.NumberInput(attrs={'class':'form-control'}),
			"mo_ketuntasan": forms.Select(attrs={'class':'form-control'}),
		}
	def __init__(self, *args, **kwargs):
		super(page_guru_nilai_ulangan_wajib_forms, self).__init__(*args, **kwargs)
		# murid = Akun.objects.filter(is_murid=True)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		self.fields['mo_kompetensi_dasar'].queryset = Gu_Data_Kompetensi_Dasar.objects.filter(guru_kompetensi_dasar_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib)
		self.fields['mo_kkm'].queryset = Mo_Penilaian_Ulangan_KKM.objects.filter(mo_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib)

class page_guru_nilai_ulangan_jurusan_forms(forms.ModelForm):
	class Meta:
		model = Mo_Penilaian_Ulangan
		fields = [
			"mo_status",
			"mo_siswa",
			"mo_kelas",
			"mo_tahun_ajaran",
			"mo_semester",
			"mo_kompetensi_dasar",
			"mo_ulangan_ke",
			"mo_kkm",
			"mo_nilai",
			"mo_ketuntasan",
		]
		# exclude = ("mo_penilaian_ulangan_uuid")
		widgets = {
			"mo_status": forms.Select(attrs={'class': 'form-control'}),
			"mo_siswa": forms.Select(attrs={'class':'form-control'}),
			"mo_kelas": forms.Select(attrs={'class':'form-control'}),
			"mo_tahun_ajaran": forms.Select(attrs={'class':'form-control'}),
			"mo_semester": forms.Select(attrs={'class':'form-control'}),
			"mo_kompetensi_dasar": forms.Select(attrs={'class':'form-control'}),
			"mo_ulangan_ke": forms.Select(attrs={'class':'form-control'}),
			"mo_kkm": forms.Select(attrs={'class':'form-control'}),
			"mo_nilai": forms.NumberInput(attrs={'class':'form-control'}),
			"mo_ketuntasan": forms.Select(attrs={'class':'form-control'}),
		}
	def __init__(self, *args, **kwargs):
		super(page_guru_nilai_ulangan_jurusan_forms, self).__init__(*args, **kwargs)
		# murid = Akun.objects.filter(is_murid=True)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		self.fields['mo_kompetensi_dasar'].queryset = Gu_Data_Kompetensi_Dasar.objects.filter(guru_kompetensi_dasar_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan)
		self.fields['mo_kkm'].queryset = Mo_Penilaian_Ulangan_KKM.objects.filter(mo_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan)

class page_guru_input_nilai_ulangan_wajib_forms(forms.ModelForm):
	class Meta:
		model = Mo_Penilaian_Ulangan
		fields = [
			"mo_status",
			"mo_siswa",
			"mo_kelas",
			"mo_tahun_ajaran",
			"mo_semester",
			"mo_kompetensi_dasar",
			"mo_mata_pelajaran_wajib",
			"mo_mata_pelajaran_jurusan",
			"mo_ulangan_ke",
			"mo_kkm",
			"mo_nilai",
			"mo_ketuntasan",
		]
		# exclude = ("mo_penilaian_ulangan_uuid")
		widgets = {
			"mo_status": forms.Select(attrs={'class': 'form-control'}),
			"mo_siswa": forms.Select(attrs={'class':'form-control'}),
			"mo_kelas": forms.Select(attrs={'class':'form-control'}),
			"mo_tahun_ajaran": forms.Select(attrs={'class':'form-control'}),
			"mo_semester": forms.Select(attrs={'class':'form-control'}),
			"mo_kompetensi_dasar": forms.Select(attrs={'class':'form-control'}),
			"mo_mata_pelajaran_wajib": forms.Select(attrs={'class':'form-control'}),
			"mo_mata_pelajaran_jurusan": forms.Select(attrs={'class':'form-control'}),
			"mo_ulangan_ke": forms.Select(attrs={'class':'form-control'}),
			"mo_kkm": forms.Select(attrs={'class':'form-control'}),
			"mo_nilai": forms.NumberInput(attrs={'class':'form-control'}),
			"mo_ketuntasan": forms.Select(attrs={'class':'form-control'}),
		}
	def __init__(self, *args, **kwargs):
		super(page_guru_input_nilai_ulangan_wajib_forms, self).__init__(*args, **kwargs)
		# murid = Akun.objects.filter(is_murid=True)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		self.fields['mo_kompetensi_dasar'].queryset = Gu_Data_Kompetensi_Dasar.objects.filter(guru_kompetensi_dasar_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib)
		self.fields['mo_kkm'].queryset = Mo_Penilaian_Ulangan_KKM.objects.filter(mo_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib)

class page_guru_input_nilai_ulangan_jurusan_forms(forms.ModelForm):
	class Meta:
		model = Mo_Penilaian_Ulangan
		fields = [
			"mo_status",
			"mo_siswa",
			"mo_kelas",
			"mo_tahun_ajaran",
			"mo_semester",
			"mo_kompetensi_dasar",
			"mo_mata_pelajaran_wajib",
			"mo_mata_pelajaran_jurusan",
			"mo_ulangan_ke",
			"mo_kkm",
			"mo_nilai",
			"mo_ketuntasan",
		]
		# exclude = ("mo_penilaian_ulangan_uuid")
		widgets = {
			"mo_status": forms.Select(attrs={'class': 'form-control'}),
			"mo_siswa": forms.Select(attrs={'class':'form-control'}),
			"mo_kelas": forms.Select(attrs={'class':'form-control'}),
			"mo_tahun_ajaran": forms.Select(attrs={'class':'form-control'}),
			"mo_semester": forms.Select(attrs={'class':'form-control'}),
			"mo_kompetensi_dasar": forms.Select(attrs={'class':'form-control'}),
			"mo_mata_pelajaran_wajib": forms.Select(attrs={'class':'form-control'}),
			"mo_mata_pelajaran_jurusan": forms.Select(attrs={'class':'form-control'}),
			"mo_ulangan_ke": forms.Select(attrs={'class':'form-control'}),
			"mo_kkm": forms.Select(attrs={'class':'form-control'}),
			"mo_nilai": forms.NumberInput(attrs={'class':'form-control'}),
			"mo_ketuntasan": forms.Select(attrs={'class':'form-control'}),
		}
	def __init__(self, *args, **kwargs):
		super(page_guru_input_nilai_ulangan_jurusan_forms, self).__init__(*args, **kwargs)
		# murid = Akun.objects.filter(is_murid=True)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		self.fields['mo_kompetensi_dasar'].queryset = Gu_Data_Kompetensi_Dasar.objects.filter(guru_kompetensi_dasar_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan)
		self.fields['mo_kkm'].queryset = Mo_Penilaian_Ulangan_KKM.objects.filter(mo_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan)




class page_guru_nilai_uts_wajib_forms(forms.ModelForm):
	class Meta:
		model = Mo_Penilaian_UTS
		fields = [
			"mo_status",
			"mo_siswa",
			"mo_kelas",
			"mo_tahun_ajaran",
			"mo_semester",
			"mo_kkm",
			"mo_nilai",
			"mo_ketuntasan",
		]
		# exclude = ("mo_penilaian_uts_uuid")
		widgets = {
			"mo_status": forms.Select(attrs={'class': 'form-control'}),
			"mo_siswa": forms.Select(attrs={'class':'form-control'}),
			"mo_kelas": forms.Select(attrs={'class':'form-control'}),
			"mo_tahun_ajaran": forms.Select(attrs={'class':'form-control'}),
			"mo_semester": forms.Select(attrs={'class':'form-control'}),
			"mo_kkm": forms.Select(attrs={'class':'form-control'}),
			"mo_nilai": forms.NumberInput(attrs={'class':'form-control'}),
			"mo_ketuntasan": forms.Select(attrs={'class':'form-control'}),
		}
	def __init__(self, *args, **kwargs):
		super(page_guru_nilai_uts_wajib_forms, self).__init__(*args, **kwargs)
		# murid = Akun.objects.filter(is_murid=True)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		self.fields['mo_kkm'].queryset = Mo_Penilaian_Ulangan_KKM.objects.filter(mo_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib)

class page_guru_nilai_uts_jurusan_forms(forms.ModelForm):
	class Meta:
		model = Mo_Penilaian_UTS
		fields = [
			"mo_status",
			"mo_siswa",
			"mo_kelas",
			"mo_tahun_ajaran",
			"mo_semester",
			"mo_kkm",
			"mo_nilai",
			"mo_ketuntasan",
		]
		# exclude = ("mo_penilaian_uts_uuid")
		widgets = {
			"mo_status": forms.Select(attrs={'class': 'form-control'}),
			"mo_siswa": forms.Select(attrs={'class':'form-control'}),
			"mo_kelas": forms.Select(attrs={'class':'form-control'}),
			"mo_tahun_ajaran": forms.Select(attrs={'class':'form-control'}),
			"mo_semester": forms.Select(attrs={'class':'form-control'}),
			"mo_kkm": forms.Select(attrs={'class':'form-control'}),
			"mo_nilai": forms.NumberInput(attrs={'class':'form-control'}),
			"mo_ketuntasan": forms.Select(attrs={'class':'form-control'}),
		}
	def __init__(self, *args, **kwargs):
		super(page_guru_nilai_uts_jurusan_forms, self).__init__(*args, **kwargs)
		# murid = Akun.objects.filter(is_murid=True)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		self.fields['mo_kkm'].queryset = Mo_Penilaian_Ulangan_KKM.objects.filter(mo_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan)

class page_guru_input_nilai_uts_wajib_forms(forms.ModelForm):
	class Meta:
		model = Mo_Penilaian_UTS
		fields = [
			"mo_status",
			"mo_siswa",
			"mo_kelas",
			"mo_tahun_ajaran",
			"mo_semester",
			"mo_mata_pelajaran_wajib",
			"mo_mata_pelajaran_jurusan",
			"mo_kkm",
			"mo_nilai",
			"mo_ketuntasan",
		]
		# exclude = ("mo_penilaian_uts_uuid")
		widgets = {
			"mo_status": forms.Select(attrs={'class': 'form-control'}),
			"mo_siswa": forms.Select(attrs={'class':'form-control'}),
			"mo_kelas": forms.Select(attrs={'class':'form-control'}),
			"mo_tahun_ajaran": forms.Select(attrs={'class':'form-control'}),
			"mo_semester": forms.Select(attrs={'class':'form-control'}),
			"mo_mata_pelajaran_wajib": forms.Select(attrs={'class':'form-control'}),
			"mo_mata_pelajaran_jurusan": forms.Select(attrs={'class':'form-control'}),
			"mo_kkm": forms.Select(attrs={'class':'form-control'}),
			"mo_nilai": forms.NumberInput(attrs={'class':'form-control'}),
			"mo_ketuntasan": forms.Select(attrs={'class':'form-control'}),
		}
	def __init__(self, *args, **kwargs):
		super(page_guru_input_nilai_uts_wajib_forms, self).__init__(*args, **kwargs)
		# murid = Akun.objects.filter(is_murid=True)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		self.fields['mo_kkm'].queryset = Mo_Penilaian_Ulangan_KKM.objects.filter(mo_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib)

class page_guru_input_nilai_uts_jurusan_forms(forms.ModelForm):
	class Meta:
		model = Mo_Penilaian_UTS
		fields = [
			"mo_status",
			"mo_siswa",
			"mo_kelas",
			"mo_tahun_ajaran",
			"mo_semester",
			"mo_mata_pelajaran_wajib",
			"mo_mata_pelajaran_jurusan",
			"mo_kkm",
			"mo_nilai",
			"mo_ketuntasan",
		]
		# exclude = ("mo_penilaian_uts_uuid")
		widgets = {
			"mo_status": forms.Select(attrs={'class': 'form-control'}),
			"mo_siswa": forms.Select(attrs={'class':'form-control'}),
			"mo_kelas": forms.Select(attrs={'class':'form-control'}),
			"mo_tahun_ajaran": forms.Select(attrs={'class':'form-control'}),
			"mo_semester": forms.Select(attrs={'class':'form-control'}),
			"mo_mata_pelajaran_wajib": forms.Select(attrs={'class':'form-control'}),
			"mo_mata_pelajaran_jurusan": forms.Select(attrs={'class':'form-control'}),
			"mo_kkm": forms.Select(attrs={'class':'form-control'}),
			"mo_nilai": forms.NumberInput(attrs={'class':'form-control'}),
			"mo_ketuntasan": forms.Select(attrs={'class':'form-control'}),
		}
	def __init__(self, *args, **kwargs):
		super(page_guru_input_nilai_uts_jurusan_forms, self).__init__(*args, **kwargs)
		# murid = Akun.objects.filter(is_murid=True)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		self.fields['mo_kkm'].queryset = Mo_Penilaian_Ulangan_KKM.objects.filter(mo_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan)





# UAS
class page_guru_nilai_uas_wajib_forms(forms.ModelForm):
	class Meta:
		model = Mo_Penilaian_UAS
		fields = [
			"mo_status",
			"mo_siswa",
			"mo_kelas",
			"mo_tahun_ajaran",
			"mo_semester",
			"mo_kkm",
			"mo_nilai",
			"mo_ketuntasan",
		]
		# exclude = ("mo_penilaian_uas_uuid")
		widgets = {
			"mo_status": forms.Select(attrs={'class': 'form-control'}),
			"mo_siswa": forms.Select(attrs={'class':'form-control'}),
			"mo_kelas": forms.Select(attrs={'class':'form-control'}),
			"mo_tahun_ajaran": forms.Select(attrs={'class':'form-control'}),
			"mo_semester": forms.Select(attrs={'class':'form-control'}),
			"mo_kkm": forms.Select(attrs={'class':'form-control'}),
			"mo_nilai": forms.NumberInput(attrs={'class':'form-control'}),
			"mo_ketuntasan": forms.Select(attrs={'class':'form-control'}),
		}
	def __init__(self, *args, **kwargs):
		super(page_guru_nilai_uas_wajib_forms, self).__init__(*args, **kwargs)
		# murid = Akun.objects.filter(is_murid=True)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		self.fields['mo_kkm'].queryset = Mo_Penilaian_Ulangan_KKM.objects.filter(mo_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib)

class page_guru_nilai_uas_jurusan_forms(forms.ModelForm):
	class Meta:
		model = Mo_Penilaian_UAS
		fields = [
			"mo_status",
			"mo_siswa",
			"mo_kelas",
			"mo_tahun_ajaran",
			"mo_semester",
			"mo_kkm",
			"mo_nilai",
			"mo_ketuntasan",
		]
		# exclude = ("mo_penilaian_uas_uuid")
		widgets = {
			"mo_status": forms.Select(attrs={'class': 'form-control'}),
			"mo_siswa": forms.Select(attrs={'class':'form-control'}),
			"mo_kelas": forms.Select(attrs={'class':'form-control'}),
			"mo_tahun_ajaran": forms.Select(attrs={'class':'form-control'}),
			"mo_semester": forms.Select(attrs={'class':'form-control'}),
			"mo_kkm": forms.Select(attrs={'class':'form-control'}),
			"mo_nilai": forms.NumberInput(attrs={'class':'form-control'}),
			"mo_ketuntasan": forms.Select(attrs={'class':'form-control'}),
		}
	def __init__(self, *args, **kwargs):
		super(page_guru_nilai_uas_jurusan_forms, self).__init__(*args, **kwargs)
		# murid = Akun.objects.filter(is_murid=True)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		self.fields['mo_kkm'].queryset = Mo_Penilaian_Ulangan_KKM.objects.filter(mo_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan)

class page_guru_input_nilai_uas_wajib_forms(forms.ModelForm):
	class Meta:
		model = Mo_Penilaian_UAS
		fields = [
			"mo_status",
			"mo_siswa",
			"mo_kelas",
			"mo_tahun_ajaran",
			"mo_semester",
			"mo_mata_pelajaran_wajib",
			"mo_mata_pelajaran_jurusan",
			"mo_kkm",
			"mo_nilai",
			"mo_ketuntasan",
		]
		# exclude = ("mo_penilaian_uas_uuid")
		widgets = {
			"mo_status": forms.Select(attrs={'class': 'form-control'}),
			"mo_siswa": forms.Select(attrs={'class':'form-control'}),
			"mo_kelas": forms.Select(attrs={'class':'form-control'}),
			"mo_tahun_ajaran": forms.Select(attrs={'class':'form-control'}),
			"mo_semester": forms.Select(attrs={'class':'form-control'}),
			"mo_mata_pelajaran_wajib": forms.Select(attrs={'class':'form-control'}),
			"mo_mata_pelajaran_jurusan": forms.Select(attrs={'class':'form-control'}),
			"mo_kkm": forms.Select(attrs={'class':'form-control'}),
			"mo_nilai": forms.NumberInput(attrs={'class':'form-control'}),
			"mo_ketuntasan": forms.Select(attrs={'class':'form-control'}),
		}
	def __init__(self, *args, **kwargs):
		super(page_guru_input_nilai_uas_wajib_forms, self).__init__(*args, **kwargs)
		# murid = Akun.objects.filter(is_murid=True)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		self.fields['mo_kkm'].queryset = Mo_Penilaian_Ulangan_KKM.objects.filter(mo_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib)

class page_guru_input_nilai_uas_jurusan_forms(forms.ModelForm):
	class Meta:
		model = Mo_Penilaian_UAS
		fields = [
			"mo_status",
			"mo_siswa",
			"mo_kelas",
			"mo_tahun_ajaran",
			"mo_semester",
			"mo_mata_pelajaran_wajib",
			"mo_mata_pelajaran_jurusan",
			"mo_kkm",
			"mo_nilai",
			"mo_ketuntasan",
		]
		# exclude = ("mo_penilaian_uas_uuid")
		widgets = {
			"mo_status": forms.Select(attrs={'class': 'form-control'}),
			"mo_siswa": forms.Select(attrs={'class':'form-control'}),
			"mo_kelas": forms.Select(attrs={'class':'form-control'}),
			"mo_tahun_ajaran": forms.Select(attrs={'class':'form-control'}),
			"mo_semester": forms.Select(attrs={'class':'form-control'}),
			"mo_mata_pelajaran_wajib": forms.Select(attrs={'class':'form-control'}),
			"mo_mata_pelajaran_jurusan": forms.Select(attrs={'class':'form-control'}),
			"mo_kkm": forms.Select(attrs={'class':'form-control'}),
			"mo_nilai": forms.NumberInput(attrs={'class':'form-control'}),
			"mo_ketuntasan": forms.Select(attrs={'class':'form-control'}),
		}
	def __init__(self, *args, **kwargs):
		super(page_guru_input_nilai_uas_jurusan_forms, self).__init__(*args, **kwargs)
		# murid = Akun.objects.filter(is_murid=True)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		self.fields['mo_kkm'].queryset = Mo_Penilaian_Ulangan_KKM.objects.filter(mo_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan)

