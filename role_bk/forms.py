from django import forms
from role_guru.models import *
from role_kepala_sekolah.models import *
from role_bk.models import *
from monitoring.models import *
from sekolah.models import *
from crum import get_current_user

class page_bk_profil_forms(forms.ModelForm):
	class Meta:
		model = Profil_BK
		fields = [
			"bk_nama",
			"bk_nip",
			"bk_nuptk",
			"bk_tempat_tanggal_lahir",
			"bk_jabatan",
			"bk_pangkat_golongan",
		]
		exclude = ('guru_profil_uuid',)
		widgets = {
			"bk_nama": forms.TextInput(attrs={'class':'form-control'}),
			"bk_nip": forms.TextInput(attrs={'class':'form-control'}),
			"bk_nuptk": forms.TextInput(attrs={'class':'form-control'}),
			"bk_tempat_tanggal_lahir": forms.TextInput(attrs={'class':'form-control'}),
			"bk_jabatan": forms.TextInput(attrs={'class':'form-control'}),
			"bk_pangkat_golongan": forms.TextInput(attrs={'class':'form-control'}),
		}

class page_bk_catatan_forms(forms.ModelForm):
	class Meta:
		model = BK_Catatan
		fields = "__all__"
		exclude = ('bk_catatan_uuid',)
		att = {
			'class': 'form-control',
		}

		widgets = {
			'bk_catatan_status': forms.Select(attrs=att),
			'bk_catatan_siswa': forms.Select(attrs=att),
			'bk_catatan_catatan': forms.Textarea(attrs=att),
		}