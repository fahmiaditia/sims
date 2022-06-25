from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.forms import modelformset_factory, formset_factory
from django.db.models import Avg, Count, Sum, Max
from sekolah.models import *
from role_guru.models import *
from role_kepala_sekolah.forms import *
from role_kepala_sekolah.filters import *
from role_bk.models import *
from role_bk.filters import *
from role_bk.forms import *
from role_murid.models import *
from role_kepala_sekolah.models import Profil_Kepsek
from monitoring.models import *
from sekolah.models import *
import json
import statistics

def jarak(var):
	print("\n"*var)

# Create your views here.


def page_bk_dashboard(request):
	context = {

	}
	return render(request, "templates_bk/dashboard_bk_r.html", context)

def page_bk_profil(request):
	profil_bk = Profil_BK.objects.get(bk_user=request.user)
	kelas = SKL_Kelas.objects.all()
	context={
		'profil_bk': profil_bk,
		'kelas': kelas,
	}
	return render(request, 'templates_bk/page_profil_bk/profil_bk.html', context)

class page_bk_profil_update(UpdateView):
	model = Profil_BK
	form_class = page_bk_profil_forms
	success_url = reverse_lazy("monitoring:page_bk_profil")
	template_name = 'templates_bk/page_profil_bk/profil_bk_update.html'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['kelas'] = SKL_Kelas.objects.all()
		return context

