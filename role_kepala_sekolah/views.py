from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.forms import modelformset_factory, formset_factory
from django.db.models import Avg, Count, Sum, Max
from sekolah.models import *
from role_guru.models import *
from role_kepala_sekolah.forms import *
from role_kepala_sekolah.filters import *
from role_murid.models import *
from role_kepala_sekolah.models import Profil_Kepsek
from monitoring.models import *
from sekolah.models import *
import json
import statistics


def queryTerbanyakKata(var):
	aa = var
	bb = {}
	cc = {
		'siswa': [],
		'nilai': [],
	}
	for x in aa:
		o = []
		for l in aa:
			o.append(x['mo_nilai'])
		try:
			bb[x['mo_siswa__murid_nama']] = statistics.mode(o)
		except:
			bb[x['mo_siswa__murid_nama']] = 'Tidak ada data'
	for x in bb:
		cc['siswa'].append(str(x))
		cc['nilai'].append(bb[x])
	pp = zip(cc['siswa'], cc['nilai'])
	return pp

def aksesQueryUntukGrafik(var1, var2, uuidPelajaran):
	if var1 == 'pengetahuan_wajib':
		aa = Mo_Penilaian_Pengetahuan.objects.filter(mo_kelas__skl_k_kelas_nama__contains=var2, mo_mata_pelajaran_wajib__mapel_wajib_pelajaran_uuid=uuidPelajaran).values('mo_semester__skl_s_semester', 'mo_kelas__skl_k_kelas_nama',).annotate(avg_a=(Avg('mo_nilai_P1_TGS') + Avg('mo_nilai_P2_TLS') + Avg('mo_nilai_P3_TLS'))/3)
		return aa
	elif var1 == 'keterampilan_wajib':
		aa = Mo_Penilaian_Keterampilan.objects.filter(mo_kelas__skl_k_kelas_nama__contains=var2, mo_mata_pelajaran_wajib__mapel_wajib_pelajaran_uuid=uuidPelajaran).values('mo_semester__skl_s_semester', 'mo_kelas__skl_k_kelas_nama',).annotate(avg_a=(Avg('mo_praktek') + Avg('mo_produk') + Avg('mo_proyek') + Avg('mo_portofolio'))/4)
		return aa
	elif var1 == 'pengetahuan_jurusan':
		aa = Mo_Penilaian_Pengetahuan.objects.filter(mo_kelas__skl_k_kelas_nama__contains=var2, mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran_uuid=uuidPelajaran).values('mo_semester__skl_s_semester', 'mo_kelas__skl_k_kelas_nama',).annotate(avg_a=(Avg('mo_nilai_P1_TGS') + Avg('mo_nilai_P2_TLS') + Avg('mo_nilai_P3_TLS'))/3)
		return aa
	elif var1 == 'keterampilan_jurusan':
		aa = Mo_Penilaian_Keterampilan.objects.filter(mo_kelas__skl_k_kelas_nama__contains=var2, mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran_uuid=uuidPelajaran).values('mo_semester__skl_s_semester', 'mo_kelas__skl_k_kelas_nama',).annotate(avg_a=(Avg('mo_praktek') + Avg('mo_produk') + Avg('mo_proyek') + Avg('mo_portofolio'))/4)
		return aa


# Create your views here.
def page_kepsek_dashboard(request):
	kelas = SKL_Kelas.objects.all()
	context={
		'kelas':kelas,
	}
	return render(request, 'templates_kepsek/dashboard_kepsek_r.html', context)

def page_kepsek_profil(request):
	profil_kepsek = Profil_Kepsek.objects.get(kepsek_user=request.user)
	kelas = SKL_Kelas.objects.all()
	context={
		'profil_kepsek': profil_kepsek,
		'kelas': kelas,
	}
	return render(request, 'templates_kepsek/page_profil_kepsek/profil_kepsek.html', context)

class page_kepsek_profil_update(UpdateView):
	model = Profil_Kepsek
	form_class = page_kepsek_profil_forms
	success_url = reverse_lazy("monitoring:page_kepsek_profil")
	template_name = 'templates_kepsek/page_profil_kepsek/profil_kepsek_update.html'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['kelas'] = SKL_Kelas.objects.all()
		return context

def page_kepsek_kompetensi_dasar(request):
	mapel_wajib = SKL_Mata_Pelajaran_Wajib.objects.all()
	mapel_jurusan = SKL_Mata_Pelajaran_Jurusan.objects.all().order_by('-mapel_jurusan_jurusan')
	kd_mapel_wajib = Gu_Data_Kompetensi_Dasar.objects.all()

	context = {
		'mapel_wajib': mapel_wajib,
		'mapel_jurusan': mapel_jurusan,
	}

	return render(request, 'templates_kepsek/page_kompetensi_dasar/page_kompetensi_dasar_landing.html', context)

