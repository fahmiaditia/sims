from monitoring.models import *
from role_ekskul.models import *
from crum import get_current_user
import django_filters


class page_ekskul_nilai_filter(django_filters.FilterSet):
	class Meta:
		model = Mo_Penilaian_Ekskul
		fields = "__all__"
	def __init__(self, *args, **kwargs):
		super(page_ekskul_nilai_filter, self).__init__(*args, **kwargs)
		pembimbing = Profil_Pembimbing.objects.get(ekskul_user=get_current_user())
		self.filters['mo_siswa'].queryset = Profil_Murid.objects.filter(murid_user__is_murid=True, murid_ekskul=pembimbing.ekskul_mata_ekskul)


class page_ekskul_kejuaraan_filter(django_filters.FilterSet):
	class Meta:
		model = Mo_Juara_Ekskul
		fields = "__all__"
	def __init__(self, *args, **kwargs):
		super(page_ekskul_kejuaraan_filter, self).__init__(*args, **kwargs)
		pembimbing = Profil_Pembimbing.objects.get(ekskul_user=get_current_user())
		self.filters['mo_siswa'].queryset = Profil_Murid.objects.filter(murid_user__is_murid=True, murid_ekskul=pembimbing.ekskul_mata_ekskul)