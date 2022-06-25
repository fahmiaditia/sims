from django.contrib import admin
from role_ekskul.models import *
import csv
from django.http import HttpResponse

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


# Register your models here.
class Profil_Pembimbing_admin(admin.ModelAdmin, ExportCsvMixin):
	list_display = (
			'ekskul_profil_uuid',
			'ekskul_nama',
			'ekskul_telp',
		)
	readonly_fields = ['ekskul_profil_uuid',]
	actions = ['export_as_csv']
	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if db_field.name == 'ekskul_user':
			kwargs['queryset'] = Akun.objects.filter(is_pembimbing_ekskul=True)
		return super().formfield_for_foreignkey(db_field, request, **kwargs)
admin.site.register(Profil_Pembimbing, Profil_Pembimbing_admin)