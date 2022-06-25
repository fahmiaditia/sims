from django.urls import path, include, re_path as url
from django.contrib.auth import views
from role_guru.views import *
from role_ekskul.views import *
from role_kepala_sekolah.views import *
from role_bk.views import *
from role_murid.views import *
from monitoring.views import *

app_name = 'monitoring'
urlpatterns = [
	path('guru', page_guru_dashboard, name='page_guru_dashboard'),
	path('profil-guru/', page_guru_profil, name="page_guru_profil"),
	path('profil-guru-update/<pk>/', page_guru_profil_update.as_view(), name="page_guru_profil_update"),
	# PAGE INPUT KOMPETENSI DASAR
	path('guru/kompetensi-dasar-list-mapel-wajib/', page_guru_list_kompetensi_dasar_wajib, name="page_guru_list_kompetensi_dasar_wajib"),
	path('guru/kompetensi-dasar-input-mapel-wajib/', page_guru_input_kompetensi_dasar_wajib, name="page_guru_input_kompetensi_dasar_wajib"),
	path('guru/kompetensi-dasar-update-mapel-wajib/<pk>/', page_guru_update_kompetensi_dasar_wajib.as_view(), name="page_guru_update_kompetensi_dasar_wajib"),
	path('guru/kompetensi-dasar-delete-mapel-wajib/<pk>/', page_guru_delete_kompetensi_dasar_wajib.as_view(), name="page_guru_delete_kompetensi_dasar_wajib"),

	path('guru/kompetensi-dasar-list-mapel-jurusan/', page_guru_list_kompetensi_dasar_jurusan, name="page_guru_list_kompetensi_dasar_jurusan"),
	path('guru/kompetensi-dasar-input-mapel-jurusan/', page_guru_input_kompetensi_dasar_jurusan, name="page_guru_input_kompetensi_dasar_jurusan"),
	path('guru/kompetensi-dasar-update-mapel-jurusan/<pk>/', page_guru_update_kompetensi_dasar_jurusan.as_view(), name="page_guru_update_kompetensi_dasar_jurusan"),
	path('guru/kompetensi-dasar-delete-mapel-jurusan/<pk>/', page_guru_delete_kompetensi_dasar_jurusan.as_view(), name="page_guru_delete_kompetensi_dasar_jurusan"),


	# PAGE INPUT NILAI PENGETAHUAN
	path('guru/pengetahuan-list-nilai-mapel-wajib/', page_guru_list_pengetahuan_wajib, name="page_guru_list_pengetahuan_wajib"),
	path('guru/pengetahuan-input-nilai-mapel-wajib/', page_guru_input_pengetahuan_wajib, name="page_guru_input_pengetahuan_wajib"),
	path('guru/pengetahuan-update-nilai-mapel-wajib/<pk>/', page_guru_update_pengetahuan_wajib.as_view(), name="page_guru_update_pengetahuan_wajib"),
	path('guru/pengetahuan-delete-nilai-mapel-wajib/<pk>/', page_guru_delete_pengetahuan_wajib.as_view(), name="page_guru_delete_pengetahuan_wajib"),

	path('guru/pengetahuan-list-nilai-mapel-jurusan/', page_guru_list_pengetahuan_jurusan, name="page_guru_list_pengetahuan_jurusan"),
	path('guru/pengetahuan-input-nilai-mapel-jurusan/', page_guru_input_pengetahuan_jurusan, name="page_guru_input_pengetahuan_jurusan"),
	path('guru/pengetahuan-update-nilai-mapel-jurusan/<pk>/', page_guru_update_pengetahuan_jurusan.as_view(), name="page_guru_update_pengetahuan_jurusan"),
	path('guru/pengetahuan-delete-nilai-mapel-jurusan/<pk>/', page_guru_delete_pengetahuan_jurusan.as_view(), name="page_guru_delete_pengetahuan_jurusan"),


	# PAGE INPUT NILAI KETERAMPILAN
	path('guru/keterampilan-list-nilai-mapel-wajib/', page_guru_list_keterampilan_wajib, name="page_guru_list_keterampilan_wajib"),
	path('guru/keterampilan-input-nilai-mapel-wajib/', page_guru_input_keterampilan_wajib, name="page_guru_input_keterampilan_wajib"),
	path('guru/keterampilan-update-nilai-mapel-wajib/<pk>/', page_guru_update_keterampilan_wajib.as_view(), name="page_guru_update_keterampilan_wajib"),
	path('guru/keterampilan-delete-nilai-mapel-wajib/<pk>/', page_guru_delete_keterampilan_wajib.as_view(), name="page_guru_delete_keterampilan_wajib"),

	path('guru/keterampilan-list-nilai-mapel-jurusan/', page_guru_list_keterampilan_jurusan, name="page_guru_list_keterampilan_jurusan"),
	path('guru/keterampilan-input-nilai-mapel-jurusan/', page_guru_input_keterampilan_jurusan, name="page_guru_input_keterampilan_jurusan"),
	path('guru/keterampilan-update-nilai-mapel-jurusan/<pk>/', page_guru_update_keterampilan_jurusan.as_view(), name="page_guru_update_keterampilan_jurusan"),
	path('guru/keterampilan-delete-nilai-mapel-jurusan/<pk>/', page_guru_delete_keterampilan_jurusan.as_view(), name="page_guru_delete_keterampilan_jurusan"),


	# PAGE INPUT NILAI SIKAP SOSIAL
	path('guru/sikap-sosial-list-nilai-mapel-wajib/', page_guru_list_sikap_sosial_wajib, name="page_guru_list_sikap_sosial_wajib"),
	path('guru/sikap-sosial-input-nilai-mapel-wajib/', page_guru_input_sikap_sosial_wajib, name="page_guru_input_sikap_sosial_wajib"),
	path('guru/sikap-sosial-update-nilai-mapel-wajib/<pk>/', page_guru_update_sikap_sosial_wajib.as_view(), name="page_guru_update_sikap_sosial_wajib"),
	path('guru/sikap-sosial-delete-nilai-mapel-wajib/<pk>/', page_guru_delete_sikap_sosial_wajib.as_view(), name="page_guru_delete_sikap_sosial_wajib"),

	path('guru/sikap-sosial-list-nilai-mapel-jurusan/', page_guru_list_sikap_sosial_jurusan, name="page_guru_list_sikap_sosial_jurusan"),
	path('guru/sikap-sosial-input-nilai-mapel-jurusan/', page_guru_input_sikap_sosial_jurusan, name="page_guru_input_sikap_sosial_jurusan"),
	path('guru/sikap-sosial-update-nilai-mapel-jurusan/<pk>/', page_guru_update_sikap_sosial_jurusan.as_view(), name="page_guru_update_sikap_sosial_jurusan"),
	path('guru/sikap-sosial-delete-nilai-mapel-jurusan/<pk>/', page_guru_delete_sikap_sosial_jurusan.as_view(), name="page_guru_delete_sikap_sosial_jurusan"),


	# PAGE INPUT NILAI SIKAP SPIRITUAL
	path('guru/sikap-spiritual-list-nilai-mapel-wajib/', page_guru_list_sikap_spiritual_wajib, name="page_guru_list_sikap_spiritual_wajib"),
	path('guru/sikap-spiritual-input-nilai-mapel-wajib/', page_guru_input_sikap_spiritual_wajib, name="page_guru_input_sikap_spiritual_wajib"),
	path('guru/sikap-spiritual-update-nilai-mapel-wajib/<pk>/', page_guru_update_sikap_spiritual_wajib.as_view(), name="page_guru_update_sikap_spiritual_wajib"),
	path('guru/sikap-spiritual-delete-nilai-mapel-wajib/<pk>/', page_guru_delete_sikap_spiritual_wajib.as_view(), name="page_guru_delete_sikap_spiritual_wajib"),

	path('guru/sikap-spiritual-list-nilai-mapel-jurusan/', page_guru_list_sikap_spiritual_jurusan, name="page_guru_list_sikap_spiritual_jurusan"),
	path('guru/sikap-spiritual-input-nilai-mapel-jurusan/', page_guru_input_sikap_spiritual_jurusan, name="page_guru_input_sikap_spiritual_jurusan"),
	path('guru/sikap-spiritual-update-nilai-mapel-jurusan/<pk>/', page_guru_update_sikap_spiritual_jurusan.as_view(), name="page_guru_update_sikap_spiritual_jurusan"),
	path('guru/sikap-spiritual-delete-nilai-mapel-jurusan/<pk>/', page_guru_delete_sikap_spiritual_jurusan.as_view(), name="page_guru_delete_sikap_spiritual_jurusan"),


	# PAGE MEAN NILAI SISWA
	path('guru/mean-nilai-siswa-wajib/', page_guru_mean_nilai_siswa_wajib, name="page_guru_mean_nilai_siswa_wajib"),
	path('guru/mean-nilai-siswa-jurusan/', page_guru_mean_nilai_siswa_jurusan, name="page_guru_mean_nilai_siswa_jurusan"),
	path('guru/mean-nilai-siswa-wajib-detail/<uuidnyaMurid>/', page_guru_mean_nilai_siswa_wajib_detail, name="page_guru_mean_nilai_siswa_wajib_pengetahuan_detail"),
	path('guru/mean-nilai-siswa-jurusan-detail/<uuidnyaMurid>/', page_guru_mean_nilai_siswa_jurusan_detail, name="page_guru_mean_nilai_siswa_jurusan_pengetahuan_detail"),


	path('guru/perfoma-kelas-landing/', page_guru_performa_kelas_landing, name="page_guru_performa_kelas_landing"),
	path('guru/perfoma-kelas-wajib-detail/<uuidnyaKelas>/', page_guru_performa_kelas_wajib_detail, name="page_guru_performa_kelas_wajib_detail"),
	path('guru/perfoma-kelas-jurusan-detail/<uuidnyaKelas>/', page_guru_performa_kelas_jurusan_detail, name="page_guru_performa_kelas_jurusan_detail"),

	path('guru/wali-kelas', page_guru_wali_kelas, name="page_guru_wali_kelas"),

	path('guru/kelola-kkm-wajib/', page_guru_kkm_wajib, name="page_guru_kkm_wajib"),
	path('guru/kelola-kkm-wajib-tambah/', page_guru_kkm_wajib_create.as_view(), name="page_guru_kkm_wajib_create"),
	path('guru/kelola-kkm-wajib-update/<pk>/', page_guru_kkm_wajib_update.as_view(), name="page_guru_kkm_wajib_update"),
	path('guru/kelola-kkm-wajib-delete/<pk>/', page_guru_kkm_wajib_delete.as_view(), name="page_guru_kkm_wajib_delete"),

	path('guru/kelola-kkm-jurusan/', page_guru_kkm_jurusan, name="page_guru_kkm_jurusan"),
	path('guru/kelola-kkm-jurusan-tambah/', page_guru_kkm_jurusan_create.as_view(), name="page_guru_kkm_jurusan_create"),
	path('guru/kelola-kkm-jurusan-update/<pk>/', page_guru_kkm_jurusan_update.as_view(), name="page_guru_kkm_jurusan_update"),
	path('guru/kelola-kkm-jurusan-delete/<pk>/', page_guru_kkm_jurusan_delete.as_view(), name="page_guru_kkm_jurusan_delete"),


	path('guru/kelola-catatan-wajib/', page_guru_catatan_wajib, name="page_guru_catatan_wajib"),
	path('guru/kelola-catatan-wajib-tambah/', page_guru_catatan_wajib_create.as_view(), name="page_guru_catatan_wajib_create"),
	path('guru/kelola-catatan-wajib-update/<pk>/', page_guru_catatan_wajib_update.as_view(), name="page_guru_catatan_wajib_update"),
	path('guru/kelola-catatan-wajib-delete/<pk>/', page_guru_catatan_wajib_delete.as_view(), name="page_guru_catatan_wajib_delete"),


	path('guru/kelola-catatan-jurusan/', page_guru_catatan_jurusan, name="page_guru_catatan_jurusan"),
	path('guru/kelola-catatan-jurusan-tambah/', page_guru_catatan_jurusan_create.as_view(), name="page_guru_catatan_jurusan_create"),
	path('guru/kelola-catatan-jurusan-update/<pk>/', page_guru_catatan_jurusan_update.as_view(), name="page_guru_catatan_jurusan_update"),
	path('guru/kelola-catatan-jurusan-delete/<pk>/', page_guru_catatan_jurusan_delete.as_view(), name="page_guru_catatan_jurusan_delete"),


	path('guru/kelola-ulangan-wajib/', page_guru_list_ulangan_wajib, name="page_guru_list_ulangan_wajib"),
	path('guru/kelola-ulangan-wajib-tambah/', page_guru_input_ulangan_wajib, name="page_guru_input_ulangan_wajib"),
	path('guru/kelola-ulangan-wajib-update/<pk>/', page_guru_update_ulangan_wajib.as_view(), name="page_guru_update_ulangan_wajib"),
	path('guru/kelola-ulangan-wajib-delete/<pk>/', page_guru_delete_ulangan_wajib.as_view(), name="page_guru_delete_ulangan_wajib"),


	path('guru/kelola-ulangan-jurusan/', page_guru_list_ulangan_jurusan, name="page_guru_list_ulangan_jurusan"),
	path('guru/kelola-ulangan-jurusan-tambah/', page_guru_input_ulangan_jurusan, name="page_guru_input_ulangan_jurusan"),
	path('guru/kelola-ulangan-jurusan-update/<pk>/', page_guru_update_ulangan_jurusan.as_view(), name="page_guru_update_ulangan_jurusan"),
	path('guru/kelola-ulangan-jurusan-delete/<pk>/', page_guru_delete_ulangan_jurusan.as_view(), name="page_guru_delete_ulangan_jurusan"),


	path('guru/kelola-uts-wajib/', page_guru_list_uts_wajib, name="page_guru_list_uts_wajib"),
	path('guru/kelola-uts-wajib-tambah/', page_guru_input_uts_wajib, name="page_guru_input_uts_wajib"),
	path('guru/kelola-uts-wajib-update/<pk>/', page_guru_update_uts_wajib.as_view(), name="page_guru_update_uts_wajib"),
	path('guru/kelola-uts-wajib-delete/<pk>/', page_guru_delete_uts_wajib.as_view(), name="page_guru_delete_uts_wajib"),

	path('guru/kelola-uts-jurusan/', page_guru_list_uts_jurusan, name="page_guru_list_uts_jurusan"),
	path('guru/kelola-uts-jurusan-tambah/', page_guru_input_uts_jurusan, name="page_guru_input_uts_jurusan"),
	path('guru/kelola-uts-jurusan-update/<pk>/', page_guru_update_uts_jurusan.as_view(), name="page_guru_update_uts_jurusan"),
	path('guru/kelola-uts-jurusan-delete/<pk>/', page_guru_delete_uts_jurusan.as_view(), name="page_guru_delete_uts_jurusan"),


	path('guru/kelola-uas-wajib/', page_guru_list_uas_wajib, name="page_guru_list_uas_wajib"),
	path('guru/kelola-uas-wajib-tambah/', page_guru_input_uas_wajib, name="page_guru_input_uas_wajib"),
	path('guru/kelola-uas-wajib-update/<pk>/', page_guru_update_uas_wajib.as_view(), name="page_guru_update_uas_wajib"),
	path('guru/kelola-uas-wajib-delete/<pk>/', page_guru_delete_uas_wajib.as_view(), name="page_guru_delete_uas_wajib"),

	path('guru/kelola-uas-jurusan/', page_guru_list_uas_jurusan, name="page_guru_list_uas_jurusan"),
	path('guru/kelola-uas-jurusan-tambah/', page_guru_input_uas_jurusan, name="page_guru_input_uas_jurusan"),
	path('guru/kelola-uas-jurusan-update/<pk>/', page_guru_update_uas_jurusan.as_view(), name="page_guru_update_uas_jurusan"),
	path('guru/kelola-uas-jurusan-delete/<pk>/', page_guru_delete_uas_jurusan.as_view(), name="page_guru_delete_uas_jurusan"),

	path('kepala-sekolah/', page_kepsek_dashboard, name='page_kepsek_dashboard'),
	path('kepala-sekolah/profil/', page_kepsek_profil, name="page_kepsek_profil"),
	path('kepala-sekolah/profil-update/<pk>/', page_kepsek_profil_update.as_view(), name="page_kepsek_profil_update"),

	path('kepala-sekolah/kompetensi-dasar-landing/', page_kepsek_kompetensi_dasar, name="page_kepsek_kompetensi_dasar"),
	path('kepala-sekolah/kompetensi-dasar-wajib-detail/<uuidPelajaran>/', page_kepsek_kompetensi_dasar_wajib_detail, name="page_kepsek_kompetensi_dasar_wajib_detail"),
	path('kepala-sekolah/kompetensi-dasar-jurusan-detail/<uuidPelajaran>/', page_kepsek_kompetensi_dasar_jurusan_detail, name="page_kepsek_kompetensi_dasar_jurusan_detail"),
		
	path('kepala-sekolah/perfoma-mapel/', page_kepsek_performa_mapel, name="page_kepsek_performa_mapel"),
	path('kepala-sekolah/perfoma-mapel-wajib/<uuidPelajaran>', page_kepsek_performa_mapel_wajib_detail, name="page_kepsek_performa_mapel_wajib_detail"),
	path('kepala-sekolah/perfoma-mapel-jurusan/<uuidPelajaran>', page_kepsek_performa_mapel_jurusan_detail, name="page_kepsek_performa_mapel_jurusan_detail"),

	path('kepala-sekolah/perfoma-kelas/', page_kepsek_performa_kelas_landing, name="page_kepsek_performa_kelas_landing"),
	path('kepala-sekolah/perfoma-kelas-detail/<uuidnyaKelas>/', page_kepsek_performa_kelas_detail, name="page_kepsek_performa_kelas_detail"),

	path('kepala-sekolah/perfoma-ekskul/', page_kepsek_performa_ekskul_landing, name="page_kepsek_performa_ekskul_landing"),
	path('kepala-sekolah/perfoma-ekskul-detail/<uuidEkskul>/', page_kepsek_performa_ekskul_detail, name="page_kepsek_performa_ekskul_detail"),


	


	path('ekskul/', page_ekskul_dashboard, name="page_ekskul_dashboard"),
	path('ekskul/profil-ekskul/', page_ekskul_profil, name="page_ekskul_profil"),
	path('ekskul/profil-ekskul/update/<pk>/', page_ekskul_profil_update.as_view(), name="page_ekskul_profil_update"),

	path('ekskul/nilai-ekskul/', page_ekskul_nilai, name="page_ekskul_nilai"),
	path('ekskul/nilai-ekskul-tambah/', page_ekskul_nilai_create.as_view(), name="page_ekskul_profil_create"),
	path('ekskul/nilai-ekskul-update/<pk>', page_ekskul_nilai_update.as_view(), name="page_ekskul_nilai_update"),
	path('ekskul/nilai-ekskul-delete/<pk>', page_ekskul_nilai_delete.as_view(), name="page_ekskul_nilai_delete"),

	path('ekskul/kejuaraan-ekskul/', page_ekskul_kejuaraan_landing, name="page_ekskul_kejuaraan_landing"),
	path('ekskul/kejuaraan-ekskul-tambah/', page_ekskul_kejuaraan_create.as_view(), name="page_ekskul_kejuaraan_create"),
	path('ekskul/kejuaraan-ekskul-update/<pk>/', page_ekskul_kejuaraan_update.as_view(), name="page_ekskul_kejuaraan_update"),
	path('ekskul/kejuaraan-ekskul-delete/<pk>/', page_ekskul_kejuaraan_delete.as_view(), name="page_ekskul_kejuaraan_delete"),

	path('ekskul/perkembangan-nilai-ekskul/', page_ekskul_perkembangan_siswa, name="page_ekskul_perkembangan_siswa"),
	path('ekskul/perkembangan-nilai-ekskul-detail/<uuidnyaMurid>', page_ekskul_perkembangan_siswa_detail, name="page_ekskul_perkembangan_siswa_detail"),

	path('bk/', page_bk_dashboard, name="page_bk_dashboard"),
	path('bk/profil/', page_bk_profil, name="page_bk_profil"),
	path('bk/profil-update/<pk>/', page_bk_profil_update.as_view(), name="page_bk_profil_update"),
	path('bk/perfoma-kelas/', page_bk_performa_kelas_landing, name="page_bk_performa_kelas_landing"),
	path('bk/perfoma-kelas-detail/<uuidnyaKelas>/', page_bk_performa_kelas_detail, name="page_bk_performa_kelas_detail"),

	path('bk/siswa/', page_bk_nilai_siswa_landing, name="page_bk_nilai_siswa_landing"),
	path('bk/nilai-siswa/<uuidnyaMurid>', page_bk_nilai_siswa_detail, name="page_bk_nilai_siswa_detail"),

	path('bk/catatan-siswa/', page_bk_catatan, name="page_bk_catatan"),
	path('bk/catatan-siswa-tambah/', page_bk_catatan_create.as_view(), name="page_bk_catatan_create"),
	path('bk/catatan-siswa-update/<pk>/', page_bk_catatan_update.as_view(), name="page_bk_catatan_update"),
	path('bk/catatan-siswa-delete/<pk>/', page_bk_catatan_delete.as_view(), name="page_bk_catatan_delete"),

	# path('bk-profil-update/<pk>/', page_bk_profil_update.as_view(), name="page_bk_profil_update"),


	path('murid/', page_murid_dashboard, name='page_murid_dashboard'),
	path('murid/profil/', page_murid_profil, name='page_murid_profil'),
	path('murid/profil-update/<pk>/', page_murid_profil_update.as_view(), name='page_murid_profil_update'),
	
	path('murid/nilai/', page_murid_nilai, name='page_murid_nilai'),
	path('murid/nilai-mapel-wajib/<uuidPelajaran>/', page_murid_nilai_wajib_detail, name='page_murid_nilai_wajib_detail'),
	path('murid/nilai-mapel-jurusan/<uuidPelajaran>/', page_murid_nilai_jurusan_detail, name='page_murid_nilai_jurusan_detail'),

	path('importing/', page_guru_import, name='page_guru_import'),
]