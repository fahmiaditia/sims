from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.forms import modelformset_factory, formset_factory
from django.db.models import Avg, Count, Sum
from role_guru.models import *
from role_guru.forms import *
from role_guru.filters import *
from role_murid.models import *
from monitoring.models import *
from sekolah.models import *
import json

##############
from role_guru.resources import *
from django.http import HttpResponse
from tablib import Dataset
##############

def IsNewChecker(var):
	is_new = True
	if var is None:
		is_new = True
	else:
		is_new = False
	return is_new

# Create your views here.
def page_guru_dashboard(request):
	kelas = SKL_Kelas.objects.all()
	guru = Gu_Profil_Guru.objects.get(guru_user=request.user)
	context={
		'kelas':kelas,
		'guru': guru,
	}
	return render(request, 'templates_guru/dashboard_guru_r.html', context)


def page_guru_profil(request):
	profil_guru = Gu_Profil_Guru.objects.get(guru_user=request.user)
	guru = Gu_Profil_Guru.objects.get(guru_user=request.user)
	kelas = SKL_Kelas.objects.all()
	context={
		'guru': guru,
		'profil_guru': profil_guru,
		'kelas': kelas,
	}
	return render(request, 'templates_guru/page_profil_guru/profil_guru.html', context)

class page_guru_profil_update(UpdateView):
	model = Gu_Profil_Guru
	form_class = page_guru_profil_forms
	success_url = reverse_lazy("monitoring:page_guru_profil")
	template_name = 'templates_guru/page_profil_guru/profil_guru_update.html'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['kelas'] = SKL_Kelas.objects.all()
		context['guru'] = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		return context


# PAGE DATA KOMPETENSI DASAR  /===================================================================================================================
def page_guru_list_kompetensi_dasar_wajib(request):
	kelas = SKL_Kelas.objects.all()
	guru = Gu_Profil_Guru.objects.get(guru_user=request.user)
	kompetensi_dasar_mapel_wajib = Gu_Data_Kompetensi_Dasar.objects.filter(guru_kompetensi_dasar_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib)
	kompetensi_dasar = page_guru_kompetensi_dasar_wajib_filter(request.GET, queryset=kompetensi_dasar_mapel_wajib)
	context = {
		'kompetensi_dasar': kompetensi_dasar,
		'guru': guru,
		'kelas': kelas,
	}
	return render(request, "templates_guru/kelola_kompetensi_dasar/page_list_kompetensi_dasar_mapel_wajib.html", context)
def page_guru_input_kompetensi_dasar_wajib(request):
	kelas = SKL_Kelas.objects.all()
	guru = Gu_Profil_Guru.objects.get(guru_user=request.user)
	kompetensi_dasar_wajib_formset = modelformset_factory(Gu_Data_Kompetensi_Dasar, form=page_guru_input_kompetensi_dasar_wajib_forms, can_delete=True, extra=3)
	kompetensi_dasar_wajib_queryset = Gu_Data_Kompetensi_Dasar.objects.filter(guru_kompetensi_dasar_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib).order_by('guru_kompetensi_dasar_kelas')
	if request.method == "POST":
		formset = kompetensi_dasar_wajib_formset(request.POST, queryset=kompetensi_dasar_wajib_queryset)
		if formset.is_valid():
			instances = formset.save()
			for instance in instances:
				if IsNewChecker(instance.guru_kompetensi_dasar_uuid):
					instance.guru_kompetensi_dasar_mata_pelajaran_wajib = guru.guru_mata_pelajaran_wajib
					instance.save()
				else:
					instance.guru_kompetensi_dasar_mata_pelajaran_wajib = guru.guru_mata_pelajaran_wajib
					instance.save()
			return redirect("monitoring:page_guru_input_kompetensi_dasar_wajib")
	formset = kompetensi_dasar_wajib_formset(queryset=kompetensi_dasar_wajib_queryset)
	context = {
		"formset": formset,
		"guru": guru,
		'kelas': kelas,
	}
	return render(request, "templates_guru/kelola_kompetensi_dasar/page_input_kompetensi_dasar/page_input_kompetensi_dasar_mapel_wajib.html", context)
class page_guru_update_kompetensi_dasar_wajib(UpdateView):
	model = Gu_Data_Kompetensi_Dasar
	form_class = page_guru_kompetensi_dasar_forms
	success_url = reverse_lazy("monitoring:page_guru_list_kompetensi_dasar_wajib")
	template_name = "templates_guru/kelola_kompetensi_dasar/page_update_kompetensi_dasar/page_update_kompetensi_dasar_mapel_wajib.html"
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		context['guru'] = guru
		context['kelas'] = SKL_Kelas.objects.all()
		return context
class page_guru_delete_kompetensi_dasar_wajib(DeleteView):
	model = Gu_Data_Kompetensi_Dasar
	success_url = reverse_lazy("monitoring:page_guru_list_kompetensi_dasar_wajib")
	template_name = "templates_guru/kelola_kompetensi_dasar/page_delete_kompetensi_dasar/page_delete_kompetensi_dasar_mapel_wajib.html"
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		context['guru'] = guru
		context['kelas'] = SKL_Kelas.objects.all()
		return context
	# END Pengetahuan Mata Pelajaran Wajib ============================================================================================


	# Pengetahuan Mata Pelajaran Jurusan ==============================================================================================

	# Pengetahuan Mata Pelajaran Jurusan ================================================================================================

def page_guru_list_kompetensi_dasar_jurusan(request):
	kelas = SKL_Kelas.objects.all()
	guru = Gu_Profil_Guru.objects.get(guru_user=request.user)
	kompetensi_dasar_mapel_jurusan = Gu_Data_Kompetensi_Dasar.objects.filter(guru_kompetensi_dasar_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan)
	kompetensi_dasar = page_guru_kompetensi_dasar_jurusan_filter(request.GET, queryset=kompetensi_dasar_mapel_jurusan)
	context = {
		'kompetensi_dasar': kompetensi_dasar,
		'guru': guru,
		'kelas': kelas,
	}
	return render(request, "templates_guru/kelola_kompetensi_dasar/page_list_kompetensi_dasar_mapel_jurusan.html", context)
def page_guru_input_kompetensi_dasar_jurusan(request):
	kelas = SKL_Kelas.objects.all()
	guru = Gu_Profil_Guru.objects.get(guru_user=request.user)
	kompetensi_dasar_jurusan_formset = modelformset_factory(Gu_Data_Kompetensi_Dasar, form=page_guru_input_kompetensi_dasar_jurusan_forms, can_delete=True, extra=3)
	kompetensi_dasar_jurusan_queryset = Gu_Data_Kompetensi_Dasar.objects.filter(guru_kompetensi_dasar_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan).order_by('guru_kompetensi_dasar_kelas')
	if request.method == "POST":
		formset = kompetensi_dasar_jurusan_formset(request.POST, queryset=kompetensi_dasar_jurusan_queryset)
		if formset.is_valid():
			instances = formset.save()
			for instance in instances:
				if IsNewChecker(instance.guru_kompetensi_dasar_uuid):
					instance.guru_kompetensi_dasar_mata_pelajaran_jurusan = guru.guru_mata_pelajaran_jurusan
					instance.save()
				else:
					instance.guru_kompetensi_dasar_mata_pelajaran_jurusan = guru.guru_mata_pelajaran_jurusan
					instance.save()
			return redirect("monitoring:page_guru_input_kompetensi_dasar_jurusan")
	formset = kompetensi_dasar_jurusan_formset(queryset=kompetensi_dasar_jurusan_queryset)
	context = {
		"formset": formset,
		"guru": guru,
		'kelas': kelas,
	}
	return render(request, "templates_guru/kelola_kompetensi_dasar/page_input_kompetensi_dasar/page_input_kompetensi_dasar_mapel_jurusan.html", context)
class page_guru_update_kompetensi_dasar_jurusan(UpdateView):
	model = Gu_Data_Kompetensi_Dasar
	form_class = page_guru_kompetensi_dasar_forms
	success_url = reverse_lazy("monitoring:page_guru_list_kompetensi_dasar_jurusan")
	template_name = "templates_guru/kelola_kompetensi_dasar/page_update_kompetensi_dasar/page_update_kompetensi_dasar_mapel_jurusan.html"
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		context['guru'] = guru
		context['kelas'] = SKL_Kelas.objects.all()
		return context
class page_guru_delete_kompetensi_dasar_jurusan(DeleteView):
	model = Gu_Data_Kompetensi_Dasar
	success_url = reverse_lazy("monitoring:page_guru_list_kompetensi_dasar_jurusan")
	template_name = "templates_guru/kelola_kompetensi_dasar/page_delete_kompetensi_dasar/page_delete_kompetensi_dasar_mapel_jurusan.html"
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		context['guru'] = guru
		context['kelas'] = SKL_Kelas.objects.all()
		return context
	# END Pengetahuan Mata Pelajaran Wajib ============================================================================================


	# Pengetahuan Mata Pelajaran Jurusan ==============================================================================================

	# Pengetahuan Mata Pelajaran Jurusan ================================================================================================

o = "disini"
def page_guru_wali_kelas(request):
	guru = Gu_Profil_Guru.objects.get(guru_user=request.user)

	q_murid = 'mo_siswa__murid_nama'
	q_semester = 'mo_semester__skl_s_semester'
	q_mapel_wajib = 'mo_mata_pelajaran_wajib__mapel_wajib_pelajaran'
	q_mapel_jurusan = 'mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran'
	q_kd_no = 'mo_kompetensi_dasar__guru_nomor_kd',
	q_kd_ket = 'mo_kompetensi_dasar__guru_kompetensi_dasar',

	data_angka = {
		'pengetahuan': Mo_Penilaian_Pengetahuan.objects.filter(mo_siswa__murid_kelas=guru.guru_wali_kelas).values('mo_siswa__murid_nama', 'mo_mata_pelajaran_wajib__mapel_wajib_pelajaran', 'mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran','mo_semester__skl_s_semester', 'mo_kompetensi_dasar__guru_nomor_kd', 'mo_kompetensi_dasar__guru_kompetensi_dasar').annotate(Avg('mo_nilai_P1_TGS'), Avg('mo_nilai_P2_TLS'), Avg('mo_nilai_P3_TLS')).order_by('mo_siswa__murid_nama', 'mo_semester'),
		'keterampilan': Mo_Penilaian_Keterampilan.objects.filter(mo_siswa__murid_kelas=guru.guru_wali_kelas).values('mo_siswa__murid_nama', 'mo_mata_pelajaran_wajib__mapel_wajib_pelajaran', 'mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran','mo_semester__skl_s_semester', 'mo_kompetensi_dasar__guru_nomor_kd', 'mo_kompetensi_dasar__guru_kompetensi_dasar').annotate(Avg('mo_praktek'), Avg('mo_produk'), Avg('mo_proyek'), Avg('mo_portofolio')).order_by('mo_siswa__murid_nama', 'mo_semester'),
		'sosial': Mo_Sikap_Sosial.objects.filter(mo_siswa__murid_kelas=guru.guru_wali_kelas).values('mo_siswa__murid_nama', 'mo_mata_pelajaran_wajib__mapel_wajib_pelajaran', 'mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran','mo_semester__skl_s_semester', 'mo_kompetensi_dasar__guru_nomor_kd', 'mo_kompetensi_dasar__guru_kompetensi_dasar').annotate(Avg('mo_proyeksi_nilai')).order_by('mo_siswa__murid_nama', 'mo_semester'),
		'spiritual': Mo_Sikap_Spiritual.objects.filter(mo_siswa__murid_kelas=guru.guru_wali_kelas).values('mo_siswa__murid_nama', 'mo_mata_pelajaran_wajib__mapel_wajib_pelajaran', 'mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran','mo_semester__skl_s_semester', 'mo_kompetensi_dasar__guru_nomor_kd', 'mo_kompetensi_dasar__guru_kompetensi_dasar').annotate(Avg('mo_proyeksi_nilai')).order_by('mo_siswa__murid_nama', 'mo_semester'),
		'ulangan': Mo_Penilaian_Ulangan.objects.filter(mo_siswa__murid_kelas=guru.guru_wali_kelas).values('mo_siswa__murid_nama', 'mo_mata_pelajaran_wajib__mapel_wajib_pelajaran', 'mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran','mo_semester__skl_s_semester', 'mo_kompetensi_dasar__guru_nomor_kd', 'mo_kompetensi_dasar__guru_kompetensi_dasar').annotate(Avg('mo_nilai')).order_by('mo_siswa__murid_nama', 'mo_semester'),
		'uts': Mo_Penilaian_UTS.objects.filter(mo_siswa__murid_kelas=guru.guru_wali_kelas).values('mo_siswa__murid_nama', 'mo_mata_pelajaran_wajib__mapel_wajib_pelajaran', 'mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran','mo_semester__skl_s_semester').annotate(Avg('mo_nilai')).order_by('mo_siswa__murid_nama', 'mo_semester'),
		'uas': Mo_Penilaian_UAS.objects.filter(mo_siswa__murid_kelas=guru.guru_wali_kelas).values('mo_siswa__murid_nama', 'mo_mata_pelajaran_wajib__mapel_wajib_pelajaran', 'mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran','mo_semester__skl_s_semester').annotate(Avg('mo_nilai')).order_by('mo_siswa__murid_nama', 'mo_semester'),
		'ekskul': Mo_Penilaian_Ekskul.objects.filter(mo_siswa__murid_kelas=guru.guru_wali_kelas).values('mo_siswa__murid_nama', 'mo_semester').annotate(Avg('mo_nilai')),
		'kejuaraan': Mo_Juara_Ekskul.objects.filter(mo_siswa__murid_kelas=guru.guru_wali_kelas).order_by('mo_siswa__murid_nama')
	}
	print(data_angka['pengetahuan'])
	context = {
		'guru': guru,
		'data_angka': data_angka,
	}
	return render(request, "templates_guru/page_wali_kelas/page_wali_kelas.html", context)



# PAGE INPUT NILAI /===================================================================================================================

	# Pengetahuan Mata Pelajaran Wajib ================================================================================================
def page_guru_list_pengetahuan_wajib(request):
	kelas = SKL_Kelas.objects.all()
	guru = Gu_Profil_Guru.objects.get(guru_user=request.user)
	nilai_pengetahuan_mapel_wajib = Mo_Penilaian_Pengetahuan.objects.filter(mo_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib)
	nilai = page_guru_nilai_pengetahuan_wajib_filter(request.GET, queryset=nilai_pengetahuan_mapel_wajib)
	if request.method == "POST":
		pengetahuan_resource = PengetahuanResources()
		queryset = nilai_pengetahuan_mapel_wajib
		dataset = pengetahuan_resource.export(queryset)
		response = HttpResponse(dataset.csv, content_type='text/csv')
		response['Content-Disposition'] = 'attachment; filename="nilai_pengetahuan.csv"'
		return response

	context = {
		'nilai': nilai,
		'guru': guru,
		'kelas': kelas,
	}
	return render(request, "templates_guru/kelola_pengetahuan/page_list_nilai_mapel_wajib.html", context)

