from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User,auth
from django.http import HttpResponse
import json
from django.http import JsonResponse
from .models import App,Archive
from django.contrib.auth.decorators import login_required
# Create your views here.
def crmhome(request):
    return render(request,'crmhome.html')

def crmnavv(request):
    return render(request,'crmnavv.html')

def crmsignin(request):
    return render(request,'crmsignin.html')

def crmregister(request):
    return render(request,'crmregister.html')

def register(request):

    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
  
        
        if User.objects.filter(username=username).exists():
                messages.info(request,'Username exists')
                return redirect('crmregister')
        elif User.objects.filter(email=email).exists():
                messages.info(request,'Email exists')
                return redirect('crmregister')
        
        else :
            user=User.objects.create_user(first_name=firstname,last_name=lastname,username=username,email=email,password=password,)
            user.save()
            messages.success(request,'Registration Successfull')
            if App.objects.exists():
                pass
            else:
        
                app1 = App(name="HP", price=600,image='image/hp.png')
                app1.save()
                app2 = App(name="DELL", price=500,image='image/dell.png')
                app2.save()
                app3 = App(name="ASUSE", price=750,image='image/asuse.png')
                app3.save()
                
            return redirect('crmsignin')
    
def signinpage(request):
    if request.method=='POST':
        uname=request.POST['user']
        password=request.POST['pas']
        user=auth.authenticate(username=uname,password=password)
        if user is not None:
            if user.is_staff:
                login(request,user)
                return redirect('adminhome')
            else:
                login(request,user)
                auth.login(request,user)
                return redirect('crmloginpage')
        else:
            messages.info(request,'Invalid Username or password')
            return redirect('crmsignin')
        
def crmcontact(request):
    return render(request,'crmcontact.html')
@login_required(login_url='crmhome')
def crmadditem(request):
    return render(request,'crmadditem.html')

def log_out(request):
    auth.logout(request)
    return redirect('crmhome')

def crmusernav(request):
    return render(request,'crmusernav.html')

@login_required(login_url='crmhome')
def crmloginpage(request):
     currentuser=request.user.username
     currentuser1=request.user
     product1=App.objects.filter(user=None)
     product=App.objects.filter(user=currentuser1)
     archived_app_ids = Archive.objects.values_list('app_id', flat=True)
     return render(request,'crmloginpage.html',{'currentuser':currentuser,'product':product,'archived_app_ids': archived_app_ids,'product1':product1})

@login_required(login_url='crmhome')
def crmarchive(request):
    currentuser=request.user.username
    return render(request,'crmarchive.html',{'currentuser':currentuser})

def adminhome(request):
    return render(request,'adminhome.html')


def appdetails(request):
    currentuser=request.user
    if request.method=='POST':
        name=request.POST['name']
        price=request.POST['price']
        if 'file' in request.FILES:
            photo = request.FILES['file']
        else:
            
            photo = 'image/download.png'
        
        data=App(name=name,price=price,user=currentuser,image=photo)
        data.save()
        if 'Next' in request.POST:
            return redirect('crmadditem')
        if "Save" in request.POST:
            return redirect('crmloginpage') 

    else:
        return redirect('crmadditem')
    
@login_required(login_url='crmhome')   
def crmarchive(request):
    currentuser=request.user
    arch=Archive.objects.filter(user=currentuser)
    return render(request,'crmarchive.html',{'arch':arch})

def archive_app(request,id):
    product=App.objects.get(id=id)
    currentuser=request.user
    data,created=Archive.objects.get_or_create(app=product,user=currentuser)
    data.save()
    return redirect('crmloginpage')

def archiveremove(request,id):
    product=Archive.objects.get(id=id)
    product.delete()
    return redirect('crmarchive')

     
