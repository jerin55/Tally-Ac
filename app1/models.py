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

    def __str__(self):
      return self.party_name  