def page_guru_import(request):
	if request.method == "POST":
		pengetahuan_resource = PengetahuanResources()
		queryset = nilai_pengetahuan_mapel_wajib
		dataset = Dataset()
		new_nilai = request.FILES('myfile')
		
		imported_data = dataset.load(new_nilai.read())
		result = pengetahuan_resource.import_data(dataset, dry_run=True)

		if not result.has_errors():
			pengetahuan_resource.import_data(dataset, dry_run=True)

	context = {}
	return render(request, "templates_guru/kelola_pengetahuan/importing.html", context)


def page_guru_input_pengetahuan_wajib(request):
	kelas = SKL_Kelas.objects.all()
	guru = Gu_Profil_Guru.objects.get(guru_user=request.user)
	nilai_pengetahuan_wajib_formset = modelformset_factory(Mo_Penilaian_Pengetahuan, form=page_guru_input_nilai_pengetahuan_wajib_forms, can_delete=True, extra=5)
	nilai_pengetahuan_wajib_queryset = Mo_Penilaian_Pengetahuan.objects.filter(mo_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib).order_by('mo_kelas')
	if request.method == "POST":
		formset = nilai_pengetahuan_wajib_formset(request.POST, queryset=nilai_pengetahuan_wajib_queryset)
		if formset.is_valid():
			instances = formset.save()
			for instance in instances:
				# if IsNewChecker(instance.mo_penilaian_pengetahuan_uuid) is not True:
				# if Mo_Penilaian_Pengetahuan.objects.filter(mo_penilaian_pengetahuan_uuid=instance.mo_penilaian_pengetahuan_uuid).exists():
				if instance.mo_kelas is not None: 
				# try:
					# Mo_Penilaian_Pengetahuan.objects.get(mo_penilaian_pengetahuan_uuid="instance.mo_penilaian_pengetahuan_uuid")
					instance.mo_mata_pelajaran_wajib = guru.guru_mata_pelajaran_wajib
					instance.save()
					# print('Tidak ada')
				else:
				# except:
					murid = Profil_Murid.objects.get(murid_user=instance.mo_siswa.murid_user)
					instance.mo_mata_pelajaran_wajib = guru.guru_mata_pelajaran_wajib
					instance.mo_kelas = murid.murid_kelas
					instance.mo_tahun_ajaran = murid.murid_tahun_ajaran
					instance.mo_semester = murid.murid_semester
					instance.save()
					# print('ada')

			return redirect("monitoring:page_guru_input_pengetahuan_wajib")
	formset = nilai_pengetahuan_wajib_formset(queryset=nilai_pengetahuan_wajib_queryset)
	context = {
		"formset": formset,
		"guru": guru,
		'kelas': kelas,
	}
	return render(request, "templates_guru/kelola_pengetahuan/page_input_nilai/page_input_nilai_pengetahuan_mapel_wajib.html", context)
class page_guru_update_pengetahuan_wajib(UpdateView):
	model = Mo_Penilaian_Pengetahuan
	form_class = page_guru_nilai_pengetahuan_forms
	success_url = reverse_lazy("monitoring:page_guru_list_pengetahuan_wajib")
	template_name = "templates_guru/kelola_pengetahuan/page_update_nilai/page_update_nilai_mapel_wajib.html"
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		context['guru'] = guru
		context['kelas'] = SKL_Kelas.objects.all()
		return context
class page_guru_delete_pengetahuan_wajib(DeleteView):
	model = Mo_Penilaian_Pengetahuan
	success_url = reverse_lazy("monitoring:page_guru_list_pengetahuan_wajib")
	template_name = "templates_guru/kelola_pengetahuan/page_delete_nilai/page_delete_nilai_mapel_wajib.html"
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		context['guru'] = guru
		context['kelas'] = SKL_Kelas.objects.all()
		return context
	# END Pengetahuan Mata Pelajaran Wajib ============================================================================================


	# Pengetahuan Mata Pelajaran Jurusan ==============================================================================================

	# Pengetahuan Mata Pelajaran Jurusan ================================================================================================



def page_guru_list_pengetahuan_jurusan(request):
	kelas = SKL_Kelas.objects.all()
	guru = Gu_Profil_Guru.objects.get(guru_user=request.user)
	nilai_pengetahuan_mapel_jurusan = Mo_Penilaian_Pengetahuan.objects.filter(mo_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan)
	nilai = page_guru_nilai_pengetahuan_jurusan_filter(request.GET, queryset=nilai_pengetahuan_mapel_jurusan)
	context = {
		'nilai': nilai,
		'guru': guru,
		'kelas': kelas,
	}
	return render(request, "templates_guru/kelola_pengetahuan/page_list_nilai_mapel_jurusan.html", context)
def page_guru_input_pengetahuan_jurusan(request):
	kelas = SKL_Kelas.objects.all()
	guru = Gu_Profil_Guru.objects.get(guru_user=request.user)
	nilai_pengetahuan_jurusan_formset = modelformset_factory(Mo_Penilaian_Pengetahuan, form=page_guru_input_nilai_pengetahuan_jurusan_forms, can_delete=True, extra=3)
	nilai_pengetahuan_jurusan_queryset = Mo_Penilaian_Pengetahuan.objects.filter(mo_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan).order_by('mo_kelas')
	if request.method == "POST":
		formset = nilai_pengetahuan_jurusan_formset(request.POST, queryset=nilai_pengetahuan_jurusan_queryset)
		if formset.is_valid():
			instances = formset.save()
			for instance in instances:
				# if IsNewChecker(instance.mo_penilaian_pengetahuan_uuid):
				if instance.mo_kelas is not None: 
					instance.mo_mata_pelajaran_jurusan = guru.guru_mata_pelajaran_jurusan
					instance.save()
				else:
					murid = Profil_Murid.objects.get(murid_user=instance.mo_siswa.murid_user)
					instance.mo_mata_pelajaran_jurusan = guru.guru_mata_pelajaran_jurusan
					instance.mo_kelas = murid.murid_kelas
					instance.mo_tahun_ajaran = murid.murid_tahun_ajaran
					instance.mo_semester = murid.murid_semester
					instance.save()
			return redirect("monitoring:page_guru_input_pengetahuan_jurusan")
	formset = nilai_pengetahuan_jurusan_formset(queryset=nilai_pengetahuan_jurusan_queryset)
	context = {
		"formset": formset,
		"guru": guru,
		'kelas': kelas,
	}
	return render(request, "templates_guru/kelola_pengetahuan/page_input_nilai/page_input_nilai_pengetahuan_mapel_jurusan.html", context)
class page_guru_update_pengetahuan_jurusan(UpdateView):
	model = Mo_Penilaian_Pengetahuan
	form_class = page_guru_nilai_pengetahuan_forms
	success_url = reverse_lazy("monitoring:page_guru_list_pengetahuan_jurusan")
	template_name = "templates_guru/kelola_pengetahuan/page_update_nilai/page_update_nilai_mapel_jurusan.html"
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		context['guru'] = guru
		context['kelas'] = SKL_Kelas.objects.all()
		return context
class page_guru_delete_pengetahuan_jurusan(DeleteView):
	model = Mo_Penilaian_Pengetahuan
	success_url = reverse_lazy("monitoring:page_guru_list_pengetahuan_jurusan")
	template_name = "templates_guru/kelola_pengetahuan/page_delete_nilai/page_delete_nilai_mapel_jurusan.html"
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		context['guru'] = guru
		context['kelas'] = SKL_Kelas.objects.all()
		return context
	# END Pengetahuan Mata Pelajaran Jurusan ==========================================================================================



	# Keterampilan Mata Pelajaran Wajib ================================================================================================




	# Keterampilan Mata Pelajaran Wajib ================================================================================================



def page_guru_list_keterampilan_wajib(request):
	kelas = SKL_Kelas.objects.all()
	guru = Gu_Profil_Guru.objects.get(guru_user=request.user)
	nilai_keterampilan_mapel_wajib = Mo_Penilaian_Keterampilan.objects.filter(mo_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib)
	nilai = page_guru_nilai_keterampilan_wajib_filter(request.GET, queryset=nilai_keterampilan_mapel_wajib)
	context = {
		'nilai': nilai,
		'guru': guru,
		'kelas': kelas
	}
	return render(request, "templates_guru/kelola_keterampilan/page_list_nilai_mapel_wajib.html", context)
def page_guru_input_keterampilan_wajib(request):
	kelas = SKL_Kelas.objects.all()
	guru = Gu_Profil_Guru.objects.get(guru_user=request.user)
	nilai_keterampilan_wajib_formset = modelformset_factory(Mo_Penilaian_Keterampilan, form=page_guru_input_nilai_keterampilan_wajib_forms, can_delete=True, extra=3)
	nilai_keterampilan_wajib_queryset = Mo_Penilaian_Keterampilan.objects.filter(mo_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib).order_by('mo_kelas')
	if request.method == "POST":
		formset = nilai_keterampilan_wajib_formset(request.POST, queryset=nilai_keterampilan_wajib_queryset)
		if formset.is_valid():
			instances = formset.save()
			for instance in instances:
				# if IsNewChecker(instance.mo_penilaian_keterampilan_uuid):
				if instance.mo_kelas is not None: 
					instance.mo_mata_pelajaran_wajib = guru.guru_mata_pelajaran_wajib
					instance.save()
				else:
					murid = Profil_Murid.objects.get(murid_user=instance.mo_siswa.murid_user)
					instance.mo_mata_pelajaran_wajib = guru.guru_mata_pelajaran_wajib
					instance.mo_kelas = murid.murid_kelas
					instance.mo_tahun_ajaran = murid.murid_tahun_ajaran
					instance.mo_semester = murid.murid_semester
					instance.save()
			return redirect("monitoring:page_guru_input_keterampilan_wajib")
	formset = nilai_keterampilan_wajib_formset(queryset=nilai_keterampilan_wajib_queryset)
	context = {
		"formset": formset,
		"guru": guru,
		'kelas': kelas
	}
	return render(request, "templates_guru/kelola_keterampilan/page_input_nilai/page_input_nilai_keterampilan_mapel_wajib.html", context)
class page_guru_update_keterampilan_wajib(UpdateView):
	model = Mo_Penilaian_Keterampilan
	form_class = page_guru_nilai_keterampilan_forms
	success_url = reverse_lazy("monitoring:page_guru_list_keterampilan_wajib")
	template_name = "templates_guru/kelola_keterampilan/page_update_nilai/page_update_nilai_mapel_wajib.html"
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		context['guru'] = guru
		context['kelas'] = SKL_Kelas.objects.all()
		return context
class page_guru_delete_keterampilan_wajib(DeleteView):
	model = Mo_Penilaian_Keterampilan
	success_url = reverse_lazy("monitoring:page_guru_list_keterampilan_wajib")
	template_name = "templates_guru/kelola_keterampilan/page_delete_nilai/page_delete_nilai_mapel_wajib.html"
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		context['guru'] = guru
		context['kelas'] = SKL_Kelas.objects.all()
		return context
	# END Keterampilan Mata Pelajaran Wajib ============================================================================================


	# Keterampilan Mata Pelajaran Jurusan ==============================================================================================

	# Keterampilan Mata Pelajaran Jurusan ================================================================================================



def page_guru_list_keterampilan_jurusan(request):
	kelas = SKL_Kelas.objects.all()
	guru = Gu_Profil_Guru.objects.get(guru_user=request.user)
	nilai_keterampilan_mapel_jurusan = Mo_Penilaian_Keterampilan.objects.filter(mo_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan)
	nilai = page_guru_nilai_keterampilan_jurusan_filter(request.GET, queryset=nilai_keterampilan_mapel_jurusan)
	context = {
		'nilai': nilai,
		'guru': guru,
		'kelas': kelas,
	}
	return render(request, "templates_guru/kelola_keterampilan/page_list_nilai_mapel_jurusan.html", context)
def page_guru_input_keterampilan_jurusan(request):
	kelas = SKL_Kelas.objects.all()
	guru = Gu_Profil_Guru.objects.get(guru_user=request.user)
	nilai_keterampilan_jurusan_formset = modelformset_factory(Mo_Penilaian_Keterampilan, form=page_guru_input_nilai_keterampilan_jurusan_forms, can_delete=True, extra=3)
	nilai_keterampilan_jurusan_queryset = Mo_Penilaian_Keterampilan.objects.filter(mo_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan).order_by('mo_kelas')
	if request.method == "POST":
		formset = nilai_keterampilan_jurusan_formset(request.POST, queryset=nilai_keterampilan_jurusan_queryset)
		if formset.is_valid():
			instances = formset.save()
			for instance in instances:
				# if IsNewChecker(instance.mo_penilaian_keterampilan_uuid):
				if instance.mo_kelas is not None: 
					instance.mo_mata_pelajaran_jurusan = guru.guru_mata_pelajaran_jurusan
					instance.save()
				else:
					murid = Profil_Murid.objects.get(murid_user=instance.mo_siswa.murid_user)
					instance.mo_mata_pelajaran_jurusan = guru.guru_mata_pelajaran_jurusan
					instance.mo_kelas = murid.murid_kelas
					instance.mo_tahun_ajaran = murid.murid_tahun_ajaran
					instance.mo_semester = murid.murid_semester
					instance.save()
			return redirect("monitoring:page_guru_input_keterampilan_jurusan")
	formset = nilai_keterampilan_jurusan_formset(queryset=nilai_keterampilan_jurusan_queryset)
	context = {
		"formset": formset,
		"guru": guru,
		'kelas': kelas,
	}
	return render(request, "templates_guru/kelola_keterampilan/page_input_nilai/page_input_nilai_keterampilan_mapel_jurusan.html", context)
class page_guru_update_keterampilan_jurusan(UpdateView):
	model = Mo_Penilaian_Keterampilan
	form_class = page_guru_nilai_keterampilan_forms
	success_url = reverse_lazy("monitoring:page_guru_list_keterampilan_jurusan")
	template_name = "templates_guru/kelola_keterampilan/page_update_nilai/page_update_nilai_mapel_jurusan.html"
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		context['guru'] = guru
		context['kelas'] = SKL_Kelas.objects.all()
		return context
