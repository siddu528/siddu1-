from django.db import models

# Create your models here.
class HospitalDetails(models.Model):
	HospitalName=models.CharField(max_length=100,default="")
	Address=models.CharField(max_length=100,default="")
	ContactNumber=models.CharField(max_length=10,default="")
	Website=models.CharField(max_length=20,default="")
	
class ReciverDetails(models.Model):
	Name=models.CharField(max_length=100,default="")
	LastName=models.CharField(max_length=100,default="")
	ContactNumber=models.CharField(max_length=10,default="")
	LandlineNumber=models.CharField(max_length=20,default="")
	Emailid=models.CharField(max_length=100,default="")
	Address1=models.CharField(max_length=100,default="")
	Address2=models.CharField(max_length=100,default="")
	Gender=models.CharField(max_length=10,default="")
	BloodGroupRequired=models.CharField(max_length=100,default="")
	DateofBirth=models.CharField(max_length=100,default="")
class DonorDetails(models.Model):
	DonorName=models.CharField(max_length=100,default="")
	LastName=models.CharField(max_length=100,default="")
	ContactNumber=models.CharField(max_length=10,default="")
	LandlineNumber=models.CharField(max_length=20,default="")
	Emailid=models.CharField(max_length=100,default="")
	Address1=models.CharField(max_length=100,default="")
	Address2=models.CharField(max_length=100,default="")
	Gender=models.CharField(max_length=10,default="")
	BloodGroupRequired=models.CharField(max_length=100,default="")
	DateofBirth=models.CharField(max_length=100,default="")
	Qualification=models.CharField(max_length=100,default="")
	Profession=models.CharField(max_length=100,default="")
	Height=models.CharField(max_length=100,default="")
	Weight=models.CharField(max_length=100,default="")
	FoodHabit=models.CharField(max_length=100,default="")
	AnyDisease=models.CharField(max_length=100,default="")

class AdminDetails(models.Model):
	username=models.CharField(max_length=100,default="")
	mobilnumber=models.CharField(max_length=100,default="")
	createpassword=models.CharField(max_length=10,default="")
	confirmpassword=models.CharField(max_length=20,default="")



