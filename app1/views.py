from unittest import TextTestRunner
from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.shortcuts import redirect


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

def creategroup(request):
    under=grunder.objects.all()
    context={'under':under}
    return render (request,'creategroup.html',context)     


def create_group(request):
    if request.method == 'POST':
        gname = request.POST['gname']
        alia = request.POST['alia']
        
        under = request.POST['under']
        gp = request.POST['subled']
        nett = request.POST['nee']
        calc = request.POST['cal']
        meth = request.POST['meth']

        mdl = GroupModel(
            name=gname,
            alias=alia,
            under=under,
            gp_behaves_like_sub_ledger=gp,
            nett_debit_credit_bal_reporting=nett,
            used_for_calculation=calc,
            method_to_allocate_usd_purchase=meth,
        )
        mdl.save()
        return redirect('/')
        

def grcreate(request):
    return render(request,'grcreate.html')    

def createledger(request):
    return render (request,'createledger.html')        

def credit(request):
    return render(request,'credit.html')

def debit(request):
    return render(request,'debit.html')        