class page_guru_delete_keterampilan_jurusan(DeleteView):
	model = Mo_Penilaian_Keterampilan
	success_url = reverse_lazy("monitoring:page_guru_list_keterampilan_jurusan")
	template_name = "templates_guru/kelola_keterampilan/page_delete_nilai/page_delete_nilai_mapel_jurusan.html"
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		context['guru'] = guru
		context['kelas'] = SKL_Kelas.objects.all()
		return context




	# Sikap Sosial Mata Pelajaran Wajib ================================================================================================



def page_guru_list_sikap_sosial_wajib(request):
	kelas = SKL_Kelas.objects.all()
	guru = Gu_Profil_Guru.objects.get(guru_user=request.user)
	nilai_sikap_sosial_mapel_wajib = Mo_Sikap_Sosial.objects.filter(mo_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib)
	nilai = page_guru_nilai_sikap_sosial_wajib_filter(request.GET, queryset=nilai_sikap_sosial_mapel_wajib)
	context = {
		'nilai': nilai,
		'guru': guru,
		'kelas': kelas,
	}
	return render(request, "templates_guru/kelola_sikap_sosial/page_list_nilai_mapel_wajib.html", context)
def page_guru_input_sikap_sosial_wajib(request):
	kelas = SKL_Kelas.objects.all()
	guru = Gu_Profil_Guru.objects.get(guru_user=request.user)
	nilai_sikap_sosial_wajib_formset = modelformset_factory(Mo_Sikap_Sosial, form=page_guru_input_nilai_sikap_sosial_wajib_forms, can_delete=True, extra=3)
	nilai_sikap_sosial_wajib_queryset = Mo_Sikap_Sosial.objects.filter(mo_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib).order_by('mo_kelas')
	if request.method == "POST":
		formset = nilai_sikap_sosial_wajib_formset(request.POST, queryset=nilai_sikap_sosial_wajib_queryset)
		if formset.is_valid():
			instances = formset.save()
			for instance in instances:
				# if IsNewChecker(instance.mo_penilaian_sikap_sosial_uuid):
				if instance.mo_kelas is not None: 
					instance.mo_mata_pelajaran_wajib = guru.guru_mata_pelajaran_wajib
					instance.save()
				else:
					murid = Profil_Murid.objects.get(murid_user=instance.mo_siswa.murid_user)
					instance.mo_mata_pelajaran_wajib = guru.guru_mata_pelajaran_wajib
					instance.mo_kelas = murid.murid_kelas
					instance.mo_tahun_ajaran = murid.murid_tahun_ajaran
					instance.mo_semester = murid.murid_semester
					instance.save()
			return redirect("monitoring:page_guru_input_sikap_sosial_wajib")
	formset = nilai_sikap_sosial_wajib_formset(queryset=nilai_sikap_sosial_wajib_queryset)
	context = {
		"formset": formset,
		"guru": guru,
		'kelas': kelas,
	}
	return render(request, "templates_guru/kelola_sikap_sosial/page_input_nilai/page_input_nilai_sikap_sosial_mapel_wajib.html", context)
class page_guru_update_sikap_sosial_wajib(UpdateView):
	model = Mo_Sikap_Sosial
	form_class = page_guru_nilai_sikap_sosial_forms
	success_url = reverse_lazy("monitoring:page_guru_list_sikap_sosial_wajib")
	template_name = "templates_guru/kelola_sikap_sosial/page_update_nilai/page_update_nilai_mapel_wajib.html"
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		context['guru'] = guru
		context['kelas'] = SKL_Kelas.objects.all()
		return context
class page_guru_delete_sikap_sosial_wajib(DeleteView):
	model = Mo_Sikap_Sosial
	success_url = reverse_lazy("monitoring:page_guru_list_sikap_sosial_wajib")
	template_name = "templates_guru/kelola_sikap_sosial/page_delete_nilai/page_delete_nilai_mapel_wajib.html"
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		context['guru'] = guru
		context['kelas'] = SKL_Kelas.objects.all()
		return context
	# END Keterampilan Mata Pelajaran Wajib ============================================================================================

	# Sikap Sosial Mata Pelajaran Jurusan ================================================================================================

	# Sikap Sosial Mata Pelajaran Jurusan ================================================================================================



def page_guru_list_sikap_sosial_jurusan(request):
	kelas = SKL_Kelas.objects.all()
	guru = Gu_Profil_Guru.objects.get(guru_user=request.user)
	nilai_sikap_sosial_mapel_jurusan = Mo_Sikap_Sosial.objects.filter(mo_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan)
	nilai = page_guru_nilai_sikap_sosial_jurusan_filter(request.GET, queryset=nilai_sikap_sosial_mapel_jurusan)
	context = {
		'nilai': nilai,
		'guru': guru,
		'kelas': kelas,
	}
	return render(request, "templates_guru/kelola_sikap_sosial/page_list_nilai_mapel_jurusan.html", context)
def page_guru_input_sikap_sosial_jurusan(request):
	kelas = SKL_Kelas.objects.all()
	guru = Gu_Profil_Guru.objects.get(guru_user=request.user)
	nilai_sikap_sosial_jurusan_formset = modelformset_factory(Mo_Sikap_Sosial, form=page_guru_input_nilai_sikap_sosial_jurusan_forms, can_delete=True, extra=3)
	nilai_sikap_sosial_jurusan_queryset = Mo_Sikap_Sosial.objects.filter(mo_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan).order_by('mo_kelas')
	if request.method == "POST":
		formset = nilai_sikap_sosial_jurusan_formset(request.POST, queryset=nilai_sikap_sosial_jurusan_queryset)
		if formset.is_valid():
			instances = formset.save()
			for instance in instances:
				# if IsNewChecker(instance.mo_penilaian_sikap_sosial_uuid):
				if instance.mo_kelas is not None: 
					instance.mo_mata_pelajaran_jurusan = guru.guru_mata_pelajaran_jurusan
					instance.save()
				else:
					murid = Profil_Murid.objects.get(murid_user=instance.mo_siswa.murid_user)
					instance.mo_mata_pelajaran_jurusan = guru.guru_mata_pelajaran_jurusan
					instance.mo_kelas = murid.murid_kelas
					instance.mo_tahun_ajaran = murid.murid_tahun_ajaran
					instance.mo_semester = murid.murid_semester
					instance.save()
			return redirect("monitoring:page_guru_input_sikap_sosial_jurusan")
	formset = nilai_sikap_sosial_jurusan_formset(queryset=nilai_sikap_sosial_jurusan_queryset)
	context = {
		"formset": formset,
		"guru": guru,
		'kelas': kelas,
	}
	return render(request, "templates_guru/kelola_sikap_sosial/page_input_nilai/page_input_nilai_sikap_sosial_mapel_jurusan.html", context)
class page_guru_update_sikap_sosial_jurusan(UpdateView):
	model = Mo_Sikap_Sosial
	form_class = page_guru_nilai_sikap_sosial_forms
	success_url = reverse_lazy("monitoring:page_guru_list_sikap_sosial_jurusan")
	template_name = "templates_guru/kelola_sikap_sosial/page_update_nilai/page_update_nilai_mapel_jurusan.html"
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		context['guru'] = guru
		context['kelas'] = SKL_Kelas.objects.all()
		return context
class page_guru_delete_sikap_sosial_jurusan(DeleteView):
	model = Mo_Sikap_Sosial
	success_url = reverse_lazy("monitoring:page_guru_list_sikap_sosial_jurusan")
	template_name = "templates_guru/kelola_sikap_sosial/page_delete_nilai/page_delete_nilai_mapel_jurusan.html"
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		context['guru'] = guru
		context['kelas'] = SKL_Kelas.objects.all()
		return context




def page_guru_list_sikap_spiritual_wajib(request):
	kelas = SKL_Kelas.objects.all()
	guru = Gu_Profil_Guru.objects.get(guru_user=request.user)
	nilai_sikap_spiritual_mapel_wajib = Mo_Sikap_Spiritual.objects.filter(mo_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib)
	nilai = page_guru_nilai_sikap_spiritual_wajib_filter(request.GET, queryset=nilai_sikap_spiritual_mapel_wajib)
	context = {
		'nilai': nilai,
		'guru': guru,
		'kelas': kelas,
	}
	return render(request, "templates_guru/kelola_sikap_spiritual/page_list_nilai_mapel_wajib.html", context)
def page_guru_input_sikap_spiritual_wajib(request):
	kelas = SKL_Kelas.objects.all()
	guru = Gu_Profil_Guru.objects.get(guru_user=request.user)
	nilai_sikap_spiritual_wajib_formset = modelformset_factory(Mo_Sikap_Spiritual, form=page_guru_input_nilai_sikap_spiritual_wajib_forms, can_delete=True, extra=3)
	nilai_sikap_spiritual_wajib_queryset = Mo_Sikap_Spiritual.objects.filter(mo_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib).order_by('mo_kelas')
	if request.method == "POST":
		formset = nilai_sikap_spiritual_wajib_formset(request.POST, queryset=nilai_sikap_spiritual_wajib_queryset)
		if formset.is_valid():
			instances = formset.save()
			for instance in instances:
				# if IsNewChecker(instance.mo_penilaian_sikap_spiritual_uuid):
				if instance.mo_kelas is not None: 
					instance.mo_mata_pelajaran_wajib = guru.guru_mata_pelajaran_wajib
					instance.save()
				else:
					murid = Profil_Murid.objects.get(murid_user=instance.mo_siswa.murid_user)
					instance.mo_mata_pelajaran_wajib = guru.guru_mata_pelajaran_wajib
					instance.mo_kelas = murid.murid_kelas
					instance.mo_tahun_ajaran = murid.murid_tahun_ajaran
					instance.mo_semester = murid.murid_semester
					instance.save()
			return redirect("monitoring:page_guru_input_sikap_spiritual_wajib")
	formset = nilai_sikap_spiritual_wajib_formset(queryset=nilai_sikap_spiritual_wajib_queryset)
	context = {
		"formset": formset,
		"guru": guru,
		'kelas': kelas,
	}
	return render(request, "templates_guru/kelola_sikap_spiritual/page_input_nilai/page_input_nilai_sikap_spiritual_mapel_wajib.html", context)
class page_guru_update_sikap_spiritual_wajib(UpdateView):
	model = Mo_Sikap_Spiritual
	form_class = page_guru_nilai_sikap_spiritual_forms
	success_url = reverse_lazy("monitoring:page_guru_list_sikap_spiritual_wajib")
	template_name = "templates_guru/kelola_sikap_spiritual/page_update_nilai/page_update_nilai_mapel_wajib.html"
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		context['guru'] = guru
		context['kelas'] = SKL_Kelas.objects.all()
		return context
class page_guru_delete_sikap_spiritual_wajib(DeleteView):
	model = Mo_Sikap_Spiritual
	success_url = reverse_lazy("monitoring:page_guru_list_sikap_spiritual_wajib")
	template_name = "templates_guru/kelola_sikap_spiritual/page_delete_nilai/page_delete_nilai_mapel_wajib.html"
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		context['guru'] = guru
		context['kelas'] = SKL_Kelas.objects.all()
		return context
	# END Keterampilan Mata Pelajaran Wajib ============================================================================================

	# Sikap Sosial Mata Pelajaran Jurusan ================================================================================================

	# Sikap Sosial Mata Pelajaran Jurusan ================================================================================================


def page_guru_list_sikap_spiritual_jurusan(request):
	kelas = SKL_Kelas.objects.all()
	guru = Gu_Profil_Guru.objects.get(guru_user=request.user)
	nilai_sikap_spiritual_mapel_jurusan = Mo_Sikap_Spiritual.objects.filter(mo_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan)
	nilai = page_guru_nilai_sikap_sosial_jurusan_filter(request.GET, queryset=nilai_sikap_spiritual_mapel_jurusan)
	context = {
		'nilai': nilai,
		'guru': guru,
		'kelas': kelas,
	}
	return render(request, "templates_guru/kelola_sikap_spiritual/page_list_nilai_mapel_jurusan.html", context)
def page_guru_input_sikap_spiritual_jurusan(request):
	kelas = SKL_Kelas.objects.all()
	guru = Gu_Profil_Guru.objects.get(guru_user=request.user)
	nilai_sikap_spiritual_jurusan_formset = modelformset_factory(Mo_Sikap_Spiritual, form=page_guru_input_nilai_sikap_spiritual_jurusan_forms, can_delete=True, extra=3)
	nilai_sikap_spiritual_jurusan_queryset = Mo_Sikap_Spiritual.objects.filter(mo_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan).order_by('mo_kelas')
	if request.method == "POST":
		formset = nilai_sikap_spiritual_jurusan_formset(request.POST, queryset=nilai_sikap_spiritual_jurusan_queryset)
		if formset.is_valid():
			instances = formset.save()
			for instance in instances:
				# if IsNewChecker(instance.mo_penilaian_sikap_spiritual_uuid):
				if instance.mo_kelas is not None: 
					instance.mo_mata_pelajaran_jurusan = guru.guru_mata_pelajaran_jurusan
					instance.save()
				else:
					murid = Profil_Murid.objects.get(murid_user=instance.mo_siswa.murid_user)
					instance.mo_mata_pelajaran_jurusan = guru.guru_mata_pelajaran_jurusan
					instance.mo_kelas = murid.murid_kelas
					instance.mo_tahun_ajaran = murid.murid_tahun_ajaran
					instance.mo_semester = murid.murid_semester
					instance.save()
			return redirect("monitoring:page_guru_input_sikap_spiritual_jurusan")
	formset = nilai_sikap_spiritual_jurusan_formset(queryset=nilai_sikap_spiritual_jurusan_queryset)
	context = {
		"formset": formset,
		"guru": guru,
		'kelas': kelas,
	}
	return render(request, "templates_guru/kelola_sikap_spiritual/page_input_nilai/page_input_nilai_sikap_spiritual_mapel_jurusan.html", context)
class page_guru_update_sikap_spiritual_jurusan(UpdateView):
	model = Mo_Sikap_Spiritual
	form_class = page_guru_nilai_sikap_spiritual_forms
	success_url = reverse_lazy("monitoring:page_guru_list_sikap_spiritual_jurusan")
	template_name = "templates_guru/kelola_sikap_spiritual/page_update_nilai/page_update_nilai_mapel_jurusan.html"
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		context['guru'] = guru
		context['kelas'] = SKL_Kelas.objects.all()
		return context
class page_guru_delete_sikap_spiritual_jurusan(DeleteView):
	model = Mo_Sikap_Spiritual
	success_url = reverse_lazy("monitoring:page_guru_list_sikap_spiritual_jurusan")
	template_name = "templates_guru/kelola_sikap_spiritual/page_delete_nilai/page_delete_nilai_mapel_jurusan.html"
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		context['guru'] = guru
		context['kelas'] = SKL_Kelas.objects.all()
		return context

# END PAGE INPUT NILAI /===============================================================================================================



