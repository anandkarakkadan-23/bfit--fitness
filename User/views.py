from django.shortcuts import render,redirect
from Guest.models import *
from User.models import *
from Admin.models import*
from Trainer.models import*
from django.db.models import Q
from datetime import datetime


# Create your views here.
def homepage(request):
    if 'uid' not in request.session:
        return redirect('Guest:Login')
    gymplan=tbl_gymplan.objects.all()
    return render(request,'User/Homepage.html',{'data':gymplan})

def userprofile(request):
    if 'uid' not in request.session:
        return redirect('Guest:Login')
    userdata=tbl_user.objects.get(id=request.session['uid'])
    return render(request,'User/UserProfile.html',{'data':userdata}) 

def editprofile(request):
    if 'uid' not in request.session:
        return redirect('Guest:Login')
    editdata=tbl_user.objects.get(id=request.session['uid'])
    if request.method=="POST":
        editdata.user_name=request.POST.get('txt_name')
        editdata.user_email=request.POST.get('txt_email')
        editdata.user_contact=request.POST.get('txt_contact')
        editdata.user_address=request.POST.get('txt_address')
        editdata.save()
        return redirect('User:UserProfile')
    else:
        return render(request,'User/EditProfile.html',{'edit':editdata})

def changepassword(request):
    if 'uid' not in request.session:
        return redirect('Guest:Login')
    userdata=tbl_user.objects.get(id=request.session['uid'])
    if request.method=="POST":
        currentpassword=request.POST.get('current_password')
        newpassword=request.POST.get('new_password')
        confirmpassword=request.POST.get('confirm_password')
        if userdata.user_password==currentpassword:
            if newpassword==confirmpassword:
                userdata.user_password=newpassword
                userdata.save()
                return redirect('User:UserProfile')
            else:
                return render(request,'User/ChangePassword.html',{'msg2':"New Password and Confirm Password are wrong"})
        else:
                return render(request,'User/ChangePassword.html',{'msg1':"Current Password is wrong"})
    else:
        return render(request,'User/ChangePassword.html')

def feedback(request):
    if 'uid' not in request.session:
        return redirect('Guest:Login')
    user=tbl_user.objects.get(id=request.session['uid'])
    feed=tbl_feedback.objects.all()
    if request.method=="POST":
      feedback=request.POST.get('txt_feedback')
      tbl_feedback.objects.create(feedback_content=feedback,user=user)
      return redirect('User:feedback')
    else:
        return render(request,'User/FeedBack.html',{'feed':feed})

def complaint(request):
    if 'uid' not in request.session:
        return redirect('Guest:Login')
    user=tbl_user.objects.get(id=request.session['uid']) 
    complaint=tbl_complaint.objects.all()
    if request.method=="POST":
        title=request.POST.get('txt_complainttitle')
        complaint=request.POST.get('txt_complaintcontent')
        tbl_complaint.objects.create( complaint_title=title,complaint_content=complaint,user=user)
        return redirect('User:complaint') 
    else:
        return render(request,'User/Complaint.html',{'comp':complaint}) 


def ViewGymplans(request):
    if 'uid' not in request.session:
        return redirect('Guest:Login')
    gymplan=tbl_gymplan.objects.all()
    return render(request,'User/ViewGymplans.html',{'data':gymplan})

def admission(request,id):
    if 'uid' not in request.session:
        return redirect('Guest:Login')
    admission=tbl_admission.objects.filter(user=request.session['uid'])

    if request.method == "POST":
        if 'uid' not in request.session:
            return redirect('Guest:Login')
        gymplanid=tbl_gymplan.objects.get(id=id)
        userid=tbl_user.objects.get(id=request.session['uid'])
        date=request.POST.get("txt_date")
        tbl_admission.objects.create(user=userid,gymplan=gymplanid,admission_date=date)
        return render(request,'User/Admission.html',{'msg':"Admission Added",'id':id,'admission':admission})
    else:
        return render(request,'User/Admission.html',{'admission':admission,'id':id})

def MyAdmission(request):
    if 'uid' not in request.session:
        return redirect('Guest:Login')
    data=tbl_admission.objects.filter(user=request.session['uid'])
    return render(request,'User/MyAdmission.html',{'data':data})

def delcomplaint(request,did):
    if 'uid' not in request.session:
        return redirect('Guest:Login')
    tbl_complaint.objects.get(id=did).delete()
    return redirect('User:complaint') 

def delfeedback(request,dfid):
    if 'uid' not in request.session:
        return redirect('Guest:Login')
    tbl_feedback.objects.get(id=dfid).delete()
    return redirect('user:feedback')    

 