def page_kepsek_kompetensi_dasar_wajib_detail(request, uuidPelajaran):
	mapel_wajib = SKL_Mata_Pelajaran_Wajib.objects.get(mapel_wajib_pelajaran_uuid=uuidPelajaran)
	kd_mapel_wajib = Gu_Data_Kompetensi_Dasar.objects.filter(guru_kompetensi_dasar_mata_pelajaran_wajib__mapel_wajib_pelajaran_uuid=uuidPelajaran).order_by('guru_kompetensi_dasar_kelas', 'guru_nomor_kd')
	kompetensi_dasar = page_kepsek_kompetensi_dasar_wajib_filter(request.GET, queryset=kd_mapel_wajib)

	context = {
		'mapel_wajib': mapel_wajib,
		'kd_mapel_wajib': kd_mapel_wajib,
		'kompetensi_dasar': kompetensi_dasar,
	}
	return render(request, 'templates_kepsek/page_kompetensi_dasar/page_kompetensi_dasar_wajib_detail.html', context)

def page_kepsek_kompetensi_dasar_jurusan_detail(request, uuidPelajaran):
	mapel_jurusan = SKL_Mata_Pelajaran_Jurusan.objects.get(mapel_jurusan_pelajaran_uuid=uuidPelajaran)
	kd_mapel_jurusan = Gu_Data_Kompetensi_Dasar.objects.filter(guru_kompetensi_dasar_mata_pelajaran_jurusan__mapel_jurusan_pelajaran_uuid=uuidPelajaran).order_by('guru_kompetensi_dasar_kelas', 'guru_nomor_kd')
	kompetensi_dasar = page_kepsek_kompetensi_dasar_jurusan_filter(request.GET, queryset=kd_mapel_jurusan)

	context = {
		'mapel_jurusan': mapel_jurusan,
		'kd_mapel_jurusan': kd_mapel_jurusan,
		'kompetensi_dasar': kompetensi_dasar,
	}
	return render(request, 'templates_kepsek/page_kompetensi_dasar/page_kompetensi_dasar_jurusan_detail.html', context)

def page_kepsek_performa_mapel(request):
	# guru = Gu_Profil_Guru.objects.all()
	mapel_wajib = SKL_Mata_Pelajaran_Wajib.objects.all()
	mapel_jurusan = SKL_Mata_Pelajaran_Jurusan.objects.all().order_by('-mapel_jurusan_jurusan')

	context = {
		# 'guru': guru,
		'mapel_wajib': mapel_wajib,
		'mapel_jurusan': mapel_jurusan,
	}
	return render(request, 'templates_kepsek/page_performa_mapel/page_performa_mapel.html', context)


