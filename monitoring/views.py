from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.forms import modelformset_factory, formset_factory
from django.db.models import Avg, Count
from role_guru.models import *
from role_guru.forms import *
from role_guru.filters import *
from role_murid.models import *
from monitoring.models import *
from sekolah.models import *
import statistics
import pandas as pd


# CUSTOM FUNCTION FAHMI
def JarakEnter(var):
	i = 0
	while i < var:
		print("\n")
		i += 1 

def page_guru_mean_nilai_siswa_wajib(request):
	kelas = SKL_Kelas.objects.all()
	guru = Gu_Profil_Guru.objects.get(guru_user=request.user)
	data = {
		'kelas_10': {
			'pengetahuan': Mo_Penilaian_Pengetahuan.objects.filter(mo_kelas__skl_k_kelas_nama__contains="10", mo_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib).values('mo_siswa__murid_nama','mo_siswa__murid_profil_uuid', 'mo_kelas__skl_k_kelas_nama').annotate(Avg('mo_nilai_P1_TGS'), Avg('mo_nilai_P2_TLS'), Avg('mo_nilai_P3_TLS')).order_by("mo_siswa__murid_nama"),
			'keterampilan': Mo_Penilaian_Keterampilan.objects.filter(mo_kelas__skl_k_kelas_nama__contains="10", mo_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib).values('mo_siswa__murid_nama','mo_siswa__murid_profil_uuid', 'mo_kelas__skl_k_kelas_nama').annotate(Avg('mo_praktek'), Avg('mo_produk'), Avg('mo_proyek'), Avg('mo_portofolio')).order_by("mo_siswa__murid_nama"),
			'sikap_sosial': Mo_Sikap_Sosial.objects.filter(mo_kelas__skl_k_kelas_nama__contains="10", mo_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib).values('mo_siswa__murid_nama','mo_siswa__murid_profil_uuid', 'mo_kelas__skl_k_kelas_nama').annotate(Avg("mo_proyeksi_nilai")).order_by("mo_siswa__murid_nama"),
			'sikap_spiritual': Mo_Sikap_Spiritual.objects.filter(mo_kelas__skl_k_kelas_nama__contains="10", mo_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib).values('mo_siswa__murid_nama','mo_siswa__murid_profil_uuid', 'mo_kelas__skl_k_kelas_nama').annotate(Avg("mo_proyeksi_nilai")).order_by("mo_siswa__murid_nama"),
			'ulangan': Mo_Penilaian_Ulangan.objects.filter(mo_kelas__skl_k_kelas_nama__contains="10", mo_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib).values('mo_siswa__murid_nama','mo_siswa__murid_profil_uuid', 'mo_kelas__skl_k_kelas_nama').annotate(Avg('mo_nilai')),
			'uts': Mo_Penilaian_UTS.objects.filter(mo_kelas__skl_k_kelas_nama__contains="10", mo_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib).values('mo_siswa__murid_nama','mo_siswa__murid_profil_uuid', 'mo_kelas__skl_k_kelas_nama').annotate(Avg('mo_nilai')),
			'uas': Mo_Penilaian_UAS.objects.filter(mo_kelas__skl_k_kelas_nama__contains="10", mo_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib).values('mo_siswa__murid_nama','mo_siswa__murid_profil_uuid', 'mo_kelas__skl_k_kelas_nama').annotate(Avg('mo_nilai')),
		},
		'kelas_11': {
			'pengetahuan': Mo_Penilaian_Pengetahuan.objects.filter(mo_kelas__skl_k_kelas_nama__contains="11", mo_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib).values('mo_siswa__murid_nama','mo_siswa__murid_profil_uuid', 'mo_kelas__skl_k_kelas_nama').annotate(Avg('mo_nilai_P1_TGS'), Avg('mo_nilai_P2_TLS'), Avg('mo_nilai_P3_TLS')).order_by("mo_siswa__murid_nama"),
			'keterampilan': Mo_Penilaian_Keterampilan.objects.filter(mo_kelas__skl_k_kelas_nama__contains="11", mo_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib).values('mo_siswa__murid_nama','mo_siswa__murid_profil_uuid', 'mo_kelas__skl_k_kelas_nama').annotate(Avg('mo_praktek'), Avg('mo_produk'), Avg('mo_proyek'), Avg('mo_portofolio')).order_by("mo_siswa__murid_nama"),
			'sikap_sosial': Mo_Sikap_Sosial.objects.filter(mo_kelas__skl_k_kelas_nama__contains="11", mo_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib).values('mo_siswa__murid_nama','mo_siswa__murid_profil_uuid', 'mo_kelas__skl_k_kelas_nama').annotate(Avg("mo_proyeksi_nilai")).order_by("mo_siswa__murid_nama"),
			'sikap_spiritual': Mo_Sikap_Spiritual.objects.filter(mo_kelas__skl_k_kelas_nama__contains="11", mo_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib).values('mo_siswa__murid_nama','mo_siswa__murid_profil_uuid', 'mo_kelas__skl_k_kelas_nama').annotate(Avg("mo_proyeksi_nilai")).order_by("mo_siswa__murid_nama"),
			'ulangan': Mo_Penilaian_Ulangan.objects.filter(mo_kelas__skl_k_kelas_nama__contains="11", mo_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib).values('mo_siswa__murid_nama','mo_siswa__murid_profil_uuid', 'mo_kelas__skl_k_kelas_nama').annotate(Avg('mo_nilai')),
			'uts': Mo_Penilaian_UTS.objects.filter(mo_kelas__skl_k_kelas_nama__contains="11", mo_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib).values('mo_siswa__murid_nama','mo_siswa__murid_profil_uuid', 'mo_kelas__skl_k_kelas_nama').annotate(Avg('mo_nilai')),
			'uas': Mo_Penilaian_UAS.objects.filter(mo_kelas__skl_k_kelas_nama__contains="11", mo_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib).values('mo_siswa__murid_nama','mo_siswa__murid_profil_uuid', 'mo_kelas__skl_k_kelas_nama').annotate(Avg('mo_nilai')),
			
		},
		'kelas_12': {
			'pengetahuan': Mo_Penilaian_Pengetahuan.objects.filter(mo_kelas__skl_k_kelas_nama__contains="12", mo_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib).values('mo_siswa__murid_nama','mo_siswa__murid_profil_uuid', 'mo_kelas__skl_k_kelas_nama').annotate(Avg('mo_nilai_P1_TGS'), Avg('mo_nilai_P2_TLS'), Avg('mo_nilai_P3_TLS')).order_by("mo_siswa__murid_nama"),
			'keterampilan': Mo_Penilaian_Keterampilan.objects.filter(mo_kelas__skl_k_kelas_nama__contains="12", mo_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib).values('mo_siswa__murid_nama','mo_siswa__murid_profil_uuid', 'mo_kelas__skl_k_kelas_nama').annotate(Avg('mo_praktek'), Avg('mo_produk'), Avg('mo_proyek'), Avg('mo_portofolio')).order_by("mo_siswa__murid_nama"),
			'sikap_sosial': Mo_Sikap_Sosial.objects.filter(mo_kelas__skl_k_kelas_nama__contains="12", mo_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib).values('mo_siswa__murid_nama','mo_siswa__murid_profil_uuid', 'mo_kelas__skl_k_kelas_nama').annotate(Avg("mo_proyeksi_nilai")).order_by("mo_siswa__murid_nama"),
			'sikap_spiritual': Mo_Sikap_Spiritual.objects.filter(mo_kelas__skl_k_kelas_nama__contains="12", mo_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib).values('mo_siswa__murid_nama','mo_siswa__murid_profil_uuid', 'mo_kelas__skl_k_kelas_nama').annotate(Avg("mo_proyeksi_nilai")).order_by("mo_siswa__murid_nama"),
			'ulangan': Mo_Penilaian_Ulangan.objects.filter(mo_kelas__skl_k_kelas_nama__contains="12", mo_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib).values('mo_siswa__murid_nama','mo_siswa__murid_profil_uuid', 'mo_kelas__skl_k_kelas_nama').annotate(Avg('mo_nilai')),
			'uts': Mo_Penilaian_UTS.objects.filter(mo_kelas__skl_k_kelas_nama__contains="12", mo_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib).values('mo_siswa__murid_nama','mo_siswa__murid_profil_uuid', 'mo_kelas__skl_k_kelas_nama').annotate(Avg('mo_nilai')),
			'uas': Mo_Penilaian_UAS.objects.filter(mo_kelas__skl_k_kelas_nama__contains="12", mo_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib).values('mo_siswa__murid_nama','mo_siswa__murid_profil_uuid', 'mo_kelas__skl_k_kelas_nama').annotate(Avg('mo_nilai')),
			
		},
	}
	context = {
		'data': data,
		'guru': guru,
		'kelas': kelas,
	}
	return render(request, 'templates_monitoring/templates_nilai_siswa/monitoring_mean_nilai_mapel_wajib.html', context)
