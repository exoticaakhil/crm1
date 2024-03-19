from django.urls import path
from. import views

urlpatterns = [
    path('',views.crmhome,name='crmhome'),
    path('crmnavv',views.crmnavv,name='crmnavv'),
    path('crmsignin',views.crmsignin,name='crmsignin'),
    path('crmregister',views.crmregister,name='crmregister'),
    path('register',views.register,name='register'),
    path('signinpage',views.signinpage,name='signinpage'),
    path('crmusernav',views.crmusernav,name='crmusernav'),
    path('crmloginpage',views.crmloginpage,name='crmloginpage'),
    path('crmcontact',views.crmcontact,name='crmcontact'),
    path('crmpricing',views.crmpricing,name='crmpricing'),
    path('log_out',views.log_out,name='log_out'),
    path('crmarchive',views.crmarchive,name='crmarchive'),
    path('adminhome',views.adminhome,name='adminhome'),
    path('appdetails',views.appdetails,name='appdetails'),
    path('archive_app/<int:id>',views.archive_app,name='archive_app'),
    path('archiveremove/<int:id>',views.archiveremove,name='archiveremove'),
]