from re import T
from turtle import textinput
from django.db import models

# Create your models here.


class items(models.Model):
    items=models.CharField(max_length=255)
    quantity=models.IntegerField(null=True)

    def __str__(self):
      return self.items


class receivable(models.Model):
    date=models.DateField()
    party_name=models.CharField(max_length=255)
    items=models.ForeignKey(items,on_delete=models.CASCADE,null=True)
    pending_amound=models.IntegerField()
    due_date=models.DateField()
    overdue=models.IntegerField(null=True)

    def __str__(self):
      return self.party_name


class payitems(models.Model):
    items=models.CharField(max_length=255)
    quantity=models.IntegerField(null=True)

    def __str__(self):
      return self.items



class payable(models.Model):
    date=models.DateField()
    party_name=models.CharField(max_length=255)
    items=models.ForeignKey(payitems,on_delete=models.CASCADE,null=True)
    pending_amound=models.IntegerField()
    due_date=models.DateField()
    overdue=models.IntegerField(null=True)

    def total(self):
      tot=sum(self.pending_amound)
      return tot

    def __str__(self):
      return self.party_name  

class grunder(models.Model):
  und=models.CharField(max_length=255)  

  def __str__(self):
      return self.und  

     



class GroupModel(models.Model):
    group_name  = models.CharField(max_length=225)
    group_alias  = models.CharField(max_length=225,null=True)
    group_under  = models.CharField(max_length=225)
    nature = models.CharField(max_length=255,null=True)
    gross_profit = models.CharField(max_length=255 ,null=True)
    sub_ledger  = models.BooleanField(default=False)
    debit_credit  = models.BooleanField(default=False)
    calculation  = models.BooleanField(default=False)
    invoice  = models.CharField(max_length=225,null=True,blank=True)

    def _str_(self):
        return self.name      



class ledgercreation(models.Model):
  name=models.CharField(max_length=255,null=True)
  alias=models.CharField(max_length=255,null=True)
  under=models.CharField(max_length=255)
  bank_details=models.CharField(max_length=255,) 
  mname=models.CharField(max_length=255,null=True)
  address=models.CharField(max_length=255,null=True)
  country=models.CharField(max_length=255,null=True)
  state=models.CharField(max_length=255,null=True)
  pincode =models.IntegerField(null=True)
  pan_no =models.IntegerField(null=True)
  registration_type =models.CharField(max_length=255,null=True)
  gst_uin =models.IntegerField(null=True)
  set_alter_gstdetails =models.CharField(max_length=255,null=True)

  


  ac_holder_nm =models.CharField(max_length=255,null=True)
  acc_no =models.IntegerField(null=True) 
  ifsc_code =models.IntegerField(null=True)
  swift_code =models.IntegerField(null=True)
  bank_name =models.CharField(max_length=255,null=True) 
  branch =models.CharField(max_length=255,null=True)
  SA_cheque_bk =models.CharField(max_length=255,null=True)
  Echeque_p =models.CharField(max_length=255,null=True)

  occ_set_odl = models.CharField(max_length=255,null=True)
  occ_ac_holder_nm =models.CharField(max_length=255,null=True)
  occ_acc_no =models.IntegerField(null=True) 
  occ_ifsc_code =models.IntegerField(null=True)
  occ_swift_code =models.IntegerField(null=True)
  occ_bank_name =models.CharField(max_length=255,null=True) 
  occ_branch =models.CharField(max_length=255,null=True)
  occ_SA_cheque_bk =models.CharField(max_length=255,null=True)
  occ_Echeque_p =models.CharField(max_length=255,null=True)

  od_set_odl = models.CharField(max_length=255,null=True)
  od_ac_holder_nm =models.CharField(max_length=255,null=True)
  od_acc_no =models.IntegerField(null=True) 
  od_ifsc_code =models.IntegerField(null=True)
  od_swift_code =models.IntegerField(null=True)
  od_bank_name =models.CharField(max_length=255,null=True) 
  od_branch =models.CharField(max_length=255,null=True)
  od_SA_cheque_bk =models.CharField(max_length=255,null=True)
  od_Echeque_p =models.CharField(max_length=255,null=True)

  

  statutory_details=models.CharField(max_length=255,null=True)

  type_of_ledger = models.CharField(max_length=100,null=True)
  rounding_method = models.CharField(max_length=100,null=True)
  rounding_limit = models.IntegerField(blank=True, null=True, default=None)
  GST_Applicable = models.CharField(max_length=100,null=True)
  Alter_GST_Details= models.CharField(max_length=100,null=True)
  Appropriate=models.CharField(max_length=100,null=True)
  Types_of_supply=models.CharField(max_length=100,null=True)

  type_duty_tax = models.CharField(max_length=100,null=True)
  tax_type = models.CharField(max_length=100,null=True)
  percentage_of_calcution = models.CharField(max_length=100,null=True)
  rond_method = models.CharField(max_length=100,null=True)
  rond_limit = models.IntegerField(blank=True, null=True, default=None)

  balance_billbybill = models.CharField(max_length=100,null=True)
  credit_period = models.CharField(max_length=100,null=True)
  creditdays_voucher = models.CharField(max_length=100,null=True)

  def _str_(self):
        return self.name 





class debit(models.Model):
  name=models.CharField(max_length=255) 
  credit=models.IntegerField()
  debit=models.IntegerField()

  def _str_(self):
        return self.name 



class cred(models.Model):
  name=models.CharField(max_length=255) 
  credit=models.IntegerField()
  debit=models.IntegerField()

  def _str_(self):
        return self.name 

class led(models.Model):
  date=models.DateField()
  openam=models.IntegerField()
  penam=models.IntegerField()
  due=models.DateField()
  overd=models.IntegerField() 



class vouchert(models.Model):
  vdate=models.DateField()
  ledger=models.ForeignKey(ledgercreation,on_delete=models.CASCADE,null=True)
  particular=models.CharField(max_length=255)
  under=models.CharField(max_length=255,null=True)
  account=models.CharField(max_length=255)
  vouchertype=models.CharField(max_length=255)
  voucherno=models.IntegerField()
  debit=models.IntegerField(null=True)
  credit=models.IntegerField(null=True)


class inincvouchert(models.Model):
  ivdate=models.DateField()
  iledger=models.ForeignKey(ledgercreation,on_delete=models.CASCADE,null=True)
  iparticular=models.CharField(max_length=255)
  iunder=models.CharField(max_length=255,null=True)
  iaccount=models.CharField(max_length=255)
  ivouchertype=models.CharField(max_length=255)
  ivoucherno=models.IntegerField()
  idebit=models.IntegerField(null=True)
  icredit=models.IntegerField(null=True)


class ininxvouchert(models.Model):
  ivdate=models.DateField()
  iledger=models.ForeignKey(ledgercreation,on_delete=models.CASCADE,null=True)
  iparticular=models.CharField(max_length=255)
  iunder=models.CharField(max_length=255,null=True)
  iaccount=models.CharField(max_length=255)
  ivouchertype=models.CharField(max_length=255)
  ivoucherno=models.IntegerField()
  idebit=models.IntegerField(null=True)
  icredit=models.IntegerField(null=True)








       




  