# PAGE PERFORMA KELAS =================================================================================================================
def page_guru_performa_kelas_landing(request):
	kelas = SKL_Kelas.objects.all()
	jenjang_kelas = SKL_Jenjang_Kelas.objects.all()
	guru = Gu_Profil_Guru.objects.get(guru_user=request.user)

	# MAPEL WAJIB
	# nilai_pengetahuan_wajib = Mo_Penilaian_Pengetahuan.objects.filter(mo_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib).values('mo_kelas__skl_k_kelas_nama', 'mo_kelas__skl_k_kelas_uuid').annotate(Avg('mo_nilai_P1_TGS'), Avg('mo_nilai_P2_TLS'), Avg('mo_nilai_P3_TLS')).order_by('mo_kelas__skl_k_kelas_nama')
	nilai_pengetahuan_wajib = Mo_Penilaian_Pengetahuan.objects.filter(mo_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib).values('mo_kelas__skl_k_kelas_nama', 'mo_kelas__skl_k_kelas_uuid').annotate(Avg('mo_nilai_P1_TGS'), Avg('mo_nilai_P2_TLS'), Avg('mo_nilai_P3_TLS'), dominasi=((Sum('mo_nilai_P1_TGS')/Count('mo_nilai_P1_TGS') + Sum('mo_nilai_P2_TLS')/Count('mo_nilai_P2_TLS') + Sum('mo_nilai_P3_TLS')/Count('mo_nilai_P3_TLS'))/3)).order_by('mo_kelas__skl_k_kelas_nama')
	nilai_keterampilan_wajib = Mo_Penilaian_Keterampilan.objects.filter(mo_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib).values('mo_kelas__skl_k_kelas_nama', 'mo_kelas__skl_k_kelas_uuid').annotate(Avg('mo_praktek'), Avg('mo_produk'), Avg('mo_proyek'), Avg('mo_portofolio'), dominasi=((Sum('mo_praktek')/Count('mo_praktek') + Sum('mo_produk')/Count('mo_produk') + Sum('mo_proyek')/Count('mo_proyek') + Sum('mo_portofolio')/Count('mo_portofolio'))/4)).order_by('mo_kelas__skl_k_kelas_nama')
	nilai_sikap_sosial_wajib_q = Mo_Sikap_Sosial.objects.filter(mo_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib).values('mo_kelas__skl_k_kelas_nama', 'mo_kelas__skl_k_kelas_uuid', 'mo_nilai',).annotate(nilai_count=Count('mo_nilai')).order_by('mo_kelas__skl_k_kelas_nama')
	nilai_sikap_sosial_wajib_d = {}
	nilai_sikap_sosial_wajib = []
	for data in nilai_sikap_sosial_wajib_q:
		nilai_sikap_sosial_wajib_d[str(data['mo_kelas__skl_k_kelas_nama'])] = {
			'kelas': str(data['mo_kelas__skl_k_kelas_nama']),
			'uuid': str(data['mo_kelas__skl_k_kelas_uuid']),
			'SB': 0,
			'B': 0,
			'C': 0,
			'K': 0,
		}
	for data in nilai_sikap_sosial_wajib_q:
		if data['mo_nilai'] == 'Sangat Baik':
			nilai_sikap_sosial_wajib_d[str(data['mo_kelas__skl_k_kelas_nama'])]['SB'] = nilai_sikap_sosial_wajib_d[str(data['mo_kelas__skl_k_kelas_nama'])]['SB']+data['nilai_count']
		elif data['mo_nilai'] == 'Baik':
			nilai_sikap_sosial_wajib_d[str(data['mo_kelas__skl_k_kelas_nama'])]['B'] = nilai_sikap_sosial_wajib_d[str(data['mo_kelas__skl_k_kelas_nama'])]['B']+data['nilai_count']
		elif data['mo_nilai'] == 'Cukup':
			nilai_sikap_sosial_wajib_d[str(data['mo_kelas__skl_k_kelas_nama'])]['C'] = nilai_sikap_sosial_wajib_d[str(data['mo_kelas__skl_k_kelas_nama'])]['C']+data['nilai_count']
		elif data['mo_nilai'] == 'Kurang':
			nilai_sikap_sosial_wajib_d[str(data['mo_kelas__skl_k_kelas_nama'])]['K'] = nilai_sikap_sosial_wajib_d[str(data['mo_kelas__skl_k_kelas_nama'])]['K']+data['nilai_count']
	for data in nilai_sikap_sosial_wajib_d.keys():
		nilai_sikap_sosial_wajib.append(nilai_sikap_sosial_wajib_d[data])
	
	nilai_sikap_spiritual_wajib_q = Mo_Sikap_Spiritual.objects.filter(mo_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib).values('mo_kelas__skl_k_kelas_nama', 'mo_kelas__skl_k_kelas_uuid', 'mo_nilai',).annotate(nilai_count=Count('mo_nilai')).order_by('mo_kelas__skl_k_kelas_nama')
	nilai_sikap_spiritual_wajib_d = {}
	nilai_sikap_spiritual_wajib = []
	for data in nilai_sikap_spiritual_wajib_q:
		nilai_sikap_spiritual_wajib_d[str(data['mo_kelas__skl_k_kelas_nama'])] = {
			'kelas': str(data['mo_kelas__skl_k_kelas_nama']),
			'uuid': str(data['mo_kelas__skl_k_kelas_uuid']),
			'SB': 0,
			'B': 0,
			'C': 0,
			'K': 0,
		}
	for data in nilai_sikap_spiritual_wajib_q:
		if data['mo_nilai'] == 'Sangat Baik':
			nilai_sikap_spiritual_wajib_d[str(data['mo_kelas__skl_k_kelas_nama'])]['SB'] = nilai_sikap_spiritual_wajib_d[str(data['mo_kelas__skl_k_kelas_nama'])]['SB']+data['nilai_count']
		elif data['mo_nilai'] == 'Baik':
			nilai_sikap_spiritual_wajib_d[str(data['mo_kelas__skl_k_kelas_nama'])]['B'] = nilai_sikap_spiritual_wajib_d[str(data['mo_kelas__skl_k_kelas_nama'])]['B']+data['nilai_count']
		elif data['mo_nilai'] == 'Cukup':
			nilai_sikap_spiritual_wajib_d[str(data['mo_kelas__skl_k_kelas_nama'])]['C'] = nilai_sikap_spiritual_wajib_d[str(data['mo_kelas__skl_k_kelas_nama'])]['C']+data['nilai_count']
		elif data['mo_nilai'] == 'Kurang':
			nilai_sikap_spiritual_wajib_d[str(data['mo_kelas__skl_k_kelas_nama'])]['K'] = nilai_sikap_spiritual_wajib_d[str(data['mo_kelas__skl_k_kelas_nama'])]['K']+data['nilai_count']
	for data in nilai_sikap_spiritual_wajib_d.keys():
		nilai_sikap_spiritual_wajib.append(nilai_sikap_spiritual_wajib_d[data])

	nilai_ulangan_wajib = Mo_Penilaian_Ulangan.objects.filter(mo_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib).values('mo_kelas__skl_k_kelas_nama', 'mo_kelas__skl_k_kelas_uuid').annotate(dominasi=Avg('mo_nilai')).order_by('mo_kelas__skl_k_kelas_nama')
	nilai_uts_wajib = Mo_Penilaian_UTS.objects.filter(mo_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib).values('mo_kelas__skl_k_kelas_nama', 'mo_kelas__skl_k_kelas_uuid').annotate(dominasi=Avg('mo_nilai')).order_by('mo_kelas__skl_k_kelas_nama')
	nilai_uas_wajib = Mo_Penilaian_UAS.objects.filter(mo_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib).values('mo_kelas__skl_k_kelas_nama', 'mo_kelas__skl_k_kelas_uuid').annotate(dominasi=Avg('mo_nilai')).order_by('mo_kelas__skl_k_kelas_nama')



	# MAPEL jurusan
	# nilai_pengetahuan_jurusan = Mo_Penilaian_Pengetahuan.objects.filter(mo_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan).values('mo_kelas__skl_k_kelas_nama', 'mo_kelas__skl_k_kelas_uuid').annotate(Avg('mo_nilai_P1_TGS'), Avg('mo_nilai_P2_TLS'), Avg('mo_nilai_P3_TLS')).order_by('mo_kelas__skl_k_kelas_nama')
	# nilai_keterampilan_jurusan = Mo_Penilaian_Keterampilan.objects.filter(mo_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan).values('mo_kelas__skl_k_kelas_nama', 'mo_kelas__skl_k_kelas_uuid').annotate(Avg('mo_praktek'), Avg('mo_produk'), Avg('mo_proyek'), Avg('mo_portofolio')).order_by('mo_kelas__skl_k_kelas_nama')
	nilai_pengetahuan_jurusan = Mo_Penilaian_Pengetahuan.objects.filter(mo_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan).values('mo_kelas__skl_k_kelas_nama', 'mo_kelas__skl_k_kelas_uuid').annotate(Avg('mo_nilai_P1_TGS'), Avg('mo_nilai_P2_TLS'), Avg('mo_nilai_P3_TLS'), dominasi=((Sum('mo_nilai_P1_TGS')/Count('mo_nilai_P1_TGS') + Sum('mo_nilai_P2_TLS')/Count('mo_nilai_P2_TLS') + Sum('mo_nilai_P3_TLS')/Count('mo_nilai_P3_TLS'))/3)).order_by('mo_kelas__skl_k_kelas_nama')
	nilai_keterampilan_jurusan = Mo_Penilaian_Keterampilan.objects.filter(mo_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan).values('mo_kelas__skl_k_kelas_nama', 'mo_kelas__skl_k_kelas_uuid').annotate(Avg('mo_praktek'), Avg('mo_produk'), Avg('mo_proyek'), Avg('mo_portofolio'), dominasi=((Sum('mo_praktek')/Count('mo_praktek') + Sum('mo_produk')/Count('mo_produk') + Sum('mo_proyek')/Count('mo_proyek') + Sum('mo_portofolio')/Count('mo_portofolio'))/4)).order_by('mo_kelas__skl_k_kelas_nama')
	nilai_sikap_sosial_jurusan_q = Mo_Sikap_Sosial.objects.filter(mo_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan).values('mo_kelas__skl_k_kelas_nama', 'mo_kelas__skl_k_kelas_uuid', 'mo_nilai',).annotate(nilai_count=Count('mo_nilai')).order_by('mo_kelas__skl_k_kelas_nama')
	nilai_sikap_sosial_jurusan_d = {}
	nilai_sikap_sosial_jurusan = []
	for data in nilai_sikap_sosial_jurusan_q:
		nilai_sikap_sosial_jurusan_d[str(data['mo_kelas__skl_k_kelas_nama'])] = {
			'kelas': str(data['mo_kelas__skl_k_kelas_nama']),
			'uuid': str(data['mo_kelas__skl_k_kelas_uuid']),
			'SB': 0,
			'B': 0,
			'C': 0,
			'K': 0,
		}
	for data in nilai_sikap_sosial_jurusan_q:
		if data['mo_nilai'] == 'Sangat Baik':
			nilai_sikap_sosial_jurusan_d[str(data['mo_kelas__skl_k_kelas_nama'])]['SB'] = nilai_sikap_sosial_jurusan_d[str(data['mo_kelas__skl_k_kelas_nama'])]['SB']+data['nilai_count']
		elif data['mo_nilai'] == 'Baik':
			nilai_sikap_sosial_jurusan_d[str(data['mo_kelas__skl_k_kelas_nama'])]['B'] = nilai_sikap_sosial_jurusan_d[str(data['mo_kelas__skl_k_kelas_nama'])]['B']+data['nilai_count']
		elif data['mo_nilai'] == 'Cukup':
			nilai_sikap_sosial_jurusan_d[str(data['mo_kelas__skl_k_kelas_nama'])]['C'] = nilai_sikap_sosial_jurusan_d[str(data['mo_kelas__skl_k_kelas_nama'])]['C']+data['nilai_count']
		elif data['mo_nilai'] == 'Kurang':
			nilai_sikap_sosial_jurusan_d[str(data['mo_kelas__skl_k_kelas_nama'])]['K'] = nilai_sikap_sosial_jurusan_d[str(data['mo_kelas__skl_k_kelas_nama'])]['K']+data['nilai_count']
	for data in nilai_sikap_sosial_jurusan_d.keys():
		nilai_sikap_sosial_jurusan.append(nilai_sikap_sosial_jurusan_d[data])
	
	nilai_sikap_spiritual_jurusan_q = Mo_Sikap_Spiritual.objects.filter(mo_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan).values('mo_kelas__skl_k_kelas_nama', 'mo_kelas__skl_k_kelas_uuid', 'mo_nilai',).annotate(nilai_count=Count('mo_nilai')).order_by('mo_kelas__skl_k_kelas_nama')
	nilai_sikap_spiritual_jurusan_d = {}
	nilai_sikap_spiritual_jurusan = []
	for data in nilai_sikap_spiritual_jurusan_q:
		nilai_sikap_spiritual_jurusan_d[str(data['mo_kelas__skl_k_kelas_nama'])] = {
			'kelas': str(data['mo_kelas__skl_k_kelas_nama']),
			'uuid': str(data['mo_kelas__skl_k_kelas_uuid']),
			'SB': 0,
			'B': 0,
			'C': 0,
			'K': 0,
		}
	for data in nilai_sikap_spiritual_jurusan_q:
		if data['mo_nilai'] == 'Sangat Baik':
			nilai_sikap_spiritual_jurusan_d[str(data['mo_kelas__skl_k_kelas_nama'])]['SB'] = nilai_sikap_spiritual_jurusan_d[str(data['mo_kelas__skl_k_kelas_nama'])]['SB']+data['nilai_count']
		elif data['mo_nilai'] == 'Baik':
			nilai_sikap_spiritual_jurusan_d[str(data['mo_kelas__skl_k_kelas_nama'])]['B'] = nilai_sikap_spiritual_jurusan_d[str(data['mo_kelas__skl_k_kelas_nama'])]['B']+data['nilai_count']
		elif data['mo_nilai'] == 'Cukup':
			nilai_sikap_spiritual_jurusan_d[str(data['mo_kelas__skl_k_kelas_nama'])]['C'] = nilai_sikap_spiritual_jurusan_d[str(data['mo_kelas__skl_k_kelas_nama'])]['C']+data['nilai_count']
		elif data['mo_nilai'] == 'Kurang':
			nilai_sikap_spiritual_jurusan_d[str(data['mo_kelas__skl_k_kelas_nama'])]['K'] = nilai_sikap_spiritual_jurusan_d[str(data['mo_kelas__skl_k_kelas_nama'])]['K']+data['nilai_count']
	for data in nilai_sikap_spiritual_jurusan_d.keys():
		nilai_sikap_spiritual_jurusan.append(nilai_sikap_spiritual_jurusan_d[data])

	nilai_ulangan_jurusan = Mo_Penilaian_Ulangan.objects.filter(mo_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan).values('mo_kelas__skl_k_kelas_nama', 'mo_kelas__skl_k_kelas_uuid').annotate(dominasi=Avg('mo_nilai')).order_by('mo_kelas__skl_k_kelas_nama')
	nilai_uts_jurusan = Mo_Penilaian_UTS.objects.filter(mo_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan).values('mo_kelas__skl_k_kelas_nama', 'mo_kelas__skl_k_kelas_uuid').annotate(dominasi=Avg('mo_nilai')).order_by('mo_kelas__skl_k_kelas_nama')
	nilai_uas_jurusan = Mo_Penilaian_UAS.objects.filter(mo_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan).values('mo_kelas__skl_k_kelas_nama', 'mo_kelas__skl_k_kelas_uuid').annotate(dominasi=Avg('mo_nilai')).order_by('mo_kelas__skl_k_kelas_nama')


	# GRAFIK
	data_grafik = {
		'kelas_10': {
			'pengetahuan': {
				'label_kelas': [],
				'data': [],
			},
			'keterampilan': {
				'label_kelas': [],
				'data': [],
			},
			'sikap_sosial': {
				'label_kelas': [],
				'data': [],
			},
			'sikap_spiritual': {
				'label_kelas': [],
				'data': [],
			},
			'ulangan': {
				'label_kelas': [],
				'data': [],
			},
			'uts': {
				'label_kelas': [],
				'data': [],
			},
			'uas': {
				'label_kelas': [],
				'data': [],
			},
		},
		'kelas_11': {
			'pengetahuan': {
				'label_kelas': [],
				'data': [],
			},
			'keterampilan': {
				'label_kelas': [],
				'data': [],
			},
			'sikap_sosial': {
				'label_kelas': [],
				'data': [],
			},
			'sikap_spiritual': {
				'label_kelas': [],
				'data': [],
			},
			'ulangan': {
				'label_kelas': [],
				'data': [],
			},
			'uts': {
				'label_kelas': [],
				'data': [],
			},
			'uas': {
				'label_kelas': [],
				'data': [],
			},
		},
		'kelas_12': {
			'pengetahuan': {
				'label_kelas': [],
				'data': [],
			},
			'keterampilan': {
				'label_kelas': [],
				'data': [],
			},
			'sikap_sosial': {
				'label_kelas': [],
				'data': [],
			},
			'sikap_spiritual': {
				'label_kelas': [],
				'data': [],
			},
			'ulangan': {
				'label_kelas': [],
				'data': [],
			},
			'uts': {
				'label_kelas': [],
				'data': [],
			},
			'uas': {
				'label_kelas': [],
				'data': [],
			},
		},
	}
	data_grafik_huruf = {
		'sosial': {
			'label_kelas': [],
			'SB': [],
			'B': [],
			'C': [],
			'K': [],
		},
		'spiritual': {
			'label_kelas': [],
			'SB': [],
			'B': [],
			'C': [],
			'K': [],
		},
	}
	for data in nilai_sikap_sosial_wajib:
		oo = "'" + data['kelas'] + "'"
		data_grafik_huruf['sosial']['label_kelas'].append(oo)
		data_grafik_huruf['sosial']['SB'].append(data['SB'])
		data_grafik_huruf['sosial']['B'].append(data['B'])
		data_grafik_huruf['sosial']['C'].append(data['C'])
		data_grafik_huruf['sosial']['K'].append(data['K'])

	for data in nilai_sikap_spiritual_wajib:
		oo = data['kelas']
		data_grafik_huruf['spiritual']['label_kelas'].append(oo)
		data_grafik_huruf['spiritual']['SB'].append(data['SB'])
		data_grafik_huruf['spiritual']['B'].append(data['B'])
		data_grafik_huruf['spiritual']['C'].append(data['C'])
		data_grafik_huruf['spiritual']['K'].append(data['K'])

	for data in nilai_pengetahuan_wajib:
		print(data)
		if "10" in data['mo_kelas__skl_k_kelas_nama']:
			oo = data['mo_kelas__skl_k_kelas_nama']
			data_grafik['kelas_10']['pengetahuan']['label_kelas'].append(oo)
			try:
				data_grafik['kelas_10']['pengetahuan']['data'].append(round(data['dominasi'],2))
			except:
				data_grafik['kelas_10']['pengetahuan']['data'].append(0)
			# data_grafik['kelas_10']['pengetahuan']['data'].append(round(data['dominasi'],2))
		elif "11" in data['mo_kelas__skl_k_kelas_nama']:
			oo = data['mo_kelas__skl_k_kelas_nama']
			data_grafik['kelas_11']['pengetahuan']['label_kelas'].append(oo)
			try:
				data_grafik['kelas_11']['pengetahuan']['data'].append(round(data['dominasi'],2))
			except:
				data_grafik['kelas_11']['pengetahuan']['data'].append(0)
		elif "12" in data['mo_kelas__skl_k_kelas_nama']:
			oo = data['mo_kelas__skl_k_kelas_nama']
			data_grafik['kelas_12']['pengetahuan']['label_kelas'].append(oo)
			try:
				data_grafik['kelas_12']['pengetahuan']['data'].append(round(data['dominasi'],2))
			except:
				data_grafik['kelas_12']['pengetahuan']['data'].append(0)

	for data in nilai_keterampilan_wajib:
		if "10" in data['mo_kelas__skl_k_kelas_nama']:
			oo = data['mo_kelas__skl_k_kelas_nama']
			data_grafik['kelas_10']['keterampilan']['label_kelas'].append(oo)
			try:
				data_grafik['kelas_10']['keterampilan']['data'].append(round(data['dominasi'],2))
			except:
				data_grafik['kelas_10']['keterampilan']['data'].append(0)
		elif "11" in data['mo_kelas__skl_k_kelas_nama']:
			oo = data['mo_kelas__skl_k_kelas_nama']
			data_grafik['kelas_11']['keterampilan']['label_kelas'].append(oo)
			try:
				data_grafik['kelas_11']['keterampilan']['data'].append(round(data['dominasi'],2))
			except:
				data_grafik['kelas_11']['keterampilan']['data'].append(0)
		elif "12" in data['mo_kelas__skl_k_kelas_nama']:
			oo = data['mo_kelas__skl_k_kelas_nama']
			data_grafik['kelas_12']['keterampilan']['label_kelas'].append(oo)
			try:
				data_grafik['kelas_12']['keterampilan']['data'].append(round(data['dominasi'],2))
			except:
				data_grafik['kelas_12']['keterampilan']['data'].append(0)

	for data in nilai_ulangan_wajib:
		if "10" in data['mo_kelas__skl_k_kelas_nama']:
			oo = data['mo_kelas__skl_k_kelas_nama']
			data_grafik['kelas_10']['ulangan']['label_kelas'].append(oo)
			try:
				data_grafik['kelas_10']['ulangan']['data'].append(round(data['dominasi'],2))
			except:
				data_grafik['kelas_10']['ulangan']['data'].append(0)
		elif "11" in data['mo_kelas__skl_k_kelas_nama']:
			oo = data['mo_kelas__skl_k_kelas_nama']
			data_grafik['kelas_11']['ulangan']['label_kelas'].append(oo)
			try:
				data_grafik['kelas_11']['ulangan']['data'].append(round(data['dominasi'],2))
			except:
				data_grafik['kelas_11']['ulangan']['data'].append(0)
		elif "12" in data['mo_kelas__skl_k_kelas_nama']:
			oo = data['mo_kelas__skl_k_kelas_nama']
			data_grafik['kelas_12']['ulangan']['label_kelas'].append(oo)
			try:
				data_grafik['kelas_12']['ulangan']['data'].append(round(data['dominasi'],2))
			except:
				data_grafik['kelas_12']['ulangan']['data'].append(0)

	for data in nilai_uts_wajib:
		if "10" in data['mo_kelas__skl_k_kelas_nama']:
			oo = data['mo_kelas__skl_k_kelas_nama']
			data_grafik['kelas_10']['uts']['label_kelas'].append(oo)
			try:
				data_grafik['kelas_10']['uts']['data'].append(round(data['dominasi'],2))
			except:
				data_grafik['kelas_10']['uts']['data'].append(0)
		elif "11" in data['mo_kelas__skl_k_kelas_nama']:
			oo = data['mo_kelas__skl_k_kelas_nama']
			data_grafik['kelas_11']['uts']['label_kelas'].append(oo)
			try:
				data_grafik['kelas_11']['uts']['data'].append(round(data['dominasi'],2))
			except:
				data_grafik['kelas_11']['uts']['data'].append(0)
		elif "12" in data['mo_kelas__skl_k_kelas_nama']:
			oo = data['mo_kelas__skl_k_kelas_nama']
			data_grafik['kelas_12']['uts']['label_kelas'].append(oo)
			try:
				data_grafik['kelas_12']['uts']['data'].append(round(data['dominasi'],2))
			except:
				data_grafik['kelas_12']['uts']['data'].append(0)

	for data in nilai_uas_wajib:
		if "10" in data['mo_kelas__skl_k_kelas_nama']:
			oo = data['mo_kelas__skl_k_kelas_nama']
			data_grafik['kelas_10']['uas']['label_kelas'].append(oo)
			try:
				data_grafik['kelas_10']['uas']['data'].append(round(data['dominasi'],2))
			except:
				data_grafik['kelas_10']['uas']['data'].append(0)
		elif "11" in data['mo_kelas__skl_k_kelas_nama']:
			oo = data['mo_kelas__skl_k_kelas_nama']
			data_grafik['kelas_11']['uas']['label_kelas'].append(oo)
			try:
				data_grafik['kelas_11']['uas']['data'].append(round(data['dominasi'],2))
			except:
				data_grafik['kelas_11']['uas']['data'].append(0)
		elif "12" in data['mo_kelas__skl_k_kelas_nama']:
			oo = data['mo_kelas__skl_k_kelas_nama']
			data_grafik['kelas_12']['uas']['label_kelas'].append(oo)
			try:
				data_grafik['kelas_12']['uas']['data'].append(round(data['dominasi'],2))
			except:
				data_grafik['kelas_12']['uas']['data'].append(0)


	data_grafik_jurusan = {
		'kelas_10': {
			'pengetahuan': {
				'label_kelas': [],
				'data': [],
			},
			'keterampilan': {
				'label_kelas': [],
				'data': [],
			},
			'sikap_sosial': {
				'label_kelas': [],
				'data': [],
			},
			'sikap_spiritual': {
				'label_kelas': [],
				'data': [],
			},
			'ulangan': {
				'label_kelas': [],
				'data': [],
			},
			'uts': {
				'label_kelas': [],
				'data': [],
			},
			'uas': {
				'label_kelas': [],
				'data': [],
			},
		},
		'kelas_11': {
			'pengetahuan': {
				'label_kelas': [],
				'data': [],
			},
			'keterampilan': {
				'label_kelas': [],
				'data': [],
			},
			'sikap_sosial': {
				'label_kelas': [],
				'data': [],
			},
			'sikap_spiritual': {
				'label_kelas': [],
				'data': [],
			},
			'ulangan': {
				'label_kelas': [],
				'data': [],
			},
			'uts': {
				'label_kelas': [],
				'data': [],
			},
			'uas': {
				'label_kelas': [],
				'data': [],
			},
		},
		'kelas_12': {
			'pengetahuan': {
				'label_kelas': [],
				'data': [],
			},
			'keterampilan': {
				'label_kelas': [],
				'data': [],
			},
			'sikap_sosial': {
				'label_kelas': [],
				'data': [],
			},
			'sikap_spiritual': {
				'label_kelas': [],
				'data': [],
			},
			'ulangan': {
				'label_kelas': [],
				'data': [],
			},
			'uts': {
				'label_kelas': [],
				'data': [],
			},
			'uas': {
				'label_kelas': [],
				'data': [],
			},
		},
	}
	data_grafik_huruf_jurusan = {
		'sosial': {
			'label_kelas': [],
			'SB': [],
			'B': [],
			'C': [],
			'K': [],
		},
		'spiritual': {
			'label_kelas': [],
			'SB': [],
			'B': [],
			'C': [],
			'K': [],
		},
	}
	for data in nilai_sikap_sosial_jurusan:
		oo = "'" + data['kelas'] + "'"
		data_grafik_huruf_jurusan['sosial']['label_kelas'].append(oo)
		data_grafik_huruf_jurusan['sosial']['SB'].append(data['SB'])
		data_grafik_huruf_jurusan['sosial']['B'].append(data['B'])
		data_grafik_huruf_jurusan['sosial']['C'].append(data['C'])
		data_grafik_huruf_jurusan['sosial']['K'].append(data['K'])
	for data in nilai_sikap_spiritual_jurusan:
		oo = data['kelas']
		data_grafik_huruf_jurusan['spiritual']['label_kelas'].append(oo)
		data_grafik_huruf_jurusan['spiritual']['SB'].append(data['SB'])
		data_grafik_huruf_jurusan['spiritual']['B'].append(data['B'])
		data_grafik_huruf_jurusan['spiritual']['C'].append(data['C'])
		data_grafik_huruf_jurusan['spiritual']['K'].append(data['K'])

	for data in nilai_pengetahuan_jurusan:
		if "10" in data['mo_kelas__skl_k_kelas_nama']:
			oo = data['mo_kelas__skl_k_kelas_nama']
			data_grafik_jurusan['kelas_10']['pengetahuan']['label_kelas'].append(oo)
			data_grafik_jurusan['kelas_10']['pengetahuan']['data'].append(round(data['dominasi'],2))
		elif "11" in data['mo_kelas__skl_k_kelas_nama']:
			oo = data['mo_kelas__skl_k_kelas_nama']
			data_grafik_jurusan['kelas_11']['pengetahuan']['label_kelas'].append(oo)
			data_grafik_jurusan['kelas_11']['pengetahuan']['data'].append(round(data['dominasi'],2))
		elif "12" in data['mo_kelas__skl_k_kelas_nama']:
			oo = data['mo_kelas__skl_k_kelas_nama']
			data_grafik_jurusan['kelas_12']['pengetahuan']['label_kelas'].append(oo)
			data_grafik_jurusan['kelas_12']['pengetahuan']['data'].append(round(data['dominasi'],2))
			
	for data in nilai_keterampilan_jurusan:
		if "10" in data['mo_kelas__skl_k_kelas_nama']:
			oo = data['mo_kelas__skl_k_kelas_nama']
			data_grafik_jurusan['kelas_10']['keterampilan']['label_kelas'].append(oo)
			data_grafik_jurusan['kelas_10']['keterampilan']['data'].append(round(data['dominasi'],2))
		elif "11" in data['mo_kelas__skl_k_kelas_nama']:
			oo = data['mo_kelas__skl_k_kelas_nama']
			data_grafik_jurusan['kelas_11']['keterampilan']['label_kelas'].append(oo)
			data_grafik_jurusan['kelas_11']['keterampilan']['data'].append(round(data['dominasi'],2))
		elif "12" in data['mo_kelas__skl_k_kelas_nama']:
			oo = data['mo_kelas__skl_k_kelas_nama']
			data_grafik_jurusan['kelas_12']['keterampilan']['label_kelas'].append(oo)
			data_grafik_jurusan['kelas_12']['keterampilan']['data'].append(round(data['dominasi'],2))

	for data in nilai_ulangan_jurusan:
		if "10" in data['mo_kelas__skl_k_kelas_nama']:
			oo = data['mo_kelas__skl_k_kelas_nama']
			data_grafik_jurusan['kelas_10']['ulangan']['label_kelas'].append(oo)
			try:
				data_grafik_jurusan['kelas_10']['ulangan']['data'].append(round(data['dominasi'],2))
			except:
				data_grafik_jurusan['kelas_10']['ulangan']['data'].append(0)
		elif "11" in data['mo_kelas__skl_k_kelas_nama']:
			oo = data['mo_kelas__skl_k_kelas_nama']
			data_grafik_jurusan['kelas_11']['ulangan']['label_kelas'].append(oo)
			try:
				data_grafik_jurusan['kelas_11']['ulangan']['data'].append(round(data['dominasi'],2))
			except:
				data_grafik_jurusan['kelas_11']['ulangan']['data'].append(0)
		elif "12" in data['mo_kelas__skl_k_kelas_nama']:
			oo = data['mo_kelas__skl_k_kelas_nama']
			data_grafik_jurusan['kelas_12']['ulangan']['label_kelas'].append(oo)
			try:
				data_grafik_jurusan['kelas_12']['ulangan']['data'].append(round(data['dominasi'],2))
			except:
				data_grafik_jurusan['kelas_12']['ulangan']['data'].append(0)

	for data in nilai_uts_jurusan:
		if "10" in data['mo_kelas__skl_k_kelas_nama']:
			oo = data['mo_kelas__skl_k_kelas_nama']
			data_grafik_jurusan['kelas_10']['uts']['label_kelas'].append(oo)
			try:
				data_grafik_jurusan['kelas_10']['uts']['data'].append(round(data['dominasi'],2))
			except:
				data_grafik_jurusan['kelas_10']['uts']['data'].append(0)
		elif "11" in data['mo_kelas__skl_k_kelas_nama']:
			oo = data['mo_kelas__skl_k_kelas_nama']
			data_grafik_jurusan['kelas_11']['uts']['label_kelas'].append(oo)
			try:
				data_grafik_jurusan['kelas_11']['uts']['data'].append(round(data['dominasi'],2))
			except:
				data_grafik_jurusan['kelas_11']['uts']['data'].append(0)
		elif "12" in data['mo_kelas__skl_k_kelas_nama']:
			oo = data['mo_kelas__skl_k_kelas_nama']
			data_grafik_jurusan['kelas_12']['uts']['label_kelas'].append(oo)
			try:
				data_grafik_jurusan['kelas_12']['uts']['data'].append(round(data['dominasi'],2))
			except:
				data_grafik_jurusan['kelas_12']['uts']['data'].append(0)

	for data in nilai_uas_jurusan:
		if "10" in data['mo_kelas__skl_k_kelas_nama']:
			oo = data['mo_kelas__skl_k_kelas_nama']
			data_grafik_jurusan['kelas_10']['uas']['label_kelas'].append(oo)
			try:
				data_grafik_jurusan['kelas_10']['uas']['data'].append(round(data['dominasi'],2))
			except:
				data_grafik_jurusan['kelas_10']['uas']['data'].append(0)
		elif "11" in data['mo_kelas__skl_k_kelas_nama']:
			oo = data['mo_kelas__skl_k_kelas_nama']
			data_grafik_jurusan['kelas_11']['uas']['label_kelas'].append(oo)
			try:
				data_grafik_jurusan['kelas_11']['uas']['data'].append(round(data['dominasi'],2))
			except:
				data_grafik_jurusan['kelas_11']['uas']['data'].append(0)
		elif "12" in data['mo_kelas__skl_k_kelas_nama']:
			oo = data['mo_kelas__skl_k_kelas_nama']
			data_grafik_jurusan['kelas_12']['uas']['label_kelas'].append(oo)
			try:
				data_grafik_jurusan['kelas_12']['uas']['data'].append(round(data['dominasi'],2))
			except:
				data_grafik_jurusan['kelas_12']['uas']['data'].append(0)

	o = "LOG KERJA"
	context = {
		'kelas': kelas,
		'guru': guru,
		'jenjang_kelas': jenjang_kelas,

		'nilai_pengetahuan_wajib': nilai_pengetahuan_wajib,
		'nilai_keterampilan_wajib': nilai_keterampilan_wajib,
		'nilai_sikap_sosial_wajib': nilai_sikap_sosial_wajib,
		'nilai_sikap_spiritual_wajib': nilai_sikap_spiritual_wajib,
		'nilai_ulangan_wajib': nilai_ulangan_wajib,
		'nilai_uts_wajib': nilai_uts_wajib,
		'nilai_uas_wajib': nilai_uas_wajib,

		'nilai_pengetahuan_jurusan': nilai_pengetahuan_jurusan,
		'nilai_keterampilan_jurusan': nilai_keterampilan_jurusan,
		'nilai_sikap_sosial_jurusan': nilai_sikap_sosial_jurusan,
		'nilai_sikap_spiritual_jurusan': nilai_sikap_spiritual_jurusan,
		'nilai_ulangan_jurusan': nilai_ulangan_jurusan,
		'nilai_uts_jurusan': nilai_uts_jurusan,
		'nilai_uas_jurusan': nilai_uas_jurusan,

		'data_grafik': json.dumps(data_grafik),
		'data_grafik_huruf': json.dumps(data_grafik_huruf),

		'data_grafik_jurusan': json.dumps(data_grafik_jurusan),
		'data_grafik_huruf_jurusan': json.dumps(data_grafik_huruf_jurusan),
	}

	return render(request, 'templates_guru/page_performa_kelas/page_perfoma_kelas_landing.html', context)