def page_kepsek_performa_mapel_wajib_detail(request, uuidPelajaran):
	mapel_wajib = SKL_Mata_Pelajaran_Wajib.objects.get(mapel_wajib_pelajaran_uuid=uuidPelajaran)
	data_angka = {
		'kelas_10':{
			'pengetahuan': Mo_Penilaian_Pengetahuan.objects.filter(mo_kelas__skl_k_kelas_nama__contains="10", mo_mata_pelajaran_wajib__mapel_wajib_pelajaran_uuid=uuidPelajaran).values('mo_siswa__murid_nama', 'mo_kelas__skl_k_kelas_nama', 'mo_semester__skl_s_semester').annotate(Avg('mo_nilai_P1_TGS'), Avg('mo_nilai_P2_TLS'), Avg('mo_nilai_P3_TLS')).order_by('mo_kelas', 'mo_siswa__murid_nama'),
			'keterampilan': Mo_Penilaian_Keterampilan.objects.filter(mo_kelas__skl_k_kelas_nama__contains="10", mo_mata_pelajaran_wajib__mapel_wajib_pelajaran_uuid=uuidPelajaran).values('mo_siswa__murid_nama', 'mo_kelas__skl_k_kelas_nama', 'mo_semester__skl_s_semester').annotate(Avg('mo_praktek'), Avg('mo_produk'), Avg('mo_proyek'), Avg('mo_portofolio')).order_by('mo_kelas', 'mo_siswa__murid_nama'),
			'sosial': queryTerbanyakKata(Mo_Sikap_Sosial.objects.filter(mo_kelas__skl_k_kelas_nama__contains="10", mo_mata_pelajaran_wajib__mapel_wajib_pelajaran_uuid=uuidPelajaran).values('mo_siswa__murid_nama','mo_nilai')),
			'spiritual': queryTerbanyakKata(Mo_Sikap_Spiritual.objects.filter(mo_kelas__skl_k_kelas_nama__contains="10", mo_mata_pelajaran_wajib__mapel_wajib_pelajaran_uuid=uuidPelajaran).values('mo_siswa__murid_nama','mo_nilai')),
		},
		'kelas_11':{
			'pengetahuan': Mo_Penilaian_Pengetahuan.objects.filter(mo_kelas__skl_k_kelas_nama__contains="11", mo_mata_pelajaran_wajib__mapel_wajib_pelajaran_uuid=uuidPelajaran).values('mo_siswa__murid_nama', 'mo_kelas__skl_k_kelas_nama', 'mo_semester__skl_s_semester').annotate(Avg('mo_nilai_P1_TGS'), Avg('mo_nilai_P2_TLS'), Avg('mo_nilai_P3_TLS')).order_by('mo_kelas', 'mo_siswa__murid_nama'),
			'keterampilan': Mo_Penilaian_Keterampilan.objects.filter(mo_kelas__skl_k_kelas_nama__contains="11", mo_mata_pelajaran_wajib__mapel_wajib_pelajaran_uuid=uuidPelajaran).values('mo_siswa__murid_nama', 'mo_kelas__skl_k_kelas_nama', 'mo_semester__skl_s_semester').annotate(Avg('mo_praktek'), Avg('mo_produk'), Avg('mo_proyek'), Avg('mo_portofolio')).order_by('mo_kelas', 'mo_siswa__murid_nama'),
			'sosial': queryTerbanyakKata(Mo_Sikap_Sosial.objects.filter(mo_kelas__skl_k_kelas_nama__contains="11", mo_mata_pelajaran_wajib__mapel_wajib_pelajaran_uuid=uuidPelajaran).values('mo_siswa__murid_nama','mo_nilai')),
			'spiritual': queryTerbanyakKata(Mo_Sikap_Spiritual.objects.filter(mo_kelas__skl_k_kelas_nama__contains="11", mo_mata_pelajaran_wajib__mapel_wajib_pelajaran_uuid=uuidPelajaran).values('mo_siswa__murid_nama','mo_nilai')),
		},
		'kelas_12':{
			'pengetahuan': Mo_Penilaian_Pengetahuan.objects.filter(mo_kelas__skl_k_kelas_nama__contains="12", mo_mata_pelajaran_wajib__mapel_wajib_pelajaran_uuid=uuidPelajaran).values('mo_siswa__murid_nama', 'mo_kelas__skl_k_kelas_nama', 'mo_semester__skl_s_semester').annotate(Avg('mo_nilai_P1_TGS'), Avg('mo_nilai_P2_TLS'), Avg('mo_nilai_P3_TLS')).order_by('mo_kelas', 'mo_siswa__murid_nama'),
			'keterampilan': Mo_Penilaian_Keterampilan.objects.filter(mo_kelas__skl_k_kelas_nama__contains="12", mo_mata_pelajaran_wajib__mapel_wajib_pelajaran_uuid=uuidPelajaran).values('mo_siswa__murid_nama', 'mo_kelas__skl_k_kelas_nama', 'mo_semester__skl_s_semester').annotate(Avg('mo_praktek'), Avg('mo_produk'), Avg('mo_proyek'), Avg('mo_portofolio')).order_by('mo_kelas', 'mo_siswa__murid_nama'),
			'sosial': queryTerbanyakKata(Mo_Sikap_Sosial.objects.filter(mo_kelas__skl_k_kelas_nama__contains="12", mo_mata_pelajaran_wajib__mapel_wajib_pelajaran_uuid=uuidPelajaran).values('mo_siswa__murid_nama','mo_nilai')),
			'spiritual': queryTerbanyakKata(Mo_Sikap_Spiritual.objects.filter(mo_kelas__skl_k_kelas_nama__contains="12", mo_mata_pelajaran_wajib__mapel_wajib_pelajaran_uuid=uuidPelajaran).values('mo_siswa__murid_nama','mo_nilai')),
		},
	}	

	# aa = Mo_Penilaian_Pengetahuan.objects.filter(mo_kelas__skl_k_kelas_nama__contains="10", mo_mata_pelajaran_wajib__mapel_wajib_pelajaran_uuid=uuidPelajaran).values('mo_semester__skl_s_semester', 'mo_kelas__skl_k_kelas_nama',).annotate(avg_a=(Avg('mo_nilai_P1_TGS') + Avg('mo_nilai_P2_TLS') + Avg('mo_nilai_P3_TLS'))/3)
	# for a in aksesQueryUntukGrafik('pengetahuan', '10', uuidPelajaran):
	# 	print('aaaaa', a)

	data_grafik = {
		'kelas_10':{
			'pengetahuan':{
				'kelas':[],
				'semester_1':{
					'kelas': [],
					'nilai': [],
				},
				'semester_2':{
					'kelas': [],
					'nilai': [],
				},
			},
			'keterampilan':{
				'kelas':[],
				'semester_1':{
					'kelas': [],
					'nilai': [],
				},
				'semester_2':{
					'kelas': [],
					'nilai': [],
				},
			}
		},
		'kelas_11':{
			'pengetahuan':{
				'kelas':[],
				'semester_1':{
					'kelas': [],
					'nilai': [],
				},
				'semester_2':{
					'kelas': [],
					'nilai': [],
				},
			},
			'keterampilan':{
				'kelas':[],
				'semester_1':{
					'kelas': [],
					'nilai': [],
				},
				'semester_2':{
					'kelas': [],
					'nilai': [],
				},
			}
		},
		'kelas_12':{
			'pengetahuan':{
				'kelas':[],
				'semester_1':{
					'kelas': [],
					'nilai': [],
				},
				'semester_2':{
					'kelas': [],
					'nilai': [],
				},
			},
			'keterampilan':{
				'kelas':[],
				'semester_1':{
					'kelas': [],
					'nilai': [],
				},
				'semester_2':{
					'kelas': [],
					'nilai': [],
				},
			}
		}
	}

	for data in aksesQueryUntukGrafik('pengetahuan_wajib', '10', uuidPelajaran):
		data_grafik['kelas_10']['pengetahuan']['semester_1']['kelas'].append(data['mo_kelas__skl_k_kelas_nama'])
		if data['mo_semester__skl_s_semester'] == 1:
			if data['avg_a'] is not None:
				data_grafik['kelas_10']['pengetahuan']['semester_1']['nilai'].append(data['avg_a'])
			else:
				data_grafik['kelas_10']['pengetahuan']['semester_1']['nilai'].append(0)
		if data['mo_semester__skl_s_semester'] == 2:
			if data['avg_a'] is not None:
				data_grafik['kelas_10']['pengetahuan']['semester_2']['nilai'].append(data['avg_a'])
			else:
				data_grafik['kelas_10']['pengetahuan']['semester_2']['nilai'].append(0)
	data_grafik['kelas_10']['pengetahuan']['kelas'] = list(dict.fromkeys(data_grafik['kelas_10']['pengetahuan']['semester_1']['kelas']))
	for data in aksesQueryUntukGrafik('pengetahuan_wajib', '11', uuidPelajaran):
		data_grafik['kelas_11']['pengetahuan']['semester_1']['kelas'].append(data['mo_kelas__skl_k_kelas_nama'])
		if data['mo_semester__skl_s_semester'] == 1:
			if data['avg_a'] is not None:
				data_grafik['kelas_11']['pengetahuan']['semester_1']['nilai'].append(data['avg_a'])
			else:
				data_grafik['kelas_11']['pengetahuan']['semester_1']['nilai'].append(0)
		if data['mo_semester__skl_s_semester'] == 2:
			if data['avg_a'] is not None:
				data_grafik['kelas_11']['pengetahuan']['semester_2']['nilai'].append(data['avg_a'])
			else:
				data_grafik['kelas_11']['pengetahuan']['semester_2']['nilai'].append(0)
	data_grafik['kelas_11']['pengetahuan']['kelas'] = list(dict.fromkeys(data_grafik['kelas_11']['pengetahuan']['semester_1']['kelas']))
	for data in aksesQueryUntukGrafik('pengetahuan_wajib', '12', uuidPelajaran):
		data_grafik['kelas_12']['pengetahuan']['semester_1']['kelas'].append(data['mo_kelas__skl_k_kelas_nama'])
		if data['mo_semester__skl_s_semester'] == 1:
			if data['avg_a'] is not None:
				data_grafik['kelas_12']['pengetahuan']['semester_1']['nilai'].append(data['avg_a'])
			else:
				data_grafik['kelas_12']['pengetahuan']['semester_1']['nilai'].append(0)
		if data['mo_semester__skl_s_semester'] == 2:
			if data['avg_a'] is not None:
				data_grafik['kelas_12']['pengetahuan']['semester_2']['nilai'].append(data['avg_a'])
			else:
				data_grafik['kelas_12']['pengetahuan']['semester_2']['nilai'].append(0)
	data_grafik['kelas_12']['pengetahuan']['kelas'] = list(dict.fromkeys(data_grafik['kelas_12']['pengetahuan']['semester_1']['kelas']))

	for data in aksesQueryUntukGrafik('keterampilan_wajib', '10', uuidPelajaran):
		data_grafik['kelas_10']['keterampilan']['semester_1']['kelas'].append(data['mo_kelas__skl_k_kelas_nama'])
		if data['mo_semester__skl_s_semester'] == 1:
			if data['avg_a'] is not None:
				data_grafik['kelas_10']['keterampilan']['semester_1']['nilai'].append(data['avg_a'])
			else:
				data_grafik['kelas_10']['keterampilan']['semester_1']['nilai'].append(0)
		if data['mo_semester__skl_s_semester'] == 2:
			if data['avg_a'] is not None:
				data_grafik['kelas_10']['keterampilan']['semester_2']['nilai'].append(data['avg_a'])
			else:
				data_grafik['kelas_10']['keterampilan']['semester_2']['nilai'].append(0)
	data_grafik['kelas_10']['keterampilan']['kelas'] = list(dict.fromkeys(data_grafik['kelas_10']['keterampilan']['semester_1']['kelas']))
	for data in aksesQueryUntukGrafik('keterampilan_wajib', '11', uuidPelajaran):
		data_grafik['kelas_11']['keterampilan']['semester_1']['kelas'].append(data['mo_kelas__skl_k_kelas_nama'])
		if data['mo_semester__skl_s_semester'] == 1:
			if data['avg_a'] is not None:
				data_grafik['kelas_11']['keterampilan']['semester_1']['nilai'].append(data['avg_a'])
			else:
				data_grafik['kelas_11']['keterampilan']['semester_1']['nilai'].append(0)
		if data['mo_semester__skl_s_semester'] == 2:
			if data['avg_a'] is not None:
				data_grafik['kelas_11']['keterampilan']['semester_2']['nilai'].append(data['avg_a'])
			else:
				data_grafik['kelas_11']['keterampilan']['semester_2']['nilai'].append(0)
	data_grafik['kelas_11']['keterampilan']['kelas'] = list(dict.fromkeys(data_grafik['kelas_11']['keterampilan']['semester_1']['kelas']))
	for data in aksesQueryUntukGrafik('keterampilan_wajib', '12', uuidPelajaran):
		data_grafik['kelas_12']['keterampilan']['semester_1']['kelas'].append(data['mo_kelas__skl_k_kelas_nama'])
		if data['mo_semester__skl_s_semester'] == 1:
			if data['avg_a'] is not None:
				data_grafik['kelas_12']['keterampilan']['semester_1']['nilai'].append(data['avg_a'])
			else:
				data_grafik['kelas_12']['keterampilan']['semester_1']['nilai'].append(0)
		if data['mo_semester__skl_s_semester'] == 2:
			if data['avg_a'] is not None:
				data_grafik['kelas_12']['keterampilan']['semester_2']['nilai'].append(data['avg_a'])
			else:
				data_grafik['kelas_12']['keterampilan']['semester_2']['nilai'].append(0)
	data_grafik['kelas_12']['keterampilan']['kelas'] = list(dict.fromkeys(data_grafik['kelas_12']['keterampilan']['semester_1']['kelas']))
	# print(data_grafik)

	context = {
		'mapel_wajib': mapel_wajib,
		'data_angka': data_angka,
		'data_grafik': json.dumps(data_grafik)

	}
	return render(request, 'templates_kepsek/page_performa_mapel/page_performa_mapel_wajib_detail.html', context)


