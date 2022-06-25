from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



def landing(request):
	return render(request, 'index.html', {})

def login_req(request):
	pesan = None
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get("username")
			password = form.cleaned_data.get("password")
			user = authenticate(username=username, password=password)
			if user is not None and user.is_guru:
				login(request, user)
				return redirect("monitoring:page_guru_list_pengetahuan_wajib")
			elif user is not None and user.is_pembimbing_ekskul:
				login(request, user)
				return redirect("monitoring:page_ekskul_nilai")
			elif user is not None and user.is_kepsek:
				login(request, user)
				return redirect("monitoring:page_kepsek_performa_kelas_landing")
			elif user is not None and user.is_bk:
				login(request, user)
				return redirect("monitoring:page_bk_nilai_siswa_landing")
			elif user is not None and user.is_murid:
				login(request, user)
				return redirect("monitoring:page_murid_nilai")
		else:
			pesan = messages.error(request, "username atau password Anda salah")
			return redirect("login")
	form = AuthenticationForm()
	context = {
		'form': form,
		'pesan': pesan,
	}
	return render(request, 'login.html', context)

def logout_req(request):
    logout(request)
    return redirect('login')