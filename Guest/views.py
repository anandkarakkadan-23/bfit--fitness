from django.shortcuts import render,redirect
from Guest.models import *
from Admin.models import *

# Create your views here.

def userregistration(request):
    dis=tbl_district.objects.all()
    if request.method=='POST':
        name=request.POST.get('txt_name')
        email=request.POST.get('txt_email')
        contact=request.POST.get('phone')
        address=request.POST.get('txt_address')
        password=request.POST.get('txt_password')
        photo=request.FILES.get('txt_photo') 
        gender=request.POST.get('txt_gender')
        placeid=tbl_place.objects.get(id=request.POST.get('sel_place'))
        tbl_user.objects.create(user_name=name,
                                user_email=email,
                                user_contact=contact,
                                user_address=address,
                                user_password=password,
                                user_gender=gender,
                                user_photo=photo,
                                place=placeid) 
        return redirect('Guest:userregistration')
    else:
        return render(request,'Guest/UserRegistration.html',{'dis':dis})

def login(request):
    if request.method=='POST':
        email=request.POST.get('txt_email')
        password=request.POST.get('txt_password')

        usercount=tbl_user.objects.filter(user_email=email,user_password=password).count()
        admincount=tbl_admin.objects.filter(admin_email=email,admin_password=password).count()
        trainercount=tbl_trainer.objects.filter(trainer_email=email,trainer_password=password).count()

        if usercount>0:
            userdata=tbl_user.objects.get(user_email=email,user_password=password)
            request.session['uid']=userdata.id
            request.session['uname']=userdata.user_name
            return redirect('User:Homepage')
        
        elif admincount>0:
            admindata=tbl_admin.objects.get(admin_email=email,admin_password=password)
            request.session['aid']=admindata.id
            request.session['aname']=admindata.admin_name
            return redirect('Admin:dashboard')

        elif trainercount>0:
            trainerdata=tbl_trainer.objects.get(trainer_email=email,trainer_password=password)
            request.session['tid']=trainerdata.id
            request.session['tname']=trainerdata.trainer_name
            return redirect('Trainer:Homepage')    
        
        else:
            return render(request,'Guest/Login.html',{'msg':"Invalid Data"})
    else:
        return render(request,'Guest/Login.html')
    
def ajaxplace(request):
    district=tbl_district.objects.get(id=request.GET.get('did'))
    Place = tbl_place.objects.filter(district=district)
    return render(request,'Guest/Ajaxplace.html',{'place':Place}) 

def index(request):
    gymplan=tbl_gymplan.objects.all()
    return render(request,'Guest/Index.html',{'data':gymplan}) 