def page_bk_performa_kelas_landing(request):
	kelas_10 = SKL_Kelas.objects.filter(skl_k_kelas_nama__contains="10")
	
	data_angka = {
		'pengetahuan': {
			'kelas_10': Mo_Penilaian_Pengetahuan.objects.filter(mo_kelas__skl_k_kelas_nama__contains="10").values('mo_kelas__skl_k_kelas_nama', 'mo_kelas__skl_k_kelas_uuid').annotate(Avg('mo_nilai_P1_TGS'), Avg('mo_nilai_P2_TLS'), Avg('mo_nilai_P3_TLS')),
			'kelas_11': Mo_Penilaian_Pengetahuan.objects.filter(mo_kelas__skl_k_kelas_nama__contains="11").values('mo_kelas__skl_k_kelas_nama', 'mo_kelas__skl_k_kelas_uuid').annotate(Avg('mo_nilai_P1_TGS'), Avg('mo_nilai_P2_TLS'), Avg('mo_nilai_P3_TLS')),
			'kelas_12': Mo_Penilaian_Pengetahuan.objects.filter(mo_kelas__skl_k_kelas_nama__contains="12").values('mo_kelas__skl_k_kelas_nama', 'mo_kelas__skl_k_kelas_uuid').annotate(Avg('mo_nilai_P1_TGS'), Avg('mo_nilai_P2_TLS'), Avg('mo_nilai_P3_TLS')),
		},
		'keterampilan': {
			'kelas_10': Mo_Penilaian_Keterampilan.objects.filter(mo_kelas__skl_k_kelas_nama__contains="10").values('mo_kelas__skl_k_kelas_nama', 'mo_kelas__skl_k_kelas_uuid').annotate(Avg('mo_praktek'), Avg('mo_produk'), Avg('mo_proyek'), Avg('mo_portofolio')),
			'kelas_11': Mo_Penilaian_Keterampilan.objects.filter(mo_kelas__skl_k_kelas_nama__contains="11").values('mo_kelas__skl_k_kelas_nama', 'mo_kelas__skl_k_kelas_uuid').annotate(Avg('mo_praktek'), Avg('mo_produk'), Avg('mo_proyek'), Avg('mo_portofolio')),
			'kelas_12': Mo_Penilaian_Keterampilan.objects.filter(mo_kelas__skl_k_kelas_nama__contains="12").values('mo_kelas__skl_k_kelas_nama', 'mo_kelas__skl_k_kelas_uuid').annotate(Avg('mo_praktek'), Avg('mo_produk'), Avg('mo_proyek'), Avg('mo_portofolio')),
		},
		'sosial': {
			'kelas_10': Mo_Sikap_Sosial.objects.filter(mo_kelas__skl_k_kelas_nama__contains="10").values('mo_kelas__skl_k_kelas_nama', 'mo_kelas__skl_k_kelas_uuid').annotate(Avg('mo_proyeksi_nilai')).order_by('mo_kelas__skl_k_kelas_nama'),
			'kelas_11': Mo_Sikap_Sosial.objects.filter(mo_kelas__skl_k_kelas_nama__contains="11").values('mo_kelas__skl_k_kelas_nama', 'mo_kelas__skl_k_kelas_uuid').annotate(Avg('mo_proyeksi_nilai')).order_by('mo_kelas__skl_k_kelas_nama'),
			'kelas_12': Mo_Sikap_Sosial.objects.filter(mo_kelas__skl_k_kelas_nama__contains="12").values('mo_kelas__skl_k_kelas_nama', 'mo_kelas__skl_k_kelas_uuid').annotate(Avg('mo_proyeksi_nilai')).order_by('mo_kelas__skl_k_kelas_nama'),
		},
		'spiritual': {
			'kelas_10': Mo_Sikap_Spiritual.objects.filter(mo_kelas__skl_k_kelas_nama__contains="10").values('mo_kelas__skl_k_kelas_nama', 'mo_kelas__skl_k_kelas_uuid').annotate(Avg('mo_proyeksi_nilai')).order_by('mo_kelas__skl_k_kelas_nama'),
			'kelas_11': Mo_Sikap_Spiritual.objects.filter(mo_kelas__skl_k_kelas_nama__contains="11").values('mo_kelas__skl_k_kelas_nama', 'mo_kelas__skl_k_kelas_uuid').annotate(Avg('mo_proyeksi_nilai')).order_by('mo_kelas__skl_k_kelas_nama'),
			'kelas_12': Mo_Sikap_Spiritual.objects.filter(mo_kelas__skl_k_kelas_nama__contains="12").values('mo_kelas__skl_k_kelas_nama', 'mo_kelas__skl_k_kelas_uuid').annotate(Avg('mo_proyeksi_nilai')).order_by('mo_kelas__skl_k_kelas_nama'),
		},
		'ulangan': {
			'kelas_10': Mo_Penilaian_Ulangan.objects.filter(mo_kelas__skl_k_kelas_nama__contains="10").values('mo_kelas__skl_k_kelas_nama', 'mo_kelas__skl_k_kelas_uuid').annotate(Avg('mo_nilai')).order_by('mo_kelas__skl_k_kelas_nama'),
			'kelas_11': Mo_Penilaian_Ulangan.objects.filter(mo_kelas__skl_k_kelas_nama__contains="11").values('mo_kelas__skl_k_kelas_nama', 'mo_kelas__skl_k_kelas_uuid').annotate(Avg('mo_nilai')).order_by('mo_kelas__skl_k_kelas_nama'),
			'kelas_12': Mo_Penilaian_Ulangan.objects.filter(mo_kelas__skl_k_kelas_nama__contains="12").values('mo_kelas__skl_k_kelas_nama', 'mo_kelas__skl_k_kelas_uuid').annotate(Avg('mo_nilai')).order_by('mo_kelas__skl_k_kelas_nama'),
		},
		'uts': {
			'kelas_10': Mo_Penilaian_UTS.objects.filter(mo_kelas__skl_k_kelas_nama__contains="10").values('mo_kelas__skl_k_kelas_nama', 'mo_kelas__skl_k_kelas_uuid').annotate(Avg('mo_nilai')).order_by('mo_kelas__skl_k_kelas_nama'),
			'kelas_11': Mo_Penilaian_UTS.objects.filter(mo_kelas__skl_k_kelas_nama__contains="11").values('mo_kelas__skl_k_kelas_nama', 'mo_kelas__skl_k_kelas_uuid').annotate(Avg('mo_nilai')).order_by('mo_kelas__skl_k_kelas_nama'),
			'kelas_12': Mo_Penilaian_UTS.objects.filter(mo_kelas__skl_k_kelas_nama__contains="12").values('mo_kelas__skl_k_kelas_nama', 'mo_kelas__skl_k_kelas_uuid').annotate(Avg('mo_nilai')).order_by('mo_kelas__skl_k_kelas_nama'),
		},
		'uas': {
			'kelas_10': Mo_Penilaian_UAS.objects.filter(mo_kelas__skl_k_kelas_nama__contains="10").values('mo_kelas__skl_k_kelas_nama', 'mo_kelas__skl_k_kelas_uuid').annotate(Avg('mo_nilai')).order_by('mo_kelas__skl_k_kelas_nama'),
			'kelas_11': Mo_Penilaian_UAS.objects.filter(mo_kelas__skl_k_kelas_nama__contains="11").values('mo_kelas__skl_k_kelas_nama', 'mo_kelas__skl_k_kelas_uuid').annotate(Avg('mo_nilai')).order_by('mo_kelas__skl_k_kelas_nama'),
			'kelas_12': Mo_Penilaian_UAS.objects.filter(mo_kelas__skl_k_kelas_nama__contains="12").values('mo_kelas__skl_k_kelas_nama', 'mo_kelas__skl_k_kelas_uuid').annotate(Avg('mo_nilai')).order_by('mo_kelas__skl_k_kelas_nama'),
		},

	}

	data_grafik = {
		'pengetahuan': {
			'kelas_10':{
				'kelas': [],
				'nilai_P1_TGS': [],
				'nilai_P2_TLS': [],
				'nilai_P3_TLS': [],
			},
			'kelas_11':{
				'kelas': [],
				'nilai_P1_TGS': [],
				'nilai_P2_TLS': [],
				'nilai_P3_TLS': [],
			},
			'kelas_12':{
				'kelas': [],
				'nilai_P1_TGS': [],
				'nilai_P2_TLS': [],
				'nilai_P3_TLS': [],
			},
		},
		'keterampilan': {
			'kelas_10':{
				'kelas': [],
				'praktek': [],
				'produk': [],
				'proyek': [],
				'portofolio': [],	
			},
			'kelas_11':{
				'kelas': [],
				'praktek': [],
				'produk': [],
				'proyek': [],
				'portofolio': [],
			},
			'kelas_12':{
				'kelas': [],
				'praktek': [],
				'produk': [],
				'proyek': [],
				'portofolio': [],
			},
		},
		'sosial': {
			'kelas_10':{
				'kelas': [],
				'proyeksi': [],
				'keterangan': [],
			},
			'kelas_11':{
				'kelas': [],
				'proyeksi': [],
				'keterangan': [],
			},
			'kelas_12':{
				'kelas': [],
				'proyeksi': [],
				'keterangan': [],
			},
		},
		'spiritual': {
			'kelas_10':{
				'kelas': [],
				'proyeksi': [],
				'keterangan': [],
			},
			'kelas_11':{
				'kelas': [],
				'proyeksi': [],
				'keterangan': [],
			},
			'kelas_12':{
				'kelas': [],
				'proyeksi': [],
				'keterangan': [],
			},
		},
		'ulangan': {
			'kelas_10': {
				'kelas': [],
				'nilai': [],
			},
			'kelas_11': {
				'kelas': [],
				'nilai': [],
			},
			'kelas_12': {
				'kelas': [],
				'nilai': [],
			},
		},
		'uts': {
			'kelas_10': {
				'kelas': [],
				'nilai': [],
			},
			'kelas_11': {
				'kelas': [],
				'nilai': [],
			},
			'kelas_12': {
				'kelas': [],
				'nilai': [],
			},
		},
		'uas': {
			'kelas_10': {
				'kelas': [],
				'nilai': [],
			},
			'kelas_11': {
				'kelas': [],
				'nilai': [],
			},
			'kelas_12': {
				'kelas': [],
				'nilai': [],
			},
		}
		

	}
	
	# Kelas 10 ===================================================================================
	for data in data_angka['pengetahuan']['kelas_10']:
		data_grafik['pengetahuan']['kelas_10']['kelas'].append(data['mo_kelas__skl_k_kelas_nama'])
		data_grafik['pengetahuan']['kelas_10']['nilai_P1_TGS'].append(data['mo_nilai_P1_TGS__avg'])
		data_grafik['pengetahuan']['kelas_10']['nilai_P2_TLS'].append(data['mo_nilai_P2_TLS__avg'])
		data_grafik['pengetahuan']['kelas_10']['nilai_P3_TLS'].append(data['mo_nilai_P3_TLS__avg'])

	for data in data_angka['keterampilan']['kelas_10']:
		data_grafik['keterampilan']['kelas_10']['kelas'].append(data['mo_kelas__skl_k_kelas_nama'])
		data_grafik['keterampilan']['kelas_10']['praktek'].append(data['mo_praktek__avg'])
		data_grafik['keterampilan']['kelas_10']['produk'].append(data['mo_produk__avg'])
		data_grafik['keterampilan']['kelas_10']['proyek'].append(data['mo_proyek__avg'])
		data_grafik['keterampilan']['kelas_10']['portofolio'].append(data['mo_portofolio__avg'])
	
	for data in data_angka['sosial']['kelas_10']:
		data_grafik['sosial']['kelas_10']['kelas'].append(data['mo_kelas__skl_k_kelas_nama'])
		data_grafik['sosial']['kelas_10']['proyeksi'].append(data['mo_proyeksi_nilai__avg'])
		if data['mo_proyeksi_nilai__avg'] <= 100 and data['mo_proyeksi_nilai__avg'] > 75:
			data_grafik['sosial']['kelas_10']['keterangan'].append('Sangat Baik')
		elif data['mo_proyeksi_nilai__avg'] <= 75 and data['mo_proyeksi_nilai__avg'] > 50:
			data_grafik['sosial']['kelas_10']['keterangan'].append('Baik')
		elif data['mo_proyeksi_nilai__avg'] <= 50 and data['mo_proyeksi_nilai__avg'] > 25:
			data_grafik['sosial']['kelas_10']['keterangan'].append('Cukup')
		elif data['mo_proyeksi_nilai__avg'] <= 25:
			data_grafik['sosial']['kelas_10']['keterangan'].append('Kurang')

	for data in data_angka['spiritual']['kelas_10']:
		data_grafik['spiritual']['kelas_10']['kelas'].append(data['mo_kelas__skl_k_kelas_nama'])
		data_grafik['spiritual']['kelas_10']['proyeksi'].append(data['mo_proyeksi_nilai__avg'])
		if data['mo_proyeksi_nilai__avg'] <= 100 and data['mo_proyeksi_nilai__avg'] > 75:
			data_grafik['spiritual']['kelas_10']['keterangan'].append('Sangat Baik')
		elif data['mo_proyeksi_nilai__avg'] <= 75 and data['mo_proyeksi_nilai__avg'] > 50:
			data_grafik['spiritual']['kelas_10']['keterangan'].append('Baik')
		elif data['mo_proyeksi_nilai__avg'] <= 50 and data['mo_proyeksi_nilai__avg'] > 25:
			data_grafik['spiritual']['kelas_10']['keterangan'].append('Cukup')
		elif data['mo_proyeksi_nilai__avg'] <= 25:
			data_grafik['spiritual']['kelas_10']['keterangan'].append('Kurang')

	for data in data_angka['ulangan']['kelas_10']:
		data_grafik['ulangan']['kelas_10']['kelas'].append(data['mo_kelas__skl_k_kelas_nama'])
		data_grafik['ulangan']['kelas_10']['nilai'].append(data['mo_nilai__avg'])

	for data in data_angka['uts']['kelas_10']:
		data_grafik['uts']['kelas_10']['kelas'].append(data['mo_kelas__skl_k_kelas_nama'])
		data_grafik['uts']['kelas_10']['nilai'].append(data['mo_nilai__avg'])

	for data in data_angka['uas']['kelas_10']:
		data_grafik['uas']['kelas_10']['kelas'].append(data['mo_kelas__skl_k_kelas_nama'])
		data_grafik['uas']['kelas_10']['nilai'].append(data['mo_nilai__avg'])
	#  ==========================================================================================



	# Kelas 11 ===================================================================================
	for data in data_angka['pengetahuan']['kelas_11']:
		data_grafik['pengetahuan']['kelas_11']['kelas'].append(data['mo_kelas__skl_k_kelas_nama'])
		data_grafik['pengetahuan']['kelas_11']['nilai_P1_TGS'].append(data['mo_nilai_P1_TGS__avg'])
		data_grafik['pengetahuan']['kelas_11']['nilai_P2_TLS'].append(data['mo_nilai_P2_TLS__avg'])
		data_grafik['pengetahuan']['kelas_11']['nilai_P3_TLS'].append(data['mo_nilai_P3_TLS__avg'])

	for data in data_angka['keterampilan']['kelas_11']:
		data_grafik['keterampilan']['kelas_11']['kelas'].append(data['mo_kelas__skl_k_kelas_nama'])
		data_grafik['keterampilan']['kelas_11']['praktek'].append(data['mo_praktek__avg'])
		data_grafik['keterampilan']['kelas_11']['produk'].append(data['mo_produk__avg'])
		data_grafik['keterampilan']['kelas_11']['proyek'].append(data['mo_proyek__avg'])
		data_grafik['keterampilan']['kelas_11']['portofolio'].append(data['mo_portofolio__avg'])
	
	for data in data_angka['sosial']['kelas_11']:
		data_grafik['sosial']['kelas_11']['kelas'].append(data['mo_kelas__skl_k_kelas_nama'])
		data_grafik['sosial']['kelas_11']['proyeksi'].append(data['mo_proyeksi_nilai__avg'])
		if data['mo_proyeksi_nilai__avg'] <= 100 and data['mo_proyeksi_nilai__avg'] > 75:
			data_grafik['sosial']['kelas_11']['keterangan'].append('Sangat Baik')
		elif data['mo_proyeksi_nilai__avg'] <= 75 and data['mo_proyeksi_nilai__avg'] > 50:
			data_grafik['sosial']['kelas_11']['keterangan'].append('Baik')
		elif data['mo_proyeksi_nilai__avg'] <= 50 and data['mo_proyeksi_nilai__avg'] > 25:
			data_grafik['sosial']['kelas_11']['keterangan'].append('Cukup')
		elif data['mo_proyeksi_nilai__avg'] <= 25:
			data_grafik['sosial']['kelas_11']['keterangan'].append('Kurang')

	for data in data_angka['spiritual']['kelas_11']:
		data_grafik['spiritual']['kelas_11']['kelas'].append(data['mo_kelas__skl_k_kelas_nama'])
		data_grafik['spiritual']['kelas_11']['proyeksi'].append(data['mo_proyeksi_nilai__avg'])
		if data['mo_proyeksi_nilai__avg'] <= 100 and data['mo_proyeksi_nilai__avg'] > 75:
			data_grafik['spiritual']['kelas_11']['keterangan'].append('Sangat Baik')
		elif data['mo_proyeksi_nilai__avg'] <= 75 and data['mo_proyeksi_nilai__avg'] > 50:
			data_grafik['spiritual']['kelas_11']['keterangan'].append('Baik')
		elif data['mo_proyeksi_nilai__avg'] <= 50 and data['mo_proyeksi_nilai__avg'] > 25:
			data_grafik['spiritual']['kelas_11']['keterangan'].append('Cukup')
		elif data['mo_proyeksi_nilai__avg'] <= 25:
			data_grafik['spiritual']['kelas_11']['keterangan'].append('Kurang')

	for data in data_angka['ulangan']['kelas_11']:
		data_grafik['ulangan']['kelas_11']['kelas'].append(data['mo_kelas__skl_k_kelas_nama'])
		data_grafik['ulangan']['kelas_11']['nilai'].append(data['mo_nilai__avg'])

	for data in data_angka['uts']['kelas_11']:
		data_grafik['uts']['kelas_11']['kelas'].append(data['mo_kelas__skl_k_kelas_nama'])
		data_grafik['uts']['kelas_11']['nilai'].append(data['mo_nilai__avg'])

	for data in data_angka['uas']['kelas_11']:
		data_grafik['uas']['kelas_11']['kelas'].append(data['mo_kelas__skl_k_kelas_nama'])
		data_grafik['uas']['kelas_11']['nilai'].append(data['mo_nilai__avg'])
	#  ==========================================================================================



	# Kelas 12 ===================================================================================
	for data in data_angka['pengetahuan']['kelas_12']:
		data_grafik['pengetahuan']['kelas_12']['kelas'].append(data['mo_kelas__skl_k_kelas_nama'])
		data_grafik['pengetahuan']['kelas_12']['nilai_P1_TGS'].append(data['mo_nilai_P1_TGS__avg'])
		data_grafik['pengetahuan']['kelas_12']['nilai_P2_TLS'].append(data['mo_nilai_P2_TLS__avg'])
		data_grafik['pengetahuan']['kelas_12']['nilai_P3_TLS'].append(data['mo_nilai_P3_TLS__avg'])

	for data in data_angka['keterampilan']['kelas_12']:
		data_grafik['keterampilan']['kelas_12']['kelas'].append(data['mo_kelas__skl_k_kelas_nama'])
		data_grafik['keterampilan']['kelas_12']['praktek'].append(data['mo_praktek__avg'])
		data_grafik['keterampilan']['kelas_12']['produk'].append(data['mo_produk__avg'])
		data_grafik['keterampilan']['kelas_12']['proyek'].append(data['mo_proyek__avg'])
		data_grafik['keterampilan']['kelas_12']['portofolio'].append(data['mo_portofolio__avg'])
	
	for data in data_angka['sosial']['kelas_12']:
		data_grafik['sosial']['kelas_12']['kelas'].append(data['mo_kelas__skl_k_kelas_nama'])
		data_grafik['sosial']['kelas_12']['proyeksi'].append(data['mo_proyeksi_nilai__avg'])
		if data['mo_proyeksi_nilai__avg'] <= 100 and data['mo_proyeksi_nilai__avg'] > 75:
			data_grafik['sosial']['kelas_12']['keterangan'].append('Sangat Baik')
		elif data['mo_proyeksi_nilai__avg'] <= 75 and data['mo_proyeksi_nilai__avg'] > 50:
			data_grafik['sosial']['kelas_12']['keterangan'].append('Baik')
		elif data['mo_proyeksi_nilai__avg'] <= 50 and data['mo_proyeksi_nilai__avg'] > 25:
			data_grafik['sosial']['kelas_12']['keterangan'].append('Cukup')
		elif data['mo_proyeksi_nilai__avg'] <= 25:
			data_grafik['sosial']['kelas_12']['keterangan'].append('Kurang')

	for data in data_angka['spiritual']['kelas_12']:
		data_grafik['spiritual']['kelas_12']['kelas'].append(data['mo_kelas__skl_k_kelas_nama'])
		data_grafik['spiritual']['kelas_12']['proyeksi'].append(data['mo_proyeksi_nilai__avg'])
		if data['mo_proyeksi_nilai__avg'] <= 100 and data['mo_proyeksi_nilai__avg'] > 75:
			data_grafik['spiritual']['kelas_12']['keterangan'].append('Sangat Baik')
		elif data['mo_proyeksi_nilai__avg'] <= 75 and data['mo_proyeksi_nilai__avg'] > 50:
			data_grafik['spiritual']['kelas_12']['keterangan'].append('Baik')
		elif data['mo_proyeksi_nilai__avg'] <= 50 and data['mo_proyeksi_nilai__avg'] > 25:
			data_grafik['spiritual']['kelas_12']['keterangan'].append('Cukup')
		elif data['mo_proyeksi_nilai__avg'] <= 25:
			data_grafik['spiritual']['kelas_12']['keterangan'].append('Kurang')

	for data in data_angka['ulangan']['kelas_12']:
		data_grafik['ulangan']['kelas_12']['kelas'].append(data['mo_kelas__skl_k_kelas_nama'])
		data_grafik['ulangan']['kelas_12']['nilai'].append(data['mo_nilai__avg'])

	for data in data_angka['uts']['kelas_12']:
		data_grafik['uts']['kelas_12']['kelas'].append(data['mo_kelas__skl_k_kelas_nama'])
		data_grafik['uts']['kelas_12']['nilai'].append(data['mo_nilai__avg'])

	for data in data_angka['uas']['kelas_12']:
		data_grafik['uas']['kelas_12']['kelas'].append(data['mo_kelas__skl_k_kelas_nama'])
		data_grafik['uas']['kelas_12']['nilai'].append(data['mo_nilai__avg'])
	#  ==========================================================================================


	context = {
		'kelas_10': kelas_10,
		'data_angka': data_angka,
		'data_grafik': json.dumps(data_grafik),
	}
	return render(request, 'templates_bk/page_performa_kelas/page_performa_kelas.html', context)


