from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from .forms import *
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



class Akun_admin(UserAdmin):
	models = Akun
	add_form = Akun_form

	fieldsets = (
			*UserAdmin.fieldsets,
			(
				'Role Akun',
				{
					'fields': (
							'uuid_akun',
							'is_guru',
							'is_murid',
							'is_pembimbing_ekskul',
							'is_kepsek',
							'is_bk',
						)
				}
				)
		)

	readonly_fields = ["uuid_akun",]
	list_display = (
			'username', 'uuid_akun', 'is_murid', 'is_guru', 'is_pembimbing_ekskul', 'is_kepsek', 'is_bk',
		)
admin.site.register(Akun, Akun_admin)


class SKL_Jurusan_admin(admin.ModelAdmin, ExportCsvMixin):
	list_display = (
			'skl_jurusan_uuid',
			'skl_jurusan_nama'
		)
	readonly_fields = ['skl_jurusan_uuid',]
	actions = ['export_as_csv']
admin.site.register(SKL_Jurusan, SKL_Jurusan_admin)


class SKL_Jenjang_Kelas_admin(admin.ModelAdmin, ExportCsvMixin):
	list_display = (
			'skl_jenjang_uuid',
			'skl_jenjang_nama'
		)
	readonly_fields = ['skl_jenjang_uuid',]
	actions = ['export_as_csv']
admin.site.register(SKL_Jenjang_Kelas, SKL_Jenjang_Kelas_admin)


class SKL_Ruang_Kelas_admin(admin.ModelAdmin, ExportCsvMixin):
	list_display = (
			'skl_ruang_uuid',
			'skl_ruang_nama'
		)
	readonly_fields = ['skl_ruang_uuid',]
	actions = ['export_as_csv']
admin.site.register(SKL_Ruang_Kelas, SKL_Ruang_Kelas_admin)


class SKL_Kelas_admin(admin.ModelAdmin, ExportCsvMixin):
	list_display = (
			'skl_k_kelas_uuid',
			'skl_k_kelas_nama',
		)
	readonly_fields = ['skl_k_kelas_uuid',]
	actions = ['export_as_csv']
admin.site.register(SKL_Kelas, SKL_Kelas_admin)


class SKL_Profil_Sekolah_admin(admin.ModelAdmin, ExportCsvMixin):
	list_display = (
			'skl_profil_sekolah_uuid',
			'skl_nama_sekolah',
		)
	readonly_fields = ['skl_profil_sekolah_uuid',]
	actions = ['export_as_csv']
admin.site.register(SKL_Profil_Sekolah, SKL_Profil_Sekolah_admin)


class SKL_Mata_Pelajaran_Wajib_admin(admin.ModelAdmin, ExportCsvMixin):
	list_display = (
			'mapel_wajib_pelajaran_uuid',
			'mapel_wajib_pelajaran',
		)
	readonly_fields = ['mapel_wajib_pelajaran_uuid',]
	actions = ['export_as_csv']
admin.site.register(SKL_Mata_Pelajaran_Wajib, SKL_Mata_Pelajaran_Wajib_admin)


class SKL_Mata_Pelajaran_Jurusan_admin(admin.ModelAdmin, ExportCsvMixin):
	list_display = (
			'mapel_jurusan_pelajaran_uuid',
			'mapel_jurusan_pelajaran',
			'mapel_jurusan_jurusan',
		)
	readonly_fields = ['mapel_jurusan_pelajaran_uuid',]
	actions = ['export_as_csv']
admin.site.register(SKL_Mata_Pelajaran_Jurusan, SKL_Mata_Pelajaran_Jurusan_admin)


class SKL_Semester_admin(admin.ModelAdmin, ExportCsvMixin):
	list_display = (
			'skl_s_semester_uuid',
			'skl_s_semester',
		)
	readonly_fields = ['skl_s_semester_uuid',]
	actions = ['export_as_csv']
admin.site.register(SKL_Semester, SKL_Semester_admin)


class SKL_Tahun_Ajaran_admin(admin.ModelAdmin, ExportCsvMixin):
	list_display = (
			'skl_t_tahun_ajaran_uuid',
			'skl_t_tahun_ajaran',
		)
	readonly_fields = ['skl_t_tahun_ajaran_uuid',]
	actions = ['export_as_csv']
admin.site.register(SKL_Tahun_Ajaran, SKL_Tahun_Ajaran_admin)


class SKL_Ekskul_admin(admin.ModelAdmin, ExportCsvMixin):
	list_display = (
			'skl_ekskul_uuid',
			'skl_ekskul',
		)
	readonly_fields = ['skl_ekskul_uuid',]
	actions = ['export_as_csv']
admin.site.register(SKL_Ekskul, SKL_Ekskul_admin)