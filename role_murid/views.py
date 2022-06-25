from django.shortcuts import render
from role_murid.models import *
from role_murid.forms import *
from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.forms import modelformset_factory, formset_factory
from django.db.models import Avg, Count, Sum, Max
from role_guru.models import *
from monitoring.models import *
from sekolah.models import *
import json
import statistics

# Create your views here.

def page_murid_dashboard(request):

	context = {}
	return render(request, 'templates_murid/dashboard_murid_r.html')

def page_murid_profil(request):
	profil_murid = Profil_Murid.objects.get(murid_user=request.user)
	kelas = SKL_Kelas.objects.all()
	context={
		'profil_murid': profil_murid,
		'kelas': kelas,
	}
	return render(request, 'templates_murid/page_profil_murid/profil_murid.html', context)

class page_murid_profil_update(UpdateView):
	model = Profil_Murid
	form_class = page_murid_profil_forms
	success_url = reverse_lazy("monitoring:page_murid_profil")
	template_name = 'templates_murid/page_profil_murid/profil_murid_update.html'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['kelas'] = SKL_Kelas.objects.all()
		return context

def page_murid_nilai(request):
	kelas = SKL_Kelas.objects.all()
	siswa = Profil_Murid.objects.get(murid_user=request.user)

	data_angka = {
		'wajib':{
			'pengetahuan': Mo_Penilaian_Pengetahuan.objects.filter(mo_siswa__murid_profil_uuid=siswa.murid_profil_uuid, mo_mata_pelajaran_jurusan__isnull=True).values('mo_mata_pelajaran_wajib__mapel_wajib_pelajaran', 'mo_mata_pelajaran_wajib__mapel_wajib_pelajaran_uuid').annotate(Avg('mo_nilai_P1_TGS'), Avg('mo_nilai_P2_TLS'), Avg('mo_nilai_P3_TLS')).order_by("mo_mata_pelajaran_wajib__mapel_wajib_pelajaran"),
			'keterampilan': Mo_Penilaian_Keterampilan.objects.filter(mo_siswa__murid_profil_uuid=siswa.murid_profil_uuid, mo_mata_pelajaran_jurusan__isnull=True).values('mo_mata_pelajaran_wajib__mapel_wajib_pelajaran', 'mo_mata_pelajaran_wajib__mapel_wajib_pelajaran_uuid').annotate(Avg('mo_praktek'), Avg('mo_produk'), Avg('mo_proyek'), Avg('mo_portofolio')).order_by("mo_mata_pelajaran_wajib__mapel_wajib_pelajaran"),
			'sosial': Mo_Sikap_Sosial.objects.filter(mo_siswa__murid_profil_uuid=siswa.murid_profil_uuid, mo_mata_pelajaran_jurusan__isnull=True).values('mo_mata_pelajaran_wajib__mapel_wajib_pelajaran', 'mo_mata_pelajaran_wajib__mapel_wajib_pelajaran_uuid').annotate(Avg('mo_proyeksi_nilai')).order_by("mo_mata_pelajaran_wajib__mapel_wajib_pelajaran"),
			'spiritual': Mo_Sikap_Sosial.objects.filter(mo_siswa__murid_profil_uuid=siswa.murid_profil_uuid, mo_mata_pelajaran_jurusan__isnull=True).values('mo_mata_pelajaran_wajib__mapel_wajib_pelajaran', 'mo_mata_pelajaran_wajib__mapel_wajib_pelajaran_uuid').annotate(Avg('mo_proyeksi_nilai')).order_by("mo_mata_pelajaran_wajib__mapel_wajib_pelajaran"),
			'ulangan': Mo_Penilaian_Ulangan.objects.filter(mo_siswa__murid_profil_uuid=siswa.murid_profil_uuid, mo_mata_pelajaran_jurusan__isnull=True).values('mo_mata_pelajaran_wajib__mapel_wajib_pelajaran', 'mo_mata_pelajaran_wajib__mapel_wajib_pelajaran_uuid').annotate(Avg('mo_nilai')).order_by("mo_mata_pelajaran_wajib__mapel_wajib_pelajaran"),
			'uts': Mo_Penilaian_UTS.objects.filter(mo_siswa__murid_profil_uuid=siswa.murid_profil_uuid, mo_mata_pelajaran_jurusan__isnull=True).values('mo_mata_pelajaran_wajib__mapel_wajib_pelajaran', 'mo_mata_pelajaran_wajib__mapel_wajib_pelajaran_uuid').annotate(Avg('mo_nilai')).order_by("mo_mata_pelajaran_wajib__mapel_wajib_pelajaran"),
			'uas': Mo_Penilaian_UAS.objects.filter(mo_siswa__murid_profil_uuid=siswa.murid_profil_uuid, mo_mata_pelajaran_jurusan__isnull=True).values('mo_mata_pelajaran_wajib__mapel_wajib_pelajaran', 'mo_mata_pelajaran_wajib__mapel_wajib_pelajaran_uuid').annotate(Avg('mo_nilai')).order_by("mo_mata_pelajaran_wajib__mapel_wajib_pelajaran"),
			'uas': Mo_Penilaian_UAS.objects.filter(mo_siswa__murid_profil_uuid=siswa.murid_profil_uuid, mo_mata_pelajaran_jurusan__isnull=True).values('mo_mata_pelajaran_wajib__mapel_wajib_pelajaran', 'mo_mata_pelajaran_wajib__mapel_wajib_pelajaran_uuid').annotate(Avg('mo_nilai')).order_by("mo_mata_pelajaran_wajib__mapel_wajib_pelajaran"),
			'ekskul': Mo_Penilaian_Ekskul.objects.filter(mo_siswa__murid_profil_uuid=siswa.murid_profil_uuid,).values('mo_ekskul__skl_ekskul').annotate(Avg('mo_nilai')),
			'juara': Mo_Juara_Ekskul.objects.filter(mo_siswa__murid_profil_uuid=siswa.murid_profil_uuid,),
		},
		'jurusan':{
			'pengetahuan': Mo_Penilaian_Pengetahuan.objects.filter(mo_siswa__murid_profil_uuid=siswa.murid_profil_uuid, mo_mata_pelajaran_wajib__isnull=True).values('mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran', 'mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran_uuid').annotate(Avg('mo_nilai_P1_TGS'), Avg('mo_nilai_P2_TLS'), Avg('mo_nilai_P3_TLS')).order_by("mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran"),
			'keterampilan': Mo_Penilaian_Keterampilan.objects.filter(mo_siswa__murid_profil_uuid=siswa.murid_profil_uuid, mo_mata_pelajaran_wajib__isnull=True).values('mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran', 'mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran_uuid').annotate(Avg('mo_praktek'), Avg('mo_produk'), Avg('mo_proyek'), Avg('mo_portofolio')).order_by("mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran"),
			'sosial': Mo_Sikap_Sosial.objects.filter(mo_siswa__murid_profil_uuid=siswa.murid_profil_uuid, mo_mata_pelajaran_wajib__isnull=True).values('mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran', 'mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran_uuid').annotate(Avg('mo_proyeksi_nilai')).order_by("mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran"),
			'spiritual': Mo_Sikap_Sosial.objects.filter(mo_siswa__murid_profil_uuid=siswa.murid_profil_uuid, mo_mata_pelajaran_wajib__isnull=True).values('mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran', 'mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran_uuid').annotate(Avg('mo_proyeksi_nilai')).order_by("mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran"),
			'ulangan': Mo_Penilaian_Ulangan.objects.filter(mo_siswa__murid_profil_uuid=siswa.murid_profil_uuid, mo_mata_pelajaran_wajib__isnull=True).values('mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran', 'mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran_uuid').annotate(Avg('mo_nilai')).order_by("mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran"),
			'uts': Mo_Penilaian_UTS.objects.filter(mo_siswa__murid_profil_uuid=siswa.murid_profil_uuid, mo_mata_pelajaran_wajib__isnull=True).values('mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran', 'mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran_uuid').annotate(Avg('mo_nilai')).order_by("mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran"),
			'uas': Mo_Penilaian_UAS.objects.filter(mo_siswa__murid_profil_uuid=siswa.murid_profil_uuid, mo_mata_pelajaran_wajib__isnull=True).values('mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran', 'mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran_uuid').annotate(Avg('mo_nilai')).order_by("mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran"),
			'uas': Mo_Penilaian_UAS.objects.filter(mo_siswa__murid_profil_uuid=siswa.murid_profil_uuid, mo_mata_pelajaran_wajib__isnull=True).values('mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran', 'mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran_uuid').annotate(Avg('mo_nilai')).order_by("mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran"),
			'ekskul': Mo_Penilaian_Ekskul.objects.filter(mo_siswa__murid_profil_uuid=siswa.murid_profil_uuid,).values('mo_ekskul__skl_ekskul').annotate(Avg('mo_nilai')),
			'juara': Mo_Juara_Ekskul.objects.filter(mo_siswa__murid_profil_uuid=siswa.murid_profil_uuid,),
		},
		
		
	}
	context = {
		'kelas': kelas,
		'data_angka': data_angka,

	}
	return render(request, 'templates_murid/page_nilai_murid/nilai_murid.html', context)

