from django.db import models
from Guest.models import*
from User.models import*


# create your models here.

class tbl_trainercomplaint(models.Model):
    trainercomplaint_title=models.CharField(max_length=50)
    trainercomplaint_content=models.CharField(max_length=100) 
    trainercomplaint_date=models.DateField(auto_now_add=True)
    trainercomplaint_status=models.IntegerField(default=0)
    trainercomplaint_reply=models.CharField(max_length=50)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE,null=True)
    trainer=models.ForeignKey(tbl_trainer,on_delete=models.CASCADE,null=True)

class tbl_assign(models.Model):
    assign_date=models.DateField(auto_now_add=True)
    assign_status=models.IntegerField(default=0)
    admission=models.ForeignKey(tbl_admission,on_delete=models.CASCADE)
    trainer=models.ForeignKey(tbl_trainer,on_delete=models.CASCADE)

class tbl_dietplan(models.Model):
    diet_details=models.CharField(max_length=30)
    assign=models.ForeignKey(tbl_assign,on_delete=models.CASCADE)