def page_guru_mean_nilai_siswa_wajib_detail(request, uuidnyaMurid):
	kelas = SKL_Kelas.objects.all()
	guru = Gu_Profil_Guru.objects.get(guru_user=request.user)
	identitas_siswa = Profil_Murid.objects.get(murid_profil_uuid=uuidnyaMurid)
	nilai_pengetahuan = Mo_Penilaian_Pengetahuan.objects.filter(mo_siswa__murid_profil_uuid=uuidnyaMurid, mo_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib).order_by('mo_kelas__skl_k_kelas_nama','mo_kompetensi_dasar__guru_nomor_kd')
	nilai_keterampilan = Mo_Penilaian_Keterampilan.objects.filter(mo_siswa__murid_profil_uuid=uuidnyaMurid, mo_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib).order_by('mo_kelas__skl_k_kelas_nama','mo_kompetensi_dasar__guru_nomor_kd')
	nilai_sikap_sosial = Mo_Sikap_Sosial.objects.filter(mo_siswa__murid_profil_uuid=uuidnyaMurid, mo_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib).order_by('mo_kelas__skl_k_kelas_nama','mo_kompetensi_dasar__guru_nomor_kd')
	nilai_sikap_spiritual = Mo_Sikap_Spiritual.objects.filter(mo_siswa__murid_profil_uuid=uuidnyaMurid, mo_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib).order_by('mo_kelas__skl_k_kelas_nama','mo_kompetensi_dasar__guru_nomor_kd')
	
	bagan_donut_nilai_pengetahuan = Mo_Penilaian_Pengetahuan.objects.filter(mo_siswa__murid_profil_uuid=uuidnyaMurid, mo_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib).values('mo_siswa__murid_nama','mo_siswa__murid_profil_uuid', 'mo_kelas__skl_k_kelas_nama').annotate(Avg('mo_nilai_P1_TGS'), Avg('mo_nilai_P2_TLS'), Avg('mo_nilai_P3_TLS'))
	bagan_donut_nilai_keterampilan = Mo_Penilaian_Keterampilan.objects.filter(mo_siswa__murid_profil_uuid=uuidnyaMurid, mo_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib).values('mo_siswa__murid_nama','mo_siswa__murid_profil_uuid', 'mo_kelas__skl_k_kelas_nama').annotate(Avg('mo_praktek'), Avg('mo_produk'), Avg('mo_proyek'), Avg('mo_portofolio'))
	bagan_donut_nilai_sikap_sosial = Mo_Sikap_Sosial.objects.filter(mo_siswa__murid_profil_uuid=uuidnyaMurid, mo_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib).values('mo_siswa__murid_nama','mo_siswa__murid_profil_uuid', 'mo_kelas__skl_k_kelas_nama').annotate(Avg('mo_proyeksi_nilai'))
	bagan_donut_nilai_sikap_spiritual = Mo_Sikap_Spiritual.objects.filter(mo_siswa__murid_profil_uuid=uuidnyaMurid, mo_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib).values('mo_siswa__murid_nama','mo_siswa__murid_profil_uuid', 'mo_kelas__skl_k_kelas_nama').annotate(Avg('mo_proyeksi_nilai'))
	
	mean_bagan_donut_nilai_keterampilan = []
	mean_bagan_donut_nilai_pengetahuan = []
	mean_bagan_donut_nilai_sosial = []
	mean_bagan_donut_nilai_spiritual = []
	for data in bagan_donut_nilai_pengetahuan:
		if data['mo_nilai_P1_TGS__avg'] is not None:
			mean_bagan_donut_nilai_pengetahuan.append(data['mo_nilai_P1_TGS__avg'])
		else:
			mean_bagan_donut_nilai_pengetahuan.append(0)
		if data['mo_nilai_P2_TLS__avg'] is not None:
			mean_bagan_donut_nilai_pengetahuan.append(data['mo_nilai_P2_TLS__avg'])
		else:
			mean_bagan_donut_nilai_pengetahuan.append(0)
		if data['mo_nilai_P3_TLS__avg'] is not None:
			mean_bagan_donut_nilai_pengetahuan.append(data['mo_nilai_P3_TLS__avg'])
		else:
			mean_bagan_donut_nilai_pengetahuan.append(0)

	for data in bagan_donut_nilai_keterampilan:
		if data['mo_praktek__avg'] is not None:
			mean_bagan_donut_nilai_keterampilan.append(data['mo_praktek__avg'])
		else:
			mean_bagan_donut_nilai_keterampilan.append(0)
		if data['mo_produk__avg'] is not None:
			mean_bagan_donut_nilai_keterampilan.append(data['mo_produk__avg'])
		else:
			mean_bagan_donut_nilai_keterampilan.append(0)
		if data['mo_proyek__avg'] is not None:
			mean_bagan_donut_nilai_keterampilan.append(data['mo_proyek__avg'])
		else:
			mean_bagan_donut_nilai_keterampilan.append(0)
		if data['mo_portofolio__avg'] is not None:
			mean_bagan_donut_nilai_keterampilan.append(data['mo_portofolio__avg'])
		else:
			mean_bagan_donut_nilai_keterampilan.append(data['mo_portofolio__avg'])

	for data in bagan_donut_nilai_sikap_sosial:
		if data['mo_proyeksi_nilai__avg'] is not None:
			mean_bagan_donut_nilai_sosial.append(data['mo_proyeksi_nilai__avg'])
		else:
			mean_bagan_donut_nilai_sosial.append(0)

	for data in bagan_donut_nilai_sikap_spiritual:
		if data['mo_proyeksi_nilai__avg'] is not None:
			mean_bagan_donut_nilai_spiritual.append(data['mo_proyeksi_nilai__avg'])
		else:
			mean_bagan_donut_nilai_spiritual.append(0)


	# JarakEnter(5)
	# print('mean_bagan_donut_nilai_pengetahuan: ', mean_bagan_donut_nilai_pengetahuan)
	# print('mean_bagan_donut_nilai_keterampilan: ', mean_bagan_donut_nilai_keterampilan)
	# print('mean_bagan_donut_nilai_sosial: ', mean_bagan_donut_nilai_sosial)
	# print('mean_bagan_donut_nilai_spiritual: ', mean_bagan_donut_nilai_spiritual)
	pp = "LETAK ERROR"

	try:
		mean_bagan_donut_nilai_pengetahuan = statistics.mean(mean_bagan_donut_nilai_pengetahuan)
	except:
		mean_bagan_donut_nilai_pengetahuan = 0
	try:
		mean_bagan_donut_nilai_keterampilan = statistics.mean(mean_bagan_donut_nilai_keterampilan)
	except:
		mean_bagan_donut_nilai_keterampilan = 0
	try:
		mean_bagan_donut_nilai_sosial = statistics.mean(mean_bagan_donut_nilai_sosial)
	except:
		mean_bagan_donut_nilai_sosial = 0
	try:
		mean_bagan_donut_nilai_spiritual = statistics.mean(mean_bagan_donut_nilai_spiritual)
	except:
		mean_bagan_donut_nilai_spiritual = 0

	data_bagan = [
		mean_bagan_donut_nilai_pengetahuan, 
		mean_bagan_donut_nilai_keterampilan, 
		mean_bagan_donut_nilai_sosial, 
		mean_bagan_donut_nilai_spiritual
	]

	grafik_pengetahuan = {
		'kd': [],
		'nilai_P1_TGS': [],
		'nilai_P2_TLS': [],
		'nilai_P3_TLS': [],
	}
	for data in nilai_pengetahuan:
		try:
			x = "'" + data.mo_kompetensi_dasar.guru_nomor_kd + "'"
		except:
			x = "'Tidak ada KD'"
		grafik_pengetahuan['kd'].append(x)
		if data.mo_nilai_P1_TGS is not None:
			grafik_pengetahuan['nilai_P1_TGS'].append(data.mo_nilai_P1_TGS)
		else:
			grafik_pengetahuan['nilai_P1_TGS'].append(0)
		if data.mo_nilai_P2_TLS is not None:
			grafik_pengetahuan['nilai_P2_TLS'].append(data.mo_nilai_P2_TLS)
		else:
			grafik_pengetahuan['nilai_P2_TLS'].append(0)
		if data.mo_nilai_P3_TLS is not None:
			grafik_pengetahuan['nilai_P3_TLS'].append(data.mo_nilai_P3_TLS)
		else:
			grafik_pengetahuan['nilai_P3_TLS'].append(0)

	grafik_keterampilan = {
		'kd': [],
		'praktek': [],
		'produk': [],
		'proyek': [],
		'portofolio': [],
	}
	for data in nilai_keterampilan:
		try:
			x = "'" + data.mo_kompetensi_dasar.guru_nomor_kd + "'"
		except:
			x = "'Tidak ada KD'"
		grafik_keterampilan['kd'].append(x)
		if data.mo_praktek is not None:
			grafik_keterampilan['praktek'].append(data.mo_praktek)
		else:
			grafik_keterampilan['praktek'].append(0)
		if data.mo_produk is not None:
			grafik_keterampilan['produk'].append(data.mo_produk)
		else:
			grafik_keterampilan['produk'].append(0)
		if data.mo_proyek is not None:
			grafik_keterampilan['proyek'].append(data.mo_proyek)
		else:
			grafik_keterampilan['proyek'].append(0)	
		if data.mo_portofolio is not None:
			grafik_keterampilan['portofolio'].append(data.mo_portofolio)
		else:
			grafik_keterampilan['portofolio'].append(0)


	grafik_sikap_sosial = {
		'SB': None,
		'B': None,
		'C': None,
		'K': None,
		'TO': [],
		'nilai': Mo_Sikap_Sosial.objects.filter(mo_siswa__murid_profil_uuid=uuidnyaMurid, mo_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib).values('mo_nilai').annotate(nilai_count=Count('mo_nilai')).order_by('-mo_nilai'),
		'MTO': None,
		'MTOO': [],
	}
	for data in grafik_sikap_sosial['nilai']:
		if data['mo_nilai'] == "Sangat Baik":
			if data['nilai_count'] == None:
				grafik_sikap_spiritual = 0
			else:
				grafik_sikap_sosial['SB'] = data['nilai_count']
		elif data['mo_nilai'] == "Baik":
			grafik_sikap_sosial['B'] = data['nilai_count']
		elif data['mo_nilai'] == "Cukup":
			grafik_sikap_sosial['C'] = data['nilai_count']
		elif data['mo_nilai'] == "Kurang":
			grafik_sikap_sosial['K'] = data['nilai_count']
	for data in nilai_sikap_sosial:
		grafik_sikap_sosial['TO'].append(data.mo_nilai)
	try:
		grafik_sikap_sosial['TO'] = statistics.mode(grafik_sikap_sosial['TO'])
	except:
		grafik_sikap_sosial['TO'] = "Tidak ada nilai"
	grafik_sikap_sosial['MTO'] = [ grafik_sikap_sosial['SB'], grafik_sikap_sosial['B'], grafik_sikap_sosial['C'], grafik_sikap_sosial['K'] ]
	for data in grafik_sikap_sosial['MTO']:
		if data == None:
			grafik_sikap_sosial['MTOO'].append(0)
		else:
			grafik_sikap_sosial['MTOO'].append(data)

	grafik_sikap_spiritual = {
		'SB': None,
		'B': None,
		'C': None,
		'K': None,
		'TO': [],
		'nilai': Mo_Sikap_Spiritual.objects.filter(mo_siswa__murid_profil_uuid=uuidnyaMurid, mo_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib).values('mo_nilai').annotate(nilai_count=Count('mo_nilai')).order_by('-mo_nilai'),
		'MTO': None,
		'MTOO': [],
	}
	for data in grafik_sikap_spiritual['nilai']:
		if data['mo_nilai'] == "Sangat Baik":
			grafik_sikap_spiritual['SB'] = data['nilai_count']
		elif data['mo_nilai'] == "Baik":
			grafik_sikap_spiritual['B'] = data['nilai_count']
		elif data['mo_nilai'] == "Cukup":
			grafik_sikap_spiritual['C'] = data['nilai_count']
		elif data['mo_nilai'] == "Kurang":
			grafik_sikap_spiritual['K'] = data['nilai_count']
	for data in nilai_sikap_spiritual:
		grafik_sikap_spiritual['TO'].append(data.mo_nilai)

	pp = "LETAK ERROR"
	try:
		grafik_sikap_spiritual['TO'] = statistics.mode(grafik_sikap_spiritual['TO'])
	except:
		grafik_sikap_spiritual['TO'] = "Tidak ada"
	grafik_sikap_spiritual['MTO'] = [ grafik_sikap_spiritual['SB'], grafik_sikap_spiritual['B'], grafik_sikap_spiritual['C'], grafik_sikap_spiritual['K'] ]
	for data in grafik_sikap_spiritual['MTO']:
		if data == None:
			grafik_sikap_spiritual['MTOO'].append(0)
		else:
			grafik_sikap_spiritual['MTOO'].append(data)

	# print("grafik_pengetahuan", grafik_pengetahuan)
	# print("grafik_keterampilan: ", grafik_keterampilan)
	# print("grafik_sikap_sosial: ", grafik_sikap_sosial)
	# print("grafik_sikap_spiritual: ", grafik_sikap_spiritual)

	context = {
		'guru': guru,
		'identitas_siswa': identitas_siswa,
		'data_bagan': data_bagan,
		'nilai_pengetahuan': nilai_pengetahuan,
		'grafik_pengetahuan': grafik_pengetahuan,
		'nilai_keterampilan': nilai_keterampilan,
		'grafik_keterampilan': grafik_keterampilan,
		'nilai_sikap_sosial': nilai_sikap_sosial,
		'grafik_sikap_sosial': grafik_sikap_sosial,
		'nilai_sikap_spiritual': nilai_sikap_spiritual,
		'grafik_sikap_spiritual': grafik_sikap_spiritual,
		'kelas': kelas,
	}
	return render(request, 'templates_monitoring/templates_nilai_siswa/templates_detail/monitoring_detail_nilai_mapel_wajib.html', context)

