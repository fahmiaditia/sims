from django.contrib import admin
from monitoring.models import *
import csv
from django.http import HttpResponse
# Register your models here.

class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"

class Mo_Penilaian_Pengetahuan_admin(admin.ModelAdmin, ExportCsvMixin):
	list_display = (
			'mo_siswa',
			'mo_kelas',
			'mo_mata_pelajaran_wajib',
			'mo_mata_pelajaran_jurusan',
			'mo_nilai_P1_TGS',
			'mo_nilai_P2_TLS',
			'mo_nilai_P3_TLS',
		)
	readonly_fields = ['mo_penilaian_pengetahuan_uuid',]
	actions = ['export_as_csv']
admin.site.register(Mo_Penilaian_Pengetahuan, Mo_Penilaian_Pengetahuan_admin)

class Mo_Penilaian_Keterampilan_admin(admin.ModelAdmin, ExportCsvMixin):
	list_display = (
			'mo_siswa',
			'mo_kelas',
			'mo_mata_pelajaran_wajib',
			'mo_mata_pelajaran_jurusan',
			'mo_praktek',
			'mo_produk',
			'mo_proyek',
			'mo_portofolio',
		)
	readonly_fields = ['mo_penilaian_keterampilan_uuid',]
	actions = ['export_as_csv']
admin.site.register(Mo_Penilaian_Keterampilan, Mo_Penilaian_Keterampilan_admin)

class Mo_Sikap_Sosial_admin(admin.ModelAdmin, ExportCsvMixin):
	list_display = (
			'mo_siswa',
			'mo_kelas',
			'mo_mata_pelajaran_wajib',
			'mo_mata_pelajaran_jurusan',
			'mo_penilaian_ke',
			'mo_semester',
			'mo_nilai',
			'mo_proyeksi_nilai',
		)
	readonly_fields = ['mo_penilaian_sikap_sosial_uuid',]
	actions = ['export_as_csv']
admin.site.register(Mo_Sikap_Sosial, Mo_Sikap_Sosial_admin)

class Mo_Sikap_Spiritual_admin(admin.ModelAdmin, ExportCsvMixin):
	list_display = (
			'mo_siswa',
			'mo_kelas',
			'mo_mata_pelajaran_wajib',
			'mo_mata_pelajaran_jurusan',
			'mo_penilaian_ke',
			'mo_semester',
			'mo_nilai',
			'mo_proyeksi_nilai',
		)
	readonly_fields = ['mo_penilaian_sikap_spiritual_uuid',]
	actions = ['export_as_csv']
admin.site.register(Mo_Sikap_Spiritual, Mo_Sikap_Spiritual_admin)

class Mo_Penilaian_Ulangan_KKM_admin(admin.ModelAdmin, ExportCsvMixin):
	list_display = (
			'mo_mata_pelajaran_wajib',
			'mo_mata_pelajaran_jurusan',
			'mo_jenjang_kelas',
			'mo_kkm',
		)
	readonly_fields = ['mo_penilaian_kkm_uuid',]
	actions = ['export_as_csv']
admin.site.register(Mo_Penilaian_Ulangan_KKM, Mo_Penilaian_Ulangan_KKM_admin)

class Mo_Penilaian_Ulangan_admin(admin.ModelAdmin, ExportCsvMixin):
	list_display = (
			'mo_status',
			'mo_siswa',
			'mo_kelas',
			'mo_tahun_ajaran',
			'mo_semester',
			'mo_mata_pelajaran_wajib',
			'mo_mata_pelajaran_jurusan',
			'mo_ulangan_ke',
			'mo_kkm',
			'mo_nilai',
			'mo_ketuntasan',
		)
	readonly_fields = ['mo_penilaian_ulangan_uuid',]
	actions = ['export_as_csv']
admin.site.register(Mo_Penilaian_Ulangan, Mo_Penilaian_Ulangan_admin)

class Mo_Penilaian_UTS_admin(admin.ModelAdmin, ExportCsvMixin):
	list_display = (
			'mo_status',
			'mo_siswa',
			'mo_kelas',
			'mo_tahun_ajaran',
			'mo_semester',
			'mo_mata_pelajaran_wajib',
			'mo_mata_pelajaran_jurusan',
			'mo_kkm',
			'mo_nilai',
			'mo_ketuntasan',
		)
	readonly_fields = ['mo_penilaian_uts_uuid',]
	actions = ['export_as_csv']
admin.site.register(Mo_Penilaian_UTS, Mo_Penilaian_UTS_admin)

class Mo_Penilaian_UAS_admin(admin.ModelAdmin, ExportCsvMixin):
	list_display = (
			'mo_status',
			'mo_siswa',
			'mo_kelas',
			'mo_tahun_ajaran',
			'mo_semester',
			'mo_mata_pelajaran_wajib',
			'mo_mata_pelajaran_jurusan',
			'mo_kkm',
			'mo_nilai',
			'mo_ketuntasan',
		)
	readonly_fields = ['mo_penilaian_uas_uuid',]
	actions = ['export_as_csv']
admin.site.register(Mo_Penilaian_UAS, Mo_Penilaian_UAS_admin)

class Mo_Penilaian_Ekskul_admin(admin.ModelAdmin, ExportCsvMixin):
	list_display = (
			'mo_siswa',
			'mo_kelas',
			'mo_semester',
			'mo_tahun_ajaran',
			'mo_ekskul',
			'mo_nilai',
		)
	readonly_fields = ['mo_penilaian_ekskul_uuid',]
	actions = ['export_as_csv']
admin.site.register(Mo_Penilaian_Ekskul, Mo_Penilaian_Ekskul_admin)

class Mo_Juara_Ekskul_admin(admin.ModelAdmin, ExportCsvMixin):
	list_display = (
			"mo_siswa",
			"mo_ekskul",
			"mo_tahun",	
			"mo_tingkatan",
			"mo_pelaksana",
			"mo_kejuaraan",		
			"mo_juara", 
		)
	readonly_fields = ['mo_juara_ekskul_uuid',]
	actions = ['export_as_csv']
admin.site.register(Mo_Juara_Ekskul, Mo_Juara_Ekskul_admin)