from django.shortcuts import render,redirect
from Admin.models import *
from Trainer.models import *
from User.models import *
from django.db.models import Q
from datetime import datetime
# Create your views here.

def homepage(request):
    if 'tid' not in request.session:
        return redirect('Guest:Login')
    return render(request,'Trainer/Homepage.html')


def trainerprofile(request):
    if 'tid' not in request.session:
        return redirect('Guest:Login')
    trainerdata=tbl_trainer.objects.get(id=request.session['tid'])
    return render(request,'Trainer/TrainerProfile.html',{'data':trainerdata})

def editprofile(request):
    if 'tid' not in request.session:
        return redirect('Guest:Login')
    editdata=tbl_trainer.objects.get(id=request.session['tid'])
    if request.method=="POST":
        editdata.trainer_name=request.POST.get('txt_name')
        editdata.trainer_email=request.POST.get('txt_email')
        editdata.trainer_contact=request.POST.get('txt_contact')
        editdata.save()
        return redirect('Trainer:TrainerProfile')
    else:
        return render(request,'Trainer/EditProfile.html',{'edit':editdata})

def changepassword(request):
    if 'tid' not in request.session:
        return redirect('Guest:Login')
    trainerdata=tbl_trainer.objects.get(id=request.session['tid'])
    if request.method=="POST":
        currentpassword=request.POST.get('current_password')
        newpassword=request.POST.get('new_password')
        confirmpassword=request.POST.get('confirm_password')
        if trainerdata.trainer_password==currentpassword:
            if newpassword==confirmpassword:
                trainerdata.trainer_password=newpassword
                trainerdata.save()
                return redirect('Trainer:TrainerProfile')
            else:
                return render(request,'Trainer/ChangePassword.html',{'msg2':"New Password and Confirm Password are wrong"})
        else:
                return render(request,'Trainer/ChangePassword.html',{'msg1':"Current Password is wrong"})
    else:
        return render(request,'Trainer/ChangePassword.html')

def complaint(request):
    if 'tid' not in request.session:
        return redirect('Guest:Login')
    trainer=tbl_trainer.objects.get(id=request.session['tid']) 
    complaint=tbl_trainercomplaint.objects.all()
    if request.method=="POST":
        complaint=request.POST.get('txt_complaint')
        title=request.POST.get('txt_title')
        tbl_trainercomplaint.objects.create( trainercomplaint_title=title,trainercomplaint_content=complaint)
        return redirect('Trainer:Complaint') 
    else:
        return render(request,'Trainer/Complaint.html')

def assignedlist(request):
    if 'tid' not in request.session:
        return redirect('Guest:Login')
    assigned=tbl_assign.objects.filter(trainer=request.session['tid'])
    return render(request,'Trainer/AssignedList.html',{'assigned':assigned})        

def diet(request,assid):
    if 'tid' not in request.session:
        return redirect('Guest:Login')
    if request.method=='POST':
        diet=request.POST.get('txt_diet')
        assdata=tbl_assign.objects.get(id=assid)
        assdata.assign_status=1
        assdata.save()
        assignid=tbl_assign.objects.get(id=assid)
        tbl_dietplan.objects.create(diet_details=diet,assign=assignid)
        return render(request,'Trainer/AddDiet.html')
    else:
        return render(request,'Trainer/AddDiet.html')

def plan(request):
    if 'tid' not in request.session:
        return redirect('Guest:Login')
    return render(request,'Trainer/ViewDiets.html')

def viewdiets(request,dpid):
    if 'tid' not in request.session:
        return redirect('Guest:Login')
    dietdata=tbl_dietplan.objects.filter(assign_id=dpid)
    return render(request,'Trainer/ViewDiets.html',{'data':dietdata})

def deletedid(request,did):
    if 'tid' not in request.session:
        return redirect('Guest:Login')
    return render(request,'Trainer/ViewDiets.html')

def chatpage(request,id):
    if 'tid' not in request.session:
        return redirect('Guest:Login')
    user  = tbl_user.objects.get(id=id)
    return render(request,"Trainer/Chat.html",{"user":user})

def ajaxchat(request):
    if 'tid' not in request.session:
        return redirect('Guest:Login')
    from_trainer = tbl_trainer.objects.get(id=request.session["tid"])
    to_user = tbl_user.objects.get(id=request.POST.get("tid"))
    tbl_chat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),trainer_from=from_trainer,user_to=to_user,chat_file=request.FILES.get("file"))
    return render(request,"Trainer/Chat.html")

def ajaxchatview(request):
    if 'tid' not in request.session:
        return redirect('Guest:Login')
    tid = request.GET.get("tid")
    trainer = tbl_trainer.objects.get(id=request.session["tid"])
    chat_data = tbl_chat.objects.filter((Q(trainer_from=trainer) | Q(trainer_to=trainer)) & (Q(user_from=tid) | Q(user_to=tid))).order_by('chat_time')
    return render(request,"Trainer/ChatView.html",{"data":chat_data,"tid":int(tid)})

def clearchat(request):
    if 'tid' not in request.session:
        return redirect('Guest:Login')
    tbl_chat.objects.filter(Q(trainer_from=request.session["tid"]) & Q(user_to=request.GET.get("tid")) | (Q(user_from=request.GET.get("tid")) & Q(trainer_to=request.session["tid"]))).delete()
    return render(request,"Trainer/ClearChat.html",{"msg":"Chat Deleted Sucessfully...."})

def logout(request):
    if 'tid' not in request.session:
        return redirect('Guest:Login')
    del request.session['tid']
    return redirect('Guest:Login')