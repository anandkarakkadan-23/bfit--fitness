from django.shortcuts import render,redirect
from Admin.models import*
from User.models import*
from Trainer.models import*

# Create your views here.
#district--------------------------------------------------------------------
def district(request):
    if 'aid' not in request.session:
        return redirect('Guest:Login')
    disdata=tbl_district.objects.all()
    if request.method=='POST':
        districtname=request.POST.get('txt_district')
        tbl_district.objects.create(district_name=districtname)
        return render(request,'Admin/District.html',{'msg':"Data Added"})
    else:
        return render(request,'Admin/District.html',{'dis':disdata})

def deldistrict(request,did):
    if 'aid' not in request.session:
        return redirect('Guest:Login')
    tbl_district.objects.get(id=did).delete()
    return redirect('Admin:District')

def editdistrict(request,eid):
    if 'aid' not in request.session:
        return redirect('Guest:Login')
    districtdata=tbl_district.objects.get(id=eid)
    if request.method=="POST":
        districtdata.district_name=request.POST.get('txt_district')
        districtdata.save()
        return redirect('Admin:District')
    else:
        return render(request,'Admin/District.html',{'editdata':districtdata})
#category--------------------------------------------------------------------
def category(request):
    if 'aid' not in request.session:
        return redirect('Guest:Login')
    catdata=tbl_category.objects.all()
    if request.method=='POST':
        categoryname=request.POST.get('txt_Category')
        tbl_category.objects.create(category_name=categoryname)
        return render(request,'Admin/Category.html',{'msg':"Data Added"})
    else:
        return render(request,'Admin/Category.html',{'cat':catdata})
       
def delcategory(request,dcid):
    if 'aid' not in request.session:
        return redirect('Guest:Login')
    tbl_category.objects.get(id=dcid).delete()
    return redirect('Admin:Category')

def editcategory(request,ecid):
    if 'aid' not in request.session:
        return redirect('Guest:Login')
    categorydata=tbl_category.objects.get(id=ecid)
    if request.method=="POST":
        categorydata.category_name=request.POST.get('txt_Category')
        categorydata.save()
        return redirect('Admin:Category')
    else:
        return render(request,'Admin/Category.html',{'editcategory':categorydata})
#place-------------------------------------------------------------------------------------------------------
def place(request):
    if 'aid' not in request.session:
        return redirect('Guest:Login')
    placedata=tbl_place.objects.all()#for dataframe(petti coloumn)
    district=tbl_district.objects.all()#dropdown
    if request.method=='POST':
        placename=request.POST.get('txt_place')
        districtid=tbl_district.objects.get(id=request.POST.get('sel_district'))#select option from dropdown
        tbl_place.objects.create(place_name=placename,district=districtid)#insertqry
        return render(request,'Admin/Place.html',{'msg':"Data Added"})
    else:
        return render(request,'Admin/Place.html',{'data':district,'plc':placedata})
        
def delplace(request,did):
    if 'aid' not in request.session:
        return redirect('Guest:Login')
    tbl_place.objects.get(id=did).delete()
    return redirect('Admin:place')
    
def editplace(request,eid):
    if 'aid' not in request.session:
        return redirect('Guest:Login')
    district=tbl_district.objects.all()
    placedata=tbl_place.objects.get(id=eid)
    if request.method=="POST":
        placedata.place_name=request.POST.get('txt_place')
        placedata.district=tbl_district.objects.get(id=request.POST.get('sel_district'))
        placedata.save()
        return redirect('Admin:place')
    else:
        return render(request,'Admin/Place.html',{'editplace':placedata,'data':district})
#subcategory-------------------------------------------------------------------------------------------------
def subcategory(request):
    if 'aid' not in request.session:
        return redirect('Guest:Login')
    subcategorydata=tbl_subcategory.objects.all()
    data=tbl_category.objects.all()#dropdown
    if request.method=='POST':
        subcategoryname=request.POST.get('txt_subcategory')
        cat=tbl_category.objects.get(id=request.POST.get('sel_category'))#select option from dropdown
        tbl_subcategory.objects.create(subcategory_name=subcategoryname,category=cat)#insertqry
        return render(request,'Admin/subcategory.html',{'data':data,'msg':"Data Added"})         
    else:
        return render(request,'Admin/subcategory.html',{'data':data,'subcat':subcategorydata}) 

