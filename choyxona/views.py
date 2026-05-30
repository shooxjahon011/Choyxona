from django.shortcuts import render
from .models import Shashlik, Salat, YaxnaIchimlik

# Bosh sahifa
def home_page(request):
    return render(request, 'index1.html')

# Shashlik bosilganda ishlaydigan kod
def shashlik_view(request):
    # To'g'ridan-to'g'ri Shashlik klassidan hamma ma'lumotni oladi
    shashliklar = Shashlik.objects.all()
    return render(request, 'shashlik.html', {'shashliklar': shashliklar})

# Salat bosilganda ishlaydigan kod
def salat_view(request):
    # To'g'ridan-to'g'ri Salat klassidan hamma ma'lumotni oladi
    salatlar = Salat.objects.all()
    return render(request, 'salat.html', {'salatlar': salatlar})

# Yaxna ichimlik bosilganda ishlaydigan kod
def yaxna_view(request):
    # To'g'ridan-to'g'ri YaxnaIchimlik klassidan hamma ma'lumotni oladi
    yaxna_ichimliklar = YaxnaIchimlik.objects.all()
    return render(request, 'yaxna.html', {'yaxna_ichimliklar': yaxna_ichimliklar})