def page_bk_performa_kelas_detail(request, uuidnyaKelas):
	kelas = SKL_Kelas.objects.get(skl_k_kelas_uuid=uuidnyaKelas)
	data_angka = {
		'pengetahuan': Mo_Penilaian_Pengetahuan.objects.filter(mo_kelas__skl_k_kelas_uuid=uuidnyaKelas).order_by('mo_mata_pelajaran_wajib', 'mo_mata_pelajaran_jurusan', 'mo_siswa__murid_nama'),
		'keterampilan': Mo_Penilaian_Keterampilan.objects.filter(mo_kelas__skl_k_kelas_uuid=uuidnyaKelas).order_by('mo_mata_pelajaran_wajib', 'mo_mata_pelajaran_jurusan', 'mo_siswa__murid_nama'),
		'sosial': Mo_Sikap_Sosial.objects.filter(mo_kelas__skl_k_kelas_uuid=uuidnyaKelas).order_by('mo_mata_pelajaran_wajib', 'mo_mata_pelajaran_jurusan', 'mo_siswa__murid_nama'),
		'spiritual': Mo_Sikap_Spiritual.objects.filter(mo_kelas__skl_k_kelas_uuid=uuidnyaKelas).order_by('mo_mata_pelajaran_wajib', 'mo_mata_pelajaran_jurusan', 'mo_siswa__murid_nama'),
		'ulangan': Mo_Penilaian_Ulangan.objects.filter(mo_kelas__skl_k_kelas_uuid=uuidnyaKelas).order_by('mo_mata_pelajaran_wajib', 'mo_mata_pelajaran_jurusan', 'mo_siswa__murid_nama'),
		'uts': Mo_Penilaian_UTS.objects.filter(mo_kelas__skl_k_kelas_uuid=uuidnyaKelas).order_by('mo_mata_pelajaran_wajib', 'mo_mata_pelajaran_jurusan', 'mo_siswa__murid_nama'),
		'uas': Mo_Penilaian_UAS.objects.filter(mo_kelas__skl_k_kelas_uuid=uuidnyaKelas).order_by('mo_mata_pelajaran_wajib', 'mo_mata_pelajaran_jurusan', 'mo_siswa__murid_nama'),
	}

	data_grafik = {
		'pengetahuan': None,
		'keterampilan': None,
		'sosial': None,
		'spiritual': None,
		'ulangan': None,
		'uts': None,
		'uas': None,
	}

	query = Mo_Penilaian_Pengetahuan.objects.filter(mo_kelas__skl_k_kelas_uuid=uuidnyaKelas).annotate(nilai=(Avg('mo_nilai_P1_TGS') + Avg('mo_nilai_P2_TLS') + Avg('mo_nilai_P3_TLS'))/3)
	mean = []
	for data in query:
		try:
			if data.nilai is not None:
				mean.append(data.nilai)
			else:
				pass
		except:
			mean.append(0)
	try:
		data_grafik['pengetahuan'] = round(statistics.mean(mean))
	except:
		data_grafik['pengetahuan'] = 0

	query = Mo_Penilaian_Keterampilan.objects.filter(mo_kelas__skl_k_kelas_uuid=uuidnyaKelas).annotate(nilai=(Avg('mo_praktek') + Avg('mo_produk') + Avg('mo_proyek') + Avg('mo_portofolio'))/4)
	mean = []
	for data in query:
		try:
			if data.nilai is not None:
				mean.append(data.nilai)
			else:
				pass
		except:
			mean.append(0)
	try:
		data_grafik['keterampilan'] = round(statistics.mean(mean))
	except:
		data_grafik['keterampilan'] = 0

	query = Mo_Sikap_Sosial.objects.filter(mo_kelas__skl_k_kelas_uuid=uuidnyaKelas).annotate(nilai=Avg('mo_proyeksi_nilai'))
	mean = []
	for data in query:
		try:
			if data.nilai is not None:
				mean.append(data.nilai)
			else:
				pass
		except:
			mean.append(0)
	try:
		data_grafik['sosial'] = round(statistics.mean(mean))
	except:
		data_grafik['sosial'] = 0


	query = Mo_Sikap_Spiritual.objects.filter(mo_kelas__skl_k_kelas_uuid=uuidnyaKelas).annotate(nilai=Avg('mo_proyeksi_nilai'))
	mean = []
	for data in query:
		try:
			if data.nilai is not None:
				mean.append(data.nilai)
			else:
				pass
		except:
			mean.append(0)
	try:
		data_grafik['spiritual'] = round(statistics.mean(mean))
	except:
		data_grafik['spiritual'] = 0

	query = Mo_Penilaian_Ulangan.objects.filter(mo_kelas__skl_k_kelas_uuid=uuidnyaKelas).annotate(nilai=Avg('mo_nilai'))
	mean = []
	for data in query:
		try:
			if data.nilai is not None:
				mean.append(data.nilai)
			else:
				pass
		except:
			mean.append(0)
	try:
		data_grafik['ulangan'] = round(statistics.mean(mean))
	except:
		data_grafik['ulangan'] = 0

	query = Mo_Penilaian_UTS.objects.filter(mo_kelas__skl_k_kelas_uuid=uuidnyaKelas).annotate(nilai=Avg('mo_nilai'))
	mean = []
	for data in query:
		try:
			if data.nilai is not None:
				mean.append(data.nilai)
			else:
				pass
		except:
			mean.append(0)
	try:
		data_grafik['uts'] = round(statistics.mean(mean))
	except:
		data_grafik['uts'] = 0

	query = Mo_Penilaian_UAS.objects.filter(mo_kelas__skl_k_kelas_uuid=uuidnyaKelas).annotate(nilai=Avg('mo_nilai'))
	mean = []
	for data in query:
		try:
			if data.nilai is not None:
				mean.append(data.nilai)
			else:
				pass
		except:
			mean.append(0)
	try:
		data_grafik['uas'] = round(statistics.mean(mean))
	except:
		data_grafik['uas'] = 0

	print(data_grafik)

	context = {
		'kelas': kelas,
		'data_angka': data_angka,
		'data_grafik': json.dumps(data_grafik),
	}
	return render(request, 'templates_bk/page_performa_kelas/page_performa_kelas_detail.html', context)