def page_guru_mean_nilai_siswa_jurusan(request):
	kelas = SKL_Kelas.objects.all()
	guru = Gu_Profil_Guru.objects.get(guru_user=request.user)
	data = {
		'kelas_10': {
			'pengetahuan': Mo_Penilaian_Pengetahuan.objects.filter(mo_kelas__skl_k_kelas_nama__contains="10", mo_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan).values('mo_siswa__murid_nama','mo_siswa__murid_profil_uuid', 'mo_kelas__skl_k_kelas_nama').annotate(Avg('mo_nilai_P1_TGS'), Avg('mo_nilai_P2_TLS'), Avg('mo_nilai_P3_TLS')).order_by("mo_siswa__murid_nama"),
			'keterampilan': Mo_Penilaian_Keterampilan.objects.filter(mo_kelas__skl_k_kelas_nama__contains="10", mo_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan).values('mo_siswa__murid_nama','mo_siswa__murid_profil_uuid', 'mo_kelas__skl_k_kelas_nama').annotate(Avg('mo_praktek'), Avg('mo_produk'), Avg('mo_proyek'), Avg('mo_portofolio')).order_by("mo_siswa__murid_nama"),
			'sikap_sosial': Mo_Sikap_Sosial.objects.filter(mo_kelas__skl_k_kelas_nama__contains="10", mo_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan).values('mo_siswa__murid_nama','mo_siswa__murid_profil_uuid', 'mo_kelas__skl_k_kelas_nama').annotate(Avg("mo_proyeksi_nilai")).order_by("mo_siswa__murid_nama"),
			'sikap_spiritual': Mo_Sikap_Spiritual.objects.filter(mo_kelas__skl_k_kelas_nama__contains="10", mo_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan).values('mo_siswa__murid_nama','mo_siswa__murid_profil_uuid', 'mo_kelas__skl_k_kelas_nama').annotate(Avg("mo_proyeksi_nilai")).order_by("mo_siswa__murid_nama"),
			'ulangan': Mo_Penilaian_Ulangan.objects.filter(mo_kelas__skl_k_kelas_nama__contains="10", mo_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan).values('mo_siswa__murid_nama','mo_siswa__murid_profil_uuid', 'mo_kelas__skl_k_kelas_nama').annotate(Avg('mo_nilai')),
			'uts': Mo_Penilaian_UTS.objects.filter(mo_kelas__skl_k_kelas_nama__contains="10", mo_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan).values('mo_siswa__murid_nama','mo_siswa__murid_profil_uuid', 'mo_kelas__skl_k_kelas_nama').annotate(Avg('mo_nilai')),
			'uas': Mo_Penilaian_UAS.objects.filter(mo_kelas__skl_k_kelas_nama__contains="10", mo_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan).values('mo_siswa__murid_nama','mo_siswa__murid_profil_uuid', 'mo_kelas__skl_k_kelas_nama').annotate(Avg('mo_nilai')),
		},
		'kelas_11': {
			'pengetahuan': Mo_Penilaian_Pengetahuan.objects.filter(mo_kelas__skl_k_kelas_nama__contains="11", mo_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan).values('mo_siswa__murid_nama','mo_siswa__murid_profil_uuid', 'mo_kelas__skl_k_kelas_nama').annotate(Avg('mo_nilai_P1_TGS'), Avg('mo_nilai_P2_TLS'), Avg('mo_nilai_P3_TLS')).order_by("mo_siswa__murid_nama"),
			'keterampilan': Mo_Penilaian_Keterampilan.objects.filter(mo_kelas__skl_k_kelas_nama__contains="11", mo_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan).values('mo_siswa__murid_nama','mo_siswa__murid_profil_uuid', 'mo_kelas__skl_k_kelas_nama').annotate(Avg('mo_praktek'), Avg('mo_produk'), Avg('mo_proyek'), Avg('mo_portofolio')).order_by("mo_siswa__murid_nama"),
			'sikap_sosial': Mo_Sikap_Sosial.objects.filter(mo_kelas__skl_k_kelas_nama__contains="11", mo_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan).values('mo_siswa__murid_nama','mo_siswa__murid_profil_uuid', 'mo_kelas__skl_k_kelas_nama').annotate(Avg("mo_proyeksi_nilai")).order_by("mo_siswa__murid_nama"),
			'sikap_spiritual': Mo_Sikap_Spiritual.objects.filter(mo_kelas__skl_k_kelas_nama__contains="11", mo_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan).values('mo_siswa__murid_nama','mo_siswa__murid_profil_uuid', 'mo_kelas__skl_k_kelas_nama').annotate(Avg("mo_proyeksi_nilai")).order_by("mo_siswa__murid_nama"),
			'ulangan': Mo_Penilaian_Ulangan.objects.filter(mo_kelas__skl_k_kelas_nama__contains="11", mo_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan).values('mo_siswa__murid_nama','mo_siswa__murid_profil_uuid', 'mo_kelas__skl_k_kelas_nama').annotate(Avg('mo_nilai')),
			'uts': Mo_Penilaian_UTS.objects.filter(mo_kelas__skl_k_kelas_nama__contains="11", mo_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan).values('mo_siswa__murid_nama','mo_siswa__murid_profil_uuid', 'mo_kelas__skl_k_kelas_nama').annotate(Avg('mo_nilai')),
			'uas': Mo_Penilaian_UAS.objects.filter(mo_kelas__skl_k_kelas_nama__contains="11", mo_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan).values('mo_siswa__murid_nama','mo_siswa__murid_profil_uuid', 'mo_kelas__skl_k_kelas_nama').annotate(Avg('mo_nilai')),
			
		},
		'kelas_12': {
			'pengetahuan': Mo_Penilaian_Pengetahuan.objects.filter(mo_kelas__skl_k_kelas_nama__contains="12", mo_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan).values('mo_siswa__murid_nama','mo_siswa__murid_profil_uuid', 'mo_kelas__skl_k_kelas_nama').annotate(Avg('mo_nilai_P1_TGS'), Avg('mo_nilai_P2_TLS'), Avg('mo_nilai_P3_TLS')).order_by("mo_siswa__murid_nama"),
			'keterampilan': Mo_Penilaian_Keterampilan.objects.filter(mo_kelas__skl_k_kelas_nama__contains="12", mo_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan).values('mo_siswa__murid_nama','mo_siswa__murid_profil_uuid', 'mo_kelas__skl_k_kelas_nama').annotate(Avg('mo_praktek'), Avg('mo_produk'), Avg('mo_proyek'), Avg('mo_portofolio')).order_by("mo_siswa__murid_nama"),
			'sikap_sosial': Mo_Sikap_Sosial.objects.filter(mo_kelas__skl_k_kelas_nama__contains="12", mo_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan).values('mo_siswa__murid_nama','mo_siswa__murid_profil_uuid', 'mo_kelas__skl_k_kelas_nama').annotate(Avg("mo_proyeksi_nilai")).order_by("mo_siswa__murid_nama"),
			'sikap_spiritual': Mo_Sikap_Spiritual.objects.filter(mo_kelas__skl_k_kelas_nama__contains="12", mo_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan).values('mo_siswa__murid_nama','mo_siswa__murid_profil_uuid', 'mo_kelas__skl_k_kelas_nama').annotate(Avg("mo_proyeksi_nilai")).order_by("mo_siswa__murid_nama"),
			'ulangan': Mo_Penilaian_Ulangan.objects.filter(mo_kelas__skl_k_kelas_nama__contains="12", mo_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan).values('mo_siswa__murid_nama','mo_siswa__murid_profil_uuid', 'mo_kelas__skl_k_kelas_nama').annotate(Avg('mo_nilai')),
			'uts': Mo_Penilaian_UTS.objects.filter(mo_kelas__skl_k_kelas_nama__contains="12", mo_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan).values('mo_siswa__murid_nama','mo_siswa__murid_profil_uuid', 'mo_kelas__skl_k_kelas_nama').annotate(Avg('mo_nilai')),
			'uas': Mo_Penilaian_UAS.objects.filter(mo_kelas__skl_k_kelas_nama__contains="12", mo_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan).values('mo_siswa__murid_nama','mo_siswa__murid_profil_uuid', 'mo_kelas__skl_k_kelas_nama').annotate(Avg('mo_nilai')),
			
		},
	}
	context = {
		'data': data,
		'guru': guru,
		'kelas': kelas,
	}
	return render(request, 'templates_monitoring/templates_nilai_siswa/monitoring_mean_nilai_mapel_jurusan.html', context)