def page_guru_performa_kelas_wajib_detail(request, uuidnyaKelas):
	kelas = SKL_Kelas.objects.all()
	kelas_page = SKL_Kelas.objects.get(skl_k_kelas_uuid=uuidnyaKelas)
	guru = Gu_Profil_Guru.objects.get(guru_user=request.user)

	# PERFOMA KELAS MAPEL WAJIB
	nilai_pengetahuan_wajib = Mo_Penilaian_Pengetahuan.objects.filter(mo_kelas__skl_k_kelas_uuid=uuidnyaKelas, mo_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib).order_by('mo_siswa', 'mo_tahun_ajaran', 'mo_semester', 'mo_kompetensi_dasar', 'mo_kompetensi_dasar__guru_nomor_kd' ,'mo_penilaian_ke')
	nilai_keterampilan_wajib = Mo_Penilaian_Keterampilan.objects.filter(mo_kelas__skl_k_kelas_uuid=uuidnyaKelas, mo_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib).order_by('mo_siswa', 'mo_tahun_ajaran', 'mo_semester', 'mo_kompetensi_dasar', 'mo_kompetensi_dasar__guru_nomor_kd' ,'mo_penilaian_ke')
	nilai_sikap_sosial_wajib = Mo_Sikap_Sosial.objects.filter(mo_kelas__skl_k_kelas_uuid=uuidnyaKelas, mo_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib).order_by('mo_siswa', 'mo_tahun_ajaran', 'mo_semester', 'mo_kompetensi_dasar', 'mo_kompetensi_dasar__guru_nomor_kd' ,'mo_penilaian_ke')
	nilai_sikap_spiritual_wajib = Mo_Sikap_Spiritual.objects.filter(mo_kelas__skl_k_kelas_uuid=uuidnyaKelas, mo_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib).order_by('mo_siswa', 'mo_tahun_ajaran', 'mo_semester', 'mo_kompetensi_dasar', 'mo_kompetensi_dasar__guru_nomor_kd' ,'mo_penilaian_ke')
	nilai_ulangan_wajib = Mo_Penilaian_Ulangan.objects.filter(mo_kelas__skl_k_kelas_uuid=uuidnyaKelas, mo_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib).order_by('mo_siswa', 'mo_tahun_ajaran', 'mo_semester', 'mo_kompetensi_dasar', 'mo_kompetensi_dasar__guru_nomor_kd' ,'mo_ulangan_ke')
	nilai_uts_wajib = Mo_Penilaian_UTS.objects.filter(mo_kelas__skl_k_kelas_uuid=uuidnyaKelas, mo_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib).order_by('mo_siswa', 'mo_tahun_ajaran', 'mo_semester',)
	nilai_uas_wajib = Mo_Penilaian_UAS.objects.filter(mo_kelas__skl_k_kelas_uuid=uuidnyaKelas, mo_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib).order_by('mo_siswa', 'mo_tahun_ajaran', 'mo_semester',)
	
	context = {
		'guru': guru,
		'kelas': kelas,
		'kelas_page': kelas_page,
		'nilai_pengetahuan_wajib': nilai_pengetahuan_wajib,
		'nilai_keterampilan_wajib': nilai_keterampilan_wajib,
		'nilai_sikap_sosial_wajib': nilai_sikap_sosial_wajib,
		'nilai_sikap_spiritual_wajib': nilai_sikap_spiritual_wajib,
		'nilai_ulangan_wajib': nilai_ulangan_wajib,
		'nilai_uts_wajib': nilai_uts_wajib,
		'nilai_uas_wajib': nilai_uas_wajib,
	}
	return render(request, 'templates_guru/page_performa_kelas/page_perfoma_kelas_wajib_detail.html', context)


