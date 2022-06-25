# FILTERING DISINI
from monitoring.models import *
from role_guru.models import *
from crum import get_current_user
import django_filters


class page_guru_nilai_pengetahuan_filter(django_filters.FilterSet):
	class Meta:
		model = Mo_Penilaian_Pengetahuan
		fields = "__all__"


# FILTER KOMPETENSI DASAR
class page_guru_kompetensi_dasar_wajib_filter(django_filters.FilterSet):
	class Meta:
		model = Gu_Data_Kompetensi_Dasar
		fields = "__all__"
	def __init__(self, *args, **kwargs):
		super(page_guru_kompetensi_dasar_wajib_filter, self).__init__(*args, **kwargs)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
class page_guru_kompetensi_dasar_jurusan_filter(django_filters.FilterSet):
	class Meta:
		model = Gu_Data_Kompetensi_Dasar
		fields = "__all__"
	def __init__(self, *args, **kwargs):
		super(page_guru_kompetensi_dasar_jurusan_filter, self).__init__(*args, **kwargs)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())


# FILTER PENGETAHUAN
class page_guru_nilai_pengetahuan_wajib_filter(django_filters.FilterSet):
	class Meta:
		model = Mo_Penilaian_Pengetahuan
		fields = "__all__"
	def __init__(self, *args, **kwargs):
		super(page_guru_nilai_pengetahuan_wajib_filter, self).__init__(*args, **kwargs)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		self.filters['mo_kompetensi_dasar'].queryset = Gu_Data_Kompetensi_Dasar.objects.filter(guru_kompetensi_dasar_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib)
		self.filters['mo_siswa'].queryset = Profil_Murid.objects.filter(murid_user__is_murid=True)
class page_guru_nilai_pengetahuan_jurusan_filter(django_filters.FilterSet):
	class Meta:
		model = Mo_Penilaian_Pengetahuan
		fields = "__all__"
	def __init__(self, *args, **kwargs):
		super(page_guru_nilai_pengetahuan_jurusan_filter, self).__init__(*args, **kwargs)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		self.filters['mo_kompetensi_dasar'].queryset = Gu_Data_Kompetensi_Dasar.objects.filter(guru_kompetensi_dasar_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan)
		self.filters['mo_siswa'].queryset = Profil_Murid.objects.filter(murid_user__is_murid=True)



# FILTER KETERAMPILAN
class page_guru_nilai_keterampilan_wajib_filter(django_filters.FilterSet):
	class Meta:
		model = Mo_Penilaian_Keterampilan
		fields = "__all__"
	def __init__(self, *args, **kwargs):
		super(page_guru_nilai_keterampilan_wajib_filter, self).__init__(*args, **kwargs)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		self.filters['mo_kompetensi_dasar'].queryset = Gu_Data_Kompetensi_Dasar.objects.filter(guru_kompetensi_dasar_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib)
		self.filters['mo_siswa'].queryset = Profil_Murid.objects.filter(murid_user__is_murid=True)
class page_guru_nilai_keterampilan_jurusan_filter(django_filters.FilterSet):
	class Meta:
		model = Mo_Penilaian_Keterampilan
		fields = "__all__"
	def __init__(self, *args, **kwargs):
		super(page_guru_nilai_keterampilan_jurusan_filter, self).__init__(*args, **kwargs)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		self.filters['mo_kompetensi_dasar'].queryset = Gu_Data_Kompetensi_Dasar.objects.filter(guru_kompetensi_dasar_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan)
		self.filters['mo_siswa'].queryset = Profil_Murid.objects.filter(murid_user__is_murid=True)



# FILTER SIKAP SOSIAL
class page_guru_nilai_sikap_sosial_wajib_filter(django_filters.FilterSet):
	class Meta:
		model = Mo_Sikap_Sosial
		fields = "__all__"
	def __init__(self, *args, **kwargs):
		super(page_guru_nilai_sikap_sosial_wajib_filter, self).__init__(*args, **kwargs)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		self.filters['mo_kompetensi_dasar'].queryset = Gu_Data_Kompetensi_Dasar.objects.filter(guru_kompetensi_dasar_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib)
		self.filters['mo_siswa'].queryset = Profil_Murid.objects.filter(murid_user__is_murid=True)
