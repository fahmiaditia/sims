from django import forms
from role_guru.models import *
from role_kepala_sekolah.models import *
from monitoring.models import *
from sekolah.models import *
from crum import get_current_user

class page_kepsek_profil_forms(forms.ModelForm):
	class Meta:
		model = Profil_Kepsek
		fields = [
			"kepsek_nama",
			"kepsek_nip",
			"kepsek_nuptk",
			"kepsek_tempat_tanggal_lahir",
			"kepsek_jabatan",
			"kepsek_pangkat_golongan",
		]
		exclude = ('guru_profil_uuid',)
		widgets = {
			"kepsek_nama": forms.TextInput(attrs={'class':'form-control'}),
			"kepsek_nip": forms.TextInput(attrs={'class':'form-control'}),
			"kepsek_nuptk": forms.TextInput(attrs={'class':'form-control'}),
			"kepsek_tempat_tanggal_lahir": forms.TextInput(attrs={'class':'form-control'}),
			"kepsek_jabatan": forms.TextInput(attrs={'class':'form-control'}),
			"kepsek_pangkat_golongan": forms.TextInput(attrs={'class':'form-control'}),
		}