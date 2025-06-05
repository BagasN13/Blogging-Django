from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from django.contrib import messages
from artikel.models import Kategori, Blogpost
from artikel.forms import KategoriForms, BlogpostForms

# Create your views here.
def in_operator(user):
    get_user = user.groups.filter(name='Operator').count()
    if get_user == 0:
        return False
    else:
        return True

########################### User Biasa ##############################################
@login_required (login_url='/auth-login')
def artikel_list(request):
    template_name = "dashboard/user/artikel_list.html"
    artikel = Blogpost.objects.filter(created_by=request.user)
    context = {
        "artikel":artikel,
    }
    return render(request, template_name, context)

@login_required (login_url='/auth-login')
def artikel_tambah(request):
    template_name = "dashboard/admin/artikel_forms.html"
    if request.method == "POST":
        forms = BlogpostForms(request.POST, request.FILES)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
            messages.success(request, 'berhasil tambah artikel')
            return redirect(artikel_list)
        
    forms = BlogpostForms()
    context = {
        'forms':forms
    }
    return render(request, template_name, context)

@login_required (login_url='/auth-login')
def artikel_update(request, id_artikel):
    template_name = "dashboard/admin/artikel_forms.html"
    try:
        artikel = Blogpost.objects.get(id=id_artikel, created_by=request.user)
    except:
        messages.error(request, "Halaman tidak ditemukan...")
        return redirect("/dashboard")
    if request.method == "POST":
        forms = BlogpostForms(request.POST, request.FILES, instance=artikel)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
            messages.success(request, 'berhasil melakukan update artikel')
            return redirect(artikel_list)
    forms = BlogpostForms(instance=artikel)
    context = {
        'forms':forms
    }
    return render(request, template_name, context)

@login_required (login_url='/auth-login')
def artikel_delete(request, id_artikel):
    try:
        Blogpost.objects.get(id=id_artikel, created_by=request.user).delete()
        messages.success(request, 'berhasil delete artikel')
    except:
        messages.error(request, 'gagal delete artikel')

    return redirect(artikel_list)


############################## admin ####################################
@login_required (login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_kategori_list(request):
    template_name = "dashboard/admin/kategori_list.html"
    kategori = Kategori.objects.all()
    context = {
        "kategori":kategori
    }
    return render(request, template_name, context)

@login_required (login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_kategori_tambah(request):
    template_name = "dashboard/admin/kategori_forms.html"
    if request.method == "POST":
        forms = KategoriForms(request.POST)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
            messages.success(request, 'berhasil tambah kategori')
            return redirect(admin_kategori_list)
    forms = KategoriForms()
    context = {
        'forms':forms
    }
    return render(request, template_name, context)

@login_required (login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_kategori_update(request, id_kategori):
    template_name = "dashboard/admin/kategori_forms.html"
    kategori = Kategori.objects.get(id=id_kategori)
    if request.method == "POST":
        forms = KategoriForms(request.POST, instance=kategori)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
            messages.success(request, 'berhasil melakukan update kategori')
            return redirect(admin_kategori_list)
    forms = KategoriForms(instance=kategori)
    context = {
        'forms':forms
    }
    return render(request, template_name, context)

@login_required (login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_kategori_delete(request, id_kategori):
    try:
        Kategori.objects.get(id=id_kategori).delete()
        messages.success(request, 'berhasil delete kategori')
    except:
        messages.error(request, 'gagal delete kategori')

    return redirect(admin_kategori_list)

########################## Blogpost ################################

@login_required (login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_artikel_list(request):
    template_name = "dashboard/admin/artikel_list.html"
    artikel = Blogpost.objects.all()
    context = {
        "artikel":artikel
    }
    return render(request, template_name, context)

@login_required (login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_artikel_tambah(request):
    template_name = "dashboard/admin/artikel_forms.html"
    if request.method == "POST":
        forms = BlogpostForms(request.POST, request.FILES)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
            messages.success(request, 'berhasil tambah artikel')
            return redirect(admin_artikel_list)
        
    forms = BlogpostForms()
    context = {
        'forms':forms
    }
    return render(request, template_name, context)

@login_required (login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_artikel_update(request, id_artikel):
    template_name = "dashboard/admin/artikel_forms.html"
    artikel = Blogpost.objects.get(id=id_artikel)
    if request.method == "POST":
        forms = BlogpostForms(request.POST, request.FILES, instance=artikel)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
            messages.success(request, 'berhasil melakukan update artikel')
            return redirect(admin_artikel_list)
    forms = BlogpostForms(instance=artikel)
    context = {
        'forms':forms
    }
    return render(request, template_name, context)

@login_required (login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_artikel_delete(request, id_artikel):
    try:
        Blogpost.objects.get(id=id_artikel).delete()
        messages.success(request, 'berhasil delete artikel')
    except:
        messages.error(request, 'gagal delete artikel')

    return redirect(admin_artikel_list)



######################## Management User oleh Operator ###################################
@login_required (login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_management_user_list(request):
    template_name="dashboard/admin/user_list.html"
    daftar_user = User.objects.all()
    context = {
        "daftar_user":daftar_user
    }
    return render(request, template_name, context)
