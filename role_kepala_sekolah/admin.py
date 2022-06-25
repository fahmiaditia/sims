from django.contrib import admin
from role_kepala_sekolah.models import *
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


class Profil_Kepsek_admin(admin.ModelAdmin, ExportCsvMixin):
	list_display = (
			'kepsek_profil_uuid',
			'kepsek_nama',
		)
	readonly_fields = ['kepsek_profil_uuid',]
	actions = ['export_as_csv']
	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if db_field.name == 'kepsek_user':
			kwargs['queryset'] = Akun.objects.filter(is_kepsek=True)
		return super().formfield_for_foreignkey(db_field, request, **kwargs)
admin.site.register(Profil_Kepsek, Profil_Kepsek_admin)