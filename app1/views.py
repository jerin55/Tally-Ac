
from multiprocessing import context
from tabnanny import check
from tokenize import blank_re
from unittest import TextTestRunner
from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.shortcuts import redirect
from django.contrib import messages



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
    grp=GroupModel.objects.all()
    return render (request,'creategroup.html',{'grp':grp})     


def create_group(request):
    if request.method == 'POST':
        group_name = request.POST['group_name']

       
        group_alias = request.POST['group_alias']
        
        group_under = request.POST['group_under']
        nature=request.POST['nature']

        gross_profit=request.POST['gross_profit']


        sub_ledger = request.POST['sub_ledger']
        debit_credit = request.POST['debit_credit']
        calculation = request.POST['calculation']
        invoice = request.POST['invoice']

        mdl = GroupModel(
            group_name=group_name,
            group_alias=group_alias,
            group_under=group_under,
            nature=nature,
            gross_profit=gross_profit,
            sub_ledger=sub_ledger,
            debit_credit=debit_credit,
            calculation=calculation,
            invoice=invoice,
        )
        mdl.save()
        return redirect('createledger')
        

def grcreate(request):
    gr=GroupModel.objects.all()
    return render(request,'grcreate.html',{'gr':gr})    

def createledger(request):
    grp=GroupModel.objects.all()
    return render (request,'createledger.html',{'grp':grp})        

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
        
        name=request.POST['name']

        alias=request.POST['alias']
        under=request.POST['under']
        bank_details=request.POST['bank_details']
        
        ac_holder_nm=request.POST['ac_holder_nm']

        acc_no=request.POST['acc_no']
        if acc_no=="":
            acc_no=None

        ifsc_code=request.POST['ifsc_code']
        if ifsc_code=="":
            ifsc_code=None

        swift_code=request.POST['swift_code']
        if swift_code=="":
            swift_code=None

        bank_name=request.POST['bank_name']
        branch=request.POST['branch']
        SA_cheque_bk=request.POST['SA_cheque_bk']
        Echeque_p=request.POST['Echeque_p']

        occ_set_odl=request.POST['occ_set_odl']
        occ_ac_holder_nm=request.POST['occ_ac_holder_nm']
        occ_acc_no=request.POST['occ_acc_no']
        if occ_acc_no=="":
            occ_acc_no=None

        occ_ifsc_code=request.POST['occ_ifsc_code']
        if occ_ifsc_code=="":
            occ_ifsc_code=None

        occ_swift_code=request.POST['occ_swift_code']    
        if occ_swift_code=="":
            occ_swift_code=None

        occ_bank_name=request.POST['occ_bank_name']   
        occ_branch=request.POST['occ_branch']
        occ_SA_cheque_bk=request.POST['occ_SA_cheque_bk']
        occ_Echeque_p=request.POST['occ_Echeque_p']

        od_set_odl=request.POST['od_set_odl']
        od_ac_holder_nm=request.POST['od_ac_holder_nm']
        od_acc_no=request.POST['od_acc_no']
        if od_acc_no=="":
            od_acc_no=None

        od_ifsc_code=request.POST['od_ifsc_code']  
        if od_ifsc_code=="":
            od_ifsc_code=None

        od_swift_code=request.POST['od_swift_code']
        if od_swift_code=="":
            od_swift_code=None

        od_bank_name=request.POST['od_bank_name']
        if od_bank_name=="":
            od_bank_name=None

        od_branch=request.POST['od_branch']
        od_SA_cheque_bk=request.POST['od_SA_cheque_bk']
        od_Echeque_p=request.POST['od_Echeque_p']






        mname=request.POST['mname']
        address=request.POST['address']
        country=request.POST['country']
        state=request.POST['state']

        pincode=request.POST['pincode']
        if pincode=="":
            pincode=None

        pan_no=request.POST['pan_no']
        if pan_no=="":
            pan_no=None

        registration_type=request.POST['registration_type']    

        gst_uin=request.POST['gst_uin']
        if gst_uin=="":
            gst_uin=None

        set_alter_gstdetails=request.POST['set_alter_gstdetails']

        statutory_details=request.POST['statutory_details']

        type_of_ledger=request.POST['type_of_ledger']
        rounding_method=request.POST['rounding_method']
        rounding_limit=request.POST['rounding_limit']
        if rounding_limit=="":
            rounding_limit=None
        GST_Applicable=request.POST['GST_Applicable']
        Alter_GST_Details=request.POST['Alter_GST_Details']
        Appropriate=request.POST['Appropriate']
        Types_of_supply=request.POST['Types_of_supply']

        type_duty_tax=request.POST['type_duty_tax']
        tax_type=request.POST['tax_type']
        percentage_of_calcution=request.POST['percentage_of_calcution']
        rond_method=request.POST['rond_method']
        rond_limit=request.POST['rond_limit']
        if rond_limit=="":
            rond_limit=None
        balance_billbybill=request.POST['balance_billbybill']
        credit_period=request.POST['credit_period']
        creditdays_voucher=request.POST['creditdays_voucher']
      




        led=ledgercreation(
            name=name,
            alias=alias,
            under=under,
            bank_details=bank_details,
            ac_holder_nm=ac_holder_nm,
            acc_no=acc_no,
            ifsc_code=ifsc_code,
            swift_code=swift_code,
            bank_name=bank_name,
            branch=branch,
            SA_cheque_bk=SA_cheque_bk,
            Echeque_p=Echeque_p,
            mname=mname,
            address=address,
            country=country,
            state=state,
            pincode=pincode,
            pan_no=pan_no,
            registration_type=registration_type,
            gst_uin=gst_uin,
            set_alter_gstdetails=set_alter_gstdetails,
            type_of_ledger=type_of_ledger,
            rounding_method=rounding_method,
            rounding_limit=rounding_limit,
            GST_Applicable=GST_Applicable,
            Alter_GST_Details=Alter_GST_Details,
            Appropriate=Appropriate,
            Types_of_supply=Types_of_supply,
            type_duty_tax=type_duty_tax,
            tax_type=tax_type,
            percentage_of_calcution=percentage_of_calcution,
            rond_method=rond_method,
            rond_limit=rond_limit,
            balance_billbybill=balance_billbybill,
            credit_period=credit_period,
            creditdays_voucher=creditdays_voucher,
            statutory_details=statutory_details,
            occ_set_odl=occ_set_odl,
            occ_acc_no=occ_acc_no,
            occ_bank_name=occ_bank_name,
            occ_ac_holder_nm=occ_ac_holder_nm,
            occ_branch=occ_branch,
            occ_Echeque_p=occ_Echeque_p,
            occ_ifsc_code=occ_ifsc_code,
            occ_SA_cheque_bk=occ_SA_cheque_bk,
            occ_swift_code=occ_swift_code,
            od_ac_holder_nm=od_ac_holder_nm,
            od_acc_no=od_acc_no,
            od_bank_name=od_bank_name,
            od_branch=od_branch,
            od_Echeque_p=od_Echeque_p,
            od_SA_cheque_bk=od_SA_cheque_bk,
            od_ifsc_code=od_ifsc_code,
            od_set_odl=od_set_odl,
            od_swift_code=od_swift_code

            


        )
        led.save()
        return redirect('ledgerlist')