def page_guru_mean_nilai_siswa_jurusan_detail(request, uuidnyaMurid):
	kelas = SKL_Kelas.objects.all()
	guru = Gu_Profil_Guru.objects.get(guru_user=request.user)
	identitas_siswa = Profil_Murid.objects.get(murid_profil_uuid=uuidnyaMurid)
	nilai_pengetahuan = Mo_Penilaian_Pengetahuan.objects.filter(mo_siswa__murid_profil_uuid=uuidnyaMurid, mo_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan).order_by('mo_kelas__skl_k_kelas_nama', 'mo_kompetensi_dasar__guru_nomor_kd')
	nilai_keterampilan = Mo_Penilaian_Keterampilan.objects.filter(mo_siswa__murid_profil_uuid=uuidnyaMurid, mo_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan).order_by('mo_kelas__skl_k_kelas_nama', 'mo_kompetensi_dasar__guru_nomor_kd')
	nilai_sikap_sosial = Mo_Sikap_Sosial.objects.filter(mo_siswa__murid_profil_uuid=uuidnyaMurid, mo_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan).order_by('mo_kelas__skl_k_kelas_nama', 'mo_kompetensi_dasar__guru_nomor_kd')
	nilai_sikap_spiritual = Mo_Sikap_Spiritual.objects.filter(mo_siswa__murid_profil_uuid=uuidnyaMurid, mo_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan).order_by('mo_kelas__skl_k_kelas_nama', 'mo_kompetensi_dasar__guru_nomor_kd')
	
	bagan_donut_nilai_pengetahuan = Mo_Penilaian_Pengetahuan.objects.filter(mo_siswa__murid_profil_uuid=uuidnyaMurid, mo_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan).values('mo_siswa__murid_nama','mo_siswa__murid_profil_uuid', 'mo_kelas__skl_k_kelas_nama').annotate(Avg('mo_nilai_P1_TGS'), Avg('mo_nilai_P2_TLS'), Avg('mo_nilai_P3_TLS'))
	bagan_donut_nilai_keterampilan = Mo_Penilaian_Keterampilan.objects.filter(mo_siswa__murid_profil_uuid=uuidnyaMurid, mo_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan).values('mo_siswa__murid_nama','mo_siswa__murid_profil_uuid', 'mo_kelas__skl_k_kelas_nama').annotate(Avg('mo_praktek'), Avg('mo_produk'), Avg('mo_proyek'), Avg('mo_portofolio'))
	bagan_donut_nilai_sikap_sosial = Mo_Sikap_Sosial.objects.filter(mo_siswa__murid_profil_uuid=uuidnyaMurid, mo_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan).values('mo_siswa__murid_nama','mo_siswa__murid_profil_uuid', 'mo_kelas__skl_k_kelas_nama').annotate(Avg('mo_proyeksi_nilai'))
	bagan_donut_nilai_sikap_spiritual = Mo_Sikap_Spiritual.objects.filter(mo_siswa__murid_profil_uuid=uuidnyaMurid, mo_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan).values('mo_siswa__murid_nama','mo_siswa__murid_profil_uuid', 'mo_kelas__skl_k_kelas_nama').annotate(Avg('mo_proyeksi_nilai'))
	
	mean_bagan_donut_nilai_keterampilan = []
	mean_bagan_donut_nilai_pengetahuan = []
	mean_bagan_donut_nilai_sosial = []
	mean_bagan_donut_nilai_spiritual = []
	for data in bagan_donut_nilai_pengetahuan:
		if data['mo_nilai_P1_TGS__avg'] is not None:
			mean_bagan_donut_nilai_pengetahuan.append(data['mo_nilai_P1_TGS__avg'])
		else:
			mean_bagan_donut_nilai_pengetahuan.append(0)
		if data['mo_nilai_P2_TLS__avg'] is not None:
			mean_bagan_donut_nilai_pengetahuan.append(data['mo_nilai_P2_TLS__avg'])
		else:
			mean_bagan_donut_nilai_pengetahuan.append(0)
		if data['mo_nilai_P3_TLS__avg'] is not None:
			mean_bagan_donut_nilai_pengetahuan.append(data['mo_nilai_P3_TLS__avg'])
		else:
			mean_bagan_donut_nilai_pengetahuan.append(0)
	for data in bagan_donut_nilai_keterampilan:
		if data['mo_praktek__avg'] is not None:
			mean_bagan_donut_nilai_keterampilan.append(data['mo_praktek__avg'])
		else:
			mean_bagan_donut_nilai_keterampilan.append(0)
		if data['mo_produk__avg'] is not None:
			mean_bagan_donut_nilai_keterampilan.append(data['mo_produk__avg'])
		else:
			mean_bagan_donut_nilai_keterampilan.append(0)
		if data['mo_proyek__avg'] is not None:
			mean_bagan_donut_nilai_keterampilan.append(data['mo_proyek__avg'])
		else:
			mean_bagan_donut_nilai_keterampilan.append(0)
		if data['mo_portofolio__avg'] is not None:
			mean_bagan_donut_nilai_keterampilan.append(data['mo_portofolio__avg'])
		else:
			mean_bagan_donut_nilai_keterampilan.append(0)
	for data in bagan_donut_nilai_sikap_sosial:
		if data['mo_proyeksi_nilai__avg'] is not None:
			mean_bagan_donut_nilai_sosial.append(data['mo_proyeksi_nilai__avg'])
		else:
			mean_bagan_donut_nilai_sosial.append(0)
	for data in bagan_donut_nilai_sikap_spiritual:
		if data['mo_proyeksi_nilai__avg'] is not None:
			mean_bagan_donut_nilai_spiritual.append(data['mo_proyeksi_nilai__avg'])
		else:
			mean_bagan_donut_nilai_spiritual.append(0)

	try:
		m_pengetahuan = float(statistics.mean(mean_bagan_donut_nilai_pengetahuan))
	except:
		m_pengetahuan = 0

	try:
		m_keterampilan = float(statistics.mean(mean_bagan_donut_nilai_keterampilan))
	except:
		m_keterampilan = 0

	try:
		m_sosial = float(statistics.mean(mean_bagan_donut_nilai_sosial))
	except:
		m_sosial = 0

	try:
		m_spiritual = float(statistics.mean(mean_bagan_donut_nilai_spiritual))
	except:
		m_spiritual = 0


	data_bagan = [
		m_pengetahuan, 
		m_keterampilan, 
		m_sosial, 
		m_spiritual
	]

	grafik_pengetahuan = {
		'kd': [],
		'nilai_P1_TGS': [],
		'nilai_P2_TLS': [],
		'nilai_P3_TLS': [],
	}
	for data in nilai_pengetahuan:
		try:
			x = "'" + data.mo_kompetensi_dasar.guru_nomor_kd + "'"
		except:
			x = "'Tidak ada KD'"
		grafik_pengetahuan['kd'].append(x)
		if data.mo_nilai_P1_TGS is not None:
			grafik_pengetahuan['nilai_P1_TGS'].append(data.mo_nilai_P1_TGS)
		else:
			grafik_pengetahuan['nilai_P1_TGS'].append(0)
		if data.mo_nilai_P2_TLS is not None:
			grafik_pengetahuan['nilai_P2_TLS'].append(data.mo_nilai_P2_TLS)
		else:
			grafik_pengetahuan['nilai_P2_TLS'].append(0)
		if data.mo_nilai_P3_TLS is not None:
			grafik_pengetahuan['nilai_P3_TLS'].append(data.mo_nilai_P3_TLS)
		else:
			grafik_pengetahuan['nilai_P3_TLS'].append(0)

	grafik_keterampilan = {
		'kd': [],
		'praktek': [],
		'produk': [],
		'proyek': [],
		'portofolio': [],
	}
	for data in nilai_keterampilan:
		try:
			x = "'" + data.mo_kompetensi_dasar.guru_nomor_kd + "'"
		except:
			x = "'Tidak ada KD'"
		grafik_keterampilan['kd'].append(x)
		if data.mo_praktek is not None:
			grafik_keterampilan['praktek'].append(data.mo_praktek)
		else:
			grafik_keterampilan['praktek'].append(0)
		if data.mo_produk is not None:
			grafik_keterampilan['produk'].append(data.mo_produk)
		else:
			grafik_keterampilan['produk'].append(0)
		if data.mo_proyek is not None:
			grafik_keterampilan['proyek'].append(data.mo_proyek)
		else:
			grafik_keterampilan['proyek'].append(0)
		if data.mo_portofolio is not None:
			grafik_keterampilan['portofolio'].append(data.mo_portofolio)
		else:
			grafik_keterampilan['portofolio'].append(0)

	grafik_sikap_sosial = {
		'SB': None,
		'B': None,
		'C': None,
		'K': None,
		'TO': [],
		'nilai': Mo_Sikap_Sosial.objects.filter(mo_siswa__murid_profil_uuid=uuidnyaMurid, mo_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib).values('mo_nilai').annotate(nilai_count=Count('mo_nilai')).order_by('-mo_nilai'),
		'MTO': None,
		'MTOO': [],
	}
	for data in grafik_sikap_sosial['nilai']:
		if data['mo_nilai'] == "Sangat Baik":
			if data['nilai_count'] == None:
				grafik_sikap_spiritual = 0
			else:
				grafik_sikap_sosial['SB'] = data['nilai_count']
		elif data['mo_nilai'] == "Baik":
			grafik_sikap_sosial['B'] = data['nilai_count']
		elif data['mo_nilai'] == "Cukup":
			grafik_sikap_sosial['C'] = data['nilai_count']
		elif data['mo_nilai'] == "Kurang":
			grafik_sikap_sosial['K'] = data['nilai_count']
	for data in nilai_sikap_sosial:
		grafik_sikap_sosial['TO'].append(data.mo_nilai)
	try:
		grafik_sikap_sosial['TO'] = statistics.mode(grafik_sikap_sosial['TO'])
	except:
		grafik_sikap_sosial['TO'] = "Tidak ada nilai"
	grafik_sikap_sosial['MTO'] = [ grafik_sikap_sosial['SB'], grafik_sikap_sosial['B'], grafik_sikap_sosial['C'], grafik_sikap_sosial['K'] ]
	for data in grafik_sikap_sosial['MTO']:
		if data == None:
			grafik_sikap_sosial['MTOO'].append(0)
		else:
			grafik_sikap_sosial['MTOO'].append(data)

	grafik_sikap_spiritual = {
		'SB': None,
		'B': None,
		'C': None,
		'K': None,
		'TO': [],
		'nilai': Mo_Sikap_Spiritual.objects.filter(mo_siswa__murid_profil_uuid=uuidnyaMurid, mo_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib).values('mo_nilai').annotate(nilai_count=Count('mo_nilai')).order_by('-mo_nilai'),
		'MTO': None,
		'MTOO': [],
	}
	for data in grafik_sikap_spiritual['nilai']:
		if data['mo_nilai'] == "Sangat Baik":
			grafik_sikap_spiritual['SB'] = data['nilai_count']
		elif data['mo_nilai'] == "Baik":
			grafik_sikap_spiritual['B'] = data['nilai_count']
		elif data['mo_nilai'] == "Cukup":
			grafik_sikap_spiritual['C'] = data['nilai_count']
		elif data['mo_nilai'] == "Kurang":
			grafik_sikap_spiritual['K'] = data['nilai_count']
	for data in nilai_sikap_spiritual:
		grafik_sikap_spiritual['TO'].append(data.mo_nilai)
	try:
		grafik_sikap_spiritual['TO'] = statistics.mode(grafik_sikap_spiritual['TO'])
	except:
		grafik_sikap_spiritual['TO'] = "Tidak ada nilai"
	grafik_sikap_spiritual['MTO'] = [ grafik_sikap_spiritual['SB'], grafik_sikap_spiritual['B'], grafik_sikap_spiritual['C'], grafik_sikap_spiritual['K'] ]
	for data in grafik_sikap_spiritual['MTO']:
		if data == None:
			grafik_sikap_spiritual['MTOO'].append(0)
		else:
			grafik_sikap_spiritual['MTOO'].append(data)

	# print("grafik_pengetahuan", grafik_pengetahuan)
	# print("grafik_keterampilan: ", grafik_keterampilan)
	# print("grafik_sikap_sosial: ", grafik_sikap_sosial)
	# print("grafik_sikap_spiritual: ", grafik_sikap_spiritual)

	context = {
		'guru': guru,
		'identitas_siswa': identitas_siswa,
		'data_bagan': data_bagan,
		'nilai_pengetahuan': nilai_pengetahuan,
		'grafik_pengetahuan': grafik_pengetahuan,
		'nilai_keterampilan': nilai_keterampilan,
		'grafik_keterampilan': grafik_keterampilan,
		'nilai_sikap_sosial': nilai_sikap_sosial,
		'grafik_sikap_sosial': grafik_sikap_sosial,
		'nilai_sikap_spiritual': nilai_sikap_spiritual,
		'grafik_sikap_spiritual': grafik_sikap_spiritual,
		'kelas': kelas,
	}
	return render(request, 'templates_monitoring/templates_nilai_siswa/templates_detail/monitoring_detail_nilai_mapel_jurusan.html', context)
