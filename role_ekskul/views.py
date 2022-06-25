from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.db.models import Avg, Count, Sum
from monitoring.models import *
from role_murid.models import *
from role_ekskul.models import *
from role_ekskul.forms import *
from role_ekskul.filters import *
from sekolah.models import *
from crum import get_current_user
from django_filters.views import FilterView
import json
# Create your views here.

def page_ekskul_dashboard(request):
	context = {}
	return render(request, 'templates_ekskul/dashboard_ekskul_r.html', context)


def page_ekskul_profil(request):
	profil_ekskul = Profil_Pembimbing.objects.get(ekskul_user=request.user)
	context = {
		'profil_ekskul': profil_ekskul,
	}
	return render(request, 'templates_ekskul/page_profil_ekskul/profil_ekskul.html', context)

class page_ekskul_profil_update(UpdateView):
	model = Profil_Pembimbing
	form_class = page_ekskul_profil_forms
	success_url = reverse_lazy('monitoring:page_ekskul_profil')
	template_name = 'templates_ekskul/page_profil_ekskul/profil_ekskul_update.html'


def page_ekskul_nilai(request):
	pembina = Profil_Pembimbing.objects.get(ekskul_user=request.user)
	info = SKL_Ekskul.objects.get(skl_ekskul=pembina.ekskul_mata_ekskul.skl_ekskul)
	nilai_ekskul_qs = Mo_Penilaian_Ekskul.objects.filter(mo_ekskul=pembina.ekskul_mata_ekskul)
	nilai = page_ekskul_nilai_filter(request.GET, queryset=nilai_ekskul_qs)

	context = {
		'info': info,
		'nilai': nilai,
	}
	return render(request, 'templates_ekskul/kelola_nilai_ekskul/page_nilai.html', context)

class page_ekskul_nilai_create(CreateView):
	model = Mo_Penilaian_Ekskul
	form_class = page_ekskul_penilaian_forms
	success_url = reverse_lazy('monitoring:page_ekskul_nilai')
	template_name = "templates_ekskul/kelola_nilai_ekskul/page_nilai_input.html"
	def get_context_data(self,*args, **kwargs):
		pengampu = Profil_Pembimbing.objects.get(ekskul_user=get_current_user())
		context = super(page_ekskul_nilai_create, self).get_context_data(*args,**kwargs)
		context['info'] = SKL_Ekskul.objects.get(skl_ekskul=pengampu.ekskul_mata_ekskul.skl_ekskul)
		return context
	def form_valid(self, form):
		response = super(page_ekskul_nilai_create, self).form_valid(form)
		pengampu = Profil_Pembimbing.objects.get(ekskul_user=get_current_user())
		form.instance.mo_ekskul = pengampu.ekskul_mata_ekskul
		form.save()
		return response

class page_ekskul_nilai_update(UpdateView):
	model = Mo_Penilaian_Ekskul
	form_class = page_ekskul_penilaian_forms
	success_url = reverse_lazy('monitoring:page_ekskul_nilai')
	template_name = 'templates_ekskul/kelola_nilai_ekskul/page_nilai_update.html'
	def get_context_data(self,*args, **kwargs):
		pengampu = Profil_Pembimbing.objects.get(ekskul_user=get_current_user())
		context = super(page_ekskul_nilai_update, self).get_context_data(*args,**kwargs)
		context['info'] = SKL_Ekskul.objects.get(skl_ekskul=pengampu.ekskul_mata_ekskul.skl_ekskul)
		return context

class page_ekskul_nilai_delete(DeleteView):
	model = Mo_Penilaian_Ekskul
	success_url = reverse_lazy('monitoring:page_ekskul_nilai')
	template_name = 'templates_ekskul/kelola_nilai_ekskul/page_nilai_delete.html'
	def get_context_data(self,*args, **kwargs):
		pengampu = Profil_Pembimbing.objects.get(ekskul_user=get_current_user())
		context = super(page_ekskul_nilai_delete, self).get_context_data(*args,**kwargs)
		context['info'] = SKL_Ekskul.objects.get(skl_ekskul=pengampu.ekskul_mata_ekskul.skl_ekskul)
		return context

def page_ekskul_perkembangan_siswa(request):
	pembina = Profil_Pembimbing.objects.get(ekskul_user=request.user)
	info = SKL_Ekskul.objects.get(skl_ekskul=pembina.ekskul_mata_ekskul.skl_ekskul)
	nilai = Mo_Penilaian_Ekskul.objects.filter(mo_ekskul=pembina.ekskul_mata_ekskul).values('mo_siswa__murid_nama', 'mo_siswa__murid_profil_uuid').annotate(Avg('mo_nilai')).order_by('mo_siswa__murid_nama')
	data_grafik = {
		'nama': [],
		'nilai': [],
	}
	p = 0
	for data in nilai:
		ff = f"{data['mo_siswa__murid_nama']}"
		data_grafik['nama'].append(ff)
		data_grafik['nilai'].append(data['mo_nilai__avg'])
	context = {
		'info': info,
		'nilai': nilai,
		'data_grafik': json.dumps(data_grafik),
	}
	return render(request, 'templates_ekskul/page_perkembangan_siswa/page_perkembangan_siswa_landing.html', context)