def nw(request):
    ledi=led.objects.all()
    return render(request,'nw.html',{'ledg':ledi})

  

  

  



def voucheradd(request):
    ledg=ledgercreation.objects.all()
    return render(request,'voucheradd.html',{'ledg':ledg})    

def vouchadd(request):
    if request.method == 'POST':
        vdate=request.POST['vdate']
        particular=request.POST['particular']
        account=request.POST['account']
        vouchertype=request.POST['vouchertype']
        voucherno=request.POST['voucherno']
        openingbal=request.POST['openingbal']
        
        
        debit=request.POST['debit']
       
        credit=request.POST['credit']
        

        vou=vouchert(
            vdate=vdate,
            particular=particular,
            account=account,
            vouchertype=vouchertype,
            voucherno=voucherno,
            debit=debit,
            credit=credit,
            openingbal=openingbal
            

        )
        vou.save()
        return redirect('voucheradd')

       


def groupsummery(request):

   
    vouch=vouchert.objects.filter()

    sum1=0
    sum2=0
    for a in vouch:
        sum1+=a.credit

    for b in vouch:
        sum2+=b.debit    

    context={'vouch':vouch,'sum1':sum1,'sum2':sum2}    
    return render(request,'groupsummery.html',context)        

def ledgersummary(request,pk):
    vch=vouchert.objects.get(id=pk)  
    vouch=vouchert.objects.filter(id=pk)

    sum1=0
    sum2=0
    sum3=0
    for a in vouch:
        sum1+=a.credit

    for b in vouch:
        sum2+=b.debit 

    

    for c in vouch:
        sum3+=c.openingbal   

    tot=sum1+sum2 
    cltot=tot-sum3  
      
    
    context={'vch':vch,'vouch':vouch,'sum1':sum1,'sum2':sum2,'sum3':sum3,'sum3':sum3,'tot':tot,'cltot':cltot}      
    return render(request,'ledgersummary.html',context)    