def page_murid_nilai_wajib_detail(request, uuidPelajaran):
	siswa = Profil_Murid.objects.get(murid_user=request.user)
	nilai = Mo_Penilaian_Pengetahuan.objects.filter(mo_mata_pelajaran_wajib__mapel_wajib_pelajaran_uuid=uuidPelajaran).order_by('mo_kelas', 'mo_semester', 'mo_tahun_ajaran')
	pelajaran = SKL_Mata_Pelajaran_Wajib.objects.get(mapel_wajib_pelajaran_uuid=uuidPelajaran)
	
	data_angka = {
		'wajib':{
			'pengetahuan': Mo_Penilaian_Pengetahuan.objects.filter(mo_siswa__murid_profil_uuid=siswa.murid_profil_uuid, mo_mata_pelajaran_wajib__mapel_wajib_pelajaran_uuid=uuidPelajaran).order_by('mo_kelas', 'mo_semester', 'mo_tahun_ajaran'),
			'keterampilan': Mo_Penilaian_Keterampilan.objects.filter(mo_siswa__murid_profil_uuid=siswa.murid_profil_uuid, mo_mata_pelajaran_wajib__mapel_wajib_pelajaran_uuid=uuidPelajaran).order_by('mo_kelas', 'mo_semester', 'mo_tahun_ajaran'),
			'sosial': Mo_Sikap_Sosial.objects.filter(mo_siswa__murid_profil_uuid=siswa.murid_profil_uuid, mo_mata_pelajaran_wajib__mapel_wajib_pelajaran_uuid=uuidPelajaran).order_by('mo_kelas', 'mo_semester', 'mo_tahun_ajaran'),
			'spiritual': Mo_Sikap_Spiritual.objects.filter(mo_siswa__murid_profil_uuid=siswa.murid_profil_uuid, mo_mata_pelajaran_wajib__mapel_wajib_pelajaran_uuid=uuidPelajaran).order_by('mo_kelas', 'mo_semester', 'mo_tahun_ajaran'),
			'ulangan': Mo_Penilaian_Ulangan.objects.filter(mo_siswa__murid_profil_uuid=siswa.murid_profil_uuid, mo_mata_pelajaran_wajib__mapel_wajib_pelajaran_uuid=uuidPelajaran).order_by('mo_kelas', 'mo_semester', 'mo_tahun_ajaran'),
			'uts': Mo_Penilaian_UTS.objects.filter(mo_siswa__murid_profil_uuid=siswa.murid_profil_uuid, mo_mata_pelajaran_wajib__mapel_wajib_pelajaran_uuid=uuidPelajaran).order_by('mo_kelas', 'mo_semester', 'mo_tahun_ajaran'),
			'uas': Mo_Penilaian_UAS.objects.filter(mo_siswa__murid_profil_uuid=siswa.murid_profil_uuid, mo_mata_pelajaran_wajib__mapel_wajib_pelajaran_uuid=uuidPelajaran).order_by('mo_kelas', 'mo_semester', 'mo_tahun_ajaran'),
			'uas': Mo_Penilaian_UAS.objects.filter(mo_siswa__murid_profil_uuid=siswa.murid_profil_uuid, mo_mata_pelajaran_wajib__mapel_wajib_pelajaran_uuid=uuidPelajaran).order_by('mo_kelas', 'mo_semester', 'mo_tahun_ajaran'),
		},
		
	}

	data_grafik = {
		'wajib': {
			'pengetahuan': {
				'label': [],
				'nilai': [],
			},
			'keterampilan': {
				'label': [],
				'nilai': [],
			},
			'sosial': {
				
			},
			'spiritual': {
			
			},
			'ulangan': {
				'label': [],
				'nilai': [],
			},
			'uts': {
				'label': [],
				'nilai': [],
			},
			'uas': {
				'label': [],
				'nilai': [],
			},

		}
	}

	grafik_pengetahuan = data_angka['wajib']['pengetahuan'].values('mo_semester__skl_s_semester').annotate(avg_sem=(Avg('mo_nilai_P1_TGS') + Avg('mo_nilai_P2_TLS') + Avg('mo_nilai_P3_TLS'))/3)
	for data in grafik_pengetahuan:
		# print(data)
		# o = f"'{data['mo_semester__skl_s_semester']}'"
		o = str(data['mo_semester__skl_s_semester'])
		data_grafik['wajib']['pengetahuan']['label'].append(o)
		data_grafik['wajib']['pengetahuan']['nilai'].append(round(data['avg_sem'],1))

	grafik_keterampilan = data_angka['wajib']['keterampilan'].values('mo_semester__skl_s_semester').annotate(avg_sem=(Avg('mo_praktek') + Avg('mo_produk') + Avg('mo_proyek') + Avg('mo_portofolio'))/4)
	for data in grafik_keterampilan:
		# print(data)
		# o = f"'{data['mo_semester__skl_s_semester']}'"
		o = str(data['mo_semester__skl_s_semester'])
		data_grafik['wajib']['keterampilan']['label'].append(o)
		data_grafik['wajib']['keterampilan']['nilai'].append(round(data['avg_sem'],1))

	# grafik_sosial = data_angka['wajib']['sosial'].values('mo_semester__skl_s_semester', 'mo_nilai').annotate(Count('mo_nilai', distinct=True))
	grafik_sosial = data_angka['wajib']['sosial'].values('mo_semester__skl_s_semester', 'mo_nilai')
	x = data_grafik['wajib']['sosial']
	for data in grafik_sosial:
		d = str(data['mo_semester__skl_s_semester'])
		x[d] = []
		for data_2 in grafik_sosial:
			l = str(data_2['mo_semester__skl_s_semester'])
			if d == l:
				x[d].append(data_2['mo_nilai'])
	for key in x.keys():
		q = []
		for data in x[key]:
			q.append(data)
		x[key] = statistics.mode(q)

	grafik_spiritual = data_angka['wajib']['spiritual'].values('mo_semester__skl_s_semester', 'mo_nilai')
	xx = data_grafik['wajib']['spiritual']
	for data in grafik_spiritual:
		d = str(data['mo_semester__skl_s_semester'])
		xx[d] = []
		for data_2 in grafik_spiritual:
			l = str(data_2['mo_semester__skl_s_semester'])
			if d == l:
				xx[d].append(data_2['mo_nilai'])
	for key in xx.keys():
		q = []
		for data in xx[key]:
			q.append(data)
		xx[key] = statistics.mode(q)



	context = {
		'pelajaran': pelajaran,
		'data_angka': data_angka,
		'data_grafik': json.dumps(data_grafik),
	}
	
	return render(request, 'templates_murid/page_nilai_murid/nilai_murid_detail.html', context)


