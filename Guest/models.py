from django.db import models
from Admin.models import*

# Create your models here.
class tbl_user(models.Model):
    user_name=models.CharField(max_length=30)
    user_email= models.CharField(max_length=50)
    user_contact=models.CharField(max_length=30)
    user_address=models.CharField(max_length=100)
    user_password=models.CharField(max_length=30)
    user_gender=models.CharField(max_length=30)
    user_photo=models.FileField(upload_to='Assets/File/User/')
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    user_status=models.IntegerField(default=0)
