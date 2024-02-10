from django.shortcuts import render
from student.models import *

# Create your views here.
def hospital(request):
	msg=""
	if request.method=="POST":
		sd=HospitalDetails()
		sd.HospitalName=request.POST["HospitalName"]
		sd.Address=request.POST["Address"]
		sd.ContactNumber=request.POST["ContactNumber"]
		sd.Website=request.POST["Website"]
		sd.save()
		msg="Register successfully"
	return render(request,"hospital.html",{"msg":msg})
def hospitaldata(request):
	data=""
	msg=""
	if request.method=="POST":
		sid=request.POST["sid"]
		HospitalDetails.objects.filter(id=sid).delete()
		msg="Record deleted successfully"
	data=HospitalDetails.objects.all()
	return render(request,"hospitaldata.html",{"data":data,"msg":msg})
def search(request):
	data=''
	if request.method=="POST":
		searchby=int(request.POST["searchby"])
		value=request.POST["value"]
		if searchby==1:
			data=HospitalDetails.objects.filter(id=value)
		elif searchby==2:
			data=HospitalDetails.objects.filter(HospitalName__contains=value)
		elif searchby==3:
			data=HospitalDetails.objects.filter(ContactNumber__contains=value)		
	return render(request,"search.html",{"data":data,})
def reciver(request):
	msg=""
	if request.method=="POST":
		sd=ReciverDetails()
		sd.Name=request.POST["Name"]
		sd.LastName=request.POST["LastName"]
		sd.ContactNumber=request.POST["ContactNumber"]
		sd.LandlineNumber=request.POST["LandlineNumber"]
		sd.Emailid=request.POST["Emailid"]
		sd.Address1=request.POST["Address1"]
		sd.Address2=request.POST["Address2"]
		sd.Gender=request.POST["Gender"]
		sd.BloodGroupRequired=request.POST["BloodGroupRequired"]
		sd.DateofBirth=request.POST["DateofBirth"]
		sd.save()
		msg="Register successfully"
	return render(request,"reciver.html",{"msg":msg})
def reciverdata(request):
	data=""
	msg=""
	if request.method=="POST":
		sid=request.POST["sid"]
		ReciverDetails.objects.filter(id=sid).delete()
		msg="Record deleted successfully"
	data=ReciverDetails.objects.all()
	return render(request,"reciverdata.html",{"data":data,"msg":msg})
def rsearch(request):
	data=''
	if request.method=="POST":
		searchby=int(request.POST["searchby"])
		value=request.POST["value"]
		if searchby==1:
			data=ReciverDetails.objects.filter(id=value)
		elif searchby==2:
			data=ReciverDetails.objects.filter(Name__contains=value)
		elif searchby==3:
			data=ReciverDetails.objects.filter(ContactNumber__contains=value)		
	return render(request,"rsearch.html",{"data":data,})
def donor(request):
	msg=""
	if request.method=="POST":
		sd=DonorDetails()
		sd.DonorName=request.POST["DonorName"]
		sd.LastName=request.POST["LastName"]
		sd.ContactNumber=request.POST["ContactNumber"]
		sd.LandlineNumber=request.POST["LandlineNumber"]
		sd.Emailid=request.POST["Emailid"]
		sd.Address1=request.POST["Address1"]
		sd.Address2=request.POST["Address2"]
		sd.Gender=request.POST["Gender"]
		sd.BloodGroupRequired=request.POST["BloodGroupRequired"]
		sd.DateofBirth=request.POST["DateofBirth"]
		sd.Qualification=request.POST["Qualification"]
		sd.Profession=request.POST["Profession"]
		sd.Height=request.POST["Height"]
		sd.Weight=request.POST["Weight"]
		sd.FoodHabit=request.POST["FoodHabit"]
		sd.AnyDisease=request.POST["AnyDisease"]
		sd.save()
		msg="Register successfully"
	return render(request,"donor.html",{"msg":msg})	
def donordata(request):
	data=""
	msg=""
	if request.method=="POST":
		sid=request.POST["sid"]
		DonorDetails.objects.filter(id=sid).delete()
		msg="Record deleted successfully"
	data=DonorDetails.objects.all()
	return render(request,"donordata.html",{"data":data,"msg":msg})	
def dsearch(request):
	data=''
	if request.method=="POST":
		searchby=int(request.POST["searchby"])
		value=request.POST["value"]
		if searchby==1:
			data=DonorDetails.objects.filter(id=value)
		elif searchby==2:
			data=DonorDetails.objects.filter(DonorName__contains=value)
		elif searchby==3:
			data=DonorDetails.objects.filter(ContactNumber__contains=value)		
	return render(request,"dsearch.html",{"data":data,})
def adminregistration(request):
	msg=""
	if request.method=="POST":
		sd=AdminDetails()
		sd.username=request.POST["username"]
		sd.mobilnumber=request.POST["mobilnumber"]
		sd.createpassword=request.POST["createpassword"]
		sd.confirmpassword=request.POST["confirmpassword"]
		sd.save()
		msg="Register successfully"
	return render(request,"adminregistration.html",{"msg":msg})
def admindata(request):
	data=""
	msg=""
	if request.method=="POST":
		sid=request.POST["sid"]
		AdminDetails.objects.filter(id=sid).delete()
		msg="Record deleted successfully"
	data=AdminDetails.objects.all()
	return render(request,"admindata.html",{"data":data,"msg":msg})
def asearch(request):
	data=''
	if request.method=="POST":
		searchby=int(request.POST["searchby"])
		value=request.POST["value"]
		if searchby==1:
			data=AdminDetails.objects.filter(id=value)
		elif searchby==2:
			data=AdminDetails.objects.filter(username__contains=value)
		elif searchby==3:
			data=AdminDetails.objects.filter(mobilnumber__contains=value)		
	return render(request,"asearch.html",{"data":data,})
def adminhome(request):		
	return render(request,"adminhome.html")
def adminlogin(request):
	msg=""
	if request.method=="POST":
		p_mobilnumber=request.POST["mobilnumber"]
		p_password=request.POST['confirmpassword']
		if AdminDetails.objects.filter(mobilnumber=p_mobilnumber,confirmpassword=p_password).exists():
			request.session["mobilnumber"]=p_mobilnumber
			return render(request,"adminhome.html")
		else:
			msg="Invalide mobilnumber or Password"
	return render(request,"adminlogin.html",{"msg":msg})		
def adminchangepassword(request):
	msg=""
	if request.method=="POST":
		currentpassword=request.POST["confirmpassword"]
		newpassword=request.POST['newpassword']
		confirmnewpassword=request.POST['confirmnewpassword']
		p_mobilnumber=request.session["mobilnumber"]
		if newpassword==confirmnewpassword:
			if AdminDetails.objects.filter(mobilnumber=p_mobilnumber,confirmpassword=currentpassword).exists():
				AdminDetails.objects.filter(mobilnumber=p_mobilnumber,confirmpassword=currentpassword).update(confirmpassword=newpassword)
				msg='password updated successfully'
			else:
				msg="currentpassword password is Invalide"
		else:
			msg="newpassword and confirmnewpassword must be same"
	return render(request,"adminchangepassword.html",{"msg":msg})
def menu(request):		
	return render(request,"menu.html")	