def page_murid_nilai_jurusan_detail(request, uuidPelajaran):
	siswa = Profil_Murid.objects.get(murid_user=request.user)
	nilai = Mo_Penilaian_Pengetahuan.objects.filter(mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran_uuid=uuidPelajaran).order_by('mo_kelas', 'mo_semester', 'mo_tahun_ajaran')
	pelajaran = SKL_Mata_Pelajaran_Jurusan.objects.get(mapel_jurusan_pelajaran_uuid=uuidPelajaran)
	
	data_angka = {
		'jurusan':{
			'pengetahuan': Mo_Penilaian_Pengetahuan.objects.filter(mo_siswa__murid_profil_uuid=siswa.murid_profil_uuid, mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran_uuid=uuidPelajaran).order_by('mo_kelas', 'mo_semester', 'mo_tahun_ajaran'),
			'keterampilan': Mo_Penilaian_Keterampilan.objects.filter(mo_siswa__murid_profil_uuid=siswa.murid_profil_uuid, mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran_uuid=uuidPelajaran).order_by('mo_kelas', 'mo_semester', 'mo_tahun_ajaran'),
			'sosial': Mo_Sikap_Sosial.objects.filter(mo_siswa__murid_profil_uuid=siswa.murid_profil_uuid, mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran_uuid=uuidPelajaran).order_by('mo_kelas', 'mo_semester', 'mo_tahun_ajaran'),
			'spiritual': Mo_Sikap_Spiritual.objects.filter(mo_siswa__murid_profil_uuid=siswa.murid_profil_uuid, mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran_uuid=uuidPelajaran).order_by('mo_kelas', 'mo_semester', 'mo_tahun_ajaran'),
			'ulangan': Mo_Penilaian_Ulangan.objects.filter(mo_siswa__murid_profil_uuid=siswa.murid_profil_uuid, mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran_uuid=uuidPelajaran).order_by('mo_kelas', 'mo_semester', 'mo_tahun_ajaran'),
			'uts': Mo_Penilaian_UTS.objects.filter(mo_siswa__murid_profil_uuid=siswa.murid_profil_uuid, mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran_uuid=uuidPelajaran).order_by('mo_kelas', 'mo_semester', 'mo_tahun_ajaran'),
			'uas': Mo_Penilaian_UAS.objects.filter(mo_siswa__murid_profil_uuid=siswa.murid_profil_uuid, mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran_uuid=uuidPelajaran).order_by('mo_kelas', 'mo_semester', 'mo_tahun_ajaran'),
			'uas': Mo_Penilaian_UAS.objects.filter(mo_siswa__murid_profil_uuid=siswa.murid_profil_uuid, mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran_uuid=uuidPelajaran).order_by('mo_kelas', 'mo_semester', 'mo_tahun_ajaran'),
		},
		
	}

	data_grafik = {
		'jurusan': {
			'pengetahuan': {
				'label': [],
				'nilai': [],
			},
			'keterampilan': {
				'label': [],
				'nilai': [],
			},
			'sosial': {
				
			},
			'spiritual': {
			
			},
			'ulangan': {
				'label': [],
				'nilai': [],
			},
			'uts': {
				'label': [],
				'nilai': [],
			},
			'uas': {
				'label': [],
				'nilai': [],
			},

		}
	}

	grafik_pengetahuan = data_angka['jurusan']['pengetahuan'].values('mo_semester__skl_s_semester').annotate(avg_sem=(Avg('mo_nilai_P1_TGS') + Avg('mo_nilai_P2_TLS') + Avg('mo_nilai_P3_TLS'))/3)
	for data in grafik_pengetahuan:
		# print(data)
		# o = f"'{data['mo_semester__skl_s_semester']}'"
		o = str(data['mo_semester__skl_s_semester'])
		data_grafik['jurusan']['pengetahuan']['label'].append(o)
		data_grafik['jurusan']['pengetahuan']['nilai'].append(round(data['avg_sem'],1))

	grafik_keterampilan = data_angka['jurusan']['keterampilan'].values('mo_semester__skl_s_semester').annotate(avg_sem=(Avg('mo_praktek') + Avg('mo_produk') + Avg('mo_proyek') + Avg('mo_portofolio'))/4)
	for data in grafik_keterampilan:
		# print(data)
		# o = f"'{data['mo_semester__skl_s_semester']}'"
		o = str(data['mo_semester__skl_s_semester'])
		data_grafik['jurusan']['keterampilan']['label'].append(o)
		data_grafik['jurusan']['keterampilan']['nilai'].append(round(data['avg_sem'],1))

	# grafik_sosial = data_angka['jurusan']['sosial'].values('mo_semester__skl_s_semester', 'mo_nilai').annotate(Count('mo_nilai', distinct=True))
	grafik_sosial = data_angka['jurusan']['sosial'].values('mo_semester__skl_s_semester', 'mo_nilai')
	x = data_grafik['jurusan']['sosial']
	for data in grafik_sosial:
		d = str(data['mo_semester__skl_s_semester'])
		x[d] = []
		for data_2 in grafik_sosial:
			l = str(data_2['mo_semester__skl_s_semester'])
			if d == l:
				x[d].append(data_2['mo_nilai'])
	for key in x.keys():
		q = []
		for data in x[key]:
			q.append(data)
		x[key] = statistics.mode(q)

	grafik_spiritual = data_angka['jurusan']['spiritual'].values('mo_semester__skl_s_semester', 'mo_nilai')
	xx = data_grafik['jurusan']['spiritual']
	for data in grafik_spiritual:
		d = str(data['mo_semester__skl_s_semester'])
		xx[d] = []
		for data_2 in grafik_spiritual:
			l = str(data_2['mo_semester__skl_s_semester'])
			if d == l:
				xx[d].append(data_2['mo_nilai'])
	for key in xx.keys():
		q = []
		for data in xx[key]:
			q.append(data)
		xx[key] = statistics.mode(q)



	context = {
		'pelajaran': pelajaran,
		'data_angka': data_angka,
		'data_grafik': json.dumps(data_grafik),
	}
	
	return render(request, 'templates_murid/page_nilai_murid/nilai_murid_detail_jurusan.html', context)