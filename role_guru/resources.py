from role_guru.models import *
from monitoring.models import *
from import_export import resources


class PengetahuanResources(resources.ModelResource):
	class Meta:
		model = Mo_Penilaian_Pengetahuan
		fields = (
				"mo_penilaian_pengetahuan_uuid",
				'mo_siswa',
				'mo_siswa__murid_nama', 
				'mo_kelas',
				'mo_kelas__skl_k_kelas_nama', 
				'mo_mata_pelajaran_wajib',
				'mo_mata_pelajaran_wajib__mapel_wajib_pelajaran',
				'mo_mata_pelajaran_jurusan',
				'mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran',
				'mo_nilai_P1_TGS',
				'mo_nilai_P2_TLS',
				'mo_nilai_P3_TLS',
			)
		# exclude = ("mo_penilaian_pengetahuan_uuid", )
		export_order = (
				"mo_penilaian_pengetahuan_uuid",
				'mo_siswa',
				'mo_siswa__murid_nama', 
				'mo_kelas',
				'mo_kelas__skl_k_kelas_nama', 
				'mo_mata_pelajaran_wajib',
				'mo_mata_pelajaran_wajib__mapel_wajib_pelajaran',
				'mo_mata_pelajaran_jurusan',
				'mo_mata_pelajaran_jurusan__mapel_jurusan_pelajaran',
				'mo_nilai_P1_TGS',
				'mo_nilai_P2_TLS',
				'mo_nilai_P3_TLS',
			)
