from django.db import models

# Create your models here.
class faculty(models.Model):
    Fid=models.IntegerField(primary_key=True)
    Name=models.CharField(max_length=20)
    Address=models.CharField(max_length=20)
    Dob=models.DateField()
    Gender=models.CharField(max_length=10)
    Qualification=models.CharField(max_length=10)
    Mobile=models.IntegerField(max_length=10,null=True,blank=True)
    BatchInCharge=models.CharField(max_length=10)
    Email=models.EmailField()
    Password=models.CharField(max_length=1)
    Designation=models.CharField(max_length=15,default='trainer')
    Joiningdate=models.DateField(default='2019-01-01')
    Blood=models.CharField(max_length=5,default='O+')

  

class students(models.Model):
    Sid=models.IntegerField(primary_key=True)
    AdmNo=models.IntegerField(max_length=10,null=True,blank=True)
    AdmDate=models.DateField()
    Name=models.CharField(max_length=20)
    Address=models.CharField(max_length=20)
    Dob=models.DateField()
    Gender=models.CharField(max_length=10)
    Guardian=models.CharField(max_length=20)
    Mobile=models.IntegerField(max_length=10,null=True,blank=True)
    Batch=models.CharField(max_length=10)
    Email=models.EmailField()
    Password=models.CharField(max_length=10)
    Rollno=models.IntegerField(default=1)
    Qualification=models.CharField(max_length=15,default='BSc')
    Religion=models.CharField(max_length=10,default='Christian')
    Category=models.CharField(max_length=10,default='Catholic')
    Course=models.CharField(max_length=10,default='JSD1')

class leave(models.Model):
    Name=models.CharField(max_length=20)
    Leavetype=models.CharField(max_length=15)
    Day=models.CharField(max_length=10)
    Date=models.DateField()
    Session=models.CharField(max_length=10)
    Leavereason=models.CharField(max_length=30)
    Leavedescription=models.CharField(max_length=30)
    Status=models.CharField(max_length=10)
    Batch=models.CharField(max_length=10,default='JSD2')

class assessment(models.Model):
    Assessmentname=models.CharField(max_length=15)
    Date=models.DateField()
    Name=models.CharField(max_length=20,null=True,blank=True)
    Sub1=models.FloatField(default='0')
    Sub2=models.FloatField(default='0')
    Sub3=models.FloatField(default='0')
    Sub4=models.FloatField(default='0')
    Total=models.FloatField(default='0')
    Batch=models.CharField(max_length=10,default='JSD2')

class attendance(models.Model):
    Name=models.CharField(max_length=20)
    Date=models.DateField()
    Status_h1=models.CharField(max_length=10)
    Status_h2=models.CharField(max_length=10)
    Status_h3=models.CharField(max_length=10)
    Status_h4=models.CharField(max_length=10)

class Meta:
    db_table="faculty"
    db_table="students"
    db_table="leave"  
    db_table="attendance" 
