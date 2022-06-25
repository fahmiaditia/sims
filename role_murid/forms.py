from django import forms
from role_murid.models import *
from crum import get_current_user


class page_murid_profil_forms(forms.ModelForm):
	class Meta:
		model = Profil_Murid
		fields = [
			"murid_nama",
		]
		exclude = ('murid_profil_uuid',)
		widgets = {
			"murid_nama": forms.TextInput(attrs={'class':'form-control'}),
		}