def page_kepsek_performa_mapel_jurusan_detail(request, uuidPelajaran):
	mapel_jurusan = SKL_Mata_Pelajaran_Jurusan.objects.get(mapel_jurusan_pelajaran_uuid=uuidPelajaran)
	data_angka = {
		'kelas_10':{
			'pengetahuan': Mo_Penilaian_Pengetahuan.objects.filter(mo_kelas__skl_k_kelas_nama__contains="10", mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran_uuid=uuidPelajaran).values('mo_siswa__murid_nama', 'mo_kelas__skl_k_kelas_nama', 'mo_semester__skl_s_semester').annotate(Avg('mo_nilai_P1_TGS'), Avg('mo_nilai_P2_TLS'), Avg('mo_nilai_P3_TLS')).order_by('mo_kelas', 'mo_siswa__murid_nama'),
			'keterampilan': Mo_Penilaian_Keterampilan.objects.filter(mo_kelas__skl_k_kelas_nama__contains="10", mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran_uuid=uuidPelajaran).values('mo_siswa__murid_nama', 'mo_kelas__skl_k_kelas_nama', 'mo_semester__skl_s_semester').annotate(Avg('mo_praktek'), Avg('mo_produk'), Avg('mo_proyek'), Avg('mo_portofolio')).order_by('mo_kelas', 'mo_siswa__murid_nama'),
			'sosial': queryTerbanyakKata(Mo_Sikap_Sosial.objects.filter(mo_kelas__skl_k_kelas_nama__contains="10", mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran_uuid=uuidPelajaran).values('mo_siswa__murid_nama','mo_nilai')),
			'spiritual': queryTerbanyakKata(Mo_Sikap_Spiritual.objects.filter(mo_kelas__skl_k_kelas_nama__contains="10", mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran_uuid=uuidPelajaran).values('mo_siswa__murid_nama','mo_nilai')),
		},
		'kelas_11':{
			'pengetahuan': Mo_Penilaian_Pengetahuan.objects.filter(mo_kelas__skl_k_kelas_nama__contains="11", mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran_uuid=uuidPelajaran).values('mo_siswa__murid_nama', 'mo_kelas__skl_k_kelas_nama', 'mo_semester__skl_s_semester').annotate(Avg('mo_nilai_P1_TGS'), Avg('mo_nilai_P2_TLS'), Avg('mo_nilai_P3_TLS')).order_by('mo_kelas', 'mo_siswa__murid_nama'),
			'keterampilan': Mo_Penilaian_Keterampilan.objects.filter(mo_kelas__skl_k_kelas_nama__contains="11", mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran_uuid=uuidPelajaran).values('mo_siswa__murid_nama', 'mo_kelas__skl_k_kelas_nama', 'mo_semester__skl_s_semester').annotate(Avg('mo_praktek'), Avg('mo_produk'), Avg('mo_proyek'), Avg('mo_portofolio')).order_by('mo_kelas', 'mo_siswa__murid_nama'),
			'sosial': queryTerbanyakKata(Mo_Sikap_Sosial.objects.filter(mo_kelas__skl_k_kelas_nama__contains="11", mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran_uuid=uuidPelajaran).values('mo_siswa__murid_nama','mo_nilai')),
			'spiritual': queryTerbanyakKata(Mo_Sikap_Spiritual.objects.filter(mo_kelas__skl_k_kelas_nama__contains="11", mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran_uuid=uuidPelajaran).values('mo_siswa__murid_nama','mo_nilai')),
		},
		'kelas_12':{
			'pengetahuan': Mo_Penilaian_Pengetahuan.objects.filter(mo_kelas__skl_k_kelas_nama__contains="12", mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran_uuid=uuidPelajaran).values('mo_siswa__murid_nama', 'mo_kelas__skl_k_kelas_nama', 'mo_semester__skl_s_semester').annotate(Avg('mo_nilai_P1_TGS'), Avg('mo_nilai_P2_TLS'), Avg('mo_nilai_P3_TLS')).order_by('mo_kelas', 'mo_siswa__murid_nama'),
			'keterampilan': Mo_Penilaian_Keterampilan.objects.filter(mo_kelas__skl_k_kelas_nama__contains="12", mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran_uuid=uuidPelajaran).values('mo_siswa__murid_nama', 'mo_kelas__skl_k_kelas_nama', 'mo_semester__skl_s_semester').annotate(Avg('mo_praktek'), Avg('mo_produk'), Avg('mo_proyek'), Avg('mo_portofolio')).order_by('mo_kelas', 'mo_siswa__murid_nama'),
			'sosial': queryTerbanyakKata(Mo_Sikap_Sosial.objects.filter(mo_kelas__skl_k_kelas_nama__contains="12", mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran_uuid=uuidPelajaran).values('mo_siswa__murid_nama','mo_nilai')),
			'spiritual': queryTerbanyakKata(Mo_Sikap_Spiritual.objects.filter(mo_kelas__skl_k_kelas_nama__contains="12", mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran_uuid=uuidPelajaran).values('mo_siswa__murid_nama','mo_nilai')),
		},
	}	

	# aa = Mo_Penilaian_Pengetahuan.objects.filter(mo_kelas__skl_k_kelas_nama__contains="10", mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran_uuid=uuidPelajaran).values('mo_semester__skl_s_semester', 'mo_kelas__skl_k_kelas_nama',).annotate(avg_a=(Avg('mo_nilai_P1_TGS') + Avg('mo_nilai_P2_TLS') + Avg('mo_nilai_P3_TLS'))/3)
	# for a in aksesQueryUntukGrafik('pengetahuan', '10', uuidPelajaran):
	# 	print('aaaaa', a)

	data_grafik = {
		'kelas_10':{
			'pengetahuan':{
				'kelas':[],
				'semester_1':{
					'kelas': [],
					'nilai': [],
				},
				'semester_2':{
					'kelas': [],
					'nilai': [],
				},
			},
			'keterampilan':{
				'kelas':[],
				'semester_1':{
					'kelas': [],
					'nilai': [],
				},
				'semester_2':{
					'kelas': [],
					'nilai': [],
				},
			}
		},
		'kelas_11':{
			'pengetahuan':{
				'kelas':[],
				'semester_1':{
					'kelas': [],
					'nilai': [],
				},
				'semester_2':{
					'kelas': [],
					'nilai': [],
				},
			},
			'keterampilan':{
				'kelas':[],
				'semester_1':{
					'kelas': [],
					'nilai': [],
				},
				'semester_2':{
					'kelas': [],
					'nilai': [],
				},
			}
		},
		'kelas_12':{
			'pengetahuan':{
				'kelas':[],
				'semester_1':{
					'kelas': [],
					'nilai': [],
				},
				'semester_2':{
					'kelas': [],
					'nilai': [],
				},
			},
			'keterampilan':{
				'kelas':[],
				'semester_1':{
					'kelas': [],
					'nilai': [],
				},
				'semester_2':{
					'kelas': [],
					'nilai': [],
				},
			}
		}
	}

	for data in aksesQueryUntukGrafik('pengetahuan_jurusan', '10', uuidPelajaran):
		data_grafik['kelas_10']['pengetahuan']['semester_1']['kelas'].append(data['mo_kelas__skl_k_kelas_nama'])
		if data['mo_semester__skl_s_semester'] == 1:
			if data['avg_a'] is not None:
				data_grafik['kelas_10']['pengetahuan']['semester_1']['nilai'].append(data['avg_a'])
			else:
				data_grafik['kelas_10']['pengetahuan']['semester_1']['nilai'].append(0)
		if data['mo_semester__skl_s_semester'] == 2:
			if data['avg_a'] is not None:
				data_grafik['kelas_10']['pengetahuan']['semester_2']['nilai'].append(data['avg_a'])
			else:
				data_grafik['kelas_10']['pengetahuan']['semester_2']['nilai'].append(0)
	data_grafik['kelas_10']['pengetahuan']['kelas'] = list(dict.fromkeys(data_grafik['kelas_10']['pengetahuan']['semester_1']['kelas']))
	for data in aksesQueryUntukGrafik('pengetahuan_jurusan', '11', uuidPelajaran):
		data_grafik['kelas_11']['pengetahuan']['semester_1']['kelas'].append(data['mo_kelas__skl_k_kelas_nama'])
		if data['mo_semester__skl_s_semester'] == 1:
			if data['avg_a'] is not None:
				data_grafik['kelas_11']['pengetahuan']['semester_1']['nilai'].append(data['avg_a'])
			else:
				data_grafik['kelas_11']['pengetahuan']['semester_1']['nilai'].append(0)
		if data['mo_semester__skl_s_semester'] == 2:
			if data['avg_a'] is not None:
				data_grafik['kelas_11']['pengetahuan']['semester_2']['nilai'].append(data['avg_a'])
			else:
				data_grafik['kelas_11']['pengetahuan']['semester_2']['nilai'].append(0)
	data_grafik['kelas_11']['pengetahuan']['kelas'] = list(dict.fromkeys(data_grafik['kelas_11']['pengetahuan']['semester_1']['kelas']))
	for data in aksesQueryUntukGrafik('pengetahuan_jurusan', '12', uuidPelajaran):
		data_grafik['kelas_12']['pengetahuan']['semester_1']['kelas'].append(data['mo_kelas__skl_k_kelas_nama'])
		if data['mo_semester__skl_s_semester'] == 1:
			if data['avg_a'] is not None:
				data_grafik['kelas_12']['pengetahuan']['semester_1']['nilai'].append(data['avg_a'])
			else:
				data_grafik['kelas_12']['pengetahuan']['semester_1']['nilai'].append(0)
		if data['mo_semester__skl_s_semester'] == 2:
			if data['avg_a'] is not None:
				data_grafik['kelas_12']['pengetahuan']['semester_2']['nilai'].append(data['avg_a'])
			else:
				data_grafik['kelas_12']['pengetahuan']['semester_2']['nilai'].append(0)
	data_grafik['kelas_12']['pengetahuan']['kelas'] = list(dict.fromkeys(data_grafik['kelas_12']['pengetahuan']['semester_1']['kelas']))

	for data in aksesQueryUntukGrafik('keterampilan_jurusan', '10', uuidPelajaran):
		data_grafik['kelas_10']['keterampilan']['semester_1']['kelas'].append(data['mo_kelas__skl_k_kelas_nama'])
		if data['mo_semester__skl_s_semester'] == 1:
			if data['avg_a'] is not None:
				data_grafik['kelas_10']['keterampilan']['semester_1']['nilai'].append(data['avg_a'])
			else:
				data_grafik['kelas_10']['keterampilan']['semester_1']['nilai'].append(0)
		if data['mo_semester__skl_s_semester'] == 2:
			if data['avg_a'] is not None:
				data_grafik['kelas_10']['keterampilan']['semester_2']['nilai'].append(data['avg_a'])
			else:
				data_grafik['kelas_10']['keterampilan']['semester_2']['nilai'].append(0)
	data_grafik['kelas_10']['keterampilan']['kelas'] = list(dict.fromkeys(data_grafik['kelas_10']['keterampilan']['semester_1']['kelas']))
	for data in aksesQueryUntukGrafik('keterampilan_jurusan', '11', uuidPelajaran):
		data_grafik['kelas_11']['keterampilan']['semester_1']['kelas'].append(data['mo_kelas__skl_k_kelas_nama'])
		if data['mo_semester__skl_s_semester'] == 1:
			if data['avg_a'] is not None:
				data_grafik['kelas_11']['keterampilan']['semester_1']['nilai'].append(data['avg_a'])
			else:
				data_grafik['kelas_11']['keterampilan']['semester_1']['nilai'].append(0)
		if data['mo_semester__skl_s_semester'] == 2:
			if data['avg_a'] is not None:
				data_grafik['kelas_11']['keterampilan']['semester_2']['nilai'].append(data['avg_a'])
			else:
				data_grafik['kelas_11']['keterampilan']['semester_2']['nilai'].append(0)
	data_grafik['kelas_11']['keterampilan']['kelas'] = list(dict.fromkeys(data_grafik['kelas_11']['keterampilan']['semester_1']['kelas']))
	for data in aksesQueryUntukGrafik('keterampilan_jurusan', '12', uuidPelajaran):
		data_grafik['kelas_12']['keterampilan']['semester_1']['kelas'].append(data['mo_kelas__skl_k_kelas_nama'])
		if data['mo_semester__skl_s_semester'] == 1:
			if data['avg_a'] is not None:
				data_grafik['kelas_12']['keterampilan']['semester_1']['nilai'].append(data['avg_a'])
			else:
				data_grafik['kelas_12']['keterampilan']['semester_1']['nilai'].append(0)
		if data['mo_semester__skl_s_semester'] == 2:
			if data['avg_a'] is not None:
				data_grafik['kelas_12']['keterampilan']['semester_2']['nilai'].append(data['avg_a'])
			else:
				data_grafik['kelas_12']['keterampilan']['semester_2']['nilai'].append(0)
	data_grafik['kelas_12']['keterampilan']['kelas'] = list(dict.fromkeys(data_grafik['kelas_12']['keterampilan']['semester_1']['kelas']))
	# print(data_grafik)

	context = {
		'mapel_jurusan': mapel_jurusan,
		'data_angka': data_angka,
		'data_grafik': json.dumps(data_grafik)

	}
	return render(request, 'templates_kepsek/page_performa_mapel/page_performa_mapel_jurusan_detail.html', context)


