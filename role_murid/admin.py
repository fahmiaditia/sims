from django.contrib import admin
from role_murid.models import *
from sekolah.models import *
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



class Profil_Murid_admin(admin.ModelAdmin, ExportCsvMixin):
	list_display = (
			'murid_profil_uuid',
			'murid_nama',
			'murid_nisn',
			'murid_kelas',
			'murid_semester',
			'murid_tahun_ajaran'
		)
	readonly_fields = ['murid_profil_uuid',]
	actions = ['export_as_csv']
	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if db_field.name == 'murid_user':
			kwargs['queryset'] = Akun.objects.filter(is_murid=True)
		return super().formfield_for_foreignkey(db_field, request, **kwargs)
admin.site.register(Profil_Murid, Profil_Murid_admin)