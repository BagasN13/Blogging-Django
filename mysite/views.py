from django.shortcuts import render, redirect
from artikel.models import Kategori, Blogpost
from django.contrib.auth.models import User

from django.db.models.functions import TruncMonth
from django.db.models import Count
from django.utils.dateformat import DateFormat
from django.utils.formats import date_format
import json

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
    
    user_count = User.objects.count()
    artikel_count = Blogpost.objects.count()
    kategori_count = Kategori.objects.count()
    artikel = Blogpost.objects.all()
    

    # Hitung jumlah kategori per bulan
    kategori_per_month = (
        Kategori.objects.annotate(month=TruncMonth("created_at"))  # Sesuaikan dengan field tanggal
        .values("month")
        .annotate(count=Count("id"))
        .order_by("month")
    )

    kategori_labels = [date_format(item["month"], "F") for item in kategori_per_month]
    kategori_data = [item["count"] for item in kategori_per_month]

     # Hitung jumlah user per bulan
    user_per_month = (
        User.objects.annotate(month=TruncMonth("date_joined"))
        .values("month")
        .annotate(count=Count("id"))
        .order_by("month")
    )

    # Ubah hasil ke format label dan data untuk grafik
    labels = [date_format(item["month"], "F Y") for item in user_per_month]
    counts = [item["count"] for item in user_per_month]

    template_name = "dashboard/index.html"
    context = {
        "title":"halaman kontak",
        "user_count": user_count,
        "artikel_count": artikel_count,
        "kategori_count": kategori_count,
        "kategori_chart_labels": json.dumps(kategori_labels),
        "kategori_chart_data": json.dumps(kategori_data),
        "user_chart_labels": json.dumps(labels),
        "user_chart_data": json.dumps(counts),
        "artikel": artikel,
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