def page_kepsek_performa_kelas_landing(request):
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
	return render(request, 'templates_kepsek/page_performa_kelas/page_performa_kelas.html', context)


def page_kepsek_performa_kelas_detail(request, uuidnyaKelas):
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
	return render(request, 'templates_kepsek/page_performa_kelas/page_performa_kelas_detail.html', context)


def page_kepsek_performa_ekskul_landing(request):
	ekskul = SKL_Ekskul.objects.all()
	context = {
		'ekskul': ekskul,
	}
	return render(request, 'templates_kepsek/page_performa_ekskul/page_performa_ekskul.html', context)
	
def page_kepsek_performa_ekskul_detail(request, uuidEkskul):
	info = SKL_Ekskul.objects.get(skl_ekskul_uuid=uuidEkskul)
	nilai_ekskul = Mo_Penilaian_Ekskul.objects.filter(mo_ekskul__skl_ekskul_uuid=uuidEkskul)
	nilai_ekskul_mean = nilai_ekskul.values('mo_siswa__murid_nama').annotate(Avg('mo_nilai'))
	juara = Mo_Juara_Ekskul.objects.filter(mo_ekskul__skl_ekskul_uuid=uuidEkskul)

	context = {
		'info': info,
		'nilai_ekskul': nilai_ekskul.order_by('mo_kelas', 'mo_siswa__murid_nama', 'mo_tahun_ajaran'),
		'nilai_ekskul_mean': nilai_ekskul_mean.order_by('mo_siswa__murid_nama'),
		'juara': juara,
		'total_juara': juara.count(),
	}
	return render(request, 'templates_kepsek/page_performa_ekskul/page_performa_ekskul_detail.html', context)
	