def delsubcategory(request,dsid):
    if 'aid' not in request.session:
        return redirect('Guest:Login')
    tbl_subcategory.objects.get(id=dsid).delete()
    return redirect('Admin:subcategory')

def editsubcategory(request,esid):
    if 'aid' not in request.session:
        return redirect('Guest:Login')
    data=tbl_category.objects.all()
    subcategorydata=tbl_subcategory.objects.get(id=esid)
    if request.method=="POST":
     subcategorydata.subcategory_name=request.POST.get('txt_subcategory')
     subcategorydata.category=tbl_category.objects.get(id=request.POST.get('sel_category'))
     subcategorydata.save()
     return redirect('Admin:subcategory') 
    else:
     return render(request,'Admin/Subcategory.html',{'editsubcategory':subcategorydata,'data':data})   

def trainer(request):
    if 'aid' not in request.session:
        return redirect('Guest:Login')
    tisdata=tbl_trainer.objects.all()
    if request.method=='POST':
        trainername=request.POST.get('txt_name')
        traineremail=request.POST.get('txt_email')
        trainercontact=request.POST.get('txt_contact')
        trainergender=request.POST.get('txt_gender')
        trainerphoto=request.FILES.get('txt_photo')
        trainerpassword=request.POST.get('txt_password')
        tbl_trainer.objects.create(trainer_name=trainername,trainer_email=traineremail,trainer_contact=trainercontact,trainer_gender=trainergender,trainer_photo=trainerphoto,trainer_password=trainerpassword)
        return redirect("Admin:Trainer")
    else:
        return render(request,'Admin/Trainer.html',{'tis':tisdata})    
        
def gymplan(request):
    if 'aid' not in request.session:
        return redirect('Guest:Login')
    gisdata=tbl_gymplan.objects.all()
    if request.method=='POST':
        gymplandetails=request.POST.get('txt_details')
        gymplanamount=request.POST.get('txt_amount')
        tbl_gymplan.objects.create(gymplan_details=gymplandetails,gymplan_amount=gymplanamount)
        return render(request,'Admin/GymPlan.html',{'msg':"Data Added"})
    else:
        return render(request,'Admin/GymPlan.html',{'gis':gisdata}) 

def delgymplan(request,gid):
    if 'aid' not in request.session:
        return redirect('Guest:Login')
    tbl_gymplan.objects.get(id=gid).delete()
    return redirect('Admin:GymPlan')

def editgymplan(request,hid):
    if 'aid' not in request.session:
        return redirect('Guest:Login')
    gymplan=tbl_gymplan.objects.all()
    gymplandata=tbl_gymplan.objects.get(id=hid)
    if request.method=="POST":
        gymplandata.gymplan_details=request.POST.get('txt_details')
        gymplandata.gymplan_amount=request.POST.get('txt_amount')
        gymplandata.save()
        return redirect('Admin:GymPlan')
    else:
        return render(request,'Admin/GymPlan.html',{'editgymplan':gymplandata,'data':gymplan})

def adminregistration(request):
    if 'aid' not in request.session:
        return redirect('Guest:Login')
    tisdata=tbl_admin.objects.all()
    if request.method=='POST':
        adminname=request.POST.get('txt_name')
        adminemail=request.POST.get('txt_email')
        adminpassword=request.POST.get('txt_password')
        tbl_admin.objects.create(admin_name=adminname,admin_email=adminemail,admin_password=adminpassword)
        return redirect("Admin:AdminRegistration")
    else:
        return render(request,'Admin/AdminRegistration.html',{'data':tisdata})

def viewusercomplaint(request):
    if 'aid' not in request.session:
        return redirect('Guest:Login')
    complaint=tbl_complaint.objects.all()       
    return render(request,'Admin/ViewUserComplaint.html',{'view':complaint})

