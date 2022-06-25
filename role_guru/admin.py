from django.contrib import admin
from role_guru.models import *
from sekolah.models import *
from django.http import HttpResponse
import csv

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



class Gu_Profil_Guru_admin(admin.ModelAdmin, ExportCsvMixin):
	list_display = (
			'guru_profil_uuid',
			'guru_nama',
			'guru_mata_pelajaran_wajib',
			'guru_mata_pelajaran_jurusan',
		)
	readonly_fields = ['guru_profil_uuid',]
	actions = ['export_as_csv']
	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if db_field.name == 'guru_user':
			kwargs['queryset'] = Akun.objects.filter(is_guru=True)
		return super().formfield_for_foreignkey(db_field, request, **kwargs)
admin.site.register(Gu_Profil_Guru, Gu_Profil_Guru_admin)


class Gu_Data_Kompetensi_Dasar_admin(admin.ModelAdmin, ExportCsvMixin):
	list_display = (
			'guru_kompetensi_dasar_uuid',
			'guru_nomor_kd',
			'guru_kompetensi_dasar_kelas',
			'guru_kompetensi_dasar_semester',
			'guru_kompetensi_dasar_mata_pelajaran_wajib',
			'guru_kompetensi_dasar_mata_pelajaran_jurusan',
		)
	readonly_fields = ['guru_kompetensi_dasar_uuid',]
	actions = ['export_as_csv']
admin.site.register(Gu_Data_Kompetensi_Dasar, Gu_Data_Kompetensi_Dasar_admin)


class Gu_Data_Teknik_Penilaian_admin(admin.ModelAdmin, ExportCsvMixin):
	list_display = (
			'guru_teknik_penilaian_uuid',
			'guru_teknik_penilaian',
		)
	readonly_fields = ['guru_teknik_penilaian_uuid',]
	actions = ['export_as_csv']
admin.site.register(Gu_Data_Teknik_Penilaian, Gu_Data_Teknik_Penilaian_admin)

class Gu_Catatan_admin(admin.ModelAdmin, ExportCsvMixin):
	list_display = (
			'guru_catatan_uuid',
			'guru_catatan_status',
			'guru_catatan_siswa',
			'guru_catatan_mata_pelajaran_wajib',
			'guru_catatan_mata_pelajaran_jurusan',
		)
	readonly_fields = ['guru_catatan_uuid',]
	actions = ['export_as_csv']
admin.site.register(Gu_Catatan, Gu_Catatan_admin)