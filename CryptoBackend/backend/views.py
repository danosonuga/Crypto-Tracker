from django.shortcuts import render
from django.http import HttpResponse
from django_pandas.io import read_frame
from fetch24HDateRange import fetch24Db
from fetch15MDateRange import fetch15Db
from fetch1HDateRange import fetch1Db
from fetch4HDateRange import fetch4Db

# Create your views here.
def call_default(request):
    data = fetch24Db()
    return render(request, 'backend/index.html', {'data': data})

def call_last_15(request):
    data = fetch15Db()
    return render(request, 'backend/index.html', {'data': data})

def call_last_1(request):
    data = fetch1Db()
    return render(request, 'backend/index.html', {'data': data, 'sn': 0})

def call_last_4(request):
    data = fetch4Db()
    return render(request, 'backend/index.html', {'data': data})