def page_guru_performa_kelas_jurusan_detail(request, uuidnyaKelas):
	kelas = SKL_Kelas.objects.all()
	kelas_page = SKL_Kelas.objects.get(skl_k_kelas_uuid=uuidnyaKelas)
	guru = Gu_Profil_Guru.objects.get(guru_user=request.user)

	# PERFOMA KELAS MAPEL jurusan
	nilai_pengetahuan_jurusan = Mo_Penilaian_Pengetahuan.objects.filter(mo_kelas__skl_k_kelas_uuid=uuidnyaKelas, mo_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan).order_by('mo_siswa', 'mo_tahun_ajaran', 'mo_semester', 'mo_kompetensi_dasar', 'mo_kompetensi_dasar__guru_nomor_kd' ,'mo_penilaian_ke')
	nilai_keterampilan_jurusan = Mo_Penilaian_Keterampilan.objects.filter(mo_kelas__skl_k_kelas_uuid=uuidnyaKelas, mo_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan).order_by('mo_siswa', 'mo_tahun_ajaran', 'mo_semester', 'mo_kompetensi_dasar', 'mo_kompetensi_dasar__guru_nomor_kd' ,'mo_penilaian_ke')
	nilai_sikap_sosial_jurusan = Mo_Sikap_Sosial.objects.filter(mo_kelas__skl_k_kelas_uuid=uuidnyaKelas, mo_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan).order_by('mo_siswa', 'mo_tahun_ajaran', 'mo_semester', 'mo_kompetensi_dasar', 'mo_kompetensi_dasar__guru_nomor_kd' ,'mo_penilaian_ke')
	nilai_sikap_spiritual_jurusan = Mo_Sikap_Spiritual.objects.filter(mo_kelas__skl_k_kelas_uuid=uuidnyaKelas, mo_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan).order_by('mo_siswa', 'mo_tahun_ajaran', 'mo_semester', 'mo_kompetensi_dasar', 'mo_kompetensi_dasar__guru_nomor_kd' ,'mo_penilaian_ke')
	nilai_ulangan_jurusan = Mo_Penilaian_Ulangan.objects.filter(mo_kelas__skl_k_kelas_uuid=uuidnyaKelas, mo_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan).order_by('mo_siswa', 'mo_tahun_ajaran', 'mo_semester', 'mo_kompetensi_dasar', 'mo_kompetensi_dasar__guru_nomor_kd' ,'mo_ulangan_ke')
	nilai_uts_jurusan = Mo_Penilaian_UTS.objects.filter(mo_kelas__skl_k_kelas_uuid=uuidnyaKelas, mo_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan).order_by('mo_siswa', 'mo_tahun_ajaran', 'mo_semester',)
	nilai_uas_jurusan = Mo_Penilaian_UAS.objects.filter(mo_kelas__skl_k_kelas_uuid=uuidnyaKelas, mo_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan).order_by('mo_siswa', 'mo_tahun_ajaran', 'mo_semester',)
	
	context = {
		'guru': guru,
		'kelas': kelas,
		'kelas_page': kelas_page,
		'nilai_pengetahuan_jurusan': nilai_pengetahuan_jurusan,
		'nilai_keterampilan_jurusan': nilai_keterampilan_jurusan,
		'nilai_sikap_sosial_jurusan': nilai_sikap_sosial_jurusan,
		'nilai_sikap_spiritual_jurusan': nilai_sikap_spiritual_jurusan,
		'nilai_ulangan_jurusan': nilai_ulangan_jurusan,
		'nilai_uts_jurusan': nilai_uts_jurusan,
		'nilai_uas_jurusan': nilai_uas_jurusan,
	}
	return render(request, 'templates_guru/page_performa_kelas/page_perfoma_kelas_jurusan_detail.html', context)
# END PAGE PERFORMA KELAS =============================================================================================================



# KELOLA KKM =============================================================================================================

def page_guru_kkm_wajib(request):
	guru = Gu_Profil_Guru.objects.get(guru_user=request.user)
	kkm = Mo_Penilaian_Ulangan_KKM.objects.filter(mo_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib).order_by('mo_jenjang_kelas')

	context = {
		'guru': guru,
		'kkm': kkm,
	}
	return render(request, 'templates_guru/kelola_kkm/page_guru_kkm_wajib.html', context)

class page_guru_kkm_wajib_create(CreateView):
	model = Mo_Penilaian_Ulangan_KKM
	form_class = page_guru_kkm_create_forms
	success_url = reverse_lazy("monitoring:page_guru_kkm_wajib")
	template_name = "templates_guru/kelola_kkm/page_guru_kkm_wajib_create.html"
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		context['guru'] = guru
		context['kelas'] = SKL_Kelas.objects.all()
		return context
	def form_valid(self, form):
		response = super(page_guru_kkm_wajib_create, self).form_valid(form)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		form.instance.mo_mata_pelajaran_wajib = guru.guru_mata_pelajaran_wajib
		form.save()
		return response

