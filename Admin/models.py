from django.db import models

# Create your models here.
class tbl_district(models.Model):
    district_name=models.CharField(max_length=30)

class tbl_category(models.Model):
    category_name=models.CharField(max_length=30)

class tbl_place(models.Model):
    place_name=models.CharField(max_length=30) 
    district=models.ForeignKey(tbl_district,on_delete=models.CASCADE) 

class tbl_subcategory(models.Model):
    subcategory_name=models.CharField(max_length=30)
    category=models.ForeignKey(tbl_category,on_delete=models.CASCADE)

class tbl_trainer(models.Model):
    trainer_name=models.CharField(max_length=50)
    trainer_email=models.CharField(max_length=50)
    trainer_contact=models.CharField(max_length=50)
    trainer_password=models.CharField(max_length=50)
    trainer_photo=models.FileField(upload_to='Assets/File/Trainer')
    trainer_gender=models.CharField(max_length=50)  

class tbl_gymplan(models.Model):
    gymplan_details=models.CharField(max_length=50)
    gymplan_amount=models.CharField(max_length=50)     

class tbl_admin(models.Model):
    admin_name=models.CharField(max_length=50)
    admin_email=models.CharField(max_length=50)
    admin_password=models.CharField(max_length=50)