def page_ekskul_perkembangan_siswa_detail(request, uuidnyaMurid):
	pembina = Profil_Pembimbing.objects.get(ekskul_user=request.user)
	info = SKL_Ekskul.objects.get(skl_ekskul=pembina.ekskul_mata_ekskul.skl_ekskul)
	nilai = Mo_Penilaian_Ekskul.objects.filter(mo_siswa__murid_profil_uuid=uuidnyaMurid)
	data_grafik = {
		'urutan': [],
		'nilai': [],
	}
	p = 0
	for data in nilai:
		p += 1
		# ff = "'" + "Nilai ke:" + str(p) + "'"
		ff = f"Nilai ke {p}"
		data_grafik['urutan'].append(ff)
		data_grafik['nilai'].append(data.mo_nilai)
	context = {
		'info': info,
		'nilai': nilai,
		'data_grafik': json.dumps(data_grafik),
	}
	return render(request, 'templates_ekskul/page_perkembangan_siswa/page_perkembangan_siswa_landing_detail.html', context)

def page_ekskul_kejuaraan_landing(request):
	pembina = Profil_Pembimbing.objects.get(ekskul_user=request.user)
	info = SKL_Ekskul.objects.get(skl_ekskul=pembina.ekskul_mata_ekskul.skl_ekskul)
	juara_ekskul_qs = Mo_Juara_Ekskul.objects.filter(mo_ekskul=pembina.ekskul_mata_ekskul)
	juara = page_ekskul_kejuaraan_filter(request.GET, queryset=juara_ekskul_qs)

	context = {
		'info': info,
		'juara': juara,
	}
	return render(request, 'templates_ekskul/page_kejuaraan_ekskul/page_kejuaraan.html', context)

class page_ekskul_kejuaraan_create(CreateView):
	model = Mo_Juara_Ekskul
	form_class = page_ekskul_kejuaraan_penilaian_forms
	success_url = reverse_lazy('monitoring:page_ekskul_kejuaraan_landing')
	template_name = "templates_ekskul/page_kejuaraan_ekskul/page_kejuaraan_input.html"
	def get_context_data(self,*args, **kwargs):
		pengampu = Profil_Pembimbing.objects.get(ekskul_user=get_current_user())
		context = super(page_ekskul_kejuaraan_create, self).get_context_data(*args,**kwargs)
		context['info'] = SKL_Ekskul.objects.get(skl_ekskul=pengampu.ekskul_mata_ekskul.skl_ekskul)
		return context
	def form_valid(self, form):
		response = super(page_ekskul_kejuaraan_create, self).form_valid(form)
		pengampu = Profil_Pembimbing.objects.get(ekskul_user=get_current_user())
		form.instance.mo_ekskul = pengampu.ekskul_mata_ekskul
		form.save()
		return response

class page_ekskul_kejuaraan_update(UpdateView):
	model = Mo_Juara_Ekskul
	form_class = page_ekskul_kejuaraan_penilaian_forms
	success_url = reverse_lazy('monitoring:page_ekskul_kejuaraan_landing')
	template_name = 'templates_ekskul/page_kejuaraan_ekskul/page_kejuaraan_update.html'
	def get_context_data(self,*args, **kwargs):
		pengampu = Profil_Pembimbing.objects.get(ekskul_user=get_current_user())
		context = super(page_ekskul_kejuaraan_update, self).get_context_data(*args,**kwargs)
		context['info'] = SKL_Ekskul.objects.get(skl_ekskul=pengampu.ekskul_mata_ekskul.skl_ekskul)
		return context

class page_ekskul_kejuaraan_delete(DeleteView):
	model = Mo_Juara_Ekskul
	success_url = reverse_lazy('monitoring:page_ekskul_kejuaraan_landing')
	template_name = 'templates_ekskul/page_kejuaraan_ekskul/page_kejuaraan_delete.html'
	def get_context_data(self,*args, **kwargs):
		pengampu = Profil_Pembimbing.objects.get(ekskul_user=get_current_user())
		context = super(page_ekskul_kejuaraan_delete, self).get_context_data(*args,**kwargs)
		context['info'] = SKL_Ekskul.objects.get(skl_ekskul=pengampu.ekskul_mata_ekskul.skl_ekskul)
		return context