class page_guru_kkm_wajib_update(UpdateView):
	model = Mo_Penilaian_Ulangan_KKM
	form_class = page_guru_kkm_forms
	success_url = reverse_lazy("monitoring:page_guru_kkm_wajib")
	template_name = "templates_guru/kelola_kkm/page_guru_kkm_wajib_update.html"
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		context['guru'] = guru
		context['kelas'] = SKL_Kelas.objects.all()
		return context

class page_guru_kkm_wajib_delete(DeleteView):
	model = Mo_Penilaian_Ulangan_KKM
	success_url = reverse_lazy("monitoring:page_guru_kkm_wajib")
	template_name = "templates_guru/kelola_kkm/page_guru_kkm_wajib_delete.html"
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		context['guru'] = guru
		context['kelas'] = SKL_Kelas.objects.all()
		return context


def page_guru_kkm_jurusan(request):
	guru = Gu_Profil_Guru.objects.get(guru_user=request.user)
	kkm = Mo_Penilaian_Ulangan_KKM.objects.filter(mo_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan).order_by('mo_jenjang_kelas')

	context = {
		'guru': guru,
		'kkm': kkm,
	}
	return render(request, 'templates_guru/kelola_kkm/page_guru_kkm_jurusan.html', context)

class page_guru_kkm_jurusan_create(CreateView):
	model = Mo_Penilaian_Ulangan_KKM
	form_class = page_guru_kkm_create_forms
	success_url = reverse_lazy("monitoring:page_guru_kkm_jurusan")
	template_name = "templates_guru/kelola_kkm/page_guru_kkm_jurusan_create.html"
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		context['guru'] = guru
		context['kelas'] = SKL_Kelas.objects.all()
		return context
	def form_valid(self, form):
		response = super(page_guru_kkm_jurusan_create, self).form_valid(form)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		form.instance.mo_mata_pelajaran_jurusan = guru.guru_mata_pelajaran_jurusan
		form.save()
		return response

class page_guru_kkm_jurusan_update(UpdateView):
	model = Mo_Penilaian_Ulangan_KKM
	form_class = page_guru_kkm_forms
	success_url = reverse_lazy("monitoring:page_guru_kkm_jurusan")
	template_name = "templates_guru/kelola_kkm/page_guru_kkm_jurusan_update.html"
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		context['guru'] = guru
		context['kelas'] = SKL_Kelas.objects.all()
		return context

class page_guru_kkm_jurusan_delete(DeleteView):
	model = Mo_Penilaian_Ulangan_KKM
	success_url = reverse_lazy("monitoring:page_guru_kkm_jurusan")
	template_name = "templates_guru/kelola_kkm/page_guru_kkm_jurusan_delete.html"
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		context['guru'] = guru
		context['kelas'] = SKL_Kelas.objects.all()
		return context
# END KELOLA KKM =============================================================================================================



# CATATAN SISWA ==============================================================================================================

def page_guru_catatan_wajib(request):
	guru = Gu_Profil_Guru.objects.get(guru_user=request.user)
	catatan = Gu_Catatan.objects.filter(guru_catatan_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib).order_by('guru_catatan_siswa__murid_nama')

	context = {
		'guru': guru,
		'catatan': catatan,
	}
	return render(request, 'templates_guru/kelola_catatan/page_guru_catatan_wajib.html', context)

class page_guru_catatan_wajib_create(CreateView):
	model = Gu_Catatan
	form_class = page_guru_catatan_create_forms
	success_url = reverse_lazy("monitoring:page_guru_catatan_wajib")
	template_name = "templates_guru/kelola_catatan/page_guru_catatan_wajib_create.html"
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		context['guru'] = guru
		context['kelas'] = SKL_Kelas.objects.all()
		return context
	def form_valid(self, form):
		response = super(page_guru_catatan_wajib_create, self).form_valid(form)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		form.instance.guru_catatan_mata_pelajaran_wajib = guru.guru_mata_pelajaran_wajib
		form.save()
		return response

class page_guru_catatan_wajib_update(UpdateView):
	model = Gu_Catatan
	form_class = page_guru_catatan_forms
	success_url = reverse_lazy("monitoring:page_guru_catatan_wajib")
	template_name = "templates_guru/kelola_catatan/page_guru_catatan_wajib_update.html"
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		context['guru'] = guru
		context['kelas'] = SKL_Kelas.objects.all()
		return context

class page_guru_catatan_wajib_delete(DeleteView):
	model = Gu_Catatan
	success_url = reverse_lazy("monitoring:page_guru_catatan_wajib")
	template_name = "templates_guru/kelola_catatan/page_guru_catatan_wajib_delete.html"
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		context['guru'] = guru
		context['kelas'] = SKL_Kelas.objects.all()
		return context


def page_guru_catatan_jurusan(request):
	guru = Gu_Profil_Guru.objects.get(guru_user=request.user)
	catatan = Gu_Catatan.objects.filter(guru_catatan_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan).order_by('guru_catatan_siswa__murid_nama')

	context = {
		'guru': guru,
		'catatan': catatan,
	}
	return render(request, 'templates_guru/kelola_catatan/page_guru_catatan_jurusan.html', context)

class page_guru_catatan_jurusan_create(CreateView):
	model = Gu_Catatan
	form_class = page_guru_catatan_create_forms
	success_url = reverse_lazy("monitoring:page_guru_catatan_jurusan")
	template_name = "templates_guru/kelola_catatan/page_guru_catatan_jurusan_create.html"
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		context['guru'] = guru
		context['kelas'] = SKL_Kelas.objects.all()
		return context
	def form_valid(self, form):
		response = super(page_guru_catatan_jurusan_create, self).form_valid(form)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		form.instance.guru_catatan_mata_pelajaran_jurusan = guru.guru_mata_pelajaran_jurusan
		form.save()
		return response

class page_guru_catatan_jurusan_update(UpdateView):
	model = Gu_Catatan
	form_class = page_guru_catatan_forms
	success_url = reverse_lazy("monitoring:page_guru_catatan_jurusan")
	template_name = "templates_guru/kelola_catatan/page_guru_catatan_jurusan_update.html"
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		context['guru'] = guru
		context['kelas'] = SKL_Kelas.objects.all()
		return context

class page_guru_catatan_jurusan_delete(DeleteView):
	model = Gu_Catatan
	success_url = reverse_lazy("monitoring:page_guru_catatan_jurusan")
	template_name = "templates_guru/kelola_catatan/page_guru_catatan_jurusan_delete.html"
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		context['guru'] = guru
		context['kelas'] = SKL_Kelas.objects.all()
		return context


# END CATATAN SISWA ==========================================================================================================


# ULANGAN SISWA ==============================================================================================================
def page_guru_list_ulangan_wajib(request):
	kelas = SKL_Kelas.objects.all()
	guru = Gu_Profil_Guru.objects.get(guru_user=request.user)
	nilai_ulangan_mapel_wajib = Mo_Penilaian_Ulangan.objects.filter(mo_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib)
	nilai = page_guru_nilai_ulangan_wajib_filter(request.GET, queryset=nilai_ulangan_mapel_wajib)
	context = {
		'nilai': nilai,
		'guru': guru,
		'kelas': kelas,
	}
	return render(request, "templates_guru/kelola_ulangan/page_list_nilai_mapel_wajib.html", context)
def page_guru_input_ulangan_wajib(request):
	kelas = SKL_Kelas.objects.all()
	guru = Gu_Profil_Guru.objects.get(guru_user=request.user)
	nilai_ulangan_wajib_formset = modelformset_factory(Mo_Penilaian_Ulangan, form=page_guru_input_nilai_ulangan_wajib_forms, can_delete=True, extra=5)
	nilai_ulangan_wajib_queryset = Mo_Penilaian_Ulangan.objects.filter(mo_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib).order_by('mo_kelas')
	if request.method == "POST":
		formset = nilai_ulangan_wajib_formset(request.POST, queryset=nilai_ulangan_wajib_queryset)
		if formset.is_valid():
			instances = formset.save()
			for instance in instances:
				# if IsNewChecker(instance.mo_penilaian_ulangan_uuid) is not True:
				# if Mo_Penilaian_ulangan.objects.filter(mo_penilaian_ulangan_uuid=instance.mo_penilaian_ulangan_uuid).exists():
				if instance.mo_kelas is not None or instance.mo_tahun_ajaran is not None or instance.mo_semester is not None: 
				# try:
					# Mo_Penilaian_ulangan.objects.get(mo_penilaian_ulangan_uuid="instance.mo_penilaian_ulangan_uuid")
					instance.mo_mata_pelajaran_wajib = guru.guru_mata_pelajaran_wajib
					instance.save()
					# print('Tidak ada')
				else:
				# except:
					murid = Profil_Murid.objects.get(murid_user=instance.mo_siswa.murid_user)
					instance.mo_mata_pelajaran_wajib = guru.guru_mata_pelajaran_wajib
					instance.mo_kelas = murid.murid_kelas
					instance.mo_tahun_ajaran = murid.murid_tahun_ajaran
					instance.mo_semester = murid.murid_semester
					instance.save()
					# print('ada')

			return redirect("monitoring:page_guru_input_ulangan_wajib")
	formset = nilai_ulangan_wajib_formset(queryset=nilai_ulangan_wajib_queryset)
	context = {
		"formset": formset,
		"guru": guru,
		'kelas': kelas,
	}
	return render(request, "templates_guru/kelola_ulangan/page_input_nilai/page_input_nilai_ulangan_mapel_wajib.html", context)
class page_guru_update_ulangan_wajib(UpdateView):
	model = Mo_Penilaian_Ulangan
	form_class = page_guru_nilai_ulangan_wajib_forms
	success_url = reverse_lazy("monitoring:page_guru_list_ulangan_wajib")
	template_name = "templates_guru/kelola_ulangan/page_update_nilai/page_update_nilai_mapel_wajib.html"
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		context['guru'] = guru
		context['kelas'] = SKL_Kelas.objects.all()
		return context
class page_guru_delete_ulangan_wajib(DeleteView):
	model = Mo_Penilaian_Ulangan
	success_url = reverse_lazy("monitoring:page_guru_list_ulangan_wajib")
	template_name = "templates_guru/kelola_ulangan/page_delete_nilai/page_delete_nilai_mapel_wajib.html"
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		context['guru'] = guru
		context['kelas'] = SKL_Kelas.objects.all()
		return context






def page_guru_list_ulangan_jurusan(request):
	kelas = SKL_Kelas.objects.all()
	guru = Gu_Profil_Guru.objects.get(guru_user=request.user)
	nilai_ulangan_mapel_jurusan = Mo_Penilaian_Ulangan.objects.filter(mo_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan)
	nilai = page_guru_nilai_ulangan_jurusan_filter(request.GET, queryset=nilai_ulangan_mapel_jurusan)
	context = {
		'nilai': nilai,
		'guru': guru,
		'kelas': kelas,
	}
	return render(request, "templates_guru/kelola_ulangan/page_list_nilai_mapel_jurusan.html", context)
def page_guru_input_ulangan_jurusan(request):
	kelas = SKL_Kelas.objects.all()
	guru = Gu_Profil_Guru.objects.get(guru_user=request.user)
	nilai_ulangan_jurusan_formset = modelformset_factory(Mo_Penilaian_Ulangan, form=page_guru_input_nilai_ulangan_jurusan_forms, can_delete=True, extra=5)
	nilai_ulangan_jurusan_queryset = Mo_Penilaian_Ulangan.objects.filter(mo_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan).order_by('mo_kelas')
	if request.method == "POST":
		formset = nilai_ulangan_jurusan_formset(request.POST, queryset=nilai_ulangan_jurusan_queryset)
		if formset.is_valid():
			instances = formset.save()
			for instance in instances:
				# if IsNewChecker(instance.mo_penilaian_ulangan_uuid) is not True:
				# if Mo_Penilaian_ulangan.objects.filter(mo_penilaian_ulangan_uuid=instance.mo_penilaian_ulangan_uuid).exists():
				if instance.mo_kelas is not None or instance.mo_tahun_ajaran is not None or instance.mo_semester is not None: 
				# try:
					# Mo_Penilaian_ulangan.objects.get(mo_penilaian_ulangan_uuid="instance.mo_penilaian_ulangan_uuid")
					instance.mo_mata_pelajaran_jurusan = guru.guru_mata_pelajaran_jurusan
					instance.save()
					# print('Tidak ada')
				else:
				# except:
					murid = Profil_Murid.objects.get(murid_user=instance.mo_siswa.murid_user)
					instance.mo_mata_pelajaran_jurusan = guru.guru_mata_pelajaran_jurusan
					instance.mo_kelas = murid.murid_kelas
					instance.mo_tahun_ajaran = murid.murid_tahun_ajaran
					instance.mo_semester = murid.murid_semester
					instance.save()
					# print('ada')

			return redirect("monitoring:page_guru_input_ulangan_jurusan")
	formset = nilai_ulangan_jurusan_formset(queryset=nilai_ulangan_jurusan_queryset)
	context = {
		"formset": formset,
		"guru": guru,
		'kelas': kelas,
	}
	return render(request, "templates_guru/kelola_ulangan/page_input_nilai/page_input_nilai_ulangan_mapel_jurusan.html", context)
class page_guru_update_ulangan_jurusan(UpdateView):
	model = Mo_Penilaian_Ulangan
	form_class = page_guru_nilai_ulangan_jurusan_forms
	success_url = reverse_lazy("monitoring:page_guru_list_ulangan_jurusan")
	template_name = "templates_guru/kelola_ulangan/page_update_nilai/page_update_nilai_mapel_jurusan.html"
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		context['guru'] = guru
		context['kelas'] = SKL_Kelas.objects.all()
		return context
class page_guru_delete_ulangan_jurusan(DeleteView):
	model = Mo_Penilaian_Ulangan
	success_url = reverse_lazy("monitoring:page_guru_list_ulangan_jurusan")
	template_name = "templates_guru/kelola_ulangan/page_delete_nilai/page_delete_nilai_mapel_jurusan.html"
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		context['guru'] = guru
		context['kelas'] = SKL_Kelas.objects.all()
		return context
# END ULANGAN SISWA ==========================================================================================================




