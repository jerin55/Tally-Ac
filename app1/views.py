from django.shortcuts import render
from .models import *

# Create your views here.

def base(request):
    return render(request, 'base.html')

def index(request):
    return render(request, 'home.html')

def group(request):
    return render(request, 'groups.html')

def branch(request):
    return render(request, 'branch.html')

def ledger(request):
    return render(request, 'ledger.html')

def primary(request):
    return render(request, 'primarycost.html')

def costcat(request):
    return render(request, 'costcat.html')

def costcentr(request):
    return render(request, 'costcentr.html')

def voucher(request):
    return render(request, 'voucher.html')

def vouchpage(request):
    return render(request, 'vouchpage.html')


def receivabl(request):
    rec=receivable.objects.all()
    return render (request,'receivable.html',{'rec':rec})    


def payabl(request):
    pay=payable.objects.all()
    return render(request,'payable.html',{'pay':pay})    