def ledgervoucher(request,pk):
    vch=vouchert.objects.get(id=pk)
    vouch=vouchert.objects.filter(id=pk)

    sum1=0
    sum2=0
    sum3=0

    for a in vouch:
        sum1+=a.credit

    for b in vouch:
        sum2+=b.debit  

    for c in vouch:
        sum3+=c.openingbal   

    tot=sum1+sum2 
    cltot=tot-sum3  

        
    context={'vch':vch,'vouch':vouch,'sum1':sum1,'sum2':sum2,'sum3':sum3,'tot':tot,'cltot':cltot}     
    return render(request,'ledgervoucher.html',context)      

def ex(request):
    return render(request,'ex.html')  






def inincvoucher(request):
    ledg=ledgercreation.objects.all()
    return render(request,'inincvoucher.html',{'ledg':ledg})    

def inincvouchadd(request):
    if request.method == 'POST':
        ivdate=request.POST['ivdate']
        iparticular=request.POST['iparticular']
        iaccount=request.POST['iaccount']
        ivouchertype=request.POST['ivouchertype']
        ivoucherno=request.POST['ivoucherno']
        
        idebit=request.POST['idebit']
       
        icredit=request.POST['icredit']
        

        voui=inincvouchert(
            ivdate=ivdate,
            iparticular=iparticular,
            iaccount=iaccount,
            ivouchertype=ivouchertype,
            ivoucherno=ivoucherno,
            idebit=idebit,
            icredit=icredit,
            

        )
        voui.save()
        return redirect('inincvoucher')

def incgroupsummary(request): 
    vouch=inincvouchert.objects.filter()

    sum1=0
    sum2=0
    for a in vouch:
        sum1+=a.icredit
        
    for b in vouch:
        sum2+=b.idebit

    context={'vouch':vouch,'sum1':sum1,'sum2':sum2}    
    return render(request,'incgroupsummary.html',context)

def incledgersummary(request,pk):
    vch=inincvouchert.objects.get(id=pk)
    vouch=inincvouchert.objects.filter(id=pk)

    sum1=0
    sum2=0

    for a in vouch:
        sum1+=a.icredit

    for b in vouch:
        sum2+=b.idebit 

    clsum=sum1+sum2       
        
    context={'vch':vch,'vouch':vouch,'sum1':sum1,'sum2':sum2,'clsum':clsum}   
    return render(request,'incledgersummary.html',context) 


def incledgervoucher(request,pk):
    vch=inincvouchert.objects.get(id=pk)
    vouch=inincvouchert.objects.filter(id=pk)

    sum1=0
    sum2=0

    for a in vouch:
        sum1+=a.idebit

    for b in vouch:
        sum2+=b.icredit 

    context={'vch':vch,'vouch':vouch,'sum1':sum1,'sum2':sum2}     
    return render(request,'incledgervoucher.html',context)    






def ininxvoucher(request):
    ledg=ledgercreation.objects.all()
    return render(request,'ininxvoucher.html',{'ledg':ledg})    

