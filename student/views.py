from django.shortcuts import render,redirect
from student.models import faculty,students,leave,assessment,attendance
from django.http import HttpResponse

# Create your views here.
def stud_profile(request):
    q=students.objects.filter(Name=request.session['usernm'])
    return render(request,'student-profile.html',{'a':q})

def stud_pro_view(request):
    q=students.objects.filter(Name=request.session['usernm'])
    return render(request,'student-edit.html',{'a':q})

def stud_pro_edit(request):
    if request.method=='POST':
        admno=request.POST.get('admno')
        name=request.POST.get('name')
        rollno=request.POST.get('rollno')
        qualification=request.POST.get('qualification')
        gender=request.POST.get('gender')
        mobile=request.POST.get('mobile')
        email=request.POST.get('email')
        course=request.POST.get('course')
        batch=request.POST.get('batch')
        admdate=request.POST.get('admdate')
        dob=request.POST.get('dob')
        address=request.POST.get('address')
        religion=request.POST.get('religion')
        category=request.POST.get('category')
        password=request.POST.get('con_password')
        students.objects.filter(Name=request.session['usernm']).update(AdmNo=admno,AdmDate=admdate,Rollno=rollno,Name=name,Address=address,Qualification=qualification,Gender=gender,Mobile=mobile,Email=email,Batch=batch,Course=course,Dob=dob,Password=password,Religion=religion,Category=category)
    return redirect('student-profile')

def stud_leave_apply(request):
    if request.method=='POST':
        name=request.session['usernm']
        leavetype=request.POST.get['leave']
        day=request.POST.get['day']
        date=request.POST.get['leave_on']
        session=request.POST.getlist['session']
        leavereason=request.POST.get['reason']
        leavedescription=request.POST.get['message']
        
        c=leave(Name=name,Leavetype=leavetype,Day=day,Date=date,Session=session,Leavereason=leavereason,Leavedescription=leavedescription,Status='Pending')
        c.save()
        return redirect('student-leave-management')

def stud_assmnt_view(request):
    q=assessment.objects.all().filter(Name=request.session['usernm'])
    return render(request,'student-assessment.html',{'a':q})


def view_applied_leave(request):
    q=leave.objects.all().filter(Name=request.session['usernm'])
    return render(request,'student-applied-leave.html',{'a':q})

def view_attendance(request):
    q=attendance.objects.all().filter(Name=request.session['usernm'])
    return render(request,'student-attendence.html',{'a':q})

