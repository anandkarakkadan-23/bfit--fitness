from django.db import models
from Guest.models import*
from Admin.models import*



# Create your models here.


class tbl_feedback(models.Model):
    feedback_content=models.CharField(max_length=50)
    feedback_date=models.DateField(auto_now_add=True)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE,null=True)

class tbl_complaint(models.Model):
    complaint_title=models.CharField(max_length=50) 
    complaint_content=models.CharField(max_length=100) 
    complaint_date=models.DateField(auto_now_add=True)
    complaint_status=models.IntegerField(default=0)
    complaint_reply=models.CharField(max_length=50)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE,null=True)
    trainer=models.ForeignKey(tbl_trainer,on_delete=models.CASCADE,null=True)

class tbl_admission(models.Model):
    admission_date=models.DateField()
    admission_status=models.IntegerField(default=0)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    gymplan=models.ForeignKey(tbl_gymplan,on_delete=models.CASCADE)


class tbl_monthlypayment(models.Model):
    monthly_date=models.DateField(auto_now_add=True)
    monthly_status=models.IntegerField(default=0)
    admission=models.ForeignKey(tbl_admission,on_delete=models.CASCADE)

class tbl_chat(models.Model):
    chat_content = models.CharField(max_length=500)
    chat_time = models.DateTimeField()
    chat_file = models.FileField(upload_to='ChatFiles/')
    user_from = models.ForeignKey(tbl_user,on_delete=models.CASCADE,related_name="user_from",null=True)
    user_to = models.ForeignKey(tbl_user,on_delete=models.CASCADE,related_name="user_to",null=True)
    trainer_from = models.ForeignKey(tbl_trainer,on_delete=models.CASCADE,related_name="trainer_from",null=True)
    trainer_to = models.ForeignKey(tbl_trainer,on_delete=models.CASCADE,related_name="trainer_to",null=True)