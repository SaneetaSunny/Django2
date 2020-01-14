from django.shortcuts import render,redirect
from student.models import faculty,students,leave,assessment,attendance
from django.http import HttpResponse

# Create your views here.
def authentication(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        username=str(username)
        password=str(password)
        u=faculty.objects.filter(Name=username,Password=password)
        if(u.count()==1):
            request.session['user']=username
            qry=faculty.objects.all().filter(Name=username)[0]
            batch=qry.BatchInCharge
            request.session['batch']=batch
            return render(request,'faculty-login.html')
        else:
            u1=students.objects.filter(Name=username,Password=password)
            if(u1.count()==1):
                request.session['usernm']=username
                return render(request,'home.html')
            else:
                return HttpResponse('Login Unsuccessful')

def fac_profile(request):
    q=faculty.objects.filter(Name=request.session['user'])
    return render(request,'faculty-profile.html',{'a':q})

def fac_pro_view(request):
    q=faculty.objects.filter(Name=request.session['user'])
    return render(request,'faculty-profile-edit.html',{'a':q})

def fac_profile_edit(request):
    if request.method=='POST':
        name=request.POST.get('full-name')
        designation=request.POST.get('designation')
        joindate=request.POST.get('joindate')
        qualification=request.POST.get('qualification')
        gender=request.POST.get('gender')
        mobile=request.POST.get('number')
        email=request.POST.get('email')
        batch=request.POST.get('batch')
        blood=request.POST.get('blood')
        dob=request.POST.get('dob')
        address=request.POST.get('address')
        password=request.POST.get('con_password')
        faculty.objects.filter(Name=request.session['user']).update(Name=name,Address=address,Designation=designation,Joiningdate=joindate,Qualification=qualification,Gender=gender,Mobile=mobile,Email=email,BatchInCharge=batch,Blood=blood,Dob=dob,Password=password)
        return redirect('faculty-profile')

def viewleave(request):
    qry=faculty.objects.all().filter(Name=request.session['user'])[0]
    batch=qry.BatchInCharge
    q=leave.objects.filter(Batch=batch)
    return render(request,'student-leave.html',{'a':q})


def leaveapprove(request):
    if request.method=='POST':
        name=request.POST.get('stname')
        leave.objects.filter(Name=name).update(Status='Approved')
        return redirect('student-leave')

def submit_assessment(request):
    if request.method=='POST':
        ass_name=request.POST.get('ass_name')
        ass_date=request.POST.get('ass_date')
        name=request.POST.get('name')
        sub1=request.POST.get('sub1')
        sub2=request.POST.get('sub2')
        sub3=request.POST.get('sub3')
        sub4=request.POST.get('sub4')
        total=request.POST.get('total')
        c=assessment(Assessmentname=ass_name,Date=ass_date,Name=name,Sub1=sub1,Sub2=sub2,Sub3=sub3,Sub4=sub4,Total=total,Batch=request.session['batch'])
        c.save()
        return redirect('assessment')

def viewassmnt(request):
    q=assessment.objects.all().filter(Batch=request.session['batch'])
    return render(request,'student-leave.html',{'a':q})

def submit_att(request):
    if request.method=='POST':
        name=request.POST.get('name')
        date=request.POST.get('date')
        h1=request.POST.get('status_h1')
        h2=request.POST.get('status_h2')
        h3=request.POST.get('status_h3')
        h4=request.POST.get('status_h4')
        c=attendance(Name=name,Date=date,Status_h1=h1,Status_h2=h2,Status_h3=h3,Status_h4=h4)
        c.save()
        return render(request,'attendence_1.html')
