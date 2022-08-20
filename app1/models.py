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
    name = models.CharField(max_length=225)
    alias = models.CharField(max_length=225,null=True)
    under = models.CharField(max_length=225)
    namegroup=models.CharField(max_length=255,null=True)
    gp_behaves_like_sub_ledger = models.BooleanField(default=False)
    nett_debit_credit_bal_reporting = models.BooleanField(default=False)
    used_for_calculation = models.BooleanField(default=False)
    method_to_allocate_usd_purchase = models.CharField(max_length=225,null=True,blank=True)

    def _str_(self):
        return self.name      



class ledgercreation(models.Model):
  lname=models.CharField(max_length=255,null=True)
  alias=models.CharField(max_length=255,null=True)
  under=models.CharField(max_length=255)
  prbankdetals=models.CharField(max_length=255,)
  holders_name=models.CharField(max_length=255,null=True)
  ac_no=models.IntegerField(null=True) 
  ifsc=models.IntegerField(null=True)
  swiftcode=models.IntegerField(null=True)
  bankname=models.CharField(max_length=255,null=True) 
  branch=models.CharField(max_length=255,null=True)
  checkbook=models.CharField(max_length=255,null=True)
  checkprinting=models.CharField(max_length=255,null=True) 
  mailname=models.CharField(max_length=255,null=True)
  mailaddress=models.CharField(max_length=255,null=True)
  mailcontry=models.CharField(max_length=255,null=True)
  mailstate=models.CharField(max_length=255,null=True)
  mailpin=models.IntegerField(null=True)
  pan=models.IntegerField(null=True)
  regtype=models.CharField(max_length=255,null=True)
  gst=models.IntegerField(null=True)
  gstdetails=models.CharField(max_length=255,null=True)


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




  

