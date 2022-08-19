from tabnanny import check
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
        namegroup=request.POST['namegroup']
        gp = request.POST['subled']
        nett = request.POST['nee']
        calc = request.POST['cal']
        meth = request.POST['meth']

        mdl = GroupModel(
            name=gname,
            alias=alia,
            under=under,
            namegroup=namegroup,
            gp_behaves_like_sub_ledger=gp,
            nett_debit_credit_bal_reporting=nett,
            used_for_calculation=calc,
            method_to_allocate_usd_purchase=meth,
        )
        mdl.save()
        return redirect('/')
        

def grcreate(request):
    gr=GroupModel.objects.all()
    return render(request,'grcreate.html',{'gr':gr})    

def createledger(request):
    return render (request,'createledger.html')        

def credit(request):
    cre=cred.objects.all()
    return render(request,'credit.html',{'cre':cre})

def debi(request):
    debi=debit.objects.all()
    return render(request,'debit.html',{'debi':debi})    

def ledgerlist(request):
    ledg=ledgercreation.objects.all()
    return render(request,'ledgerlist.html',{'ledg':ledg})    



def ledgercreations(request):
    if request.method == 'POST':
        
        lname=request.POST['lname']
        alias=request.POST['alias']
        under=request.POST['under']
        prbankdetals=request.POST['prbankdetals']
        holders_name=request.POST['holders_name']

        ac_no=request.POST['ac_no']
        if ac_no=="":
            ac_no=None

        ifsc=request.POST['ifsc']
        if ifsc=="":
            ifsc=None

        swiftcode=request.POST['swiftcode']
        if swiftcode=="":
            swiftcode=None

        bankname=request.POST['bankname']
        branch=request.POST['branch']
        checkbook=request.POST['checkbook']
        checkprinting=request.POST['checkprinting']
        mailname=request.POST['mailname']
        mailaddress=request.POST['mailaddress']
        mailcontry=request.POST['mailcontry']
        mailstate=request.POST['mailstate']

        mailpin=request.POST['mailpin']
        if mailpin=="":
            mailpin=None

        pan=request.POST['pan']
        if pan=="":
            pan=None

        gst=request.POST['gst']
        if gst=="":
            gst=None

        gstdetails=request.POST['gstdetails']

        led=ledgercreation(
            lname=lname,
            alias=alias,
            under=under,
            prbankdetals=prbankdetals,
            holders_name=holders_name,
            ac_no=ac_no,
            ifsc=ifsc,
            swiftcode=swiftcode,
            bankname=bankname,
            branch=branch,
            checkbook=checkbook,
            checkprinting=checkprinting,
            mailname=mailname,
            mailaddress=mailaddress,
            mailcontry=mailcontry,
            mailstate=mailstate,
            mailpin=mailpin,
            pan=pan,
            gst=gst,
            gstdetails=gstdetails
        )
        led.save()
        return redirect('ledgerlist')
































