from django.contrib import admin
from role_bk.models import *
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


class Profil_BK_admin(admin.ModelAdmin, ExportCsvMixin):
	list_display = (
			'bk_profil_uuid',
			'bk_nama',
		)
	readonly_fields = ['bk_profil_uuid',]
	actions = ['export_as_csv']
	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if db_field.name == 'bk_user':
			kwargs['queryset'] = Akun.objects.filter(is_bk=True)
		return super().formfield_for_foreignkey(db_field, request, **kwargs)
admin.site.register(Profil_BK, Profil_BK_admin)


class BK_Catatan_admin(admin.ModelAdmin, ExportCsvMixin):
	list_display = (
			'bk_catatan_uuid',
			'bk_catatan_status',
			'bk_catatan_siswa',
		)
	readonly_fields = ['bk_catatan_uuid',]
	actions = ['export_as_csv']
admin.site.register(BK_Catatan, BK_Catatan_admin)