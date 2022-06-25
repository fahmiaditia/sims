from django import forms
from role_ekskul.models import *
from monitoring.models import *
from sekolah.models import *
from crum import get_current_user


class page_ekskul_profil_forms(forms.ModelForm):
	class Meta:
		model = Profil_Pembimbing
		fields = [
			"ekskul_user",
			"ekskul_nama",
			"ekskul_tempat_tanggal_lahir",
			"ekskul_alamat",
			"ekskul_telp",
			"ekskul_mata_ekskul"
		]
		exclude = ('ekskul_profil_uuid', 'ekskul_user')
		widgets = {
			"ekskul_user": forms.Select(attrs={'class':'form-control'}),
			"ekskul_nama": forms.TextInput(attrs={'class':'form-control'}),
			"ekskul_tempat_tanggal_lahir": forms.TextInput(attrs={'class':'form-control'}),
			"ekskul_alamat": forms.TextInput(attrs={'class':'form-control'}),
			"ekskul_telp": forms.TextInput(attrs={'class':'form-control'}),
			"ekskul_mata_ekskul": forms.Select(attrs={'class':'form-control'}),
		}

class page_ekskul_penilaian_forms(forms.ModelForm):
	class Meta:
		model = Mo_Penilaian_Ekskul
		fields = [
			"mo_siswa",
			"mo_kelas",
			"mo_tahun_ajaran",
			"mo_semester",
			"mo_ekskul",
			"mo_nilai"
		]
		exclude = ('mo_ekskul',)
		widgets = {
			"mo_siswa": forms.Select(attrs={'class':'form-control'}),
			"mo_kelas": forms.Select(attrs={'class':'form-control'}),
			"mo_tahun_ajaran": forms.Select(attrs={'class':'form-control'}),
			"mo_semester": forms.Select(attrs={'class':'form-control'}),
			"mo_ekskul": forms.Select(attrs={'class':'form-control'}),
			"mo_nilai": forms.NumberInput(attrs={'class':'form-control'}),
		}
	def __init__(self, *args, **kwargs):
		super(page_ekskul_penilaian_forms, self).__init__(*args, **kwargs)
		pembimbing = Profil_Pembimbing.objects.get(ekskul_user=get_current_user())
		self.fields['mo_siswa'].queryset = Profil_Murid.objects.filter(murid_user__is_murid=True, murid_ekskul=pembimbing.ekskul_mata_ekskul)
	def save(self, commit=True):
		instance = super(page_ekskul_penilaian_forms, self).save(commit=False)
		murid = Profil_Murid.objects.get(murid_user=instance.mo_siswa.murid_user)
		instance.mo_kelas = murid.murid_kelas
		instance.mo_tahun_ajaran = murid.murid_tahun_ajaran
		instance.mo_semester = murid.murid_semester
		if commit:
			instance.save()
		return instance

class page_ekskul_kejuaraan_penilaian_forms(forms.ModelForm):
	class Meta:
		model = Mo_Juara_Ekskul
		fields = [
			"mo_siswa",
			"mo_ekskul",
			"mo_tahun",
			"mo_tingkatan",
			"mo_pelaksana",
			"mo_kejuaraan",
			"mo_juara",
		]
		exclude = ('mo_ekskul',)
		widgets = {
			"mo_siswa": forms.Select(attrs={'class':'form-control'}),
			"mo_ekskul": forms.Select(attrs={'class':'form-control'}),
			"mo_tahun": forms.TextInput(attrs={'class':'form-control'}),
			"mo_tingkatan": forms.Select(attrs={'class':'form-control'}),
			"mo_pelaksana": forms.TextInput(attrs={'class':'form-control'}),
			"mo_kejuaraan": forms.TextInput(attrs={'class':'form-control'}),
			"mo_juara": forms.Select(attrs={'class':'form-control'}),
		}
	def __init__(self, *args, **kwargs):
		super(page_ekskul_kejuaraan_penilaian_forms, self).__init__(*args, **kwargs)
		pembimbing = Profil_Pembimbing.objects.get(ekskul_user=get_current_user())
		self.fields['mo_siswa'].queryset = Profil_Murid.objects.filter(murid_user__is_murid=True, murid_ekskul=pembimbing.ekskul_mata_ekskul)
	# def save(self, commit=True):
	# 	instance = super(page_ekskul_kejuaraan_penilaian_forms, self).save(commit=False)
	# 	murid = Profil_Murid.objects.get(murid_user=instance.mo_siswa.murid_user)
	# 	instance.mo_kelas = murid.murid_kelas
	# 	instance.mo_tahun_ajaran = murid.murid_tahun_ajaran
	# 	instance.mo_semester = murid.murid_semester
	# 	if commit:
	# 		instance.save()
	# 	return instance