# UTS SISWA ===============================================================================
def page_guru_list_uts_wajib(request):
	kelas = SKL_Kelas.objects.all()
	guru = Gu_Profil_Guru.objects.get(guru_user=request.user)
	nilai_uts_mapel_wajib = Mo_Penilaian_UTS.objects.filter(mo_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib)
	nilai = page_guru_nilai_uts_wajib_filter(request.GET, queryset=nilai_uts_mapel_wajib)
	context = {
		'nilai': nilai,
		'guru': guru,
		'kelas': kelas,
	}
	return render(request, "templates_guru/kelola_uts/page_list_nilai_mapel_wajib.html", context)
def page_guru_input_uts_wajib(request):
	kelas = SKL_Kelas.objects.all()
	guru = Gu_Profil_Guru.objects.get(guru_user=request.user)
	nilai_uts_wajib_formset = modelformset_factory(Mo_Penilaian_UTS, form=page_guru_input_nilai_uts_wajib_forms, can_delete=True, extra=5)
	nilai_uts_wajib_queryset = Mo_Penilaian_UTS.objects.filter(mo_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib).order_by('mo_kelas')
	if request.method == "POST":
		formset = nilai_uts_wajib_formset(request.POST, queryset=nilai_uts_wajib_queryset)
		if formset.is_valid():
			instances = formset.save()
			for instance in instances:
				# if IsNewChecker(instance.mo_penilaian_uts_uuid) is not True:
				# if Mo_Penilaian_uts.objects.filter(mo_penilaian_uts_uuid=instance.mo_penilaian_uts_uuid).exists():
				if instance.mo_kelas is not None or instance.mo_tahun_ajaran is not None or instance.mo_semester is not None: 
				# try:
					# Mo_Penilaian_uts.objects.get(mo_penilaian_uts_uuid="instance.mo_penilaian_uts_uuid")
					instance.mo_mata_pelajaran_wajib = guru.guru_mata_pelajaran_wajib
					instance.save()
					# print('Tidak ada')
				else:
				# except:
					murid = Profil_Murid.objects.get(murid_user=instance.mo_siswa.murid_user)
					instance.mo_mata_pelajaran_wajib = guru.guru_mata_pelajaran_wajib
					instance.mo_kelas = murid.murid_kelas
					instance.mo_tahun_ajaran = murid.murid_tahun_ajaran
					instance.mo_semester = murid.murid_semester
					instance.save()
					# print('ada')

			return redirect("monitoring:page_guru_input_uts_wajib")
	formset = nilai_uts_wajib_formset(queryset=nilai_uts_wajib_queryset)
	context = {
		"formset": formset,
		"guru": guru,
		'kelas': kelas,
	}
	return render(request, "templates_guru/kelola_uts/page_input_nilai/page_input_nilai_uts_mapel_wajib.html", context)
class page_guru_update_uts_wajib(UpdateView):
	model = Mo_Penilaian_UTS
	form_class = page_guru_nilai_uts_wajib_forms
	success_url = reverse_lazy("monitoring:page_guru_list_uts_wajib")
	template_name = "templates_guru/kelola_uts/page_update_nilai/page_update_nilai_mapel_wajib.html"
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		context['guru'] = guru
		context['kelas'] = SKL_Kelas.objects.all()
		return context
class page_guru_delete_uts_wajib(DeleteView):
	model = Mo_Penilaian_UTS
	success_url = reverse_lazy("monitoring:page_guru_list_uts_wajib")
	template_name = "templates_guru/kelola_uts/page_delete_nilai/page_delete_nilai_mapel_wajib.html"
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		context['guru'] = guru
		context['kelas'] = SKL_Kelas.objects.all()
		return context



def page_guru_list_uts_jurusan(request):
	kelas = SKL_Kelas.objects.all()
	guru = Gu_Profil_Guru.objects.get(guru_user=request.user)
	nilai_uts_mapel_jurusan = Mo_Penilaian_UTS.objects.filter(mo_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan)
	nilai = page_guru_nilai_uts_jurusan_filter(request.GET, queryset=nilai_uts_mapel_jurusan)
	context = {
		'nilai': nilai,
		'guru': guru,
		'kelas': kelas,
	}
	return render(request, "templates_guru/kelola_uts/page_list_nilai_mapel_jurusan.html", context)
def page_guru_input_uts_jurusan(request):
	kelas = SKL_Kelas.objects.all()
	guru = Gu_Profil_Guru.objects.get(guru_user=request.user)
	nilai_uts_jurusan_formset = modelformset_factory(Mo_Penilaian_UTS, form=page_guru_input_nilai_uts_jurusan_forms, can_delete=True, extra=5)
	nilai_uts_jurusan_queryset = Mo_Penilaian_UTS.objects.filter(mo_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan).order_by('mo_kelas')
	if request.method == "POST":
		formset = nilai_uts_jurusan_formset(request.POST, queryset=nilai_uts_jurusan_queryset)
		if formset.is_valid():
			instances = formset.save()
			for instance in instances:
				# if IsNewChecker(instance.mo_penilaian_uts_uuid) is not True:
				# if Mo_Penilaian_uts.objects.filter(mo_penilaian_uts_uuid=instance.mo_penilaian_uts_uuid).exists():
				if instance.mo_kelas is not None or instance.mo_tahun_ajaran is not None or instance.mo_semester is not None: 
				# try:
					# Mo_Penilaian_uts.objects.get(mo_penilaian_uts_uuid="instance.mo_penilaian_uts_uuid")
					instance.mo_mata_pelajaran_jurusan = guru.guru_mata_pelajaran_jurusan
					instance.save()
					# print('Tidak ada')
				else:
				# except:
					murid = Profil_Murid.objects.get(murid_user=instance.mo_siswa.murid_user)
					instance.mo_mata_pelajaran_jurusan = guru.guru_mata_pelajaran_jurusan
					instance.mo_kelas = murid.murid_kelas
					instance.mo_tahun_ajaran = murid.murid_tahun_ajaran
					instance.mo_semester = murid.murid_semester
					instance.save()
					# print('ada')

			return redirect("monitoring:page_guru_input_uts_jurusan")
	formset = nilai_uts_jurusan_formset(queryset=nilai_uts_jurusan_queryset)
	context = {
		"formset": formset,
		"guru": guru,
		'kelas': kelas,
	}
	return render(request, "templates_guru/kelola_uts/page_input_nilai/page_input_nilai_uts_mapel_jurusan.html", context)
class page_guru_update_uts_jurusan(UpdateView):
	model = Mo_Penilaian_UTS
	form_class = page_guru_nilai_uts_jurusan_forms
	success_url = reverse_lazy("monitoring:page_guru_list_uts_jurusan")
	template_name = "templates_guru/kelola_uts/page_update_nilai/page_update_nilai_mapel_jurusan.html"
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		context['guru'] = guru
		context['kelas'] = SKL_Kelas.objects.all()
		return context
class page_guru_delete_uts_jurusan(DeleteView):
	model = Mo_Penilaian_UTS
	success_url = reverse_lazy("monitoring:page_guru_list_uts_jurusan")
	template_name = "templates_guru/kelola_uts/page_delete_nilai/page_delete_nilai_mapel_jurusan.html"
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		context['guru'] = guru
		context['kelas'] = SKL_Kelas.objects.all()
		return context
# END UTS SISWA ===========================================================================




# uas SISWA ===============================================================================
def page_guru_list_uas_wajib(request):
	kelas = SKL_Kelas.objects.all()
	guru = Gu_Profil_Guru.objects.get(guru_user=request.user)
	nilai_uas_mapel_wajib = Mo_Penilaian_UAS.objects.filter(mo_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib)
	nilai = page_guru_nilai_uas_wajib_filter(request.GET, queryset=nilai_uas_mapel_wajib)
	context = {
		'nilai': nilai,
		'guru': guru,
		'kelas': kelas,
	}
	return render(request, "templates_guru/kelola_uas/page_list_nilai_mapel_wajib.html", context)
def page_guru_input_uas_wajib(request):
	kelas = SKL_Kelas.objects.all()
	guru = Gu_Profil_Guru.objects.get(guru_user=request.user)
	nilai_uas_wajib_formset = modelformset_factory(Mo_Penilaian_UAS, form=page_guru_input_nilai_uas_wajib_forms, can_delete=True, extra=5)
	nilai_uas_wajib_queryset = Mo_Penilaian_UAS.objects.filter(mo_mata_pelajaran_wajib=guru.guru_mata_pelajaran_wajib).order_by('mo_kelas')
	if request.method == "POST":
		formset = nilai_uas_wajib_formset(request.POST, queryset=nilai_uas_wajib_queryset)
		if formset.is_valid():
			instances = formset.save()
			for instance in instances:
				# if IsNewChecker(instance.mo_penilaian_uas_uuid) is not True:
				# if Mo_Penilaian_uas.objects.filter(mo_penilaian_uas_uuid=instance.mo_penilaian_uas_uuid).exists():
				if instance.mo_kelas is not None or instance.mo_tahun_ajaran is not None or instance.mo_semester is not None: 
				# try:
					# Mo_Penilaian_uas.objects.get(mo_penilaian_uas_uuid="instance.mo_penilaian_uas_uuid")
					instance.mo_mata_pelajaran_wajib = guru.guru_mata_pelajaran_wajib
					instance.save()
					# print('Tidak ada')
				else:
				# except:
					murid = Profil_Murid.objects.get(murid_user=instance.mo_siswa.murid_user)
					instance.mo_mata_pelajaran_wajib = guru.guru_mata_pelajaran_wajib
					instance.mo_kelas = murid.murid_kelas
					instance.mo_tahun_ajaran = murid.murid_tahun_ajaran
					instance.mo_semester = murid.murid_semester
					instance.save()
					# print('ada')

			return redirect("monitoring:page_guru_input_uas_wajib")
	formset = nilai_uas_wajib_formset(queryset=nilai_uas_wajib_queryset)
	context = {
		"formset": formset,
		"guru": guru,
		'kelas': kelas,
	}
	return render(request, "templates_guru/kelola_uas/page_input_nilai/page_input_nilai_uas_mapel_wajib.html", context)
class page_guru_update_uas_wajib(UpdateView):
	model = Mo_Penilaian_UAS
	form_class = page_guru_nilai_uas_wajib_forms
	success_url = reverse_lazy("monitoring:page_guru_list_uas_wajib")
	template_name = "templates_guru/kelola_uas/page_update_nilai/page_update_nilai_mapel_wajib.html"
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		context['guru'] = guru
		context['kelas'] = SKL_Kelas.objects.all()
		return context
class page_guru_delete_uas_wajib(DeleteView):
	model = Mo_Penilaian_UAS
	success_url = reverse_lazy("monitoring:page_guru_list_uas_wajib")
	template_name = "templates_guru/kelola_uas/page_delete_nilai/page_delete_nilai_mapel_wajib.html"
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		context['guru'] = guru
		context['kelas'] = SKL_Kelas.objects.all()
		return context



def page_guru_list_uas_jurusan(request):
	kelas = SKL_Kelas.objects.all()
	guru = Gu_Profil_Guru.objects.get(guru_user=request.user)
	nilai_uas_mapel_jurusan = Mo_Penilaian_UAS.objects.filter(mo_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan)
	nilai = page_guru_nilai_uas_jurusan_filter(request.GET, queryset=nilai_uas_mapel_jurusan)
	context = {
		'nilai': nilai,
		'guru': guru,
		'kelas': kelas,
	}
	return render(request, "templates_guru/kelola_uas/page_list_nilai_mapel_jurusan.html", context)
def page_guru_input_uas_jurusan(request):
	kelas = SKL_Kelas.objects.all()
	guru = Gu_Profil_Guru.objects.get(guru_user=request.user)
	nilai_uas_jurusan_formset = modelformset_factory(Mo_Penilaian_UAS, form=page_guru_input_nilai_uas_jurusan_forms, can_delete=True, extra=5)
	nilai_uas_jurusan_queryset = Mo_Penilaian_UAS.objects.filter(mo_mata_pelajaran_jurusan=guru.guru_mata_pelajaran_jurusan).order_by('mo_kelas')
	if request.method == "POST":
		formset = nilai_uas_jurusan_formset(request.POST, queryset=nilai_uas_jurusan_queryset)
		if formset.is_valid():
			instances = formset.save()
			for instance in instances:
				# if IsNewChecker(instance.mo_penilaian_uas_uuid) is not True:
				# if Mo_Penilaian_uas.objects.filter(mo_penilaian_uas_uuid=instance.mo_penilaian_uas_uuid).exists():
				if instance.mo_kelas is not None or instance.mo_tahun_ajaran is not None or instance.mo_semester is not None: 
				# try:
					# Mo_Penilaian_uas.objects.get(mo_penilaian_uas_uuid="instance.mo_penilaian_uas_uuid")
					instance.mo_mata_pelajaran_jurusan = guru.guru_mata_pelajaran_jurusan
					instance.save()
					# print('Tidak ada')
				else:
				# except:
					murid = Profil_Murid.objects.get(murid_user=instance.mo_siswa.murid_user)
					instance.mo_mata_pelajaran_jurusan = guru.guru_mata_pelajaran_jurusan
					instance.mo_kelas = murid.murid_kelas
					instance.mo_tahun_ajaran = murid.murid_tahun_ajaran
					instance.mo_semester = murid.murid_semester
					instance.save()
					# print('ada')

			return redirect("monitoring:page_guru_input_uas_jurusan")
	formset = nilai_uas_jurusan_formset(queryset=nilai_uas_jurusan_queryset)
	context = {
		"formset": formset,
		"guru": guru,
		'kelas': kelas,
	}
	return render(request, "templates_guru/kelola_uas/page_input_nilai/page_input_nilai_uas_mapel_jurusan.html", context)
class page_guru_update_uas_jurusan(UpdateView):
	model = Mo_Penilaian_UAS
	form_class = page_guru_nilai_uas_jurusan_forms
	success_url = reverse_lazy("monitoring:page_guru_list_uas_jurusan")
	template_name = "templates_guru/kelola_uas/page_update_nilai/page_update_nilai_mapel_jurusan.html"
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		context['guru'] = guru
		context['kelas'] = SKL_Kelas.objects.all()
		return context
class page_guru_delete_uas_jurusan(DeleteView):
	model = Mo_Penilaian_UAS
	success_url = reverse_lazy("monitoring:page_guru_list_uas_jurusan")
	template_name = "templates_guru/kelola_uas/page_delete_nilai/page_delete_nilai_mapel_jurusan.html"
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		guru = Gu_Profil_Guru.objects.get(guru_user=get_current_user())
		context['guru'] = guru
		context['kelas'] = SKL_Kelas.objects.all()
		return context
# END uas SISWA ===========================================================================





# EXPORT IMPORT
# def export(request):
# 	pengetahuan_resource = PengetahuanResources()
# 	dataset = pengetahuan.export()
# 	response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
# 	response['Content-Disposition'] = "attachment; filename='nilai_pengetahuan.xls'"
# 	return response