def page_bk_nilai_siswa_landing(request):
	siswa_qs = Profil_Murid.objects.all().order_by('murid_kelas__skl_k_kelas_nama', 'murid_nama')
	siswa = page_bk_nilai_siswa_filter(request.GET, queryset=siswa_qs)

	context = {
		'siswa': siswa,
	}
	return render(request, 'templates_bk/page_nilai_siswa/page_nilai_siswa.html', context)

from itertools import chain 
def page_bk_nilai_siswa_detail(request, uuidnyaMurid):
	siswa = Profil_Murid.objects.get(murid_profil_uuid=uuidnyaMurid)
	
	data_angka = {
		'pengetahuan': Mo_Penilaian_Pengetahuan.objects.filter(mo_siswa__murid_profil_uuid=uuidnyaMurid).values('mo_kelas__skl_k_kelas_nama', 'mo_semester__skl_s_semester').annotate(Avg('mo_nilai_P1_TGS'), Avg('mo_nilai_P2_TLS'), Avg('mo_nilai_P3_TLS'), avg_sem=(Avg('mo_nilai_P1_TGS')+Avg('mo_nilai_P2_TLS')+Avg('mo_nilai_P3_TLS'))/3).order_by('mo_semester'),
		'keterampilan': Mo_Penilaian_Keterampilan.objects.filter(mo_siswa__murid_profil_uuid=uuidnyaMurid).values('mo_kelas__skl_k_kelas_nama', 'mo_semester__skl_s_semester').annotate(Avg('mo_praktek'), Avg('mo_produk'), Avg('mo_proyek'), Avg('mo_portofolio'), avg_sem=(Avg('mo_praktek')+Avg('mo_produk')+Avg('mo_proyek')+Avg('mo_portofolio'))/4).order_by('mo_semester'),
		'sosial': Mo_Sikap_Sosial.objects.filter(mo_siswa__murid_profil_uuid=uuidnyaMurid).values('mo_kelas__skl_k_kelas_nama', 'mo_semester__skl_s_semester').annotate(Avg('mo_proyeksi_nilai'),).order_by('mo_semester'),
		'spiritual': Mo_Sikap_Spiritual.objects.filter(mo_siswa__murid_profil_uuid=uuidnyaMurid).values('mo_kelas__skl_k_kelas_nama', 'mo_semester__skl_s_semester').annotate(Avg('mo_proyeksi_nilai'),).order_by('mo_semester'),
		'ulangan': Mo_Penilaian_Ulangan.objects.filter(mo_siswa__murid_profil_uuid=uuidnyaMurid).values('mo_kelas__skl_k_kelas_nama', 'mo_semester__skl_s_semester').annotate(avg_sem=Avg('mo_nilai'),).order_by('mo_semester'),
		'uts': Mo_Penilaian_UTS.objects.filter(mo_siswa__murid_profil_uuid=uuidnyaMurid).values('mo_kelas__skl_k_kelas_nama', 'mo_semester__skl_s_semester').annotate(avg_sem=Avg('mo_nilai'),).order_by('mo_semester'),
		'uas': Mo_Penilaian_UAS.objects.filter(mo_siswa__murid_profil_uuid=uuidnyaMurid).values('mo_kelas__skl_k_kelas_nama', 'mo_semester__skl_s_semester').annotate(avg_sem=Avg('mo_nilai'),).order_by('mo_semester'),
		'ekskul': Mo_Penilaian_Ekskul.objects.filter(mo_siswa__murid_profil_uuid=uuidnyaMurid).values('mo_kelas__skl_k_kelas_nama', 'mo_semester__skl_s_semester').annotate(Avg('mo_nilai')).order_by('mo_semester'),
		'juara_ekskul': Mo_Juara_Ekskul.objects.filter(mo_siswa__murid_profil_uuid=uuidnyaMurid),
	}

	data_grafik = {
		'tugas':{
			'1': [],
			'2': [],
			'3': [],
			'4': [],
			'5': [],
			'6': [],
		},
		'avg_sem':{
			'1': [],
			'2': [],
			'3': [],
			'4': [],
			'5': [],
			'6': [],
		},
		'all_mean': None,
		
	}
	x = chain(data_angka['pengetahuan'], data_angka['keterampilan'], data_angka['ulangan'], data_angka['uts'], data_angka['uas'])
	for a in x:
		if a['mo_semester__skl_s_semester'] == 1:
			data_grafik['avg_sem']['1'].append(a['avg_sem'])
		elif a['mo_semester__skl_s_semester'] == 2:
			data_grafik['avg_sem']['2'].append(a['avg_sem'])
		elif a['mo_semester__skl_s_semester'] == 3:
			data_grafik['avg_sem']['3'].append(a['avg_sem'])
		elif a['mo_semester__skl_s_semester'] == 4:
			data_grafik['avg_sem']['4'].append(a['avg_sem'])
		elif a['mo_semester__skl_s_semester'] == 5:
			data_grafik['avg_sem']['5'].append(a['avg_sem'])
		elif a['mo_semester__skl_s_semester'] == 6:
			data_grafik['avg_sem']['6'].append(a['avg_sem'])
	
	try:
		data_grafik['avg_sem']['1'] = round(statistics.mean(data_grafik['avg_sem']['1']))
	except:
		data_grafik['avg_sem']['1'] = 'NaN'
	try:
		data_grafik['avg_sem']['2'] = round(statistics.mean(data_grafik['avg_sem']['2']))
	except:
		data_grafik['avg_sem']['2'] = 'NaN'
	try:
		data_grafik['avg_sem']['3'] = round(statistics.mean(data_grafik['avg_sem']['3']))
	except:
		data_grafik['avg_sem']['3'] = 'NaN'
	try:
		data_grafik['avg_sem']['4'] = round(statistics.mean(data_grafik['avg_sem']['4']))
	except:
		data_grafik['avg_sem']['4'] = 'NaN'
	try:
		data_grafik['avg_sem']['5'] = round(statistics.mean(data_grafik['avg_sem']['5']))
	except:
		data_grafik['avg_sem']['5'] = 'NaN'
	try:
		data_grafik['avg_sem']['6'] = round(statistics.mean(data_grafik['avg_sem']['6']))
	except:
		data_grafik['avg_sem']['6'] = 'NaN'

	all_mean = 0
	i = 0
	for n in range(1,7):
		o = str(n)
		if data_grafik['avg_sem'][o] != "NaN":
			all_mean += data_grafik['avg_sem'][o]
			i += 1
		else:
			pass
	data_grafik['all_mean'] = all_mean/i



	data_mean_pelajaran = {
		'pengetahuan': Mo_Penilaian_Pengetahuan.objects.filter(mo_siswa__murid_profil_uuid=uuidnyaMurid).values('mo_mata_pelajaran_wajib__mapel_wajib_pelajaran', 'mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran').annotate(Avg('mo_nilai_P1_TGS'), Avg('mo_nilai_P2_TLS'), Avg('mo_nilai_P3_TLS'), avg_sem=(Avg('mo_nilai_P1_TGS')+Avg('mo_nilai_P2_TLS')+Avg('mo_nilai_P3_TLS'))/3).order_by('mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran',),
		'keterampilan': Mo_Penilaian_Keterampilan.objects.filter(mo_siswa__murid_profil_uuid=uuidnyaMurid).values('mo_mata_pelajaran_wajib__mapel_wajib_pelajaran', 'mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran').annotate(Avg('mo_praktek'), Avg('mo_produk'), Avg('mo_proyek'), Avg('mo_portofolio'), avg_sem=(Avg('mo_praktek')+Avg('mo_produk')+Avg('mo_proyek')+Avg('mo_portofolio'))/4).order_by('mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran',),
		'sosial': Mo_Sikap_Sosial.objects.filter(mo_siswa__murid_profil_uuid=uuidnyaMurid).values('mo_mata_pelajaran_wajib__mapel_wajib_pelajaran', 'mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran').annotate(avg_sem=Avg('mo_proyeksi_nilai'),).order_by('mo_mata_pelajaran_wajib__mapel_wajib_pelajaran', 'mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran'),
		'spiritual': Mo_Sikap_Spiritual.objects.filter(mo_siswa__murid_profil_uuid=uuidnyaMurid).values('mo_mata_pelajaran_wajib__mapel_wajib_pelajaran', 'mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran').annotate(avg_sem=Avg('mo_proyeksi_nilai'),).order_by('mo_mata_pelajaran_wajib__mapel_wajib_pelajaran', 'mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran'),
		'ulangan': Mo_Penilaian_Ulangan.objects.filter(mo_siswa__murid_profil_uuid=uuidnyaMurid).values('mo_mata_pelajaran_wajib__mapel_wajib_pelajaran', 'mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran').annotate(avg_sem=Avg('mo_nilai'),).order_by('mo_mata_pelajaran_wajib__mapel_wajib_pelajaran', 'mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran'),
		'uts': Mo_Penilaian_UTS.objects.filter(mo_siswa__murid_profil_uuid=uuidnyaMurid).values('mo_mata_pelajaran_wajib__mapel_wajib_pelajaran', 'mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran').annotate(avg_sem=Avg('mo_nilai'),).order_by('mo_mata_pelajaran_wajib__mapel_wajib_pelajaran', 'mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran'),
		'uas': Mo_Penilaian_UAS.objects.filter(mo_siswa__murid_profil_uuid=uuidnyaMurid).values('mo_mata_pelajaran_wajib__mapel_wajib_pelajaran', 'mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran').annotate(avg_sem=Avg('mo_nilai'),).order_by('mo_mata_pelajaran_wajib__mapel_wajib_pelajaran', 'mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran'),
	}
	data_pelajaran = {
		'pengetahuan': {},
		'keterampilan': {},
		'sosial': {},
		'spiritual': {},
		'ulangan': {},
		'uts': {},
		'uas': {},
	}
	for data_keys in data_pelajaran.keys():
		print(data_keys)
		for data in data_mean_pelajaran[data_keys]:
			if data['mo_mata_pelajaran_wajib__mapel_wajib_pelajaran'] is not None:
				try:
					data_pelajaran[data_keys][data['mo_mata_pelajaran_wajib__mapel_wajib_pelajaran']] = round(data['avg_sem'], 1)
				except:
					data_pelajaran[data_keys][data['mo_mata_pelajaran_wajib__mapel_wajib_pelajaran']] = 0
			elif data['mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran'] is not None:
				try:
					data_pelajaran[data_keys][data['mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran']] = round(data['avg_sem'], 1)
				except:
					data_pelajaran[data_keys][data['mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran']] = 0


	data_avg_tugas_sem = {
		'label': {},
		'nilai': {},
	}

	list_avg_tugas_sem = {
		'label': [],
		'nilai': [],
	}

	for x in data_pelajaran['pengetahuan'].keys():
		for y in data_pelajaran['keterampilan'].keys():
			if x == y:
				o = str(x)
				k = o.replace(" ", "")
				data_avg_tugas_sem['nilai'][o] = round(((data_pelajaran['pengetahuan'][x] + data_pelajaran['keterampilan'][x])/2),1)
				data_avg_tugas_sem['label'][o] = str(o)
			else:
				o = str(x)
				k = o.replace(" ", "")
				data_avg_tugas_sem['nilai'][o] = round(data_pelajaran['pengetahuan'][x], 1)
				data_avg_tugas_sem['label'][o] = str(o)
	for a in data_avg_tugas_sem['nilai'].keys():
		list_avg_tugas_sem['label'].append(str(a))
		list_avg_tugas_sem['nilai'].append(data_avg_tugas_sem['nilai'][str(a)])
	zip_avg = zip(list_avg_tugas_sem['label'], list_avg_tugas_sem['nilai'])



	catatan_bk = BK_Catatan.objects.filter(bk_catatan_siswa__murid_profil_uuid=uuidnyaMurid)
	catatan_guru = Gu_Catatan.objects.filter(guru_catatan_siswa__murid_profil_uuid=uuidnyaMurid)
	context = {
		'data_angka': data_angka,
		'data_grafik': json.dumps(data_grafik),
		'data_mean_pelajaran': data_mean_pelajaran,
		'data_avg_tugas_sem': data_avg_tugas_sem,
		'all_mean': data_grafik['all_mean'],
		'catatan_bk': catatan_bk,
		'catatan_guru': catatan_guru,
		'siswa': siswa,


		'zip_avg': zip_avg,
	}
	return render(request, 'templates_bk/page_nilai_siswa/page_nilai_siswa_detail.html', context)

def page_bk_catatan(request):
	catatan = BK_Catatan.objects.all()

	context = {
		'catatan': catatan,
	}	
	return render(request, 'templates_bk/page_kelola_catatan/page_bk_catatan.html', context)

class page_bk_catatan_create(CreateView):
	model = BK_Catatan
	form_class = page_bk_catatan_forms
	success_url = reverse_lazy('monitoring:page_bk_catatan')
	template_name = 'templates_bk/page_kelola_catatan/page_bk_catatan_create.html'

class page_bk_catatan_update(UpdateView):
	model = BK_Catatan
	form_class = page_bk_catatan_forms
	success_url = reverse_lazy('monitoring:page_bk_catatan')
	template_name = 'templates_bk/page_kelola_catatan/page_bk_catatan_update.html'

class page_bk_catatan_delete(DeleteView):
	model = BK_Catatan
	success_url = reverse_lazy('monitoring:page_bk_catatan')
	template_name = 'templates_bk/page_kelola_catatan/page_bk_catatan_delete.html'