class page_guru_nilai_sikap_sosial_jurusan_filter(django_filters.FilterSet):
	class Meta:
		model = Mo_Sikap_Sosial
		fields = "__all__"
	def __init__(self, *args, **kwargs):
		super(page_guru_nilai_sikap_sosial_jurusan_filter, self).__init__(*args, **kwargs)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		self.filters['mo_kompetensi_dasar'].queryset = Gu_Data_Kompetensi_Dasar.objects.filter(guru_kompetensi_dasar_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan)
		self.filters['mo_siswa'].queryset = Profil_Murid.objects.filter(murid_user__is_murid=True)



# FILTER SIKAP SPIRITUAL
class page_guru_nilai_sikap_spiritual_wajib_filter(django_filters.FilterSet):
	class Meta:
		model = Mo_Sikap_Spiritual
		fields = "__all__"
	def __init__(self, *args, **kwargs):
		super(page_guru_nilai_sikap_spiritual_wajib_filter, self).__init__(*args, **kwargs)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		self.filters['mo_kompetensi_dasar'].queryset = Gu_Data_Kompetensi_Dasar.objects.filter(guru_kompetensi_dasar_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib)
		self.filters['mo_siswa'].queryset = Profil_Murid.objects.filter(murid_user__is_murid=True)
class page_guru_nilai_sikap_spiritual_jurusan_filter(django_filters.FilterSet):
	class Meta:
		model = Mo_Sikap_Spiritual
		fields = "__all__"
	def __init__(self, *args, **kwargs):
		super(page_guru_nilai_sikap_spiritual_jurusan_filter, self).__init__(*args, **kwargs)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		self.filters['mo_kompetensi_dasar'].queryset = Gu_Data_Kompetensi_Dasar.objects.filter(guru_kompetensi_dasar_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan)
		self.filters['mo_siswa'].queryset = Profil_Murid.objects.filter(murid_user__is_murid=True)


class page_guru_nilai_ulangan_wajib_filter(django_filters.FilterSet):
	class Meta:
		model = Mo_Penilaian_Ulangan
		fields = "__all__"
	def __init__(self, *args, **kwargs):
		super(page_guru_nilai_ulangan_wajib_filter, self).__init__(*args, **kwargs)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		self.filters['mo_kompetensi_dasar'].queryset = Gu_Data_Kompetensi_Dasar.objects.filter(guru_kompetensi_dasar_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib)
		self.filters['mo_siswa'].queryset = Profil_Murid.objects.filter(murid_user__is_murid=True)
class page_guru_nilai_ulangan_jurusan_filter(django_filters.FilterSet):
	class Meta:
		model = Mo_Penilaian_Ulangan
		fields = "__all__"
	def __init__(self, *args, **kwargs):
		super(page_guru_nilai_ulangan_jurusan_filter, self).__init__(*args, **kwargs)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		self.filters['mo_kompetensi_dasar'].queryset = Gu_Data_Kompetensi_Dasar.objects.filter(guru_kompetensi_dasar_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan)
		self.filters['mo_siswa'].queryset = Profil_Murid.objects.filter(murid_user__is_murid=True)


class page_guru_nilai_uts_wajib_filter(django_filters.FilterSet):
	class Meta:
		model = Mo_Penilaian_UTS
		fields = "__all__"
	def __init__(self, *args, **kwargs):
		super(page_guru_nilai_uts_wajib_filter, self).__init__(*args, **kwargs)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		self.filters['mo_siswa'].queryset = Profil_Murid.objects.filter(murid_user__is_murid=True)
class page_guru_nilai_uts_jurusan_filter(django_filters.FilterSet):
	class Meta:
		model = Mo_Penilaian_UTS
		fields = "__all__"
	def __init__(self, *args, **kwargs):
		super(page_guru_nilai_uts_jurusan_filter, self).__init__(*args, **kwargs)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		self.filters['mo_siswa'].queryset = Profil_Murid.objects.filter(murid_user__is_murid=True)


class page_guru_nilai_uas_wajib_filter(django_filters.FilterSet):
	class Meta:
		model = Mo_Penilaian_UAS
		fields = "__all__"
	def __init__(self, *args, **kwargs):
		super(page_guru_nilai_uas_wajib_filter, self).__init__(*args, **kwargs)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		self.filters['mo_siswa'].queryset = Profil_Murid.objects.filter(murid_user__is_murid=True)
class page_guru_nilai_uas_jurusan_filter(django_filters.FilterSet):
	class Meta:
		model = Mo_Penilaian_UAS
		fields = "__all__"
	def __init__(self, *args, **kwargs):
		super(page_guru_nilai_uas_jurusan_filter, self).__init__(*args, **kwargs)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		self.filters['mo_siswa'].queryset = Profil_Murid.objects.filter(murid_user__is_murid=True)