def reply(request,rid):
    if 'aid' not in request.session:
        return redirect('Guest:Login')
    complaint=tbl_complaint.objects.get(id=rid)
    if request.method=='POST':
        complaint.complaint_reply=request.POST.get('txt_reply')
        complaint.complaint_status=1
        complaint.save()
        return redirect('Admin:ViewUserComplaint')
    else:    
        return render(request,'Admin/Reply.html',)

def trainerreply(request,tid):
    if 'aid' not in request.session:
        return redirect('Guest:Login')
    complaint=tbl_trainercomplaint.objects.get(id=tid)
    if request.method=='POST':
        complaint.trainercomplaint_reply=request.POST.get('txt_trainerreply')
        complaint.trainercomplaint_status=1
        complaint.save()
        return redirect('Admin:ViewTrainerComplaint')
    else:    
        return render(request,'Admin/TrainerReply.html',)        
    
def viewtrainercomplaint(request):
    if 'aid' not in request.session:
        return redirect('Guest:Login')
    complaint= tbl_trainercomplaint.objects.all() 
    return render(request,'Admin/ViewTrainerComplaint.html',{'train':complaint})  

def viewfeedback(request):
    if 'aid' not in request.session:
        return redirect('Guest:Login')
    feedback=tbl_feedback.objects.all()
    return render(request,'Admin/ViewFeedback.html',{'back':feedback})

def viewadmission(request):
    if 'aid' not in request.session:
        return redirect('Guest:Login')
    admission=tbl_monthlypayment.objects.filter(monthly_status=1)
    return render(request,'Admin/ViewAdmission.html',{'admission':admission})

def viewusers(request):
    if 'aid' not in request.session:
        return redirect('Guest:Login')
    newuser=tbl_user.objects.filter(user_status=0)
    auser=tbl_user.objects.filter(user_status=1)
    ruser=tbl_user.objects.filter(user_status=2)
    return render(request,'Admin\ViewUser.html',{'view':newuser,'au':auser,'ru':ruser})

def acceptuser(request,accid):
    if 'aid' not in request.session:
        return redirect('Guest:Login')
    userdata=tbl_user.objects.get(id=accid)
    userdata.user_status=1
    userdata.save()
    return redirect('Admin:viewusers')

def rejectuser(request,rejid):
    if 'aid' not in request.session:
        return redirect('Guest:Login')
    userdata=tbl_user.objects.get(id=rejid)
    userdata.user_status=2
    userdata.save()
    return redirect('Admin:viewusers')   

def assigntrainer(request,admid):
    if 'aid' not in request.session:
        return redirect('Guest:Login')
    data=tbl_trainer.objects.all()
    data2=tbl_assign.objects.filter(admission=admid)
    if request.method=='POST':
        trainerid=tbl_trainer.objects.get(id=request.POST.get('sel_trainer'))
        admissionid=tbl_admission.objects.get(id=admid)
        addata=tbl_admission.objects.get(id=admid)
        addata.admission_status=1
        addata.save()
        tbl_assign.objects.create(admission=admissionid,trainer=trainerid)
        return render(request,'Admin/Assign.html',{'msg':"Trainer Assigned"})
    else:
        return render(request,'Admin/Assign.html',{'trainer':data})

def dashboard(request):
    if 'aid' not in request.session:
        return redirect('Guest:Login')
    data=tbl_admin.objects.get(id=request.session['aid'])
    user=tbl_user.objects.all().count()  
    trainer=tbl_trainer.objects.all().count() 
    complaint=tbl_complaint.objects.all().count() 
    complaintd=tbl_complaint.objects.filter(complaint_status=1).count() 
    return render(request,'Admin/Dashboard.html',{'data':data,'user':user,'trainer':trainer,'complaint':complaint,'comp':complaintd})


def logout(request):
    if 'aid' not in request.session:
        return redirect('Guest:Login')
    del request.session['aid']
    return redirect('Guest:Login')