def deladmission(request,adid,id):
    if 'uid' not in request.session:
        return redirect('Guest:Login')
    tbl_admission.objects.get(id=adid).delete()
    return redirect('User:Admission',id)      

def payment(request,id):
    if 'uid' not in request.session:
        return redirect('Guest:Login')
    admission = tbl_admission.objects.get(id=id)
    gymplan = tbl_gymplan.objects.get(id=admission.gymplan.id)
    amount = gymplan.gymplan_amount
    if request.method == "POST":
        tbl_monthlypayment.objects.create(monthly_status='1',admission=admission)
        return redirect("User:loader")
    else:
        return render(request,"User/Payment.html", {"total":amount})

def loader(request):
    if 'uid' not in request.session:
        return redirect('Guest:Login')
    return render(request,"User/Loader.html")

def paymentsuc(request):
    if 'uid' not in request.session:
        return redirect('Guest:Login')
    return render(request,"User/Payment_suc.html")


def mydiet(request,dmid):
    if 'uid' not in request.session:
        return redirect('Guest:Login')
    dietdata=tbl_dietplan.objects.filter(assign_id=dmid)
    return render(request,"User/MyDiet.html",{"dietdata":dietdata})


def delmydiet(request,dietdata):
    if 'uid' not in request.session:
        return redirect('Guest:Login')
    tbl_admission.ojects.get(id=dietdata).delete()
    return redirect('User:MyDiet')

def Viewassign(request):
    if 'uid' not in request.session:
        return redirect('Guest:Login')
    assign=tbl_assign.objects.filter(admission__user=request.session['uid'])
    return render(request,"user/ViewAssign.html",{"assign":assign})

def chatpage(request,id):
    if 'uid' not in request.session:
        return redirect('Guest:Login')
    trainer  = tbl_trainer.objects.get(id=id)
    return render(request,"User/Chat.html",{"user":trainer})

def ajaxchat(request):
    if 'uid' not in request.session:
        return redirect('Guest:Login')
    from_user = tbl_user.objects.get(id=request.session["uid"])
    to_trainer = tbl_trainer.objects.get(id=request.POST.get("tid"))
    tbl_chat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),user_from=from_user,trainer_to=to_trainer,chat_file=request.FILES.get("file"))
    return render(request,"User/Chat.html")

def ajaxchatview(request):
    if 'uid' not in request.session:
        return redirect('Guest:Login')
    tid = request.GET.get("tid")
    user = tbl_user.objects.get(id=request.session["uid"])
    chat_data = tbl_chat.objects.filter((Q(user_from=user) | Q(user_to=user)) & (Q(trainer_from=tid) | Q(trainer_to=tid))).order_by('chat_time')
    return render(request,"User/ChatView.html",{"data":chat_data,"tid":int(tid)})

def clearchat(request):
    if 'uid' not in request.session:
        return redirect('Guest:Login')
    tbl_chat.objects.filter(Q(user_from=request.session["uid"]) & Q(trainer_to=request.GET.get("tid")) | (Q(trainer_from=request.GET.get("tid")) & Q(user_to=request.session["uid"]))).delete()
    return render(request,"User/ClearChat.html",{"msg":"Chat Deleted Sucessfully...."})

def logout(request):
    if 'uid' not in request.session:
        return redirect('Guest:Login')
    del request.session['uid']
    return redirect('Guest:Login')

def workout(request):
    if 'uid' not in request.session:
        return redirect('Guest:Login')

    return render(request,'User/Workout.html')

def musclegaining(request):
    if 'uid' not in request.session:
        return redirect('Guest:Login')

    return render(request,'User/Muscle Gaining.html')   


def workouts(request):
    if 'uid' not in request.session:
        return redirect('Guest:Login')

    return render(request,'User/Workouts.html')


def absworkout(request):
    if 'uid' not in request.session:
        return redirect('Guest:Login')

    return render(request,'User/ABS Workout.html')         


def Legsworkout(request):
    if 'uid' not in request.session:
        return redirect('Guest:Login')
    return render(request,'User/LegsWorkout.html')    


def fullbody(request):
    if 'uid' not in request.session:
        return redirect('Guest:Login')

    return render(request,'User/FullBody.html')    

def cardio(request):
    if 'uid' not in request.session:
        return redirect('Guest:Login')
    return render(request,'User/Cardio.html')  

def shoulder(request):
    if 'uid' not in request.session:
        return redirect('Guest:Login')

    return render(request,'User/Shoulder.html')   