def ininxvouchadd(request):
    if request.method == 'POST':
        ivdate=request.POST['ivdate']
        iparticular=request.POST['iparticular']
        iaccount=request.POST['iaccount']
        ivouchertype=request.POST['ivouchertype']
        ivoucherno=request.POST['ivoucherno']
        
        idebit=request.POST['idebit']
       
        icredit=request.POST['icredit']
        

        voui=ininxvouchert(
            ivdate=ivdate,
            iparticular=iparticular,
            iaccount=iaccount,
            ivouchertype=ivouchertype,
            ivoucherno=ivoucherno,
            idebit=idebit,
            icredit=icredit,
            

        )
        voui.save()
        return redirect('ininxvoucher')     


def inxgroupsummary(request):
    vouch=ininxvouchert.objects.all()
    sum1=0
    sum2=0
    for a in vouch:
        sum1+=a.icredit

    for b in vouch:
        sum2+=b.idebit

    context={'vouch':vouch,'sum1':sum1,'sum2':sum2}        

    return render(request,'inxgroupsummary.html',context)  


def inxledgersummary(request,pk):
    vch=ininxvouchert.objects.get(id=pk)
    vouch=ininxvouchert.objects.filter(id=pk)

    sum1=0
    sum2=0

    for a in vouch:
        sum1+=a.icredit

    for b in vouch:
        sum2+=b.idebit

    clsum=sum1+sum2


    context={'vch':vch,'vouch':vouch,'sum1':sum1,'sum2':sum2,'clsum':clsum}
    return render(request,'inxledgersummary.html',context)

def inxledgervoucher(request,pk):
    vch=ininxvouchert.objects.get(id=pk)
    vouch=ininxvouchert.objects.filter(id=pk)

    sum1=0
    sum2=0
    for a in vouch:
        sum1+=a.icredit

    for b in vouch:
        sum2+=b.idebit    

    context={'vch':vch,'sum1':sum1,'sum2':sum2}
    return render(request,'inxledgervoucher.html',context)





def trialbalance(request):
    total=vouchert.objects.all()

    sum1=0
    sum2=0
    for a in total:
        sum1+=a.credit

    for b in total:
        sum2+=b.debit    

    totinc=inincvouchert.objects.all()


    sum3=0
    sum4=0

    for a in totinc:
        sum3+=a.icredit

    for b in totinc:
        sum4+=b.idebit

    totinx=ininxvouchert.objects.all() 

    sum6=0
    sum7=0

    for a in totinx:
        sum6+=a.icredit

    for b in totinx:
        sum7+=b.idebit   

    cpsum1=22000 
    cpsum2=45000
    loan=50000
    loan2=60000
    crl=75000
    crl2=65000
    fxa=55000
    fxa2=40000
    invst=80000
    invst2=30000
    cuas=50000
    cuas2=40000
    brdv=45000
    brdv2=25000
    sala=35000
    sala2=20000
    pur=45000
    pur2=80000
    dirin=65000
    dirin2=35000

    crtot=sum1+sum3+cpsum1+loan+crl+fxa+invst+cuas+brdv+sala+pur+dirin+sum6
    drtot=sum2+sum4+sum7+cpsum2+loan2+crl2+fxa2+invst2+cuas2+brdv2+sala2+pur2+dirin2
    diff=crtot-drtot

    



    context={'total':total,'totinc':totinc,'sum1':sum1,'sum2':sum2,'sum3':sum3,'sum4':sum4,'sum6':sum6,'sum7':sum7,'totinx':totinx,
    'cpsum1':cpsum1,'cpsum2':cpsum2,'loan':loan,'loan2':loan2,'crl':crl,'crl2':crl2,'fxa':fxa,'fxa2':fxa2,
    'invst':invst,'invst2':invst2,'brdv':brdv,'sala':sala,'sala2':sala2,'pur':pur,'pur2':pur2,'dirin':dirin,
    'dirin2':dirin2,'brdv2':brdv2,'cuas':cuas,'cuas2':cuas2,'crtot':crtot,'drtot':drtot,'diff':diff}
    return render(request,'trialbalance.html',context)                








































