# FILTERING DISINI
from monitoring.models import *
from role_guru.models import *
from role_bk.models import *
from role_murid.models import *
from crum import get_current_user
import django_filters


class page_bk_kompetensi_dasar_wajib_filter(django_filters.FilterSet):
	class Meta:
		model = Gu_Data_Kompetensi_Dasar
		fields = "__all__"
	# def __init__(self, *args, **kwargs):
	# 	super(page_guru_kompetensi_dasar_wajib_filter, self).__init__(*args, **kwargs)
	# 	guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())


class page_bk_kompetensi_dasar_jurusan_filter(django_filters.FilterSet):
	class Meta:
		model = Gu_Data_Kompetensi_Dasar
		fields = "__all__"

class page_bk_nilai_siswa_filter(django_filters.FilterSet):
	class Meta:
		model = Profil_Murid
		fields = "__all__"