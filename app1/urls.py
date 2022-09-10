from django.urls import path,include
from.import views



urlpatterns = [

    path('',views.base,name='base'),
    path('index',views.index,name='index'),
    path('group',views.group,name='group'),
    path('branch',views.branch,name='branch'),
    path('ledger',views.ledger,name='ledger'),
    path('primary',views.primary,name='primary'),
    path('costcat',views.costcat,name='costcat'),
    path('costcentr',views.costcentr,name='costcentr'),
    path('voucher',views.voucher,name='voucher'),
    path('vouchpage',views.vouchpage,name='vouchpage'),
    path('receivabl',views.receivabl,name='receivabl'),
    path('payabl',views.payabl,name='payabl'),
    path('creategroup',views.creategroup,name='creategroup'),
    path('create_group',views.create_group,name='create_group'),
    path('grcreate',views.grcreate,name='grcreate'),
    path('createledger',views.createledger,name='createledger'),
    path('credit',views.credit,name='credit'),
    path('debi',views.debi,name='debi'),
    path('ledgercreations',views.ledgercreations,name='ledgercreations'),
    path('ledgerlist',views.ledgerlist,name='ledgerlist'),
    path('nw',views.nw,name='nw'),
    path('groupsummery',views.groupsummery,name='groupsummery'),
    path('ledgersummary/<int:pk>',views.ledgersummary,name='ledgersummary'),
    path('ledgervoucher/<int:pk>',views.ledgervoucher,name='ledgervoucher'),
    path('voucheradd',views.voucheradd,name='voucheradd'),
    path('trialbalance',views.trialbalance,name='trialbalance'),
    path('vouchadd',views.vouchadd,name='vouchadd'),
    path('ex',views.ex,name='ex'),
    path('inincvoucher',views.inincvoucher,name='inincvoucher'),
    path('inincvouchadd',views.inincvouchadd,name='inincvouchadd'),
    path('ininxvoucher',views.ininxvoucher,name='ininxvoucher'),
    path('ininxvouchadd',views.ininxvouchadd,name='ininxvouchadd'),
    path('incgroupsummary',views.incgroupsummary,name='incgroupsummary'),
    path('incledgersummary/<int:pk>',views.incledgersummary,name='incledgersummary'),
    path('incledgervoucher/<int:pk>',views.incledgervoucher,name='incledgervoucher'),
    path('inxgroupsummary',views.inxgroupsummary,name='inxgroupsummary'),
    path('inxledgersummary/<int:pk>',views.inxledgersummary,name='inxledgersummary'),
    path('inxledgervoucher/<int:pk>',views.inxledgervoucher,name='inxledgervoucher')







    
]