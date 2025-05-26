from django.shortcuts import render, redirect
from artikel.models import Kategori, Blogpost

def welcome(request):
    template_name = "landingpage/index.html"
    kategori = Kategori.objects.all()
    artikel = Blogpost.objects.all()
    print (request.user)

    for k in kategori:
        print(k)
    
    for a in artikel:
        print(a)

    context = {
        "title":"selamat datang",
        "kategori":kategori,
        "artikel":artikel,
    }
    return render(request, template_name, context)

def detail_artikel(request, id):
    template_name = "landingpage/detail.html"
    try:
        artikel = Blogpost.objects.get(id=id)
    except Blogpost.DoesNotExist :
        return redirect(not_found_artikel)
    
    artikel_lainnya = Blogpost.objects.all().exclude(id=id)

    context = {
        "title":"selamat datang",
        "artikel":artikel,
        "artikel_lainnya":artikel_lainnya,
    }
    return render(request, template_name, context)

def not_found_artikel(request):
    template_name = "artikel_not_found.html"
    return render(request, template_name)

def buku(request):
    template_name = "buku.html"
    context = {
        "title":"halaman buku"
    }
    return render(request, template_name, context)

def kontak(request):
    template_name = "kontak.html"
    context = {
        "title":"halaman kontak"
    }
    return render(request, template_name, context)


def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('/auth-login')
    
    template_name = "dashboard/index.html"
    context = {
        "title":"halaman kontak"
    }
    return render(request, template_name, context)

def artikel_list(request):
    template_name = "dashboard/artikel_list.html"
    context = {
        "title":"halaman kontak"
    }
    return render(request, template_name, context)


def landing_page(request):
    kategori = Kategori.objects.all()[:4]
    return render(request, 'landingpage/index.html', {'kategori': kategori})
